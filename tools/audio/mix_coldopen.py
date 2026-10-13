#!/usr/bin/env python3
"""Mix the Ep 1 cold open (first 68.5 s of narration) with the SFX cue plan.

Sound sources: Freesound (sfx/raw_fs). Cue times are on the narration timeline
(t=0 = first sample of "एक"). Levels follow Manu's rule: every effect sits
12-17 dB under the narration and never peaks more than 3 dB below the voice
peak, so nothing masks the words. The bed stays far below (background only).

Each cue file is a longer recording, so the mix takes the first non-silent
stretch (silence-gated) and at most TAKE seconds of it — no extra hits or room
tone drag in.
"""
import json
import os
import re
import subprocess
import sys

BASE = "/home/itcell/audiobooks/tdoi/ep01"
RAW = os.path.join(BASE, "sfx", "raw_fs")
NARR = os.path.join(BASE, "sfx", "narration_68s.wav")
OUT = os.path.join(BASE, "sfx", "ep01_coldopen_sfx.mp3")
FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
FP = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffprobe"

# name, source, start (s), level (dB under voice), pan (-1 L .. +1 R), extra filter, max take (s)
CUES = [
    ("c1",  "s1_dig",     0.0,  -15, -0.35, "", 0.9),
    ("c2",  "s1_dig",     1.4,  -15, -0.35, "", 0.9),
    ("c3",  "s2_gravel",  2.1,  -16, -0.30, "", 1.2),
    ("c4",  "s4_brush",   5.2,  -16, -0.30, "", 1.0),
    ("c5",  "s3_stab",    11.1, -14, -0.35, "", 0.8),
    ("c6",  "s4_brush",   12.4, -16, -0.25, "", 0.9),
    ("c7",  "s4_brush",   13.5, -16, -0.25, "", 0.9),
    ("c8",  "s4_brush",   14.5, -16, -0.25, "", 0.9),
    ("c9",  "s5_crow",    21.2, -15, +0.40, "lowpass=6000", 1.2),
    ("c10", "s6_latch",   27.6, -16, +0.40, "lowpass=3000,highpass=120", 1.0),
    ("c11", "s1_dig",     42.5, -16, -0.35, "", 0.9),
    ("c12", "s8b_pen",    50.4, -16, -0.30, "", 0.8),
    ("c13", "s8_paper",   52.0, -17, -0.20, "", 0.9),
    ("c14", "s9_writing", 65.2, -16, +0.15, "", 1.6),
    ("c15", "s9_writing", 66.9, -16, +0.15, "", 1.6),
]
BED_SRC, BED_LEVEL = "b1_bed", -26      # dB under voice
BED_FADEOUT = (52.6, 0.6)               # gone before the "खुदाई बंद" beat
PEAK_HEADROOM = 3.0                     # cue peak must stay this far under voice peak


def sh(args):
    return subprocess.run(args, capture_output=True, text=True)


def stats(path, extra=None):
    args = [FF, "-hide_banner", "-i", path]
    if extra:
        args += ["-af", extra]
    args += ["-af", "volumedetect", "-f", "null", "-"]
    r = sh(args)
    mean = peak = None
    for line in (r.stderr or "").splitlines():
        if "mean_volume" in line:
            mean = float(line.rsplit(":", 1)[1].split()[0])
        if "max_volume" in line:
            peak = float(line.rsplit(":", 1)[1].split()[0])
    return mean, peak


def file_dur(path):
    r = sh([FP, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path])
    return float(r.stdout.strip())


def first_sound(path, max_take):
    """(start, dur): first non-silent stretch, capped at max_take seconds."""
    r = sh([FF, "-hide_banner", "-i", path, "-af",
            "silencedetect=noise=-38dB:d=0.25", "-f", "null", "-"])
    ends = [float(m.group(1)) for m in
            (re.search(r"silence_end: ([\d.]+)", l) for l in (r.stderr or "").splitlines()) if m]
    total = file_dur(path)
    s = max(0.0, (ends[0] if ends else 0.0) - 0.05)
    return s, min(max_take, max(0.2, total - s))


def pan_expr(pan):
    l = 1.0 if pan <= 0 else 1.0 + pan * 0.55
    r = 1.0 if pan >= 0 else 1.0 - pan * 0.55
    return l, r


def dip_expr():
    segs = [
        "if(between(t,15.8,16.2),-3*(t-15.8)/0.4,",
        "if(between(t,16.2,18.4),-3,",
        "if(between(t,18.4,19.0),-3*(1-(t-18.4)/0.6),",
        "if(between(t,28.0,29.5),-2*(t-28.0)/1.5,",
        "if(between(t,29.5,42.5),-2,",
        "if(between(t,42.5,43.5),-2*(1-(t-42.5)/1.0),",
        "0",
    ]
    e = "".join(segs) + ")" * (len(segs) - 1)
    assert e.count("(") == e.count(")"), "unbalanced envelope"
    return e


