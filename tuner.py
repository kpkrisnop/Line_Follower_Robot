# /// script
# requires-python = ">=3.11"
# dependencies = ["textual>=0.80", "pyserial>=3.5"]
# ///
"""Line follower tuner. Run: uv run tuner.py   (or just: robot)

Waits for the robot's USB, connects, pauses the car, and tunes it live.
Every change is auto-saved to the robot's EEPROM by the firmware.
Notes go to tuning-log.md next to this file, with the settings at that moment.
"""
import re
import threading
import time
from datetime import datetime
from pathlib import Path

import serial
from serial.tools import list_ports
from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Footer, Input, Sparkline, Static

BAUD = 115200
CH340_VID = 0x1A86
WIFI = "socket://192.168.77.1:23"  # wifi_bridge on the ESP8266; join Wi-Fi "LineFollower" first
LOG = Path(__file__).with_name("tuning-log.md")
LOG_HEADER = "# Tuning log\n\n| Time | Mode | Settings | Note |\n|---|---|---|---|\n"

# name, step, decimals
PARAMS = [("kp", 0.05, 3), ("kd", 0.05, 3), ("ki", 0.001, 3), ("base", 10, 0),
          ("slow", 0.01, 3), ("min", 10, 0), ("turn", 10, 0), ("bang", 10, 0), ("off", 1, 0)]


def find_port():
    ports = list_ports.comports()
    for p in ports:
        if p.vid == CH340_VID:
            return p.device
    # ponytail: fallback for a non-CH340 Uno; add its VID above if it ever matters
    return next((p.device for p in ports if "usbserial" in p.device or "usbmodem" in p.device), WIFI)


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

    def action_move(self, d):
        self.row = (self.row + d) % len(PARAMS)
        self.refresh()

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
            self.refresh()

    def on_focus(self):
        self.refresh()

    def on_blur(self):
        self.refresh()


class Tuner(App):
    CSS = """
    Screen { layout: vertical; }
    #top { height: 13; }
    Settings { width: 34; border: round $accent; border-title-align: left; padding: 0 1; }
    #live { border: round $accent; padding: 0 1; }
    #live.lost { border: round $error; }
    #livetext { height: 3; }
    Sparkline { height: 5; margin-top: 1; }
    #notes { border: round $accent; padding: 0 1; height: 1fr; }
    #msg { height: 1; padding: 0 1; color: $text-muted; }
    #entry { display: none; }
    """
    BINDINGS = [("space", "toggle_run", "run/pause"), ("m", "mode", "PID/bang"),
                ("n", "note", "note"), ("escape", "cancel", "cancel"), ("ctrl+q", "quit", "quit")]

    def compose(self) -> ComposeResult:
        with Horizontal(id="top"):
            yield Settings(id="settings")
            with Vertical(id="live"):
                yield Static("waiting for robot… plug in the USB or join Wi-Fi LineFollower", id="livetext")
                yield Sparkline([0], id="graph")
        yield Static(id="notes")
        yield Static(id="msg")
        yield Input(id="entry")
        yield Footer()

    def on_mount(self):
        self.ser = None
        self.mode = None
        self.paused = None
        self.errs = []
        self.entry_kind = None
        self.query_one("#settings").border_title = "Settings"
        self.query_one("#live").border_title = "Live (err graph, last 10 s)"
        self.query_one("#notes").border_title = "Recent notes  (tuning-log.md)"
        self.query_one("#settings").focus()
        self.show_notes()
        threading.Thread(target=self.serial_loop, daemon=True).start()

    # ---- serial (background thread) ----
    def serial_loop(self):
        while True:
            port = find_port()
            if not port:
                time.sleep(1)
                continue
            try:
                with serial.serial_for_url(port, BAUD, timeout=0.1) as ser:  # USB: opening resets the Uno
                    self.call_from_thread(self.set_msg, f"connected {port}, waiting for boot…")
                    buf, booted, t0 = "", False, time.time()
                    if port == WIFI:  # no reset over Wi-Fi: watch it drive, don't pause it
                        ser.write(b"tui\n")
                        booted, self.ser = True, ser
                        self.call_from_thread(self.set_msg, "connected over Wi-Fi (car not paused)")
                    last = time.time()
                    while True:
                        data = ser.read(4096)
                        if data:
                            last = time.time()
                        elif port == WIFI and time.time() - last > 2:  # status comes every 100 ms; Wi-Fi drops don't close the socket
                            raise serial.SerialException("no data for 2 s")
                        buf += data.decode("utf-8", "replace")
                        *lines, buf = buf.split("\n")
                        for line in lines:
                            line = line.strip()
                            if not booted and ("defaults" in line or "Loaded" in line):
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
        # serial noise garbles lines; an exception here would kill the serial thread via call_from_thread
        try:
            self.parse_line(line)
        except (ValueError, IndexError):
            self.set_msg(f"garbled: {line}")

    def parse_line(self, line):
        if " | kp " in line:  # settings reply: "[saved: ]mode PID PAUSED | kp 1.200 ki ..."
            head, tail = line.split("|", 1)
            words = head.replace("saved:", "").split()
            self.mode, self.paused = words[1], "PAUSED" in words
            vals = tail.split()
            settings = self.query_one(Settings)
            for k, v in zip(vals[::2], vals[1::2]):
                settings.values[k] = float(v)
            settings.refresh()
            self.set_msg(line)
        elif "L_spd:" in line:
            f = dict(re.findall(r"(\w+):(-?[\d.]+)", line))
            state = line.split()[-1] if line.split()[-1] in ("PAUSED", "STOP", "WAIT") else "RUNNING"
            self.mode = line.split()[0]
            self.paused = state == "PAUSED"
            self.errs = (self.errs + [float(f.get("err", 0))])[-100:]
            self.query_one(Sparkline).data = self.errs
            self.query_one("#live").remove_class("lost")
            self.query_one("#livetext").update(
                f"[b]{self.mode}  {state}[/b]\n"
                f"L_AO {f.get('L_AO')}  R_AO {f.get('R_AO')}   DO {f.get('L_DO')}/{f.get('R_DO')}   err {f.get('err')}\n"
                f"cruise {f.get('cruise')}   L_spd {f.get('L_spd')}  R_spd {f.get('R_spd')}")
        else:
            self.set_msg(line)

    def disconnected(self):
        self.query_one("#live").add_class("lost")
        self.query_one("#livetext").update("[b red]DISCONNECTED[/] — reconnecting…\nplug in the USB or join Wi-Fi LineFollower")
        self.set_msg("[b red]disconnected[/]")

    def set_msg(self, text):
        self.query_one("#msg").update(text)

    def set_param(self, name, value):
        settings = self.query_one(Settings)
        settings.values[name] = value
        settings.refresh()
        self.send(f"{name} {fmt(name, value)}")

    def action_toggle_run(self):
        self.send("run" if self.paused else "pause")

    def action_mode(self):
        self.send("b" if self.mode == "PID" else "p")

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

    def action_cancel(self):
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
            lines.append(f"[b]{time_[5:]}[/b]  {mode:<5} {note}\n   [dim]{settings}[/dim]")
        self.query_one("#notes").update("\n".join(lines) or "[dim]no notes yet — press n[/dim]")


if __name__ == "__main__":
    Tuner().run()
