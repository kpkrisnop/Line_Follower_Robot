#include <EEPROM.h>

// Line follower: Arduino UNO + L298N (ENA/ENB jumpers on), two IR sensors straddling the line.
// Two control modes in one sketch: PID (analog sensors) and bang-bang (digital sensors).
// Tune live from the Serial Monitor (115200 baud, line ending "Newline"); send "?" for the list.
// Both sensors above the "stop" level = stop line: the car stops and beeps.
// "cal" learns each sensor's own white/black readings, so both read 0 (white) .. 1000 (black).
// Motors wait 1 s after boot, so a "pause" from the tuner (opening the port resets the Uno)
// lands before the car moves.

const int IN1 = 5, IN2 = 6;    // left motor
const int IN3 = 9, IN4 = 10;   // right motor
const int LEFT_DO = 3, RIGHT_DO = 4;
const int LEFT_AO = A0, RIGHT_AO = A1;
const int BUZZER = 11;

// ---- Calibration knobs ----
char mode = 'p';               // start mode: 'p' = PID, 'b' = bang-bang
const int ON_LINE = HIGH;      // DO level over black; flip to LOW if your modules read LOW
const bool LEFT_REVERSED = true;
const bool RIGHT_REVERSED = false;

// Code defaults; all of these (and mode) can be changed over serial. Every change is saved
// to EEPROM automatically and loads at boot, overriding these. "d" goes back to these.
int BANG_SPEED = 200;          // bang-bang "on" duty, 0-255
int BASE_SPEED = 160;          // PID cruising duty, 0-255
float KP = 0.30, KI = 0.0, KD = 2.0;  // flip KP/KD sign if it steers away from the line
float SLOW = 0.0;              // PID corner slowdown: cruise = base - slow * |err|  (0 = off)
int MIN_SPEED = 80;            // cruise never drops below this in a corner
int TURN = 510;                // max steering |corr|; lower = gentler corners (510 = no cap)
int AO_OFFSET = 0;             // added to right AO (after calibration) to centre the car
int STOP_LEVEL = 700;          // both sensors above this (0-1000) = stop line; 1001 = never stop
int TRIM = 0;                  // motor balance in %: >0 slows the left motor, <0 slows the right
int calMin[2] = {0, 0}, calMax[2] = {1023, 1023};  // raw AO on white / black per sensor, set by "cal"
bool paused = false;
bool quiet = false;            // "q": silence status lines, e.g. before uploading over USB/IP
const unsigned long MUTE_MS = 5000;  // status lines pause this long after any command
unsigned long muteStart;
bool muted;
bool tui = false;              // "tui": the tuner is connected, so never mute (it shows replies itself)
const unsigned long BOOT_DELAY_MS = 1000;

// ---- EEPROM ----
const byte MAGIC = 0x45;      // change this if you add/reorder saved values, so old data is ignored

template <typename T> void io(int &addr, T &v, bool save) {
  if (save) EEPROM.put(addr, v); else EEPROM.get(addr, v);
  addr += sizeof(T);
}

void storeSettings(bool save) {
  int a = 1;                   // byte 0 holds MAGIC
  io(a, KP, save); io(a, KI, save); io(a, KD, save);
  io(a, BASE_SPEED, save); io(a, BANG_SPEED, save); io(a, AO_OFFSET, save); io(a, mode, save);
  io(a, SLOW, save); io(a, MIN_SPEED, save); io(a, TURN, save);
  io(a, STOP_LEVEL, save); io(a, TRIM, save); io(a, calMin, save); io(a, calMax, save);
  if (save) EEPROM.update(0, MAGIC);
}

// ---- Motors ----
void motor(int a, int b, int speed, bool reversed) {  // speed -255..255
  speed = constrain(speed, -255, 255);
  if (reversed) speed = -speed;
  analogWrite(a, speed > 0 ? speed : 0);
  analogWrite(b, speed < 0 ? -speed : 0);
}

int leftSpeed, rightSpeed;
void drive(int l, int r) {
  if (TRIM > 0) l = (long)l * (100 - TRIM) / 100;  // long: l*100 overflows a 16-bit int
  else r = (long)r * (100 + TRIM) / 100;
  leftSpeed = l; rightSpeed = r;
  motor(IN1, IN2, l, LEFT_REVERSED);
  motor(IN3, IN4, r, RIGHT_REVERSED);
}