def main():
    narr_rms, narr_peak = stats(NARR)
    print(f"narration: {file_dur(NARR):.2f}s  RMS {narr_rms:.1f}  peak {narr_peak:.1f} dBFS")

    bed_wav = os.path.join(RAW, "_bed.wav")
    if not os.path.exists(bed_wav):
        sh([FF, "-y", "-i", os.path.join(RAW, BED_SRC + ".mp3"), "-ac", "1",
            "-ar", "48000", bed_wav])

    prepared = []
    for name, src, start, level, pan, extra, take in CUES:
        src_path = os.path.join(RAW, src + ".mp3")
        cut = os.path.join(RAW, f"_{name}.wav")
        s, d = first_sound(src_path, take)
        fx = (extra + ",") if extra else ""
        sh([FF, "-y", "-ss", f"{s:.3f}", "-t", f"{d:.3f}", "-i", src_path,
            "-ac", "1", "-ar", "48000", "-af", fx + f"atrim=0:{d:.3f}", cut])
        _c_rms, c_peak = stats(cut)
        # place the cue by its PEAK relative to the voice peak: quiet source
        # recordings (brushes, paper) would need 30 dB of gain if matched on RMS,
        # which just lifts their hiss. |level| - 3 keeps the peak in Manu's band.
        gain = (narr_peak - (abs(level) - 3.0)) - c_peak
        gain = max(-40.0, min(10.0, gain))
        prepared.append((name, cut, start, gain, pan, d))

    inputs = ["-i", NARR, "-i", bed_wav]
    for _, p, _, _, _, _ in prepared:
        inputs += ["-i", p]
    filters = ["[0:a]aresample=48000,pan=stereo|c0=c0|c1=c0[v]"]
    labels = ["[v]"]

    bed_gain = narr_rms + BED_LEVEL
    fo_start, fo_dur = BED_FADEOUT
    filters.append(
        "[1:a]aresample=48000,aformat=channel_layouts=mono,"
        "highpass=120,lowpass=9000,"
        f"volume={bed_gain:.2f}dB,"
        f"volume=volume='{dip_expr()}':eval=frame,"
        f"afade=t=in:st=0:d=1.0,afade=t=out:st={fo_start}:d={fo_dur},"
        "aformat=channel_layouts=stereo[bed]"
    )
    labels.append("[bed]")

    for i, (name, _p, start, gain, pan, d) in enumerate(prepared, start=2):
        gl, gr = pan_expr(pan)
        ms = int(round(start * 1000))
        fo = max(0.05, min(0.12, d * 0.25))
        filters.append(
            f"[{i}:a]aresample=48000,"
            f"volume={gain:.2f}dB,"
            f"afade=t=in:d=0.01,afade=t=out:st={max(0.0, d - fo):.3f}:d={fo:.3f},"
            f"pan=stereo|c0={gl:.3f}*c0|c1={gr:.3f}*c0,"
            f"adelay={ms}|{ms}[{name}]"
        )
        labels.append(f"[{name}]")

    n = len(labels)
    nd = file_dur(NARR)
    filters.append("".join(labels) +
                   f"amix=inputs={n}:normalize=0:dropout_transition=0,"
                   "alimiter=level_in=1:level_out=1:limit=0.92:attack=5:release=60,"
                   f"atrim=0:{nd:.3f},asetpts=PTS-STARTPTS[out]")

    tmp = os.path.join(BASE, "sfx", "_mix.wav")
    r = sh([FF, "-y", *inputs, "-filter_complex", ";".join(filters),
            "-map", "[out]", "-ar", "48000", "-ac", "2", tmp])
    if r.returncode != 0:
        print(r.stderr[-4000:])
        sys.exit(1)
    m_rms, m_peak = stats(tmp)
    print(f"mixed -> {tmp}  {file_dur(tmp):.2f}s  RMS {m_rms:.1f}  peak {m_peak:.1f}")
    sh([FF, "-y", "-i", tmp, "-ar", "44100", "-codec:a", "libmp3lame", "-q:a", "2", OUT])
    print("wrote", OUT, file_dur(OUT), "s")
    json.dump({"narration_rms": narr_rms, "narration_peak": narr_peak,
               "mixed_rms": m_rms, "mixed_peak": m_peak,
               "cues": [{"name": nm, "gain": round(g, 2)}
                        for nm, _p, _s, g, _pan, _d in prepared]},
              open(os.path.join(BASE, "sfx", "mix_report.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
