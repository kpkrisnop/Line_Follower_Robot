// ESP8266 Wi-Fi bridge for the line follower.
// Makes AP "LineFollower" (192.168.77.1) and pipes TCP port 23 <-> the UNO's serial,
// so tuner.py works over Wi-Fi. The ESP's own USB serial is bridged too (debug).
// Also talks ESP-NOW to base_station (an ESP32 on the Mac's USB): once the base's beacon is
// heard, UNO output goes to it as well, and commands from it go to the UNO. Both paths work at once.
// Wiring: ESP D1 <- UNO TX (through a divider/resistor, 5 V -> 3.3 V), ESP D2 -> UNO RX, GND-GND.
// Updates to this sketch can go over Wi-Fi (ArduinoOTA, host "linefollower").
#include <ESP8266WiFi.h>
#include <ArduinoOTA.h>
#include <SoftwareSerial.h>
#include <espnow.h>
#include "secrets.h"  // AP_PASS, gitignored

const uint8_t CHANNEL = 1;     // AP and ESP-NOW channel; base_station.ino must match
enum : uint8_t { BEACON = 1, DATA = 2 };  // first byte of every ESP-NOW packet

// ponytail: software serial at 115200 can flip bits under Wi-Fi load; tuner skips garbled lines.
// If it's bad, drop both sides to 57600.
SoftwareSerial uno;
WiFiServer server(23);
WiFiClient client;

uint8_t base[6];               // base station MAC, learnt from its beacon
volatile unsigned long baseSeen;  // millis() of its last beacon; 0 = never
uint8_t rx[512];               // radio -> UNO bytes; the callback can't bit-bang SoftwareSerial
volatile uint16_t rxHead, rxTail;

void onRadio(uint8_t *mac, uint8_t *data, uint8_t len) {
  if (len < 1) return;
  if (data[0] == BEACON) {
    if (!baseSeen || memcmp(mac, base, 6)) {
      memcpy(base, mac, 6);
      esp_now_add_peer(base, ESP_NOW_ROLE_COMBO, CHANNEL, NULL, 0);
    }
    baseSeen = millis() | 1;
  } else if (data[0] == DATA) {
    for (uint8_t i = 1; i < len; i++) {
      uint16_t next = (rxHead + 1) % sizeof rx;
      if (next == rxTail) break;  // full: drop, the tuner resends nothing it needs
      rx[rxHead] = data[i];
      rxHead = next;
    }
  }
}

void setup() {
  Serial.begin(115200);
  uno.begin(115200, SWSERIAL_8N1, D1, D2, false, 256);  // rx, tx; default 64 B buffer overflowed on settings lines
  WiFi.mode(WIFI_AP);
  IPAddress ip(192, 168, 77, 1);  // not the default 192.168.4.1: KP's home LAN is 192.168.4.x
  WiFi.softAPConfig(ip, ip, IPAddress(255, 255, 255, 0));
  WiFi.softAP("LineFollower", AP_PASS, CHANNEL);
  esp_now_init();
  esp_now_set_self_role(ESP_NOW_ROLE_COMBO);
  esp_now_register_recv_cb(onRadio);
  ArduinoOTA.setHostname("linefollower");
  ArduinoOTA.begin();
  server.begin();
  server.setNoDelay(true);
  Serial.printf("\nbridge up: AP LineFollower ch %d, %s:23, ESP-NOW on\n", CHANNEL, WiFi.softAPIP().toString().c_str());
}

void loop() {
  ArduinoOTA.handle();
  if (server.hasClient()) {  // newest client wins, so a reconnecting tuner never gets locked out
    client.stop();
    client = server.accept();
    client.setNoDelay(true);
  }
  uint8_t buf[128];
  size_t n = uno.available();
  if (n) {
    n = uno.readBytes(buf + 1, min(n, sizeof buf - 1));
    if (client) client.write(buf + 1, n);
    Serial.write(buf + 1, n);
    if (baseSeen && millis() - baseSeen < 3000) {  // base gone 3 s: stop sending into the void
      buf[0] = DATA;
      esp_now_send(base, buf, n + 1);
    }
  }
  while (rxTail != rxHead) {
    uno.write(rx[rxTail]);
    rxTail = (rxTail + 1) % sizeof rx;
  }
  while (client && client.available()) uno.write(client.read());
  while (Serial.available()) uno.write(Serial.read());
}
