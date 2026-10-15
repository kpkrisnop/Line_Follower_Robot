# Tuning log

| Time | Mode | Settings | Note |
|---|---|---|---|
| 2026-10-15 14:56 | PID | kp 2.000 kd 0.200 ki 0.000 base 200 slow 0.000 min 80 bang 80 off 0 | off track |
| 2026-10-15 14:58 | PID | kp 1.500 kd 0.300 ki 0.000 base 200 slow 0.000 min 80 bang 80 off 0 | lower kp higher kd |
| 2026-10-15 14:58 | PID | kp 1.500 kd 0.300 ki 0.000 base 200 slow 0.000 min 80 bang 80 off 0 | too waggly on straight lines |
| 2026-10-15 15:00 | PID | kp 1.500 kd 0.300 ki 0.000 base 180 slow 0.000 min 80 bang 80 off 0 | goes off track, still zigzag on straightline |
| 2026-10-15 15:03 | PID | kp 0.950 kd 0.300 ki 0.000 base 180 slow 0.100 min 80 bang 80 off 0 | twitching on straightline |
| 2026-10-15 15:05 | PID | kp 0.950 kd 0.300 ki 0.000 base 180 slow 0.100 min 60 bang 80 off 0 | works, but slower or same |
| 2026-10-15 15:06 | PID | kp 0.950 kd 0.300 ki 0.000 base 255 slow 0.100 min 60 bang 80 off 0 | goes off track, sometimes faster not stable |
| 2026-10-15 15:07 | PID | kp 0.750 kd 0.500 ki 0.000 base 255 slow 0.150 min 60 bang 80 off 0 | not turning but increased kd |
| 2026-10-15 15:08 | PID | kp 0.750 kd 0.500 ki 0.000 base 255 slow 0.150 min 60 bang 80 off 0 | working but off track |
| 2026-10-15 15:09 | PID | kp 0.750 kd 0.500 ki 0.000 base 255 slow 0.300 min 60 bang 80 off 0 | not working, off track too  much, twitching |
| 2026-10-15 15:12 | PID | kp 1.200 kd 0.700 ki 0.000 base 225 slow 0.200 min 60 bang 80 off 0 | twitching on straight line |
| 2026-10-15 15:15 | PID | kp 1.200 kd 0.700 ki 0.000 base 225 slow 0.400 min 60 bang 80 off 0 | added 0.2 more slow, doesnt make thro corners |
| 2026-10-15 15:18 | PID | kp 1.200 kd 0.700 ki 0.000 base 225 slow 1.300 min 60 bang 80 off 0 | added err 0,3  makes thro most turns and WORKS |
| 2026-10-15 15:19 | PID | kp 1.200 kd 0.700 ki 0.000 base 225 slow 1.300 min 60 bang 80 off 0 | WORKS |
| 2026-10-15 15:20 | PID | kp 1.000 kd 0.700 ki 0.000 base 225 slow 1.300 min 60 bang 80 off 0 | reduced kp -.2 twitching more |
| 2026-10-15 15:30 | PID | kp 1.000 kd 0.500 ki 0.000 base 225 slow 1.300 min 60 bang 80 off 9 | WORKS |
| 2026-10-15 15:43 | PID | kp 1.200 kd 0.500 ki 0.000 base 200 slow 2.000 min 60 bang 80 off 9 | works but offtrack |
| 2026-10-15 15:56 | PID | kp 1.400 kd 0.600 ki 0.000 base 240 slow 3.000 min 60 bang 80 off 10 | slow must be below 2 |
| 2026-10-15 16:09 | PID | kp 0.900 kd 0.500 ki 0.000 base 180 slow 3.000 min 120 bang 80 off -1 | 21 sec |
