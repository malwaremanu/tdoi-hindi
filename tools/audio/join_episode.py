#!/usr/bin/env python3
"""Join an episode's mixed cold open with its clean body takes.

  python3 tools/audio/join_episode.py --workdir ep04_2 --episode 4.2 \
      --body c02,c03,c04,c05 [--pause 1.4] [--chunk c01]

Writes <workdir>/ep<id>_full_sfx.mp3 (loudnorm I=-16 TP=-1.5 LRA=11) and
<workdir>/ep<id>_coldopen_sfx.mp3 for a quick listen.
"""
import argparse
import os
import subprocess
import sys

FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
FP = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffprobe"
REPO = "/home/itcell/audiobooks/tdoi"


def sh(a):
    r = subprocess.run(a, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(r.stderr[-1500:])


def dur(p):
    r = subprocess.run([FP, "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", p], capture_output=True, text=True)
    return float(r.stdout.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", required=True)
    ap.add_argument("--episode", required=True)
    ap.add_argument("--body", required=True)
    ap.add_argument("--chunk", default="c01")
    ap.add_argument("--pause", type=float, default=1.4)
    args = ap.parse_args()

    base = args.workdir if os.path.isabs(args.workdir) else os.path.join(REPO, args.workdir)
    sfx = os.path.join(base, "sfx")
    co = os.path.join(sfx, f"_{args.chunk}_mixed.wav")
    body = [c.strip() for c in args.body.split(",") if c.strip()]
    if not os.path.exists(co):
        sys.exit(f"missing mixed cold open: {co}")

    norm = os.path.join(base, "_norm")
    os.makedirs(norm, exist_ok=True)
    layers = [co]
    for n in body:
        src = os.path.join(base, n + ".wav")
        dst = os.path.join(norm, n + ".wav")
        if not os.path.exists(dst):
            sh([FF, "-y", "-i", src, "-af", "dynaudnorm=f=200:g=5:p=0.95,aresample=48000",
                "-ac", "2", "-ar", "48000", dst])
        layers.append(dst)

    inputs, filters, offset = [], [], 0.0
    for i, p in enumerate(layers):
        inputs += ["-i", p]
        d = dur(p)
        ms = int(round(offset * 1000))
        filters.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,"
                       f"adelay={ms}|{ms}[a{i}]")
        offset += d + args.pause
    labels = "".join(f"[a{i}]" for i in range(len(layers)))
    filters.append(f"{labels}amix=inputs={len(layers)}:normalize=0,"
                   f"atrim=0:{offset + 0.8:.3f},asetpts=PTS-STARTPTS[out]")

    raw = os.path.join(base, "_full_sfx_raw.wav")
    sh([FF, "-y", *inputs, "-filter_complex", ";".join(filters), "-map", "[out]",
        "-ar", "48000", "-ac", "2", raw])

    eid = args.episode.replace(".", "_")
    out = os.path.join(base, f"ep{eid}_full_sfx.mp3")
    sh([FF, "-y", "-i", raw, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "44100",
        "-ac", "2", "-codec:a", "libmp3lame", "-q:a", "2", out])
    print(f"joined {dur(out):.1f}s -> {out}", flush=True)

    cob = os.path.join(base, f"ep{eid}_coldopen_sfx.mp3")
    sh([FF, "-y", "-i", co, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "44100",
        "-ac", "2", "-codec:a", "libmp3lame", "-q:a", "2", cob])
    print(f"cold open {dur(cob):.1f}s -> {cob}", flush=True)


if __name__ == "__main__":
    main()
