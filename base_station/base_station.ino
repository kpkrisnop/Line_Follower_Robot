// ESP32 base station for the line follower: plug it into the Mac's USB and tuner.py talks to the
// car over ESP-NOW, so the Mac stays on its normal Wi-Fi (internet while tuning).
// USB serial <-> ESP-NOW <-> wifi_bridge (ESP8266 on the car) <-> UNO.
// Beacons every 500 ms so the car learns where to send. Between lines it tells the tuner
// "base: car -55 dBm" (or "base: no car") once a second.
// Board: ESP32 Dev Module (esp32:esp32:esp32).
#include <WiFi.h>
#include <esp_now.h>
#include <esp_wifi.h>

const uint8_t CHANNEL = 1;     // must match wifi_bridge.ino
enum : uint8_t { BEACON = 1, DATA = 2 };
const uint8_t BROADCAST[6] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};

uint8_t car[6];
bool carKnown;
volatile unsigned long carSeen;
volatile int carRssi;
uint8_t rx[2048];              // radio -> USB, filled in the Wi-Fi task, drained in loop()
volatile uint16_t rxHead, rxTail;
bool midLine;                  // last byte sent to USB wasn't '\n': don't cut in with a "base:" line

void addPeer(const uint8_t *mac) {
  esp_now_peer_info_t p = {};
  memcpy(p.peer_addr, mac, 6);
  p.channel = CHANNEL;
  p.ifidx = WIFI_IF_STA;
  esp_now_add_peer(&p);
}

void onRadio(const esp_now_recv_info_t *info, const uint8_t *data, int len) {
  if (len < 2 || data[0] != DATA) return;
  if (!carKnown) {             // first packet from the car: unicast from now on (ACKed, retried)
    memcpy(car, info->src_addr, 6);
    addPeer(car);
    carKnown = true;
  }
  carSeen = millis();
  carRssi = info->rx_ctrl->rssi;
  for (int i = 1; i < len; i++) {
    uint16_t next = (rxHead + 1) % sizeof rx;
    if (next == rxTail) break;
    rx[rxHead] = data[i];
    rxHead = next;
  }
}

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  esp_wifi_set_channel(CHANNEL, WIFI_SECOND_CHAN_NONE);
  esp_now_init();
  esp_now_register_recv_cb(onRadio);
  addPeer(BROADCAST);
  Serial.println("\nbase: up");
}

void loop() {
  static unsigned long lastBeacon, lastReport;
  unsigned long now = millis();
  if (now - lastBeacon >= 500) {
    lastBeacon = now;
    uint8_t b = BEACON;
    esp_now_send(BROADCAST, &b, 1);
  }
  while (rxTail != rxHead) {
    uint8_t c = rx[rxTail];
    rxTail = (rxTail + 1) % sizeof rx;
    Serial.write(c);
    midLine = c != '\n';
  }
  bool carGone = !carSeen || now - carSeen > 2000;
  if (now - lastReport >= 1000 && (!midLine || carGone)) {
    lastReport = now;
    if (midLine) Serial.println();  // car went quiet mid-line: finish it so this line stays whole
    midLine = false;
    if (carGone) Serial.println("base: no car");
    else Serial.printf("base: car %d dBm\n", carRssi);
  }
  uint8_t buf[200];
  size_t n = Serial.available();
  if (n) {
    buf[0] = DATA;
    n = Serial.readBytes(buf + 1, min(n, sizeof buf - 1));
    esp_now_send(carKnown ? car : BROADCAST, buf, n + 1);
  }
}
