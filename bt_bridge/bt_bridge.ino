// ESP32 Bluetooth bridge for the line follower (replaces wifi_bridge on the ESP8266).
// Classic Bluetooth serial (SPP) named "LineFollower" <-> the UNO's serial, so tuner.py works over Bluetooth.
// Pair "LineFollower" once in macOS Bluetooth settings; it then appears as /dev/cu.LineFollower.
// The ESP32's own USB serial is bridged too (debug).
// Wiring: GPIO16 (RX2) <- UNO TX (D1) through a divider (5 V -> 3.3 V; ESP32 pins aren't 5 V tolerant),
//         GPIO17 (TX2) -> UNO RX (D0), GND-GND. Pull the GPIO17 -> D0 wire for USB uploads to the UNO.
// Needs an original ESP32 (WROOM/WROVER): the S2/S3/C3 have no Classic Bluetooth.
#include <BluetoothSerial.h>

const int RX_PIN = 16, TX_PIN = 17;

BluetoothSerial bt;
volatile bool linkOpen, restartBt;

// BluetoothSerial keeps one client handle. If a link dies with a failed close, the handle is never
// cleared and every later connection is refused as a "second connection" until reset.
// ponytail: reset the whole ESP32 on any close (~1 s); a proper fix would patch the library.
void onBt(esp_spp_cb_event_t event, esp_spp_cb_param_t *p) {
  if (event == ESP_SPP_SRV_OPEN_EVT) {
    Serial.printf("bt: open status %d%s\n", p->srv_open.status, linkOpen ? " (while one was open: stuck)" : "");
    if (linkOpen) restartBt = true;
    linkOpen = true;
  } else if (event == ESP_SPP_CLOSE_EVT) {
    Serial.printf("bt: close status %d by_remote %d\n", p->close.status, p->close.async);
    restartBt = true;
  }
}

void setup() {
  Serial.begin(115200);
  Serial2.setRxBufferSize(1024);  // before begin(); the ~700 B `?` help burst fits
  Serial2.begin(115200, SERIAL_8N1, RX_PIN, TX_PIN);
  // Without SSP the core does legacy PIN pairing, and with no PIN set it answers an empty one,
  // so macOS pairing fails. SSP with no input/output = "Just Works": pairs with no code.
  bt.enableSSP(false, false);
  bt.register_callback(onBt);
  bt.begin("LineFollower");
  Serial.println("\nbridge up: Bluetooth LineFollower");
}

void loop() {
  if (restartBt) {
    Serial.println("bt: restarting to clear the link");
    Serial.flush();
    ESP.restart();
  }
  uint8_t buf[256];
  size_t n = Serial2.available();
  if (n) {
    n = Serial2.readBytes(buf, min(n, sizeof buf));
    if (bt.hasClient()) bt.write(buf, n);  // no client: writing would only fill the BT queue
    Serial.write(buf, n);
  }
  while (bt.available()) Serial2.write(bt.read());
  while (Serial.available()) Serial2.write(Serial.read());
}
