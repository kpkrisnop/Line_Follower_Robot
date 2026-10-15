#include <EEPROM.h>

// Line follower: Arduino UNO + L298N (ENA/ENB jumpers on), two IR sensors straddling the line.
// Two control modes in one sketch: PID (analog sensors) and bang-bang (digital sensors).
// Tune live from the Serial Monitor (115200 baud, line ending "Newline"); send "?" for the list.
// Both sensors on black = stop line: the car stops and beeps.
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
int AO_OFFSET = 0;             // add to right AO so both read equal on white
bool paused = false;
bool quiet = false;            // "q": silence status lines, e.g. before uploading over USB/IP
const unsigned long MUTE_MS = 5000;  // status lines pause this long after any command
unsigned long muteStart;
bool muted;
bool tui = false;              // "tui": the tuner is connected, so never mute (it shows replies itself)
const unsigned long BOOT_DELAY_MS = 1000;

// ---- EEPROM ----
const byte MAGIC = 0x43;       // change this if you add/reorder saved values, so old data is ignored

template <typename T> void io(int &addr, T &v, bool save) {
  if (save) EEPROM.put(addr, v); else EEPROM.get(addr, v);
  addr += sizeof(T);
}

void storeSettings(bool save) {
  int a = 1;                   // byte 0 holds MAGIC
  io(a, KP, save); io(a, KI, save); io(a, KD, save);
  io(a, BASE_SPEED, save); io(a, BANG_SPEED, save); io(a, AO_OFFSET, save); io(a, mode, save);
  io(a, SLOW, save); io(a, MIN_SPEED, save);
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

float integral, lastErr;
int cruise;                    // PID speed after corner slowdown, before steering
unsigned long lastT, lastPrint;
bool stopped;

void showSettings() {
  Serial.print("mode "); Serial.print(mode == 'p' ? "PID" : "BANG");
  Serial.print(paused ? " PAUSED" : " RUNNING");
  Serial.print(quiet ? " QUIET" : "");
  Serial.print(" | kp "); Serial.print(KP, 3);
  Serial.print(" ki "); Serial.print(KI, 3);
  Serial.print(" kd "); Serial.print(KD, 3);
  Serial.print(" base "); Serial.print(BASE_SPEED);
  Serial.print(" slow "); Serial.print(SLOW, 3);
  Serial.print(" min "); Serial.print(MIN_SPEED);
  Serial.print(" bang "); Serial.print(BANG_SPEED);
  Serial.print(" off "); Serial.println(AO_OFFSET);
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
  else if (key == "d") { EEPROM.update(0, 0xFF); Serial.println("saved settings wiped; code defaults from next reset"); return; }
  else if (key == "?") {
    Serial.println("p | b         switch to PID / bang-bang");
    Serial.println("x             pause / resume motors (toggle)");
    Serial.println("pause | run   pause / run motors");
    Serial.println("q             silence / resume status lines");
    Serial.println("kp ki kd <n>  PID gains, e.g. kp 0.4");
    Serial.println("base <0-255>  PID cruising speed");
    Serial.println("slow <n>      PID corner slowdown per unit of |err|, 0 = off");
    Serial.println("min <0-255>   lowest PID cruise speed in corners");
    Serial.println("bang <0-255>  bang-bang speed");
    Serial.println("off <n>       added to right AO, e.g. off -3");
    Serial.println("d             wipe saved settings (code defaults after reset)");
  }
  else if (hasValue && key == "kp") { KP = v; save = true; }
  else if (hasValue && key == "ki") { KI = v; save = true; }
  else if (hasValue && key == "kd") { KD = v; save = true; }
  else if (hasValue && key == "base") { BASE_SPEED = constrain((int)v, 0, 255); save = true; }
  else if (hasValue && key == "slow") { SLOW = max(v, 0.0f); save = true; }
  else if (hasValue && key == "min") { MIN_SPEED = constrain((int)v, 0, 255); save = true; }
  else if (hasValue && key == "bang") { BANG_SPEED = constrain((int)v, 0, 255); save = true; }
  else if (hasValue && key == "off") { AO_OFFSET = (int)v; save = true; }
  else { Serial.print("?? "); Serial.println(cmd); return; }

  integral = 0; lastErr = 0;   // fresh start after any change
  if (save) {
    storeSettings(true);       // EEPROM.put only rewrites changed bytes, so wear is negligible
    Serial.print("saved: ");
  }
  showSettings();
}

void loop() {
  if (Serial.available()) handleCommand();

  bool l = digitalRead(LEFT_DO) == ON_LINE;
  bool r = digitalRead(RIGHT_DO) == ON_LINE;
  int la = analogRead(LEFT_AO), ra = analogRead(RIGHT_AO) + AO_OFFSET;
  float err = la - ra;  // >0: line is under the left sensor -> steer left

  bool waiting = millis() < BOOT_DELAY_MS;
  if (paused || waiting) {
    drive(0, 0);
  } else if (l && r) {                // stop line
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
      float corr = KP * err + KI * integral + KD * (err - lastErr);
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
    Serial.print(" L_DO:"); Serial.print(l);
    Serial.print(" R_DO:"); Serial.print(r);
    Serial.print(" L_AO:"); Serial.print(la);
    Serial.print(" R_AO:"); Serial.print(ra);
    Serial.print(" err:");  Serial.print(err);
    Serial.print(" cruise:"); Serial.print(cruise);
    Serial.print(" L_spd:"); Serial.print(leftSpeed);
    Serial.print(" R_spd:"); Serial.print(rightSpeed);
    Serial.println(paused ? " PAUSED" : waiting ? " WAIT" : stopped ? " STOP" : "");
  }
}
