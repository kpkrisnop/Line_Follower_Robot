# /// script
# requires-python = ">=3.11"
# dependencies = ["textual>=1.0", "pyserial>=3.5", "optuna>=4", "bleak>=0.22", "pyobjc-framework-CoreWLAN; sys_platform == 'darwin'"]
# ///
"""Line follower tuner. Run: uv run tuner.py   (or just: robot)

Waits for the robot's USB, connects, pauses the car, and tunes it live.
Every change is auto-saved to the robot's EEPROM by the firmware.
Notes go to tuning-log.md next to this file, with the settings at that moment.
In lap mode ("lap 1") every finished lap is logged there too.
Autotune ("a"): Optuna tries kp/kd/ki on the loop; each trial skips the lap in progress
when the values change and scores the next full lap.
"""
import asyncio
import csv
import json
import queue
import re
import statistics
import threading
import time
from datetime import datetime
from pathlib import Path

import optuna
try:
    import CoreWLAN  # macOS Wi-Fi API: signal of the Mac's link to the car's access point
except ImportError:
    CoreWLAN = None
import serial
from bleak import BleakClient, BleakScanner
from serial.tools import list_ports
from rich.text import Text
from textual.app import App, ComposeResult, SystemCommand
from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Footer, Input, MarkdownViewer, Sparkline, Static

BAUD = 115200
CH340_VID = 0x1A86
WIFI = "socket://192.168.77.1:23"  # wifi_bridge on the ESP8266; join Wi-Fi "LineFollower" first
BLE = "ble://LineFollower"  # ble_bridge on the ESP32: Nordic UART service, no pairing
NUS_RX = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"  # commands to the robot
NUS_TX = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"  # robot output, as notifications
LOG = Path(__file__).with_name("tuning-log.md")
LOG_HEADER = "# Tuning log\n\n| Time | Mode | Settings | Note |\n|---|---|---|---|\n"
TELEM_DIR = Path(__file__).with_name("telemetry")  # one CSV per tuner run, every 10 Hz status line
TELEM_FIELDS = ["L_DO", "R_DO", "L_AO", "R_AO", "err", "cruise", "L_spd", "R_spd", "cp", "laps", "lap", "split"]

# name, step, decimals
PARAMS = [("kp", 0.05, 3), ("kd", 0.05, 3), ("ki", 0.001, 3), ("base", 10, 0),
          ("slow", 0.01, 3), ("expo", 0.1, 2), ("min", 10, 0), ("turn", 10, 0), ("bang", 10, 0),
          ("off", 1, 0), ("stop", 10, 0), ("trim", 1, 0), ("lap", 1, 0), ("marks", 1, 0),
          ("mark", 10, 0), ("minlap", 1, 0), ("skew", 10, 0), ("smooth", 0.005, 3), ("reach", 0.05, 2)]
LOCAL = {"smooth": 0.03, "reach": 0.25}  # tuner-only settings (not on the robot), with defaults
LOCAL_FILE = Path(__file__).with_name("tuner-settings.json")
HELP = {
    "kp": "Proportional gain: steering = kp × err. Higher turns harder towards the line; too high zigzags on straights.",
    "kd": "Derivative gain, on the change in err per 10 ms step. Damps wobble. Too high relative to kp makes it twitchy.",
    "ki": "Integral gain. err is summed (clamped ±2000, reset on every command), so it can add at most ki × 2000. "
          "Helps hold tight turns; too much overshoots after a corner.",
    "base": "Cruise speed on straights (PWM 0–255).",
    "slow": "Corner slowdown strength: cruise = base − slow·1000·(|err|/1000)^expo. 0 = off. Curve on the right →",
    "expo": "Shape of the slowdown curve. 1 = linear; >1 barely slows for small err and brakes hard in corners; "
            "<1 slows early.",
    "min": "Lowest cruise in corners: the floor of the curve. At or above base = no slowdown at all (slow and expo do nothing).",
    "turn": "Max |steering| (0–510). 510 = no cap. Lower stops both wheels saturating in corners.",
    "bang": "Wheel speed in bang-bang mode (m switches mode).",
    "off": "Added to the right sensor reading. Set it on white so err ≈ 0 with the car centred.",
    "stop": "Both sensors above this (calibrated 0–1000) = black. lap 0: stop line. lap 1: mark or off track. "
            "1001 = never.",
    "trim": "Motor balance %. >0 slows the left motor, <0 the right. Set it on a straight until err averages 0.",
    "lap": "0 = stop on the first stop line (competition). 1 = closed loop: count marks, time laps, "
           "stop only when off track (black ≥ 1 s).",
    "marks": "Tape marks per lap. The first mark after run starts lap 1.",
    "mark": "Both black for less than this many ms = a checkpoint mark. 1 s or more = off track.",
    "smooth": "Tuner only, not on the robot. Autotune score = lap s + smooth × shake, where shake = mean |change in err| between status lines (10 Hz) over the lap. 0 = only lap time counts; raise it until shaky laps score worse than smooth ones. Every lap row shows its shake.",
    "reach": "Tuner only. How far autotune may move each gain from its value when you press a, as a share of the "
             "full range below: 0.25 = within ±25 % of it (e.g. kp 0.27 → 0.15–0.43). Lower = gentler trials. "
             "1 = the whole range. Takes effect at the next a.",
    "skew": "ms. A tape mark is straight across the track, so both sensors go black almost together; on a wiggle "
            "one goes black first. A crossing counts as a mark only if the two went black within skew ms. "
            "Every short crossing shows 'crossing: skew N ms' in the message line: set skew between the marks' and the wiggles'.",
    "minlap": "Shortest real lap, s. A mark sooner than minlap/marks s after the last counted one is ignored (corner blips). 0 = off.",
}

