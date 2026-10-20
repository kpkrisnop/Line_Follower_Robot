# /// script
# requires-python = ">=3.11"
# dependencies = ["textual>=0.80", "pyserial>=3.5", "optuna>=4", "bleak>=0.22"]
# ///
"""Tuner checks against fake robots, no hardware. Run: uv run test_tuner.py"""
import asyncio
import os
import socket
import tempfile
import threading
import time
from pathlib import Path

import tuner

REAL_LOOP = tuner.Tuner.serial_loop
tuner.LOG = Path(tempfile.mkdtemp()) / "tuning-log.md"  # never touch the real log
tuner.TELEM_DIR = Path(tempfile.mkdtemp())  # nor the real telemetry
tuner.LOCAL_FILE = Path(tempfile.mkdtemp()) / "tuner-settings.json"  # nor the real smooth setting

GARBAGE = [
    "mode PID PAUSED | k ki 0.000 kd 0.500 base 180 slow",  # seen live 2026-10-17
    "saved: | kp 0.900",
    "PID L_DO:0 err:. L_spd:0",
    "mode PID PAUSED | kp 0.9x0 ki 0.000",
    "PID L_DO:0 R_DO:0 L_AO:0 R_AO:0 err:0.00 cruise:100 L_spd:100 R_spd:100 cp:2 laps:1",  # KeyError froze the screen, 2026-10-19
    "PID L_DO:0 R_DO:0 L_AO:0 R_AO:0 err:0.00 cruise:100 L_spd:100 R_spd:100 cp:2 laps:2 lap:6305 split:-",
]


async def main():
    tuner.Tuner.serial_loop = lambda self: None  # no hardware
    app = tuner.Tuner()
    async with app.run_test():
        for line in GARBAGE:
            app.handle_line(line)  # raised before the fix → killed the serial thread
        app.handle_line("mode PID PAUSED | kp 0.900 ki 0.000 kd 0.500")
        assert app.query_one(tuner.Settings).values["kd"] == 0.5
        app.handle_line("mode PID PAUSED | kp 0.350 base 100 slow 0.000 expo -0.10 min 100")
        app.query_one(tuner.Curve).render()  # expo <= 0 crashed the curve (seen live 2026-10-19)
        await app.open_doc("docs.md")  # every setting documented, and the page opens
        assert all(f"`{n}`" in tuner.doc_text("docs.md") for n, _, _ in tuner.PARAMS)
        assert app.query_one("#doc").display
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


class FakeSer:
    def __init__(self):
        self.sent = []

    def write(self, b):
        self.sent += b.decode().split()


def lap_status(cp, laps, lap_ms, err=100, state=""):
    return (f"PID L_DO:0 R_DO:0 L_AO:500 R_AO:400 err:{err} cruise:80 L_spd:80 R_spd:80 "
            f"cp:{cp} laps:{laps} lap:{lap_ms} split:0 {state}").strip()


async def autotune():
    """Warm-up lap skipped, next lap scored, OFFTRACK penalised, stop applies the best values."""
    tuner.Tuner.serial_loop = lambda self: None
    app = tuner.Tuner()
    async with app.run_test():
        app.ser = FakeSer()
        app.handle_line("mode PID RUNNING | kp 0.500 ki 0.000 kd 0.500 base 80 lap 1 marks 1 mark 300")
        app.handle_line(lap_status(0, 0, 0))
        app.action_autotune()
        assert app.ser.sent[app.ser.sent.index("kp") + 1] == "0.500"  # first trial = current values
        app.handle_line(lap_status(1, 0, 0))
        app.handle_line(lap_status(2, 1, 25000, err=-100))   # warm-up lap: not scored
        assert len(app.study.trials) == 1 and app.trial_laps == 1
        app.handle_line(lap_status(2, 1, 25000, err=-100))  # mid-lap
        app.handle_line(lap_status(3, 2, 20000, err=300))  # scored: 20 s + 0.03 smooth * 400 shake
        assert app.study.trials[0].value == 32.0, app.study.trials[0].value
        app.handle_line(lap_status(3, 2, 20000, state="OFFTRACK"))
        assert app.study.trials[1].value == tuner.OFFTRACK_SCORE
        app.ser.sent.clear()
        app.action_autotune()  # stop
        assert app.study is None and app.ser.sent[app.ser.sent.index("kp") + 1] == "0.500"
        log = tuner.LOG.read_text()
        assert "lap 25.00 s" in log and "score 32.00" in log and "shake 400" in log and "OFFTRACK" in log
        rows = next(tuner.TELEM_DIR.glob("*.csv")).read_text().splitlines()
        assert rows[0].startswith("time,mode,state,trial,kp") and len(rows) == 7, rows  # header + 6 status lines
        assert rows[-1].split(",")[2] == "OFFTRACK"
    print("ok: autotune", flush=True)