// ---- Setup ----
void setup() {
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT);
  pinMode(LEFT_DO, INPUT); pinMode(RIGHT_DO, INPUT);
  pinMode(BUZZER, OUTPUT);
  Serial.begin(115200);
  Serial.setTimeout(20);       // so reading a command line doesn't stall the control loop
  bool saved = EEPROM.read(0) == MAGIC;
  if (saved) storeSettings(false);
  Serial.println(saved ? "Loaded saved settings. Send ? for commands" : "Code defaults. Send ? for commands");
}

int norm(int raw, byte i) {     // per-sensor calibration: 0 = white, 1000 = black
  return constrain(map(raw, calMin[i], calMax[i], 0, 1000), 0, 1000);
}

bool calibrate() {              // slide both sensors across the line by hand while this runs
  drive(0, 0);
  int mn[2] = {1023, 1023}, mx[2] = {0, 0};
  tone(BUZZER, 1500, 100);
  unsigned long t0 = millis(), shown = 0;
  while (millis() - t0 < 5000) {
    int v[2] = {analogRead(LEFT_AO), analogRead(RIGHT_AO)};
    for (byte i = 0; i < 2; i++) { mn[i] = min(mn[i], v[i]); mx[i] = max(mx[i], v[i]); }
    if (millis() - shown >= 200) {  // progress, and keeps the tuner's 2 s Wi-Fi watchdog fed
      shown = millis();
      Serial.print(F("cal L ")); Serial.print(mn[0]); Serial.print(F("-")); Serial.print(mx[0]);
      Serial.print(F("  R ")); Serial.print(mn[1]); Serial.print(F("-")); Serial.println(mx[1]);
    }
  }
  tone(BUZZER, 2500, 100);
  if (mx[0] - mn[0] < 200 || mx[1] - mn[1] < 200) {
    Serial.println(F("cal failed: a sensor never saw both white and black; kept the old calibration"));
    return false;
  }
  for (byte i = 0; i < 2; i++) { calMin[i] = mn[i]; calMax[i] = mx[i]; }
  Serial.println(F("cal done"));
  return true;
}

float integral, lastErr;
int cruise;                    // PID speed after corner slowdown, before steering
unsigned long lastT, lastPrint;
bool stopped;

void showSettings() {
  Serial.print(F("mode ")); Serial.print(mode == 'p' ? "PID" : "BANG");
  Serial.print(paused ? " PAUSED" : " RUNNING");
  Serial.print(quiet ? " QUIET" : "");
  Serial.print(F(" | kp ")); Serial.print(KP, 3);
  Serial.print(F(" ki ")); Serial.print(KI, 3);
  Serial.print(F(" kd ")); Serial.print(KD, 3);
  Serial.print(F(" base ")); Serial.print(BASE_SPEED);
  Serial.print(F(" slow ")); Serial.print(SLOW, 3);
  Serial.print(F(" min ")); Serial.print(MIN_SPEED);
  Serial.print(F(" turn ")); Serial.print(TURN);
  Serial.print(F(" bang ")); Serial.print(BANG_SPEED);
  Serial.print(F(" off ")); Serial.print(AO_OFFSET);
  Serial.print(F(" stop ")); Serial.print(STOP_LEVEL);
  Serial.print(F(" trim ")); Serial.println(TRIM);
}

