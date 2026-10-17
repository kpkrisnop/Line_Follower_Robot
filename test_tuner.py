# /// script
# requires-python = ">=3.11"
# dependencies = ["textual>=0.80", "pyserial>=3.5"]
# ///
"""Garbled serial lines must not crash the tuner. Run: uv run test_tuner.py"""
import asyncio

import tuner

GARBAGE = [
    "mode PID PAUSED | k ki 0.000 kd 0.500 base 180 slow",  # seen live 2026-10-17
    "saved: | kp 0.900",
    "PID L_DO:0 err:. L_spd:0",
    "mode PID PAUSED | kp 0.9x0 ki 0.000",
]


async def main():
    tuner.Tuner.serial_loop = lambda self: None  # no hardware
    app = tuner.Tuner()
    async with app.run_test():
        for line in GARBAGE:
            app.handle_line(line)  # raised before the fix → killed the serial thread
        app.handle_line("mode PID PAUSED | kp 0.900 ki 0.000 kd 0.500")
        assert app.query_one(tuner.Settings).values["kd"] == 0.5
    print("ok")


asyncio.run(main())
