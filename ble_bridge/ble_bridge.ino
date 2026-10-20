// ESP32 BLE bridge for the line follower (replaces wifi_bridge on the ESP8266).
// Nordic UART Service named "LineFollower" <-> the UNO's serial, so tuner.py works over BLE.
// UNO output goes out as notifications on TX; tuner commands arrive as writes on RX.
// No pairing: macOS reconnects to a BLE peripheral reliably; Classic SPP (bt_bridge, removed) didn't.
// The ESP32's own USB serial is bridged too (debug), with "ble:" lines for connects/disconnects.
// Wiring: GPIO16 (RX2) <- UNO TX (D1) through a divider (5 V -> 3.3 V; ESP32 pins aren't 5 V tolerant),
//         GPIO17 (TX2) -> UNO RX (D0), GND-GND. Pull the GPIO17 -> D0 wire for USB uploads to the UNO.
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLE2902.h>

const int RX_PIN = 16, TX_PIN = 17;
#define NUS_SERVICE "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
#define NUS_RX      "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"  // tuner writes commands here
#define NUS_TX      "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"  // UNO output is notified here

BLEServer *server;
BLECharacteristic *tx;
volatile bool connected, readvertise;

struct ServerCb : BLEServerCallbacks {
  void onConnect(BLEServer *) override {
    connected = true;
    Serial.println("ble: connected");
  }
  void onDisconnect(BLEServer *) override {
    connected = false;
    readvertise = true;  // advertising stops on connect; restart it from loop()
    Serial.println("ble: disconnected");
  }
};

struct RxCb : BLECharacteristicCallbacks {
  void onWrite(BLECharacteristic *c) override {
    Serial2.write(c->getData(), c->getLength());
  }
};

void setup() {
  Serial.begin(115200);
  Serial2.setRxBufferSize(1024);  // before begin(); the ~700 B `?` help burst fits
  Serial2.begin(115200, SERIAL_8N1, RX_PIN, TX_PIN);

  BLEDevice::init("LineFollower");
  BLEDevice::setMTU(247);  // the Mac negotiates up to this; a status line (~110 B) then fits one notification
  server = BLEDevice::createServer();
  server->setCallbacks(new ServerCb());
  BLEService *nus = server->createService(NUS_SERVICE);
  tx = nus->createCharacteristic(NUS_TX, BLECharacteristic::PROPERTY_NOTIFY);
  tx->addDescriptor(new BLE2902());
  BLECharacteristic *rx = nus->createCharacteristic(NUS_RX, BLECharacteristic::PROPERTY_WRITE | BLECharacteristic::PROPERTY_WRITE_NR);
  rx->setCallbacks(new RxCb());
  nus->start();
  BLEAdvertising *adv = BLEDevice::getAdvertising();
  adv->addServiceUUID(NUS_SERVICE);
  adv->setScanResponse(true);  // the name goes in the scan response; the 128-bit UUID fills the advert
  BLEDevice::startAdvertising();
  Serial.println("\nbridge up: BLE LineFollower");
}

void loop() {
  if (readvertise) {
    readvertise = false;
    delay(200);  // let the stack finish the disconnect
    server->startAdvertising();
    Serial.println("ble: advertising");
  }
  uint8_t buf[256];
  size_t n = Serial2.available();
  if (n) {
    size_t chunk = connected ? min<size_t>(server->getPeerMTU(server->getConnId()) - 3, sizeof buf) : sizeof buf;
    n = Serial2.readBytes(buf, min(n, chunk));
    if (connected) {
      tx->setValue(buf, n);
      tx->notify();
    }
    Serial.write(buf, n);
  }
  while (Serial.available()) Serial2.write(Serial.read());
  delay(5);  // batch bytes into fewer, fuller notifications
}