void handleCommand() {
  String cmd = Serial.readStringUntil('\n');
  cmd.trim();
  if (cmd.length() == 0) return;
  if (!tui) { muted = true; muteStart = millis(); }  // keep the reply on screen instead of scrolling it away
  int sp = cmd.indexOf(' ');
  String key = sp < 0 ? cmd : cmd.substring(0, sp);
  float v = sp < 0 ? 0 : cmd.substring(sp + 1).toFloat();
  bool hasValue = sp >= 0;

  bool save = false;           // only settings changes go to EEPROM
  if (key == "p" || key == "b") { mode = key[0]; save = true; }
  else if (key == "x") paused = !paused;
  else if (key == "pause") paused = true;
  else if (key == "run") paused = false;
  else if (key == "q") quiet = !quiet;
  else if (key == "tui") { tui = true; muted = false; }
  else if (key == "d") { EEPROM.update(0, 0xFF); Serial.println(F("saved settings wiped; code defaults from next reset")); return; }
  else if (key == "?") {
    Serial.println(F("p | b         switch to PID / bang-bang"));
    Serial.println(F("x             pause / resume motors (toggle)"));
    Serial.println(F("pause | run   pause / run motors"));
    Serial.println(F("q             silence / resume status lines"));
    Serial.println(F("kp ki kd <n>  PID gains, e.g. kp 0.4"));
    Serial.println(F("base <0-255>  PID cruising speed"));
    Serial.println(F("slow <n>      PID corner slowdown per unit of |err|, 0 = off"));
    Serial.println(F("min <0-255>   lowest PID cruise speed in corners"));
    Serial.println(F("turn <0-510>  max PID steering; lower = gentler corners"));
    Serial.println(F("bang <0-255>  bang-bang speed"));
    Serial.println(F("off <n>       added to right AO, e.g. off -3"));
    Serial.println(F("stop <0-1001> stop line when both sensors read above this; 1001 = never"));
    Serial.println(F("trim <n>      motor balance %, >0 slows left, <0 slows right"));
    Serial.println(F("cal           5 s: slide both sensors across the line by hand"));
    Serial.println(F("d             wipe saved settings (code defaults after reset)"));
  }
  else if (hasValue && key == "kp") { KP = v; save = true; }
  else if (hasValue && key == "ki") { KI = v; save = true; }
  else if (hasValue && key == "kd") { KD = v; save = true; }
  else if (hasValue && key == "base") { BASE_SPEED = constrain((int)v, 0, 255); save = true; }
  else if (hasValue && key == "slow") { SLOW = max(v, 0.0f); save = true; }
  else if (hasValue && key == "min") { MIN_SPEED = constrain((int)v, 0, 255); save = true; }
  else if (hasValue && key == "turn") { TURN = constrain((int)v, 0, 510); save = true; }
  else if (hasValue && key == "bang") { BANG_SPEED = constrain((int)v, 0, 255); save = true; }
  else if (hasValue && key == "off") { AO_OFFSET = (int)v; save = true; }
  else if (hasValue && key == "stop") { STOP_LEVEL = constrain((int)v, 0, 1001); save = true; }
  else if (hasValue && key == "trim") { TRIM = constrain((int)v, -50, 50); save = true; }
  else if (key == "cal") { save = calibrate(); paused = true; }  // you're holding the car
  else { Serial.print(F("?? ")); Serial.println(cmd); return; }

  integral = 0; lastErr = 0;   // fresh start after any change
  if (save) {
    storeSettings(true);       // EEPROM.put only rewrites changed bytes, so wear is negligible
    Serial.print(F("saved: "));
  }
  showSettings();
}

void loop() {
  if (Serial.available()) handleCommand();

  bool l = digitalRead(LEFT_DO) == ON_LINE;
  bool r = digitalRead(RIGHT_DO) == ON_LINE;
  int la = norm(analogRead(LEFT_AO), 0), ra = norm(analogRead(RIGHT_AO), 1) + AO_OFFSET;
  float err = la - ra;  // >0: line is under the left sensor -> steer left
  bool stopLine = la > STOP_LEVEL && ra > STOP_LEVEL;  // analog, not DO: the DO pots trip on glare

  bool waiting = millis() < BOOT_DELAY_MS;
  if (paused || waiting) {
    drive(0, 0);
  } else if (stopLine) {
    drive(0, 0);
    if (!stopped) tone(BUZZER, 2000, 300);
    stopped = true;
  } else {
    stopped = false;
    if (mode == 'b') {
      // Wheel on its sensor's side stops, so the car swings back over the line.
      drive(l ? 0 : BANG_SPEED, r ? 0 : BANG_SPEED);
    } else if (millis() - lastT >= 10) {   // fixed 10 ms step, so gains don't need dt
      lastT = millis();
      integral = constrain(integral + err, -2000, 2000);
      float corr = constrain(KP * err + KI * integral + KD * (err - lastErr), -TURN, TURN);
      lastErr = err;
      cruise = constrain(BASE_SPEED - SLOW * fabs(err), min(MIN_SPEED, BASE_SPEED), BASE_SPEED);
      drive(cruise - corr, cruise + corr);
    }
  }

  // ponytail: printing every loop at 115200 would still stall control; 10 Hz is enough to watch
  if (muted && millis() - muteStart >= MUTE_MS) muted = false;
  if (!quiet && !muted && millis() - lastPrint >= 100) {
    lastPrint = millis();
    Serial.print(mode == 'p' ? "PID" : "BANG");
    Serial.print(F(" L_DO:")); Serial.print(l);
    Serial.print(F(" R_DO:")); Serial.print(r);
    Serial.print(F(" L_AO:")); Serial.print(la);
    Serial.print(F(" R_AO:")); Serial.print(ra);
    Serial.print(F(" err:"));  Serial.print(err);
    Serial.print(F(" cruise:")); Serial.print(cruise);
    Serial.print(F(" L_spd:")); Serial.print(leftSpeed);
    Serial.print(F(" R_spd:")); Serial.print(rightSpeed);
    Serial.println(paused ? " PAUSED" : waiting ? " WAIT" : stopped ? " STOP" : "");
  }
}