async def fake_lap():
    """f drops the last scored trial, keeps the one running, and queues the faked one again."""
    tuner.Tuner.serial_loop = lambda self: None
    app = tuner.Tuner()
    async with app.run_test():
        app.ser = FakeSer()
        app.handle_line("mode PID RUNNING | kp 0.500 ki 0.000 kd 0.500 base 80 lap 1 marks 1 mark 300")
        app.handle_line(lap_status(0, 0, 0))
        app.action_autotune()
        app.handle_line(lap_status(1, 0, 0))
        app.handle_line(lap_status(2, 1, 13000))
        app.handle_line(lap_status(3, 2, 2000))  # a fake 2 s lap gets the trial a great score
        running = dict(app.trial.params)
        app.action_fake_lap()
        done = [t for t in app.study.trials if t.state == tuner.optuna.trial.TrialState.COMPLETE]
        assert not done and app.trial.params == running and app.best_lap == 13.0
        app.handle_line(lap_status(4, 3, 13000))  # the running trial's warm-up
        app.handle_line(lap_status(5, 4, 14000))  # scored
        assert app.study.trials[0].value == 14.0
        assert app.trial.params["kp"] == 0.5  # then the faked trial runs again
        assert "marked fake" in tuner.LOG.read_text()
    print("ok: fake lap", flush=True)


async def base_station():
    """base_station.ino on USB: recognised by its "base:" lines, car not paused, radio signal shown."""
    srv = socket.create_server(("127.0.0.1", 0))
    tuner.WIFI = "socket://192.0.2.1:23"  # not this port: the tuner must treat it as USB
    tuner.find_port = lambda: f"socket://127.0.0.1:{srv.getsockname()[1]}"
    got = []

    def base(conn):  # like the real base: "base:" line every so often (socket:// open drops what came before)
        conn.settimeout(0.3)
        for _ in range(100):
            try:
                conn.sendall(b"base: car -63 dBm\n" + STATUS)
                got.append(conn.recv(100))
            except OSError:
                pass

    def serve():  # every connection: the previous test's reader thread is still alive and reconnects too
        while True:
            threading.Thread(target=base, args=(srv.accept()[0],), daemon=True).start()

    threading.Thread(target=serve, daemon=True).start()
    tuner.Tuner.serial_loop = REAL_LOOP
    app = tuner.Tuner()
    async with app.run_test() as pilot:
        await pilot.pause(1.5)
        assert app.via == "base" and app.state == "PAUSED"  # status line got through
        assert b"tui" in b"".join(got) and b"pause" not in b"".join(got), got
        sub = str(app.query_one("#live").border_subtitle)
        assert "base station" in sub and "-63" in sub, sub
    print("ok: base station", flush=True)


async def ble():
    """ble_bridge.ino over BLE: like Wi-Fi, no reset, so the car is not paused (socket stands in for the radio)."""
    srv = socket.create_server(("127.0.0.1", 0))
    tuner.BLE = f"socket://127.0.0.1:{srv.getsockname()[1]}"
    tuner.find_port = lambda: tuner.BLE
    got = []

    def car(conn):
        conn.settimeout(0.3)
        for _ in range(100):
            try:
                conn.sendall(STATUS)
                got.append(conn.recv(100))
            except OSError:
                pass

    def serve():
        while True:
            threading.Thread(target=car, args=(srv.accept()[0],), daemon=True).start()

    threading.Thread(target=serve, daemon=True).start()
    tuner.Tuner.serial_loop = REAL_LOOP
    app = tuner.Tuner()
    async with app.run_test() as pilot:
        await pilot.pause(1.5)
        assert app.via == "ble" and app.state == "PAUSED"
        assert b"tui" in b"".join(got) and b"pause" not in b"".join(got), got
        assert "BLE" in str(app.query_one("#live").border_subtitle)
    print("ok: ble", flush=True)


STATUS = b"PID L_DO:0 R_DO:0 L_AO:23 R_AO:22 err:1.00 cruise:0 L_spd:0 R_spd:0 PAUSED\n"
asyncio.run(main())
asyncio.run(autotune())
asyncio.run(fake_lap())
asyncio.run(silent_wifi())
asyncio.run(base_station())
asyncio.run(ble())
os._exit(0)  # serial thread is a daemon blocked on the silent socket
