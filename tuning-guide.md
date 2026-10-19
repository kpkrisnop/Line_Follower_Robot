# Tuning guide

Do the steps in order. Change **one value at a time** and press `n` to note what the car did.

## 0. Before you start
- Battery charged (about 8.5 V). Speeds get weaker as it drains, so note the battery state.
- **On the track:** battery power, USB unplugged, both ESP wires on (UNO D1 → ESP D1, ESP D2 → UNO D0). Join Wi-Fi `LineFollower`, run `robot`.
- Over Wi-Fi the car is **not** paused on connect. Space runs and pauses it.

## 1. Calibrate the sensors (`c`)
1. Hold the car with the sensors just above the track, on white.
2. Press `c`. Beep → you have **5 s**: slide the car sideways back and forth across the line so both sensors see black and white.
3. Second beep: `cal done`, or `cal failed` (a sensor saw too small a range; old values kept, try again).
4. The car stays paused afterwards.
- **Recalibrate at every new venue** (lighting changes the readings).
- After a calibration, err's range widens; you may need to lower `kp` 10–15 %.

## 2. Centre the sensors (`off`)
Car still, both sensors on white: set `off` until `L_AO` ≈ `R_AO`.

## 3. Balance the motors (`trim`)
Test at your normal `base`, not full speed (`trim` is a percentage).
1. Set `ki 0` for this test (the integral hides the drift).
2. Let the car follow a **long straight** and watch `err`:
   - err averages **positive** (left motor stronger) → **raise** `trim`.
   - err averages **negative** → **lower** `trim`.
3. Change it 1–2 % at a time until err hovers around 0, then put `ki` back.

Cross-check without a line: write your gains down, set `kp 0 kd 0 ki 0`, run on plain floor. It should go straight; if it curves, the motor on the outside of the curve is stronger. Put the gains back afterwards (everything is saved to EEPROM).

## 4. Check the steering direction
If PID steers *away* from the line, negate `kp` and `kd`.

## 5. PID gains by hand
1. Raise `kp` until it follows the line.
2. Raise `kd` until it stops wobbling. If lowering `kp` makes twitching worse, `kd` is too high for that `kp`.
3. `ki`: leave at 0 unless it drifts to one side or loses tight turns. A little helps in tight 90° turns. It can add at most `ki × 2000`.

## 6. Corners: `slow`, `expo`, `min`
Watch the **Slowdown curve** box while you change these.
- `min` must be **below** `base`; at or above it there is no slowdown at all, whatever `slow` and `expo` say.
- At `slow` 1.3 or more (with `expo 1`), almost every curve runs at `min`.
- `expo` above 1 keeps speed on gentle wobbles and brakes only in real corners.
- `turn` (steering cap) exists, but in testing it didn't help much. Leave it at 510 unless corners saturate.

## 7. Lap mode on the loop
1. `lap 1`, then `marks` = the number of tape marks you laid per lap.
2. Do a few slow laps: each counted mark gives a short high beep. If marks are missed at speed, raise `mark` (ms); it must stay well under 1000 (1 s of black = off track).
   Laps far shorter than the real one (corner blips counted as marks)? Set `minlap` a bit under your real lap time in s.
3. Off the track (black ≥ 1 s): long low beep, the car stops. Put it back on the line, press space.

## 8. Autotune (`a`)
1. Car running on the loop, `marks` set, Wi-Fi connected.
2. Press `a`. It tries 30 sets of `kp`/`kd`/`ki` (about 20 min). Trial 1 is your current values.
3. Each trial: the rest of the current lap is warm-up, the next full lap is scored (lap s + `smooth` × shake; off track = 60).
   Pick `smooth` first: compare the shake of a smooth lap and a shaky one in Notes, and raise it until the shaky one scores worse.
   A lap flagged ⚠ short, or one you saw was fake: press `f` straight away (before the next lap).
4. If it goes off the track, put it back and press space.
5. `a` again stops early. Stopping or finishing **applies the best values**.

## 9. Competition
- `lap 0`: the first stop line stops the car.
- Recalibrate (`c`) at the venue, check `off` and `stop`.
