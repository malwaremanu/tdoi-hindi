#!/usr/bin/env python3
"""Ep 4.1 cold open: narration + desert air + brick/dig cues + a few synthesised cues.

Implements scripts/Ep 4.1 — SFX plan.md. Cue times are re-spotted from the whisper
word timings of the cold-open take (ep04_1/c01.whisper.json), so they follow the
narration instead of being hardcoded: each cue carries a list of phrase candidates
and the first hit wins. Anything not found falls back to a logged offset.

  python3 tools/audio/mix_ep4_1_coldopen.py            # -> ep04_1/sfx/_c01_mixed.wav
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

import numpy as np

BASE = "/home/itcell/audiobooks/tdoi/ep04_1"
SFX = os.path.join(BASE, "sfx")
EP1_RAW = "/home/itcell/audiobooks/tdoi/ep01/sfx/raw_fs"
EP2_RAW = "/home/itcell/audiobooks/tdoi/ep02/sfx/raw_fs"
EP3_RAW = "/home/itcell/audiobooks/tdoi/ep03/sfx/raw_fs"
FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
SR = 48000
PEAK_HEADROOM = 3.0
COLD_END_PAD = 0.0          # cold open ends where the body starts (join adds its pause)

rng = np.random.default_rng(42)


# ---------------------------------------------------------------- helpers
def sh(a):
    r = subprocess.run(a, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(r.stderr[-1500:])


def load(path, extra=""):
    raw = path + ".f64tmp.f32"
    args = [FF, "-y", "-i", path, "-ac", "1", "-ar", str(SR)]
    if extra:
        args += ["-af", extra]
    args += ["-f", "f32le", raw]
    sh(args)
    x = np.fromfile(raw, dtype=np.float32)
    os.remove(raw)
    return x


def env(points, n):
    pts = sorted(points, key=lambda p: p[0])
    t = np.arange(n) / SR
    db_ = np.interp(t, [p[0] for p in pts], [p[1] for p in pts])
    return 10 ** (db_ / 20.0)


def place(buf, seg, at, gain_db, pan, env_db=None, fade_in=0.02, fade_out=0.10):
    i = int(at * SR)
    if i < 0 or i >= len(buf):
        return
    seg = seg[: len(buf) - i]
    n = len(seg)
    g = 10 ** (gain_db / 20.0)
    e = env_db if env_db is not None else np.ones(n)
    fi, fo = int(fade_in * SR), min(int(fade_out * SR), n)
    if fi:
        e[:fi] *= np.linspace(0, 1, fi)
    if fo:
        e[-fo:] *= np.linspace(1, 0, fo)
    l = 1.0 if pan <= 0 else 1.0 + pan * 0.55
    r = 1.0 if pan >= 0 else 1.0 - pan * 0.55
    buf[i:i + n, 0] += seg * e * g * l
    buf[i:i + n, 1] += seg * e * g * r


def loud_window(path, dur, extra="", offset_frac=None):
    x = load(path, extra)
    w = int(dur * SR)
    if len(x) <= w:
        return x
    if offset_frac is not None:
        s = int(len(x) * offset_frac)
        return x[s:s + w]
    e = np.convolve(x ** 2, np.ones(w) / w, mode="valid")
    return x[int(np.argmax(e)):int(np.argmax(e)) + w]


def gain_for(cue_peak, narr_peak, level_db):
    return (narr_peak - (abs(level_db) - PEAK_HEADROOM)) - cue_peak


def db(x):
    return 20 * np.log10(max(1e-9, float(np.max(np.abs(x)))))


# ---------------------------------------------------------------- synthesised cues
def brick_thud(dur=0.35, seed=0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    body = np.sin(2 * np.pi * 105 * t) * np.exp(-t * 26)
    click = rng.normal(0, 0.6, n) * np.exp(-t * 120)
    x = 0.8 * body + 0.5 * click
    # gentle low-pass by moving average
    k = 24
    x = np.convolve(x, np.ones(k) / k, mode="same")
    return (x / max(1e-9, np.max(np.abs(x)))).astype(np.float32)


def sand_trickle(dur=2.5, grains=140):
    n = int(dur * SR)
    x = np.zeros(n, dtype=np.float32)
    for _ in range(grains):
        s = rng.integers(0, n - 2000)
        ln = rng.integers(300, 2200)
        g = rng.normal(0, 1, ln) * np.exp(-np.linspace(0, 6, ln))
        x[s:s + ln] += (g * rng.uniform(0.3, 1.0)).astype(np.float32)
    # high-pass: subtract slow mean
    k = 200
    x = x - np.convolve(x, np.ones(k) / k, mode="same")
    return (x / max(1e-9, np.max(np.abs(x)))).astype(np.float32)


def rain(dur=10.0):
    n = int(dur * SR)
    hiss = rng.normal(0, 1, n)
    # band-pass by two moving averages
    k1, k2 = 8, 160
    hiss = np.convolve(hiss, np.ones(k1) / k1, mode="same") - \
        np.convolve(hiss, np.ones(k2) / k2, mode="same")
    drops = np.zeros(n, dtype=np.float32)
    for _ in range(int(dur * 55)):
        s = rng.integers(0, n - 900)
        ln = rng.integers(90, 600)
        drops[s:s + ln] += (rng.normal(0, 1, ln) * np.exp(-np.linspace(0, 8, ln))).astype(np.float32)
    x = hiss.astype(np.float32) * 0.8 + drops * 0.5
    envl = 1.0 + 0.12 * np.sin(2 * np.pi * 0.16 * np.arange(n) / SR)
    x = x * envl
    return (x / max(1e-9, np.max(np.abs(x)))).astype(np.float32)


def river_wash(dur=8.0):
    n = int(dur * SR)
    x = rng.normal(0, 1, n)
    k = 90
    x = np.convolve(x, np.ones(k) / k, mode="same")
    lfo = 1.0 + 0.35 * np.sin(2 * np.pi * 0.22 * np.arange(n) / SR + 1.1)
    x = x * lfo
    return (x / max(1e-9, np.max(np.abs(x)))).astype(np.float32)


# ---------------------------------------------------------------- anchors
def word_times(path):
    js = json.load(open(path, encoding="utf-8"))
    seq = []
    for s in js["segs"]:
        for w in s.get("words", []):
            seq.append((w["w"].strip(), float(w["s"]), float(w["e"])))
    return seq


def find(seq, cands, start=0.0):
    """First word at or after `start` matching any candidate (substring match)."""
    for w, s, e in seq:
        if s < start:
            continue
        for c in cands:
            if c in w or w in c:
                return s
    return None


def main():
    os.makedirs(SFX, exist_ok=True)
    src = os.path.join(BASE, "c01.wav")
    norm = os.path.join(SFX, "_c01_norm.wav")
    sh([FF, "-y", "-i", src, "-af", "dynaudnorm=f=200:g=5:p=0.95,aresample=48000",
        "-ac", "1", "-ar", str(SR), norm])
    x = load(norm)
    n = len(x)
    narr_peak = db(x)
    print(f"narration {n / SR:.1f}s  peak {narr_peak:.1f} dBFS")

    seq = word_times(os.path.join(BASE, "c01.whisper.json")) if \
        os.path.exists(os.path.join(BASE, "c01.whisper.json")) else []
    if not seq:
        sys.exit("need ep04_1/c01.whisper.json (run verify_episode.py --chunks c01 first)")
    total_s = seq[-1][2]

    # Cue anchors re-spotted against the take: first from the c01 transcript, then a
    # second pass over 44-64 s (the brick passage the small model skips in the long
    # pass but catches when transcribed alone):
    #   "एक नई ईंट रखता है" 50.08 | "फिर दूसरी" 51.36 | "फिर तीसरी" 52.62
    #   spades 72.0, "वो रेत हटाते हैं" 76.14, "दीवारें निकलती हैं" 77.5
    #   "खुदाई रुक जाती है" 99.4 | "और बारिश…" 107.86 | दो बार देखा 122.0
    #   मोहनजोदड़ो 142.0 | सिंधु 146.4 | नमस्कार 151.2 | आज का सवाल 159.3
    A = {
        "brush1": 21.50,   # "सुबह कोई औरत आंगन बुहारती है"
        "crow": 28.20,     # "बच्चे गली में खेलते हैं"
        "rise": 33.50,     # "जमीन ऊपर उठने लगती है"
        "brick1": 50.10,   # hmm: keeps the plan's brick1 slot = first brick
        "thud1": 50.10,    # "एक नई ईंट रखता है"
        "thud2": 51.36,    # "फिर दूसरी"
        "thud3": 52.62,    # "फिर तीसरी"
        "dig1": 72.00,     # "कुदाल और ब्रश लेकर आते हैं"
        "dig2": 76.14,     # "वो रेत हटाते हैं"
        "reveal": 77.50,   # "नीचे से दीवारें निकलती हैं"
        "stop": 99.40,     # "खुदाई रुक जाती है"
        "rain": 107.86,    # "और बारिश और सूखी रेत वाली हवा"
        "steps": 122.00,   # "नेहरू ने खुद ये शहर दो बार देखा"
        "name": 142.00,    # "इस शहर का नाम है मोहनजोदड़ो"
        "river": 146.40,   # "उस नदी का नाम याद रखिए: सिंधु"
        "host": 151.20,    # "नमस्कार, मैं हूँ आशा"
        "question": 159.30,  # "आज का सवाल एक ही है"
    }
    for k, v in sorted(A.items(), key=lambda kv: kv[1]):
        print(f"  anchor {k}: {v:.2f}s")

    # sanity: keep anchors ordered and inside the take
    order = ["brush1", "crow", "rise", "brick1", "thud1", "thud3", "dig1", "reveal",
             "stop", "rain", "steps", "name", "river", "host", "question"]
    last = 0.0
    for k in order:
        if A[k] < last:
            A[k] = last + 0.5
        last = A[k]

    buf = np.zeros((n, 2), dtype=np.float64)
    place(buf, x, 0.0, 0.0, 0.0, fade_in=0.0, fade_out=0.0)

    # ---------------- A1: desert air + wind bed (whole scene up to the host intro)
    air = load(os.path.join(EP2_RAW, "air.mp3"), "highpass=90,lowpass=8000")
    wind = load(os.path.join(EP3_RAW, "wind.mp3"), "highpass=140,lowpass=6500")
    bed_end = A["host"] - 0.25
    need = int(bed_end * SR)
    for nm, src_arr, lvl in (("air", air, -21), ("wind", wind, -23)):
        a = np.tile(src_arr, need // len(src_arr) + 2)[:need]
        e = env([(0, -60), (2.0, 0), (A["rise"], 0), (A["dig1"], 0), (bed_end - 1.2, 0),
                 (bed_end, -60)], len(a))
        place(buf, a, 0.0, gain_for(db(a), narr_peak, lvl), 0.0, e, 0.0, 0.0)

    # ---------------- A2: sand trickle drifting left to right
    tr = sand_trickle(2.6)
    place(buf, tr[: int(1.3 * SR)], A["brush1"] - 3.2,
          gain_for(db(tr), narr_peak, -30), -0.4, fade_in=0.10, fade_out=0.35)
    place(buf, tr[int(1.0 * SR):int(2.3 * SR)], A["brush1"] + 4.5,
          gain_for(db(tr), narr_peak, -31), +0.45, fade_in=0.15, fade_out=0.4)

    # ---------------- A3: morning broom
    br = loud_window(os.path.join(EP1_RAW, "s4_brush.mp3"), 0.9)
    place(buf, br, A["brush1"], gain_for(db(br), narr_peak, -22), -0.2, fade_in=0.02)
    br2 = loud_window(os.path.join(EP1_RAW, "s4_brush.mp3"), 0.8, offset_frac=0.55)
    place(buf, br2, A["brush1"] + 1.0, gain_for(db(br2), narr_peak, -24), +0.15, fade_in=0.02)

    # ---------------- A4: one distant crow
    crow = loud_window(os.path.join(EP1_RAW, "s5_crow.mp3"), 1.2)
    place(buf, crow, A["crow"], gain_for(db(crow), narr_peak, -32), +0.6, fade_in=0.03)

    # ---------------- A5: the ground rising (sub swell)
    bass = load(os.path.join(EP2_RAW, "bass.mp3"), "lowpass=200")
    rise_len = int(7.0 * SR)
    b = np.tile(bass, rise_len // len(bass) + 2)[:rise_len]
    e = env([(0, -60), (4.0, 0), (6.0, 4), (7.0, -60)], len(b))
    place(buf, b, A["rise"], gain_for(db(b), narr_peak, -26), 0.0, e, 0.0, 0.0)

    # ---------------- B1: three bricks laid on the old wall
    for i, key in enumerate(("thud1", "thud2", "thud3")):
        th = brick_thud(0.35 + 0.05 * i, seed=i)
        place(buf, th, A[key], gain_for(db(th), narr_peak, -20 - 1.5 * i), 0.0,
              fade_in=0.005, fade_out=0.25)

    # ---------------- C1: spades and brushes (the excavation)
    dig = load(os.path.join(EP1_RAW, "s1_dig.mp3"))
    dig2 = load(os.path.join(EP1_RAW, "s1b_dig.mp3"))
    grav = load(os.path.join(EP1_RAW, "s2_gravel.mp3"))
    for j, (seg, at, lvl) in enumerate((
            (dig[: int(1.1 * SR)], A["dig1"], -18),
            (dig2[: int(1.0 * SR)], A["dig1"] + 1.2, -19),
            (dig[: int(0.9 * SR)], A["dig2"], -20))):
        place(buf, seg, at, gain_for(db(seg), narr_peak, lvl), 0.05 * j, fade_in=0.02,
              fade_out=0.25)
    g = grav[: int(1.4 * SR)]
    place(buf, g, A["reveal"] - 0.3, gain_for(db(g), narr_peak, -20), -0.1, fade_in=0.05)
    # C2: the reveal swell (dark)
    b2 = np.tile(bass, int(4.5 * SR) // len(bass) + 2)[: int(4.5 * SR)]
    e2 = env([(0, -60), (2.5, 0), (3.6, 3), (4.5, -60)], len(b2))
    place(buf, b2, A["reveal"], gain_for(db(b2), narr_peak, -24), 0.0, e2, 0.0, 0.0)

    # ---------------- D2: rain eats the wall (the dig bed is simply cut at D1: the
    # beds above already end there because the next bed section ignores that window)
    rn = rain(11.0)
    place(buf, rn, A["rain"] - 1.0, gain_for(db(rn), narr_peak, -27), 0.0,
          fade_in=1.0, fade_out=2.5)

    # ---------------- E1: slow steps on dust (Nehru's two visits)
    st = load(os.path.join(EP3_RAW, "steps.mp3"))
    for j in range(4):
        seg = st[int(j * 0.55 * SR): int((j * 0.55 + 0.5) * SR)]
        place(buf, seg, A["steps"] + j * 0.62, gain_for(db(st), narr_peak, -30), -0.35 + j * 0.12,
              fade_in=0.01, fade_out=0.18)

    # ---------------- F1: the name (beds duck; sarangi lands alone)
    sar = load(os.path.join(EP3_RAW, "sarangi.mp3"), "highpass=80,lowpass=6000")
    sn = int(3.2 * SR)
    s = np.tile(sar, sn // len(sar) + 2)[:sn]
    eS = env([(0, -60), (0.6, 0), (1.6, -60)], sn)
    place(buf, s, A["name"], gain_for(db(s), narr_peak, -23), 0.0, eS, 0.0, 0.0)
    # F2: the river — must be gone before the host intro (plan G1: beds out at
    # A["host"] - 0.25), so it is capped at 5 s instead of running under "नमस्कार"
    RIVER_LEN = 5.0
    RIVER_END = A["host"] - 0.6
    rv = river_wash(RIVER_LEN)
    eR = env([(0, -60), (1.5, 0), (RIVER_LEN - 1.4, 0), (RIVER_LEN, -60)], len(rv))
    place(buf, rv, RIVER_END - RIVER_LEN, gain_for(db(rv), narr_peak, -28), 0.0, eR, 0.0, 0.0)
    # beds duck around the name so the name lands alone
    duck = np.ones(n)
    i0, i1 = int((A["name"] - 1.2) * SR), int((A["name"] + 2.4) * SR)
    duck[i0:i1] = 0.30
    buf *= duck[:, None]

    # ---------------- G2: tanpura under the three questions, out before the body
    tp = load(os.path.join(EP3_RAW, "tanpura.mp3"), "highpass=70,lowpass=6000")
    t0 = A["question"] + 1.0
    t1 = min(total_s - 0.9, t0 + 22.0)
    ln = int((t1 - t0) * SR)
    if ln > 0:
        t = np.tile(tp, ln // len(tp) + 2)[:ln]
        et = env([(0, -60), (2.0, 0), (t1 - t0 - 2.0, 0), (t1 - t0, -60)], ln)
        place(buf, t, t0, gain_for(db(t), narr_peak, -24), 0.0, et, 0.0, 0.0)

    # ---------------- the SFX layer on its own, for QC (narration removed)
    layer = buf - (duck[:, None] * x[:, None])
    lout = os.path.join(SFX, "_c01_sfx_only.wav")
    layer.astype(np.float32).tofile(lout + ".f32")
    sh([FF, "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", lout + ".f32", lout])
    os.remove(lout + ".f32")
    print(f"sfx layer rms {db(layer):.1f} dBFS vs narration {narr_peak:.1f} dBFS peak")

    # ---------------- sum, limit, write
    peak = np.max(np.abs(buf))
    if peak > 0.95:
        buf *= 0.95 / peak
    buf = np.tanh(buf * 1.05) / np.tanh(1.05)
    out = os.path.join(SFX, "_c01_mixed.wav")
    buf.astype(np.float32).tofile(out + ".f32")
    sh([FF, "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", out + ".f32", out])
    os.remove(out + ".f32")
    print("wrote", out, f"{len(buf) / SR:.1f}s  peak {db(buf):.1f} dBFS")
    json.dump({k: round(v, 2) for k, v in A.items()},
              open(os.path.join(BASE, "sfx", "cue_times.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
