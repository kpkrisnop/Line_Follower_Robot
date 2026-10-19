# Tuner documentation

For the step-by-step procedure, open **Tuning guide** from the command palette (`ctrl+p`).

## Keys
| Key | Does |
|---|---|
| ↑ ↓ / click | pick a setting |
| ← → | nudge it by one step (sent and saved at once) |
| Enter / `e` / click again | type an exact value |
| space | run / pause (also restarts after OFFTRACK or STOP) |
| `m` | PID / bang-bang |
| `c` | calibrate sensors (5 s, slide the car across the line) |
| `n` | write a note to `tuning-log.md` |
| `a` | start / stop autotune |
| `f` | the last lap was fake (corner blip): drop it, re-run its trial |
| Esc | cancel typing, close this page |
| `ctrl+p` | command palette (guide, docs, theme…) |
| `ctrl+q` | quit |

## Screen
- **Live**: mode and state, sensor readings, err, cruise, wheel speeds; in lap mode the lap, last and best lap, last split and checkpoint count. The graph is the last 10 s of err. Red border = link lost. Bottom right, over Wi-Fi: the Mac's signal to the car (green above -70 dBm, yellow to -80, red below).
- **Settings**: every firmware setting. Changes are saved to the robot's EEPROM straight away.
- **Autotune**: score formula, search ranges, current trial and the best so far.
- **About**: what the selected setting does.
- **Slowdown curve**: cruise vs |err| from `base`, `slow`, `expo`, `min`. Red column = the live |err|.
- **Notes & laps**: the last rows of `tuning-log.md`.

## States
| State | Meaning |
|---|---|
| RUNNING | driving |
| PAUSED | motors off (`pause`, after `cal`, on USB connect) |
| WAIT | first 1 s after boot, motors off |
| STOP | `lap 0`: on the stop line |
| OFFTRACK | `lap 1`: both sensors black ≥ 1 s. Stays stopped until run (space) |

## Lap mode
- `lap 1`: a black crossing shorter than `mark` ms is a checkpoint (short high beep); `marks` of them make a lap. The first mark after run starts lap 1.
- `minlap`: a mark sooner than `minlap`/`marks` s after the last counted one is ignored (no beep), so corner blips can't make 0.1 s laps.
- Black for 1 s or more = off the track (the dark floor): stop, long low beep.
- `lap 0` (competition): the first black crossing stops the car.

## Autotune
- Searches `kp` 0.15–0.8, `kd` 0–1, `ki` 0–0.1 with Optuna, 30 trials. Trial 1 = the current values.
- Score = lap seconds + `smooth` × shake over the scored lap. Off track = 60. Lower is better.
- shake = mean |change in err| between status lines (10 Hz). Smooth laps have low shake; every lap row shows it, so you can pick `smooth`.
- `f` = the last lap was fake: it leaves best lap, and if it was scored its trial is dropped and run again.
- Values change mid-lap: the rest of that lap is warm-up, the next full lap is scored.
- Stopping (`a`) or finishing applies the best trial's values.
- Ranges, trial count and weights are constants at the top of `tuner.py` (`AUTO`, `AUTO_TRIALS`, `OFFTRACK_SCORE`). `smooth` is in Settings, saved in `tuner-settings.json`.
- The search lives in memory; a restart begins a new search. Every result is in `tuning-log.md`.

## Files
- `tuning-log.md`: notes, every finished lap, every trial score, with the full settings.
- `telemetry/<date-time>.csv`: every status line (10 Hz) of one tuner run: time, mode, state, trial, kp/kd/ki and all sensor fields. About 3 MB per hour. Not in git.

## Connection
- USB is found by the CH340 chip, whatever the port name. Opening USB resets the Uno; the tuner pauses the car within its 1 s boot wait.
- No USB → Wi-Fi `socket://192.168.77.1:23` (join `LineFollower`). The car is not paused. 2 s of silence = link lost, it reconnects by itself.
- **USB and the ESP D2 → D0 wire together = USB commands get lost.** Pull that wire for bench / USB work.
- Firmware uploads: direct USB only. If `MAGIC` changed, read the settings first and set them again afterwards.

## Settings reference