# Autotune hard limits; `reach` (in the app) narrows them around the starting values.
# kp 1.9 / kd 1.7 tried on 2026-10-19 were far too aggressive; hand-tuned kp was ~0.3
AUTO = {"kp": (0.15, 0.8, 0.01), "kd": (0.0, 1.0, 0.01), "ki": (0.0, 0.1, 0.001)}  # low, high, step


def auto_ranges(vals, reach):
    """Search range per gain: start ± reach × the full AUTO width, kept inside AUTO, on the step grid."""
    out = {}
    for k, (lo, hi, step) in AUTO.items():
        v, w = min(max(vals.get(k, lo), lo), hi), reach * (hi - lo)
        a, b = max(lo, v - w), min(hi, v + w)
        a, b = lo + round((a - lo) / step) * step, lo + round((b - lo) / step) * step
        out[k] = (round(a, 6), round(max(b, a), 6), step)
    return out
AUTO_TRIALS = 30
OFFTRACK_SCORE = 60.0   # score for a trial that leaves the track
optuna.logging.set_verbosity(optuna.logging.WARNING)  # its log lines would scribble over the TUI


def find_port():
    ports = list_ports.comports()
    for p in ports:
        if p.vid == CH340_VID:
            return p.device
    # ponytail: fallback for a non-CH340 Uno; add its VID above if it ever matters
    try:  # before other USB serials: the ESP32's own USB (CP2102) isn't the Uno
        if asyncio.run(BleakScanner.find_device_by_name(BLE[6:], timeout=3)):
            return BLE
    except Exception:  # Bluetooth off or not allowed
        pass
    # No Wi-Fi fallback: the ESP8266 bridge is gone, and a dead socket:// try cost 5 s per BLE drop
    return next((p.device for p in ports if "usbserial" in p.device or "usbmodem" in p.device), None)


class BleSerial:
    """Just enough of pyserial (read, write, close, with) over BLE Nordic UART for serial_loop.
    bleak is async: its own event loop runs on a thread, and calls are handed to it."""

    def __init__(self, port, baud=None, timeout=0.1):
        self.port, self.timeout = port, timeout
        self.rx, self.lost = queue.Queue(), threading.Event()
        self.loop = asyncio.new_event_loop()
        threading.Thread(target=self.loop.run_forever, daemon=True).start()
        try:
            self._call(self._connect(port[6:]), 30)
        except serial.SerialException:
            self.loop.call_soon_threadsafe(self.loop.stop)
            raise

    def _call(self, coro, timeout):
        try:
            return asyncio.run_coroutine_threadsafe(coro, self.loop).result(timeout)
        except Exception as e:  # BleakError, timeouts: serial_loop reconnects on SerialException
            raise serial.SerialException(f"BLE: {e!r}") from e

    async def _connect(self, name):
        dev = await BleakScanner.find_device_by_name(name, timeout=5)
        if not dev:
            raise serial.SerialException(f"BLE {name} not found")
        self.client = BleakClient(dev, disconnected_callback=lambda _: self.lost.set())
        await self.client.connect()
        await self.client.start_notify(NUS_TX, lambda _, d: self.rx.put(bytes(d)))

    def read(self, n=4096):  # ponytail: ignores n, returns whatever arrived; serial_loop splits lines itself
        if self.lost.is_set():
            raise serial.SerialException("BLE disconnected")
        try:
            data = self.rx.get(timeout=self.timeout)
        except queue.Empty:
            return b""
        while not self.rx.empty():
            data += self.rx.get_nowait()
        return data

    def write(self, b):
        for i in range(0, len(b), 180):  # under the 247 MTU the bridge asks for
            self._call(self.client.write_gatt_char(NUS_RX, b[i:i + 180], response=False), 5)

    def close(self):
        try:
            self._call(self.client.disconnect(), 5)
        except serial.SerialException:
            pass
        self.loop.call_soon_threadsafe(self.loop.stop)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()


