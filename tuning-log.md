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
