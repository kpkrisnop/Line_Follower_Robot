// ESP8266 Wi-Fi bridge for the line follower.
// Makes AP "LineFollower" (192.168.4.1) and pipes TCP port 23 <-> the UNO's serial,
// so tuner.py works over Wi-Fi. The ESP's own USB serial is bridged too (debug).
// Wiring: ESP D1 <- UNO TX (through a divider/resistor, 5 V -> 3.3 V), ESP D2 -> UNO RX, GND-GND.
// Updates to this sketch can go over Wi-Fi (ArduinoOTA, host "linefollower").
#include <ESP8266WiFi.h>
#include <ArduinoOTA.h>
#include <SoftwareSerial.h>
#include "secrets.h"  // AP_PASS, gitignored

// ponytail: software serial at 115200 can flip bits under Wi-Fi load; tuner skips garbled lines.
// If it's bad, drop both sides to 57600.
SoftwareSerial uno;
WiFiServer server(23);
WiFiClient client;

void setup() {
  Serial.begin(115200);
  uno.begin(115200, SWSERIAL_8N1, D1, D2, false, 256);  // rx, tx; default 64 B buffer overflowed on settings lines
  WiFi.mode(WIFI_AP);
  WiFi.softAP("LineFollower", AP_PASS);
  ArduinoOTA.setHostname("linefollower");
  ArduinoOTA.begin();
  server.begin();
  server.setNoDelay(true);
  Serial.printf("\nbridge up: AP LineFollower, %s:23\n", WiFi.softAPIP().toString().c_str());
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
    n = uno.readBytes(buf, min(n, sizeof buf));
    if (client) client.write(buf, n);
    Serial.write(buf, n);
  }
  while (client && client.available()) uno.write(client.read());
  while (Serial.available()) uno.write(Serial.read());
}
