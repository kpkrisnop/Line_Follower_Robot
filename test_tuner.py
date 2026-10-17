# /// script
# requires-python = ">=3.11"
# dependencies = ["textual>=0.80", "pyserial>=3.5"]
# ///
"""Tuner checks against fake robots, no hardware. Run: uv run test_tuner.py"""
import asyncio
import os
import socket
import threading
import time

import tuner

REAL_LOOP = tuner.Tuner.serial_loop

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
    print("ok", flush=True)


async def silent_wifi():
    """A Wi-Fi drop keeps the socket open but goes quiet: the tuner must show it's lost."""
    srv = socket.create_server(("127.0.0.1", 0))
    tuner.WIFI = f"socket://127.0.0.1:{srv.getsockname()[1]}"
    tuner.find_port = lambda: tuner.WIFI
    def robot():
        conn, _ = srv.accept()
        conn.sendall(STATUS)
        time.sleep(60)  # stay connected, say nothing

    threading.Thread(target=robot, daemon=True).start()
    tuner.Tuner.serial_loop = REAL_LOOP  # main() stubbed it out
    app = tuner.Tuner()
    async with app.run_test() as pilot:
        await pilot.pause(1)
        assert not app.query_one("#live").has_class("lost")
        await pilot.pause(2.5)
        assert app.query_one("#live").has_class("lost")
    print("ok: silent link shown as lost", flush=True)


STATUS = b"PID L_DO:0 R_DO:0 L_AO:23 R_AO:22 err:1.00 cruise:0 L_spd:0 R_spd:0 PAUSED\n"
asyncio.run(main())
asyncio.run(silent_wifi())
os._exit(0)  # serial thread is a daemon blocked on the silent socket