def rssi_color(dbm):
    return "red" if dbm < -80 else "yellow" if dbm < -70 else "green"


def fmt(name, value):
    dec = next(d for n, _, d in PARAMS if n == name)
    return f"{value:.{dec}f}"


class Settings(Widget, can_focus=True):
    BINDINGS = [("up", "move(-1)", "pick"), ("down", "move(1)", "pick"),
                ("left", "nudge(-1)", "−"), ("right", "nudge(1)", "+"),
                ("enter,e", "edit", "type value")]

    def __init__(self, **kw):
        super().__init__(**kw)
        self.values = {}
        self.row = 0

    def render(self):
        t = Text()
        for i, (name, step, _) in enumerate(PARAMS):
            val = fmt(name, self.values[name]) if name in self.values else "—"
            line = f"{'>' if i == self.row else ' '} {name:<5} {val:>8}   ±{step:g}\n"
            t.append(line, style="reverse" if i == self.row and self.has_focus else "")
        return t

    def changed(self):  # row or a value changed: redraw this and the boxes that depend on it
        self.refresh()
        self.app.show_help()
        self.app.show_auto()  # its ranges follow the gains and reach
        self.app.query_one(Curve).refresh()

    def action_move(self, d):
        self.row = (self.row + d) % len(PARAMS)
        self.changed()

    def action_nudge(self, d):
        name, step, dec = PARAMS[self.row]
        if name not in self.values:
            return
        self.app.set_param(name, round(self.values[name] + d * step, dec))

    def action_edit(self):
        self.app.open_input("value", PARAMS[self.row][0])

    def on_click(self, event):
        row = event.y - 1  # border
        if 0 <= row < len(PARAMS):
            if row == self.row:
                self.action_edit()
            self.row = row
            self.changed()

    def on_focus(self):
        self.refresh()

    def on_blur(self):
        self.refresh()


BRAILLE = [[0x01, 0x08], [0x02, 0x10], [0x04, 0x20], [0x40, 0x80]]  # dot bit for [row][col] in a cell


