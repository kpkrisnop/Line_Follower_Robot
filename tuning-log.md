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
| 2026-10-19 18:35 | BANG | kp 0.350 kd 0.000 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 0 marks 1 mark 300 | autotune stopped: no finished trials |
| 2026-10-19 18:38 | PID | kp 0.350 kd 0.000 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 173 trim 0 lap 1 marks 1 mark 300 | autotune stopped: no finished trials |
| 2026-10-19 18:39 | PID | kp 0.300 kd 0.000 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 173 trim 0 lap 1 marks 1 mark 300 | autotune stopped: no finished trials |
| 2026-10-19 18:49 | PID | kp 0.300 kd 0.000 ki 0.000 base 150 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.68 s, rms err 13 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 4.43 s, rms err 493 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 1.95 s, rms err 393 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.13 s, rms err 992 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.13 s, rms err 970 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.12 s, rms err 530 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.12 s, rms err 913 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.14 s, rms err 992 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.14 s, rms err 665 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.13 s, rms err 988 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.14 s, rms err 967 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.12 s, rms err 925 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.13 s, rms err 725 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.16 s, rms err 992 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.15 s, rms err 767 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.13 s, rms err 994 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.14 s, rms err 784 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.13 s, rms err 892 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.14 s, rms err 965 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.13 s, rms err 571 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.14 s, rms err 946 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.14 s, rms err 893 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.11 s, rms err 616 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.03 s, rms err 860 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.13 s, rms err 516 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.12 s, rms err 991 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.13 s, rms err 967 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.14 s, rms err 230 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.01 s, rms err 991 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.15 s, rms err 973 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.16 s, rms err 795 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.14 s, rms err 978 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.16 s, rms err 502 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.05 s, rms err 772 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.14 s, rms err 690 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.10 s, rms err 990 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.15 s, rms err 883 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.11 s, rms err 771 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.15 s, rms err 898 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.11 s, rms err 977 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.14 s, rms err 832 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.15 s, rms err 855 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.15 s, rms err 765 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.15 s, rms err 972 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.15 s, rms err 643 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.15 s, rms err 916 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.16 s, rms err 411 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.11 s, rms err 988 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.14 s, rms err 970 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.15 s, rms err 379 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.03 s, rms err 784 |
| 2026-10-19 18:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 353 trim 0 lap 1 marks 1 mark 300 | lap 0.04 s, rms err 924 |
| 2026-10-19 18:53 | PID | kp 0.300 kd 0.000 ki 0.000 base 130 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | lap 0.01 s, rms err 836 |
| 2026-10-19 18:53 | PID | kp 0.300 kd 0.000 ki 0.000 base 130 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | trial 1: lap 0.01 s, rms err 751 → score 7.52 |
| 2026-10-19 18:53 | PID | kp 1.260 kd 1.220 ki 0.009 base 130 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | lap 0.27 s, rms err 470 |
| 2026-10-19 18:53 | PID | kp 1.260 kd 1.220 ki 0.009 base 130 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | trial 2: lap 0.23 s, rms err 917 → score 9.40 |
| 2026-10-19 18:53 | PID | kp 2.000 kd 1.200 ki 0.033 base 130 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | lap 0.57 s, rms err 592 |
| 2026-10-19 18:53 | PID | kp 2.000 kd 1.200 ki 0.033 base 130 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | trial 3: lap 0.62 s, rms err 546 → score 6.08 |
| 2026-10-19 18:53 | PID | kp 0.340 kd 0.860 ki 0.056 base 130 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | lap 0.53 s, rms err 502 |
| 2026-10-19 18:53 | PID | kp 0.340 kd 0.860 ki 0.056 base 130 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | trial 4: lap 1.51 s, rms err 395 → score 5.47 |
| 2026-10-19 18:53 | PID | kp 1.540 kd 0.860 ki 0.054 base 130 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | lap 0.56 s, rms err 496 |
| 2026-10-19 18:53 | PID | kp 1.540 kd 0.860 ki 0.054 base 130 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | trial 5: lap 0.81 s, rms err 628 → score 7.09 |
| 2026-10-19 18:53 | PID | kp 1.040 kd 0.470 ki 0.057 base 130 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | lap 0.28 s, rms err 276 |
| 2026-10-19 18:53 | PID | kp 1.040 kd 0.470 ki 0.057 base 130 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | trial 6: lap 0.28 s, rms err 413 → score 4.41 |
| 2026-10-19 18:53 | PID | kp 1.040 kd 0.220 ki 0.070 base 130 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | lap 1.23 s, rms err 604 |
| 2026-10-19 18:54 | PID | kp 1.040 kd 0.220 ki 0.070 base 130 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | trial 7: OFFTRACK → score 60 |
| 2026-10-19 18:55 | PID | kp 0.480 kd 0.220 ki 0.070 base 130 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | lap 0.10 s, rms err 79 |
| 2026-10-19 18:57 | PID | (not connected) | lap 0.34 s, rms err 4 |
| 2026-10-19 18:57 | �PID | kp 0.200 kd 0.220 ki 0.070 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | lap 0.01 s, rms err 3 |
| 2026-10-19 18:58 | �����������������}=*�ɂ�ե͕�5����5�����b���b������������PID | kp 0.300 kd 0.220 ki 0.070 base 120 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | autotune stopped: no finished trials |
| 2026-10-19 19:51 | PID | kp 0.300 kd 0.000 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 1 mark 200 | autotune stopped: no finished trials |
| 2026-10-19 19:54 | PID | kp 0.300 kd 0.000 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 2 mark 200 | lap 6.30 s, rms err 0 |
| 2026-10-19 19:54 | PID | kp 0.300 kd 0.000 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 2 mark 200 | lap 6.30 s, rms err 0 |
| 2026-10-19 19:57 | PID | kp 0.300 kd 0.000 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 200 trim 0 lap 1 marks 2 mark 200 | lap 13.05 s, rms err 0 |
| 2026-10-19 20:04 | PID | kp 0.300 kd 0.000 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 200 | lap 6.93 s, rms err 406 |
| 2026-10-19 20:04 | PID | kp 0.300 kd 0.000 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 200 | trial 1: lap 0.21 s, rms err 715 → score 7.36 |
| 2026-10-19 20:04 | PID | kp 1.170 kd 0.180 ki 0.087 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 200 | lap 0.16 s, rms err 381 |
| 2026-10-19 20:04 | PID | kp 1.170 kd 0.180 ki 0.087 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 200 | trial 2: lap 0.31 s, rms err 728 → score 7.59 |
| 2026-10-19 20:04 | PID | kp 0.860 kd 0.520 ki 0.005 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 200 | lap 0.27 s, rms err 964 |
| 2026-10-19 20:04 | PID | kp 0.860 kd 0.520 ki 0.005 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 200 | trial 3: lap 0.28 s, rms err 923 → score 9.51 |
| 2026-10-19 20:04 | PID | kp 0.490 kd 0.520 ki 0.005 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 200 | lap 0.22 s, rms err 825 |
| 2026-10-19 20:04 | PID | kp 0.490 kd 0.520 ki 0.005 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 200 | trial 4: lap 0.12 s, rms err 328 → score 3.39 |
| 2026-10-19 20:04 | PID | kp 0.720 kd 0.520 ki 0.005 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 200 | lap 0.19 s, rms err 147 |
| 2026-10-19 20:04 | PID | kp 0.720 kd 1.310 ki 0.042 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 200 | trial 5: lap 0.14 s, rms err 775 → score 7.88 |
| 2026-10-19 20:04 | PID | kp 0.730 kd 1.600 ki 0.042 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 200 | lap 0.45 s, rms err 209 |
| 2026-10-19 20:04 | PID | kp 0.730 kd 1.600 ki 0.042 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 200 | trial 6: lap 0.58 s, rms err 170 → score 2.27 |
| 2026-10-19 20:04 | PID | kp 0.940 kd 0.560 ki 0.004 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 200 | trial 7: OFFTRACK → score 60 |
| 2026-10-19 20:30 | PID | kp 0.300 kd 0.000 ki 0.086 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 200 minlap 2 | trial 1: OFFTRACK → score 60 |
| 2026-10-19 20:31 | PID | kp 0.540 kd 1.900 ki 0.086 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 200 minlap 2 | lap 11.62 s, rms err 485 |
| 2026-10-19 20:31 | PID | kp 0.540 kd 1.900 ki 0.086 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 280 minlap 2 | trial 2: OFFTRACK → score 60 |
| 2026-10-19 20:34 | PID | kp 0.410 kd 1.900 ki 0.086 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | lap 15.43 s, rms err 0 |
| 2026-10-19 20:35 | PID | kp 0.300 kd 0.000 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | lap 7.15 s, rms err 428 |
| 2026-10-19 20:35 | PID | kp 0.300 kd 0.000 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | trial 1: lap 20.29 s, rms err 496 → score 25.25 |
| 2026-10-19 20:35 | PID | kp 1.200 kd 1.000 ki 0.009 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | lap 8.36 s, rms err 549 |
| 2026-10-19 20:36 | PID | kp 1.200 kd 1.000 ki 0.009 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | trial 2: lap 16.73 s, rms err 250 → score 19.23 |
| 2026-10-19 20:36 | PID | kp 0.620 kd 1.940 ki 0.063 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | lap 29.18 s, rms err 451 |
| 2026-10-19 20:37 | PID | kp 0.620 kd 1.940 ki 0.063 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | trial 3: lap 15.71 s, rms err 472 → score 20.43 |
| 2026-10-19 20:38 | PID | kp 1.200 kd 1.030 ki 0.009 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | autotune stopped: best trial 2, score 19.23 |
| 2026-10-19 20:39 | ���PID | kp 1.200 kd 1.000 ki 0.009 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | lap 19.58 s, rms err 328 |
| 2026-10-19 20:39 | PID | kp 1.200 kd 1.000 ki 0.009 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | trial 1: lap 19.92 s, rms err 330 → score 23.23 |
| 2026-10-19 20:39 | PID | kp 0.820 kd 0.900 ki 0.039 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | lap 22.78 s, rms err 354 |
| 2026-10-19 20:40 | PID | kp 0.820 kd 0.900 ki 0.039 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | trial 2: OFFTRACK → score 60 |
| 2026-10-19 20:41 | PID | kp 1.900 kd 0.750 ki 0.029 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | lap 2.13 s, rms err 835 |
| 2026-10-19 20:41 | PID | kp 1.900 kd 0.750 ki 0.029 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | trial 3: lap 2.06 s, rms err 537 → score 7.43 |
| 2026-10-19 20:41 | PID | kp 1.890 kd 1.660 ki 0.001 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | lap 2.20 s, rms err 449 |
| 2026-10-19 20:41 | PID | kp 1.890 kd 1.660 ki 0.001 base 100 slow 0.300 expo 3.00 min 80 turn 510 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | trial 4: lap 16.66 s, rms err 243 → score 19.09 |
| 2026-10-19 20:45 | PID | kp 0.200 kd 0.000 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 350 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | autotune stopped: no finished trials |
| 2026-10-19 20:46 | PID | kp 0.200 kd 0.000 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 350 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | lap 13.81 s, rms err 417 |
| 2026-10-19 20:46 | PID | kp 0.200 kd 0.000 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 350 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | trial 1: lap 14.57 s, rms err 479 → score 19.36 |
| 2026-10-19 20:46 | PID | kp 0.310 kd 0.710 ki 0.089 base 100 slow 0.300 expo 3.00 min 80 turn 350 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 330 minlap 2 | lap 16.17 s, rms err 617 |
| 2026-10-19 20:46 | PID | kp 0.310 kd 0.710 ki 0.089 base 100 slow 0.300 expo 3.00 min 80 turn 350 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | trial 2: lap 12.54 s, rms err 659 → score 19.12 |
| 2026-10-19 20:47 | PID | kp 0.580 kd 0.580 ki 0.030 base 100 slow 0.300 expo 3.00 min 80 turn 350 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | lap 11.12 s, rms err 413 |
| 2026-10-19 20:47 | PID | kp 0.580 kd 0.580 ki 0.030 base 100 slow 0.300 expo 3.00 min 80 turn 350 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | trial 3: lap 23.97 s, rms err 411 → score 28.09 |
| 2026-10-19 20:47 | PID | kp 0.790 kd 0.880 ki 0.025 base 100 slow 0.300 expo 3.00 min 80 turn 350 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | lap 16.65 s, rms err 204 |
| 2026-10-19 20:47 | PID | kp 0.790 kd 0.880 ki 0.025 base 100 slow 0.300 expo 3.00 min 80 turn 350 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | trial 4: lap 15.49 s, rms err 194 → score 17.43 |
| 2026-10-19 20:48 | PID | kp 0.450 kd 0.230 ki 0.034 base 100 slow 0.300 expo 3.00 min 80 turn 350 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | lap 2.55 s, rms err 661 |
| 2026-10-19 20:48 | PID | kp 0.450 kd 0.230 ki 0.034 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | trial 5: lap 37.39 s, rms err 691 → score 44.30 |
| 2026-10-19 20:49 | PID | kp 0.220 kd 0.370 ki 0.090 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | lap 33.68 s, rms err 667 |
| 2026-10-19 20:49 | PID | kp 0.220 kd 0.370 ki 0.090 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | trial 6: OFFTRACK → score 60 |
| 2026-10-19 20:49 | PID | kp 0.540 kd 0.030 ki 0.023 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | lap 4.73 s, rms err 543 |
| 2026-10-19 20:49 | PID | kp 0.540 kd 0.030 ki 0.023 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | trial 7: lap 4.21 s, rms err 447 → score 8.68 |
| 2026-10-19 20:49 | PID | kp 0.390 kd 0.790 ki 0.026 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | lap 12.11 s, rms err 257 |
| 2026-10-19 20:50 | PID | kp 0.390 kd 0.790 ki 0.026 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | trial 8: lap 15.54 s, rms err 286 → score 18.39 |
| 2026-10-19 20:50 | PID | kp 0.270 kd 0.140 ki 0.085 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | trial 9: OFFTRACK → score 60 |
| 2026-10-19 20:50 | PID | kp 0.590 kd 0.220 ki 0.004 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | lap 14.86 s, rms err 272 |
| 2026-10-19 20:51 | PID | kp 0.590 kd 0.220 ki 0.004 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | trial 10: lap 16.24 s, rms err 264 → score 18.89 |
| 2026-10-19 20:51 | PID | kp 0.170 kd 0.700 ki 0.050 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | lap 6.21 s, rms err 551 |
| 2026-10-19 20:51 | PID | kp 0.170 kd 0.700 ki 0.050 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | trial 11: lap 3.13 s, rms err 501 → score 8.15 |
| 2026-10-19 20:51 | PID | kp 0.180 kd 0.790 ki 0.055 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | lap 3.19 s, rms err 594 |
| 2026-10-19 20:51 | PID | kp 0.180 kd 0.790 ki 0.055 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | trial 12: lap 15.51 s, rms err 571 → score 21.22 |
| 2026-10-19 20:51 | PID | kp 0.270 kd 0.540 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | lap 13.07 s, rms err 227 |
| 2026-10-19 20:51 | PID | kp 0.270 kd 0.540 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | trial 13: lap 12.70 s, rms err 227 → score 14.96 |
| 2026-10-19 20:52 | PID | kp 0.690 kd 0.540 ki 0.073 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | lap 3.27 s, rms err 611 |
| 2026-10-19 20:52 | PID | kp 0.690 kd 0.540 ki 0.073 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | trial 14: lap 2.44 s, rms err 712 → score 9.57 |
| 2026-10-19 20:52 | PID | kp 0.320 kd 0.850 ki 0.050 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 2 | lap 2.72 s, rms err 540 |
| 2026-10-19 20:52 | PID | kp 0.320 kd 0.850 ki 0.050 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 15: lap 13.83 s, rms err 524 → score 19.07 |
| 2026-10-19 20:52 | PID | kp 0.320 kd 0.740 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | lap 12.80 s, rms err 204 |
| 2026-10-19 20:52 | PID | kp 0.320 kd 0.740 ki 0.000 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 16: lap 12.98 s, rms err 208 → score 15.07 |
| 2026-10-19 20:52 | PID | kp 0.160 kd 0.260 ki 0.028 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | lap 6.28 s, rms err 524 |
| 2026-10-19 20:52 | PID | kp 0.160 kd 0.260 ki 0.028 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 17: lap 6.34 s, rms err 593 → score 12.27 |
| 2026-10-19 20:53 | PID | kp 0.430 kd 0.470 ki 0.011 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | lap 13.59 s, rms err 223 |
| 2026-10-19 20:53 | PID | kp 0.430 kd 0.470 ki 0.011 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 18: lap 11.02 s, rms err 189 → score 12.91 |
| 2026-10-19 20:53 | PID | kp 0.500 kd 0.670 ki 0.067 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | lap 5.62 s, rms err 500 |
| 2026-10-19 20:53 | PID | kp 0.500 kd 0.670 ki 0.067 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 19: OFFTRACK → score 60 |
| 2026-10-19 20:53 | PID | kp 0.280 kd 0.090 ki 0.045 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 20: OFFTRACK → score 60 |
| 2026-10-19 20:54 | PID | kp 0.410 kd 0.090 ki 0.051 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 21: OFFTRACK → score 60 |
| 2026-10-19 20:54 | PID | kp 0.680 kd 0.300 ki 0.058 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | lap 14.85 s, rms err 640 |
| 2026-10-19 20:55 | PID | kp 0.680 kd 0.300 ki 0.058 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 22: lap 25.35 s, rms err 674 → score 32.10 |
| 2026-10-19 20:55 | PID | kp 0.690 kd 0.000 ki 0.041 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | lap 27.94 s, rms err 683 |
| 2026-10-19 20:56 | PID | kp 0.690 kd 0.000 ki 0.041 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 23: lap 27.79 s, rms err 724 → score 35.04 |
| 2026-10-19 20:56 | PID | kp 0.690 kd 0.580 ki 0.064 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | lap 24.72 s, rms err 639 |
| 2026-10-19 20:57 | PID | kp 0.690 kd 0.580 ki 0.064 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 24: lap 24.25 s, rms err 643 → score 30.68 |
| 2026-10-19 20:57 | PID | kp 0.190 kd 0.610 ki 0.038 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | lap 22.05 s, rms err 548 |
| 2026-10-19 20:57 | PID | kp 0.190 kd 0.610 ki 0.038 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 25: lap 21.41 s, rms err 530 → score 26.71 |
| 2026-10-19 20:58 | PID | kp 0.560 kd 0.430 ki 0.085 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 26: OFFTRACK → score 60 |
| 2026-10-19 20:58 | PID | kp 0.620 kd 0.930 ki 0.082 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | lap 23.93 s, rms err 622 |
| 2026-10-19 20:59 | PID | kp 0.620 kd 0.930 ki 0.082 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 27: lap 23.67 s, rms err 641 → score 30.07 |
| 2026-10-19 20:59 | PID | kp 0.790 kd 0.000 ki 0.068 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 28: OFFTRACK → score 60 |
| 2026-10-19 21:00 | PID | kp 0.600 kd 0.720 ki 0.088 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 29: OFFTRACK → score 60 |
| 2026-10-19 21:01 | PID | kp 0.440 kd 0.060 ki 0.021 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | lap 25.18 s, rms err 635 |
| 2026-10-19 21:01 | PID | kp 0.440 kd 0.060 ki 0.021 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | trial 30: lap 25.30 s, rms err 611 → score 31.41 |
| 2026-10-19 21:01 | PID | kp 0.170 kd 0.700 ki 0.050 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | autotune done: best trial 11, score 8.15 |
| 2026-10-19 21:01 | PID | kp 0.170 kd 0.700 ki 0.050 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | lap 22.33 s, rms err 581 |
| 2026-10-19 21:02 | PID | kp 0.170 kd 0.700 ki 0.050 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 | lap 20.55 s, rms err 564 |
| 2026-10-20 21:11 | '�}=�0 | kp 0.170 kd 0.700 ki 0.050 base 100 slow 0.300 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 2 mark 500 minlap 5 smooth 0.030 | lap 6.30 s, shake 0, rms err 1 |
| 2026-10-20 21:27 | PID | kp 0.200 kd 0.000 ki 0.000 base 150 slow 0.080 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 500 minlap 5 smooth 0.030 | trial 1: OFFTRACK → score 60 |
| 2026-10-20 21:28 | PID | kp 0.750 kd 0.680 ki 0.038 base 150 slow 0.080 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 500 minlap 5 smooth 0.030 | lap 26.13 s, shake 504, rms err 450 |
| 2026-10-20 21:28 | PID | kp 0.750 kd 0.680 ki 0.038 base 150 slow 0.080 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 500 minlap 5 smooth 0.030 | trial 2: lap 5.17 s, shake 474, rms err 374 → score 19.40 |
| 2026-10-20 21:35 | PID | kp 0.260 kd 0.580 ki 0.100 base 150 slow 0.080 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 500 minlap 5 smooth 0.030 | lap 5.45 s, shake 0, rms err 655 |
| 2026-10-20 21:36 | PID | kp 0.260 kd 0.580 ki 0.100 base 150 slow 0.080 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 500 minlap 20 smooth 0.030 | lap 35.57 s, shake 936, rms err 666 |
| 2026-10-20 21:39 | PID | kp 0.260 kd 0.580 ki 0.100 base 150 slow 0.080 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 400 minlap 30 smooth 0.030 | trial 1: lap 62.24 s, shake 939, rms err 660 → score 90.41 |
| 2026-10-20 21:39 | PID | kp 0.350 kd 0.910 ki 0.018 base 150 slow 0.080 expo 3.00 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 400 minlap 30 smooth 0.030 | trial 2: OFFTRACK → score 60 |
| 2026-10-20 22:26 | PID | kp 0.200 kd 0.000 ki 0.000 base 150 slow 0.080 expo 3.00 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 30 smooth 0.030 | trial 1: OFFTRACK → score 60 |
| 2026-10-20 22:27 | PID | kp 0.190 kd 0.450 ki 0.058 base 150 slow 0.080 expo 3.00 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 30 smooth 0.030 | lap 33.26 s, shake 932, rms err 642 |
| 2026-10-20 22:28 | PID | kp 0.190 kd 0.450 ki 0.058 base 150 slow 0.080 expo 3.00 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 30 smooth 0.030 | trial 2: lap 32.36 s, shake 820, rms err 592 → score 56.96 |
| 2026-10-20 22:28 | PID | kp 0.730 kd 0.360 ki 0.045 base 150 slow 0.080 expo 3.00 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 30 smooth 0.030 | lap 33.34 s, shake 1253, rms err 652 |
| 2026-10-20 22:28 | PID | kp 0.730 kd 0.360 ki 0.045 base 150 slow 0.080 expo 3.00 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 30 smooth 0.030 | trial 3: OFFTRACK → score 60 |
| 2026-10-20 22:31 | PID | smooth 0.030 | lap 34.15 s, shake 0, rms err 0 |
| 2026-10-20 22:34 | PID | kp 0.300 kd 0.710 ki 0.084 base 150 slow 0.080 expo 3.00 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 30 smooth 0.030 | lap 33.35 s, shake 966, rms err 625 |
| 2026-10-20 22:35 | PID | kp 0.300 kd 0.710 ki 0.084 base 150 slow 0.080 expo 3.00 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 30 smooth 0.030 | lap 33.20 s, shake 973, rms err 634 |
| 2026-10-20 22:36 | PID | kp 0.300 kd 0.710 ki 0.084 base 150 slow 0.080 expo 3.00 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 30 smooth 0.060 | lap 38.66 s, shake 937, rms err 628 |
| 2026-10-20 22:36 | PID | kp 0.300 kd 0.710 ki 0.084 base 120 slow 0.080 expo 2.80 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 30 smooth 0.100 | lap 40.85 s, shake 958, rms err 621 |
| 2026-10-20 22:37 | PID | kp 0.300 kd 0.710 ki 0.084 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 30 smooth 0.130 | trial 1: lap 47.23 s, shake 959, rms err 617 → score 171.91 |
| 2026-10-20 22:38 | PID | kp 0.670 kd 0.400 ki 0.030 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 350 trim 0 lap 1 marks 1 mark 250 minlap 30 smooth 0.130 | lap 33.24 s, shake 863, rms err 567 |
| 2026-10-20 22:38 | PID | kp 0.670 kd 0.400 ki 0.030 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 400 trim 0 lap 1 marks 1 mark 300 minlap 30 smooth 0.130 | trial 2: lap 40.63 s, shake 745, rms err 538 → score 137.54 |
| 2026-10-20 22:39 | PID | kp 0.780 kd 0.120 ki 0.026 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 400 trim 0 lap 1 marks 1 mark 300 minlap 30 smooth 0.200 | lap 32.03 s, shake 963, rms err 630 |
| 2026-10-20 22:39 | PID | kp 0.780 kd 0.120 ki 0.026 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 400 trim 0 lap 1 marks 1 mark 300 minlap 30 smooth 0.200 | trial 3: OFFTRACK → score 60 |
| 2026-10-20 22:39 | PID | kp 0.380 kd 0.470 ki 0.015 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 400 trim 0 lap 1 marks 1 mark 300 minlap 20 smooth 0.200 | lap 24.40 s, shake 383, rms err 380 |
| 2026-10-20 22:40 | PID | kp 0.380 kd 0.470 ki 0.015 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 400 trim 0 lap 1 marks 1 mark 300 minlap 20 smooth 0.200 | trial 4: lap 21.01 s, shake 353, rms err 370 → score 91.57 |
| 2026-10-20 22:40 | PID | kp 0.170 kd 0.270 ki 0.012 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 400 trim 0 lap 1 marks 1 mark 300 minlap 20 smooth 0.200 | trial 5: OFFTRACK → score 60 |
| 2026-10-20 22:41 | PID | kp 0.500 kd 0.200 ki 0.084 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 400 trim 0 lap 1 marks 1 mark 300 minlap 25 smooth 0.200 | trial 6: OFFTRACK → score 60 |
| 2026-10-20 22:41 | PID | kp 0.160 kd 0.570 ki 0.100 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 400 trim 0 lap 1 marks 1 mark 300 minlap 25 smooth 0.200 | trial 7: OFFTRACK → score 60 |
| 2026-10-20 22:42 | PID | kp 0.650 kd 0.700 ki 0.005 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 20 smooth 0.200 | lap 24.48 s, shake 463, rms err 432 |
| 2026-10-20 22:43 | PID | kp 0.650 kd 0.700 ki 0.005 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 25 smooth 0.200 | trial 8: lap 28.31 s, shake 382, rms err 380 → score 104.72 |
| 2026-10-20 22:44 | PID | kp 0.700 kd 0.150 ki 0.057 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 25 smooth 0.200 | lap 38.46 s, shake 898, rms err 631 |
| 2026-10-20 22:44 | PID | kp 0.700 kd 0.150 ki 0.057 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 25 smooth 0.200 | lap 38.46 s marked fake |
| 2026-10-20 22:45 | PID | kp 0.700 kd 0.150 ki 0.057 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 25 smooth 0.200 | trial 9: lap 27.30 s, shake 1103, rms err 698 → score 247.87 |
| 2026-10-20 22:45 | PID | kp 0.740 kd 0.520 ki 0.086 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 25 smooth 0.200 | trial 10: OFFTRACK → score 60 |
| 2026-10-21 10:44 | PID | kp 0.490 kd 0.960 ki 0.045 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 25 smooth 0.200 | trial 11: OFFTRACK → score 60 |
| 2026-10-21 10:45 | PID | kp 0.230 kd 0.000 ki 0.005 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 25 smooth 0.200 | trial 12: OFFTRACK → score 60 |
| 2026-10-21 10:46 | PID | kp 0.200 kd 0.100 ki 0.051 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 25 smooth 0.200 | trial 13: OFFTRACK → score 60 |
| 2026-10-21 10:47 | PID | kp 0.500 kd 0.160 ki 0.004 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 25 smooth 0.200 | lap 39.19 s, shake 1217, rms err 715 |
| 2026-10-21 10:47 | PID | kp 0.500 kd 0.160 ki 0.004 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 25 smooth 0.200 | lap 39.19 s marked fake |
| 2026-10-21 10:48 | PID | kp 0.500 kd 0.160 ki 0.004 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 40 smooth 0.300 | trial 14: lap 45.86 s, shake 1193, rms err 712 → score 403.63 |
| 2026-10-21 10:48 | PID | kp 0.530 kd 0.030 ki 0.044 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 40 smooth 0.300 | trial 15: OFFTRACK → score 60 |
| 2026-10-21 10:49 | PID | kp 0.240 kd 0.240 ki 0.024 base 120 slow 0.020 expo 3.30 min 80 turn 300 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 45 smooth 0.300 | trial 16: OFFTRACK → score 60 |
| 2026-10-21 10:49 | PID | kp 0.800 kd 0.430 ki 0.043 base 120 slow 0.020 expo 3.30 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 45 smooth 0.300 | trial 17: OFFTRACK → score 60 |
| 2026-10-21 10:50 | PID | kp 0.520 kd 0.000 ki 0.021 base 120 slow 0.020 expo 3.30 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 45 smooth 0.300 | trial 18: OFFTRACK → score 60 |
| 2026-10-21 10:50 | PID | kp 0.510 kd 0.230 ki 0.030 base 120 slow 0.020 expo 3.30 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 45 smooth 0.300 | trial 19: OFFTRACK → score 60 |
| 2026-10-21 10:50 | PID | kp 0.360 kd 0.330 ki 0.050 base 120 slow 0.020 expo 3.30 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 45 smooth 0.300 | trial 20: OFFTRACK → score 60 |
| 2026-10-21 10:50 | PID | kp 0.780 kd 0.120 ki 0.026 base 120 slow 0.020 expo 3.30 min 80 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 45 smooth 0.300 | autotune stopped: best trial 3, score 60.00 |
| 2026-10-21 10:51 | PID | kp 0.200 kd 0.000 ki 0.000 base 150 slow 0.070 expo 3.30 min 100 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 45 smooth 0.300 | trial 1: OFFTRACK → score 60 |
| 2026-10-21 10:51 | PID | kp 0.250 kd 0.200 ki 0.054 base 150 slow 0.070 expo 3.30 min 100 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 45 smooth 0.300 | trial 2: OFFTRACK → score 60 |
| 2026-10-21 10:51 | PID | kp 0.710 kd 0.240 ki 0.099 base 150 slow 0.070 expo 3.30 min 100 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 45 smooth 0.300 | trial 3: OFFTRACK → score 60 |
| 2026-10-21 10:52 | PID | kp 0.740 kd 0.780 ki 0.066 base 150 slow 0.070 expo 3.30 min 100 turn 250 bang 80 off 0 stop 500 trim 0 lap 1 marks 1 mark 300 minlap 45 smooth 0.300 | trial 4: OFFTRACK → score 60 |