class Curve(Widget):
    """Corner slowdown: cruise vs err (−1000..1000), as the firmware computes it, drawn RC-transmitter
    style in braille dots (2×4 per cell) with dashed centre lines; the live err is the red dot."""

    def render(self):
        v = self.app.query_one(Settings).values
        if not all(k in v for k in ("base", "slow", "expo", "min")):
            return Text("waiting for settings…", style="dim")
        base, slow = v["base"], v["slow"]
        expo = min(max(v["expo"], 0.2), 5.0)  # the firmware's clamp; a nudge shows here before its reply
        floor = min(v["min"], base)
        cols, rows = self.size.width - 5, self.size.height - 1  # 5 = y labels, 1 = x axis
        if cols < 2 or rows < 1 or base <= 0:
            return Text()
        w, h = cols * 2, rows * 4  # dots

        def y_of(px):  # dot row of the curve at dot column px (0 = top = base)
            e = abs(px / (w - 1) * 2000 - 1000)
            cruise = max(floor, min(base, base - slow * 1000 * (e / 1000) ** expo))
            return round((1 - cruise / base) * (h - 1))

        curve = [[0] * cols for _ in range(rows)]
        cross = [[0] * cols for _ in range(rows)]
        for p in range(0, w, 4):  # dashes: 2 dots on, 2 off
            for q in (p, p + 1):
                if q < w:
                    cross[h // 2 // 4][q // 2] |= BRAILLE[h // 2 % 4][q % 2]
        for p in range(0, h, 4):
            for q in (p, p + 1):
                if q < h:
                    cross[q // 4][w // 2 // 2] |= BRAILLE[q % 4][w // 2 % 2]
        prev = None
        for px in range(w):
            y = y_of(px)
            for yy in range(min(y, prev), max(y, prev) + 1) if prev is not None else (y,):  # join steps
                curve[yy // 4][px // 2] |= BRAILLE[yy % 4][px % 2]
            prev = y
        errs = self.app.errs
        live = None
        if errs:
            px = round((max(-1000, min(1000, errs[-1])) + 1000) / 2000 * (w - 1))
            live = (y_of(px) // 4, px // 2)
        t = Text()
        for r in range(rows):
            t.append(f"{base:>4.0f} " if r == 0 else "   0 " if r == rows - 1 else "     ", style="dim")
            for c in range(cols):
                bits = curve[r][c] | cross[r][c]
                style = "bold red" if (r, c) == live else "dodger_blue2" if curve[r][c] else "grey42"
                t.append(chr(0x2800 + bits) if bits else " ", style=style)
            t.append("\n")
        t.append("     -1000" + "0".center(cols - 9) + "1000", style="dim")
        return t


def doc_text(name):
    text = Path(__file__).with_name(name).read_text()
    if name == "docs.md":  # settings reference comes from HELP, so it can't drift from the About box
        text += "\n| Setting | Step | What it does |\n|---|---|---|\n" + "".join(
            f"| `{n}` | ±{step:g} | {HELP[n]} |\n" for n, step, _ in PARAMS)
    return text


class Tuner(App):
    CSS = """
    Screen { layout: vertical; layers: base doc; }
    #doc { layer: doc; display: none; width: 100%; height: 100%; border: round $accent;
           border-title-align: left; background: $surface; }
    #top { height: 21; }
    Settings { width: 30; border: round $accent; border-title-align: left; padding: 0 1; }
    #live { height: 12; border: round $accent; padding: 0 1; }
    #live.lost { border: round $error; }
    #livetext { height: 4; }
    #auto { height: 7; border: round $accent; padding: 0 1; }
    #help, Curve { width: 1fr; height: 1fr; border: round $accent; padding: 0 1; }
    Sparkline { height: 5; margin-top: 1; }
    #notes { border: round $accent; padding: 0 1; height: 1fr; }
    #msg { height: 1; padding: 0 1; color: $text-muted; }
    #entry { display: none; }
    """
    BINDINGS = [("space", "toggle_run", "run/pause"), ("m", "mode", "PID/bang"),
                ("c", "cal", "calibrate sensors"), ("n", "note", "note"), ("a", "autotune", "autotune"), ("f", "fake_lap", "fake lap"),
                ("escape", "cancel", "cancel"), ("ctrl+q", "quit", "quit")]

    def compose(self) -> ComposeResult:
        with Vertical(id="live"):
            yield Static("waiting for robot… plug in the USB, switch the car on (BLE LineFollower)", id="livetext")
            yield Sparkline([0], id="graph")
        with Horizontal(id="top"):
            yield Settings(id="settings")
            with Vertical():
                yield Static(id="auto")
                with Horizontal():
                    yield Static(id="help")
                    yield Curve(id="curve")
        yield Static(id="notes")
        yield Static(id="msg")
        yield Input(id="entry")
        yield MarkdownViewer(id="doc", show_table_of_contents=False)
        yield Footer()

    def on_mount(self):
        self.ser = None
        self.via, self.base_rssi = None, None  # "usb" | "wifi" | "base"; base: car's signal in dBm
        self.mode = None
        self.paused = None
        self.state = None
        self.errs = []
        self.entry_kind = None
        self.laps, self.lap_errs, self.best_lap = 0, [], None
        self.lap_times = []              # real laps this run (fake ones removed with f)
        self.last_lap = None             # (lap s, scored FrozenTrial or None) for f
        try:
            saved = json.loads(LOCAL_FILE.read_text())
        except (OSError, ValueError):
            saved = {}
        self.query_one(Settings).values.update({k: saved.get(k, v) for k, v in LOCAL.items()})
        self.study = self.trial = None   # autotune is on while study is set
        self.telem = None                # csv writer, opened on the first status line
        self.trial_laps = 0              # laps finished since this trial's values were sent
        self.query_one("#settings").border_title = "Settings"
        self.query_one("#live").border_title = "Live (err graph, last 10 s)"
        self.query_one("#auto").border_title = "Autotune"
        self.query_one(Curve).border_title = "Slowdown curve: cruise vs |err|"
        self.query_one("#notes").border_title = "Notes & laps  (tuning-log.md)"
        self.query_one("#settings").focus()
        self.show_notes()
        self.show_auto()
        self.show_help()
        self.last_status = time.time()
        self.set_interval(0.5, self.check_stale)
        threading.Thread(target=self.serial_loop, daemon=True).start()

    # ---- serial (background thread) ----
    def serial_loop(self):
        while True:
            port = find_port()
            if not port:
                time.sleep(1)
                continue
            try:
                opener = BleSerial if port.startswith("ble://") else serial.serial_for_url
                with opener(port, BAUD, timeout=0.1) as ser:  # USB: opening resets the Uno
                    self.call_from_thread(self.set_msg, f"connected {port}, waiting for boot…")
                    buf, booted, t0 = "", False, time.time()
                    self.via, self.base_rssi = {WIFI: "wifi", BLE: "ble"}.get(port, "usb"), None
                    wireless = port in (WIFI, BLE)
                    if wireless:  # no reset over Wi-Fi/BLE: watch it drive, don't pause it
                        ser.write(b"tui\n")
                        booted, self.ser = True, ser
                        self.call_from_thread(self.set_msg, f"connected over {'Wi-Fi' if port == WIFI else 'BLE'} (car not paused)")
                    last = time.time()
                    while True:
                        data = ser.read(4096)
                        if data:
                            last = time.time()
                        elif wireless and time.time() - last > 2:  # status comes every 100 ms; radio drops don't close the port
                            raise serial.SerialException("no data for 2 s")
                        buf += data.decode("utf-8", "replace")
                        *lines, buf = buf.split("\n")
                        for line in lines:
                            line = line.strip()
                            if line.startswith("base:"):  # base_station.ino on USB: the car is on the radio
                                self.base_rssi = int(line.split()[2]) if line.startswith("base: car") else None
                                if not booted:  # not reset by opening, like Wi-Fi: don't pause it
                                    ser.write(b"tui\n")
                                    booted, self.ser, self.via = True, ser, "base"
                                    self.call_from_thread(self.set_msg, f"connected via base station {port} (car not paused)")
                            elif not booted and ("defaults" in line or "Loaded" in line):
                                ser.write(b"pause\ntui\n")  # lands inside the firmware's 1 s boot wait
                                booted = True
                                self.ser = ser
                                self.call_from_thread(self.set_msg, f"connected {port} — car paused")
                            elif line:
                                self.call_from_thread(self.handle_line, line)
                        if not booted and time.time() - t0 > 4:  # missed the boot banner: pause anyway
                            ser.write(b"pause\ntui\n")
                            booted, self.ser = True, ser
            except (serial.SerialException, OSError):
                pass
            self.ser = None
            self.call_from_thread(self.disconnected)
            time.sleep(1)

    def send(self, cmd):
        if self.ser:
            try:
                self.ser.write((cmd + "\n").encode())
            except (serial.SerialException, OSError):
                pass
        else:
            self.set_msg("not connected")

    # ---- UI (main thread) ----
    def handle_line(self, line):
        # serial noise garbles lines (a cut-off status lacks fields → KeyError); any exception here
        # would kill the serial thread via call_from_thread, freezing the screen with no warning
        try:
            self.parse_line(line)
        except Exception as e:
            self.set_msg(f"garbled ({type(e).__name__}): {line}")

    def parse_line(self, line):
        if " | kp " in line:  # settings reply: "[saved: ]mode PID PAUSED | kp 1.200 ki ..."
            head, tail = line.split("|", 1)
            words = head.replace("saved:", "").split()
            self.mode, self.paused = words[1], "PAUSED" in words
            vals = tail.split()
            settings = self.query_one(Settings)
            for k, v in zip(vals[::2], vals[1::2]):
                settings.values[k] = float(v)
            settings.changed()
            self.set_msg(line)
        elif "L_spd:" in line:
            f = dict(re.findall(r"(\w+):(-?[\d.]+)", line))
            last = line.split()[-1]
            state = last if last in ("PAUSED", "STOP", "WAIT", "OFFTRACK") else "RUNNING"
            self.mode = line.split()[0]
            self.paused = state == "PAUSED"
            err = float(f.get("err", 0))
            self.errs = (self.errs + [err])[-100:]
            self.query_one(Sparkline).data = self.errs
            self.query_one(Curve).refresh()  # moves the live |err| marker
            self.query_one("#live").remove_class("lost")
            self.last_status = time.time()
            laps_line = ""
            if "laps" in f:  # lap mode
                self.track_laps(f, err, state)
                best = f"{self.best_lap:.2f}" if self.best_lap else "—"
                laps_line = (f"\nlap {int(f['laps']) + 1}  last {int(f['lap']) / 1000:.2f}  best {best}"
                             f"  split {int(f['split']) / 1000:.2f}  cp {f['cp']}")
            self.state = state
            self.log_telemetry(f, state)
            self.query_one("#livetext").update(
                f"[b]{self.mode}  {state}[/b]\n"
                f"L_AO {f.get('L_AO')}  R_AO {f.get('R_AO')}   DO {f.get('L_DO')}/{f.get('R_DO')}   err {f.get('err')}\n"
                f"cruise {f.get('cruise')}   L_spd {f.get('L_spd')}  R_spd {f.get('R_spd')}{laps_line}")
        else:
            self.set_msg(line)

    def log_telemetry(self, f, state):
        if not self.telem:
            TELEM_DIR.mkdir(exist_ok=True)
            path = TELEM_DIR / f"{datetime.now():%y%m%d-%H%M%S}.csv"
            self.telem_file = path.open("w", newline="", buffering=1)  # line-buffered: survives a crash
            self.telem = csv.writer(self.telem_file)
            self.telem.writerow(["time", "mode", "state", "trial", "kp", "kd", "ki"] + TELEM_FIELDS)
        vals = self.query_one(Settings).values
        trial = self.trial.number + 1 if self.study else ""
        self.telem.writerow([f"{time.time():.2f}", self.mode, state, trial]
                            + [vals.get(k, "") for k in ("kp", "kd", "ki")] + [f.get(k, "") for k in TELEM_FIELDS])

    def track_laps(self, f, err, state):
        laps = int(f["laps"])
        if f["cp"] == "0":
            self.lap_errs = []  # before the first mark after "run": not part of any lap
        else:
            self.lap_errs.append(err)
        if laps > self.laps:
            lap_s = int(f["lap"]) / 1000
            rms = (sum(e * e for e in self.lap_errs) / max(len(self.lap_errs), 1)) ** 0.5
            shake = statistics.fmean(abs(b - a) for a, b in zip(self.lap_errs, self.lap_errs[1:])) if len(self.lap_errs) > 1 else 0
            self.lap_errs = []
            self.lap_times.append(lap_s)
            self.best_lap = min(self.lap_times)
            self.on_lap(lap_s, rms, shake)
        self.laps = laps
        if state == "OFFTRACK" and self.state != "OFFTRACK":
            self.on_offtrack()

    def on_lap(self, lap_s, rms, shake):
        note = f"lap {lap_s:.2f} s, shake {shake:.0f}, rms err {rms:.0f}"
        if len(self.lap_times) >= 4 and lap_s < 0.6 * statistics.median(self.lap_times):
            note += " ⚠ short: fake? (f)"  # ponytail: median of this run's laps; minlap is the real filter
        self.last_lap = (lap_s, None)
        if self.study:
            self.trial_laps += 1
            self.show_auto()
            if self.trial_laps >= 2:  # lap 1 was in progress when the values changed
                score = lap_s + self.query_one(Settings).values["smooth"] * shake
                note = f"trial {self.trial.number + 1}: {note} → score {score:.2f}"
                self.save_note(note)
                self.study.tell(self.trial, score)
                self.last_lap = (lap_s, self.study.trials[self.trial.number])
                self.next_trial()
                return
        self.save_note(note)

    def on_offtrack(self):
        if not self.study:
            return
        self.save_note(f"trial {self.trial.number + 1}: OFFTRACK → score {OFFTRACK_SCORE:g}")
        self.study.tell(self.trial, OFFTRACK_SCORE)
        self.next_trial()
        self.set_msg("[b]off track[/b] — put the car on the line, press space")

    def action_fake_lap(self):
        if not self.last_lap:
            self.set_msg("no lap to mark fake")
            return
        lap_s, scored = self.last_lap
        self.last_lap = None
        self.lap_times.remove(lap_s)
        self.best_lap = min(self.lap_times, default=None)
        note = f"lap {lap_s:.2f} s marked fake"
        if scored and self.study:
            # Optuna can't forget a told trial: rebuild the study without it
            study = optuna.create_study(direction="minimize")
            study.add_trials([t for t in self.study.trials
                              if t.state == optuna.trial.TrialState.COMPLETE and t.number != scored.number])
            study.enqueue_trial(self.trial.params)  # the trial on the car now carries on
            study.enqueue_trial(scored.params)      # then the faked one gets another go
            self.study = study
            self.trial = study.ask()
            for k, (lo, hi, step) in self.ranges.items():
                self.trial.suggest_float(k, lo, hi, step=step)  # same values: nothing to send
            note += f", its trial discarded and queued again"
        self.save_note(note)
        self.show_auto()

    # ---- autotune ----
    def action_autotune(self):
        if self.study:
            self.stop_autotune("stopped")
            return
        vals = self.query_one(Settings).values
        if not self.ser or not all(k in vals for k in AUTO):
            self.set_msg("autotune needs the robot connected")
            return
        self.ranges = auto_ranges(vals, vals["reach"])  # fixed for the whole run: TPE needs stable ranges
        self.study = optuna.create_study(direction="minimize")
        # first trial = today's values, so the tuner starts from known-good and has a baseline
        self.study.enqueue_trial({k: min(max(vals[k], lo), hi) for k, (lo, hi, _) in self.ranges.items()})
        self.send("p")
        self.send("lap 1")
        self.next_trial()

    def next_trial(self):
        if len(self.study.trials) >= AUTO_TRIALS:
            self.stop_autotune("done")
            return
        self.trial = self.study.ask()
        for k, (lo, hi, step) in self.ranges.items():
            self.set_param(k, self.trial.suggest_float(k, lo, hi, step=step))
        self.trial_laps = 0
        self.show_auto()

    def stop_autotune(self, why):
        best = self.best_trial()
        if best:
            for k, v in best.params.items():
                self.set_param(k, v)
        self.save_note(f"autotune {why}: " + (f"best trial {best.number + 1}, score {best.value:.2f}" if best else "no finished trials"))
        self.study = self.trial = None
        self.show_auto()

    def best_trial(self):
        try:
            return self.study.best_trial
        except ValueError:  # no finished trials yet
            return None

    def show_auto(self):
        vals = self.query_one(Settings).values
        rng = self.ranges if self.study else auto_ranges(vals, vals["reach"])  # off: what a would search
        ranges = f"reach {vals['reach']:g}: " + "  ".join(f"{k} {lo:g}–{hi:g}" for k, (lo, hi, _) in rng.items())
        smooth = vals["smooth"]
        text = f"[dim]score = lap s + {smooth:g}×shake · off track {OFFTRACK_SCORE:g} · f = last lap was fake\n{ranges}[/dim]\n"
        if not self.study:
            self.query_one("#auto").update(text + f"off — [b]a[/b] starts {AUTO_TRIALS} trials (car running on the loop)")
            return
        vals = lambda params: "  ".join(f"{k} {v:g}" for k, v in params.items())
        phase = "warm-up lap" if self.trial_laps == 0 else "scoring lap"
        text += f"[b]trial {self.trial.number + 1}/{AUTO_TRIALS}[/b] · {phase}   {vals(self.trial.params)}\n"
        best = self.best_trial()
        text += f"[b]best #{best.number + 1} {best.value:.2f}[/b]   {vals(best.params)}\n" if best else "best —\n"
        self.query_one("#auto").update(text + "[dim]a = stop, keep best[/dim]")

    def show_help(self):
        name, step, _ = PARAMS[self.query_one(Settings).row]
        val = self.query_one(Settings).values.get(name)
        box = self.query_one("#help")
        box.border_title = f"About {name}"
        box.update(f"{HELP[name]}\n\n[dim]now {fmt(name, val) if val is not None else '—'} · step ±{step:g}[/dim]")

    def show_rssi(self):  # bottom right of Live: where the telemetry comes from, and its signal
        live = self.query_one("#live")
        if not self.ser:
            live.border_subtitle = ""
        elif self.via == "base":  # signal at the base, from the car's packets
            dbm = self.base_rssi
            live.border_subtitle = "base station · " + (f"radio [{rssi_color(dbm)}]{dbm} dBm[/]" if dbm else "radio [red]no car[/]")
        elif self.via == "wifi":
            iface = CoreWLAN and CoreWLAN.CWWiFiClient.sharedWiFiClient().interface()
            dbm = iface.rssiValue() if iface else 0  # 0 = not associated
            live.border_subtitle = "Wi-Fi LineFollower" + (f" · [{rssi_color(dbm)}]{dbm} dBm[/]" if dbm else "")
        elif self.via == "ble":  # ponytail: no RSSI shown; add bleak's per-connection RSSI if range matters
            live.border_subtitle = "BLE LineFollower"
        else:
            live.border_subtitle = f"USB {self.ser.port.split('/')[-1]}"

    def check_stale(self):
        self.show_rssi()
        # UI-side watchdog: catches a stuck or dead serial thread too, on USB as well as Wi-Fi
        quiet = time.time() - self.last_status
        if self.ser and quiet > 2 and not self.query_one("#live").has_class("lost"):
            self.query_one("#live").add_class("lost")
            self.set_msg(f"[b red]no status for {quiet:.0f} s[/] — link or tuner stuck; restart `robot` if it stays")

    def disconnected(self):
        self.query_one("#live").add_class("lost")
        self.query_one("#livetext").update("[b red]DISCONNECTED[/] — reconnecting…\nplug in the USB, switch the car on (BLE LineFollower)")
        self.set_msg("[b red]disconnected[/]")

    def set_msg(self, text):
        self.query_one("#msg").update(text)

    def set_param(self, name, value):
        settings = self.query_one(Settings)
        if name in LOCAL:
            value = max(value, 0)
        settings.values[name] = value
        settings.changed()
        if name in LOCAL:
            LOCAL_FILE.write_text(json.dumps({k: settings.values[k] for k in LOCAL}))
            self.show_auto()
        else:
            self.send(f"{name} {fmt(name, value)}")

    def action_toggle_run(self):
        self.send("run" if self.paused or self.state in ("OFFTRACK", "STOP") else "pause")

    def action_mode(self):
        self.send("b" if self.mode == "PID" else "p")

    def action_cal(self):
        self.send("cal")
        self.set_msg("calibrating 5 s: slide both sensors back and forth across the line")

    def open_input(self, kind, name=None):
        entry = self.query_one("#entry", Input)
        self.entry_kind, self.entry_name = kind, name
        if kind == "value":
            cur = self.query_one(Settings).values.get(name)
            entry.placeholder = f"new {name} (Enter to send, Esc to cancel)"
            entry.value = fmt(name, cur) if cur is not None else ""
        else:
            entry.placeholder = "what did the robot do? (Enter to save, Esc to cancel)"
            entry.value = ""
        entry.display = True
        entry.focus()

    def action_note(self):
        self.open_input("note")

    def get_system_commands(self, screen):
        yield from super().get_system_commands(screen)
        yield SystemCommand("Tuning guide", "Step-by-step: calibrate, trim, PID, corners, laps, autotune",
                            lambda: self.open_doc("tuning-guide.md"))
        yield SystemCommand("Documentation", "Keys, screen, states, lap mode, autotune, files, every setting",
                            lambda: self.open_doc("docs.md"))

    # an overlay on the main screen (not a pushed Screen), so the panels underneath keep updating
    async def open_doc(self, name):
        doc = self.query_one("#doc", MarkdownViewer)
        await doc.document.update(doc_text(name))
        doc.border_title = "Tuning guide" if name == "tuning-guide.md" else "Documentation"
        doc.border_subtitle = "Esc closes · ↑↓ PgUp PgDn scroll"
        doc.display = True
        doc.scroll_home(animate=False)
        doc.focus()

    def check_action(self, action, parameters):
        # while a page is open, keys like space or a must not drive the car
        doc = self.query("#doc")  # empty before compose and while the palette is open
        if doc and doc.first().display and action in ("toggle_run", "mode", "cal", "note", "autotune", "fake_lap"):
            return False
        return True

    def action_cancel(self):
        self.query_one("#doc").display = False
        entry = self.query_one("#entry", Input)
        entry.display = False
        self.query_one(Settings).focus()

    def on_input_submitted(self, event):
        text = event.value.strip()
        if self.entry_kind == "value" and text:
            try:
                self.set_param(self.entry_name, float(text))
            except ValueError:
                self.set_msg(f"not a number: {text}")
        elif self.entry_kind == "note" and text:
            self.save_note(text)
        self.action_cancel()

    def save_note(self, text):
        vals = self.query_one(Settings).values
        settings = " ".join(f"{n} {fmt(n, vals[n])}" for n, _, _ in PARAMS if n in vals) or "(not connected)"
        row = f"| {datetime.now():%Y-%m-%d %H:%M} | {self.mode or '?'} | {settings} | {text.replace('|', '/')} |\n"
        if not LOG.exists():
            LOG.write_text(LOG_HEADER)
        with LOG.open("a") as f:
            f.write(row)
        self.show_notes()
        self.set_msg("note saved")

    def show_notes(self):
        rows = [l for l in LOG.read_text().splitlines() if l.startswith("| 20")] if LOG.exists() else []
        lines = []
        for r in reversed(rows[-8:]):
            time_, mode, settings, note = [c.strip() for c in r.strip("|").split("|", 3)]
            lines.append(f"[b]{time_[5:]}[/b] · {mode:<5} {note}\n   [dim]{settings}[/dim]")
        self.query_one("#notes").update("\n".join(lines) or "[dim]no notes yet — press n[/dim]")


if __name__ == "__main__":
    Tuner().run()
