#!/usr/bin/env python3
"""Post-take stage for an episode: align -> repair anchors -> mix cold open -> join -> QC.

  python3 tools/audio/finish_episodes.py --episodes 4.2,4.3 [--skip-join] [--force]

Per episode, in the workdir ep0X_Y:
  1. `align_words.py` (GPU whisper)            -> c01.align.json
  2. `fix_anchors.py`                          -> repairs the plan's Devanagari anchors
  3. `mix_from_plan.py --check-only`           -> refuses to mix with unresolved anchors
  4. `mix_from_plan.py`                        -> sfx/_c01_mixed.wav (+ sfx layer + cue times)
  5. `qc_layer.py`                             -> the layer's dB-under-voice profile
  6. `join_episode.py`                         -> ep<id>_full_sfx.mp3 + cold-open mp3
  7. ffmpeg ebur128                             -> integrated LUFS / true peak in the log

Idempotent: a step whose output exists is skipped unless --force. State goes to
logs/finish_state.json so a re-run resumes.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import sys
import time

REPO = "/home/itcell/audiobooks/tdoi"
TOOLS = os.path.join(REPO, "tools", "audio")
VENV = "/home/itcell/.hermes/cache/scratch/whisper-venv/bin/python3"
FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
STATE = os.path.join(REPO, "logs", "finish_state.json")


def sh(cmd, log, env=None):
    with open(log, "a") as f:
        f.write(f"\n$ {' '.join(cmd)}\n")
        f.flush()
        p = subprocess.run(cmd, cwd=REPO, stdout=f, stderr=subprocess.STDOUT, text=True, env=env)
    return p.returncode


def gpu_env():
    e = dict(os.environ)
    root = os.path.dirname(os.path.dirname(VENV))        # .../whisper-venv
    libs = glob.glob(os.path.join(root, "lib", "python3.12", "site-packages", "nvidia", "*", "lib"))
    if libs:
        e["LD_LIBRARY_PATH"] = ":".join(libs + [e.get("LD_LIBRARY_PATH", "")])
    return e


def state_update(ep, **kw):
    data = json.load(open(STATE)) if os.path.exists(STATE) else {}
    rec = data.setdefault(ep, {})
    rec.update(kw)
    rec["updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
    tmp = STATE + ".tmp"
    json.dump(data, open(tmp, "w"), indent=1)
    os.replace(tmp, STATE)


def lufs(path):
    r = subprocess.run([FF, "-hide_banner", "-i", path, "-af", "ebur128=peak=true",
                        "-f", "null", "-"], capture_output=True, text=True)
    out = r.stderr
    # the progress lines carry an I: value too (the first one reads -70 LUFS at t=0.1 s),
    # so read the summary block that follows "Integrated loudness"
    summary = out[out.rfind("Integrated loudness"):] if "Integrated loudness" in out else out
    i = re.search(r"I:\s+(-?\d+\.\d+) LUFS", summary)
    tp = re.search(r"Peak:\s+(-?\d+\.\d+) dBFS", summary)
    lra = re.search(r"LRA:\s+(-?\d+\.\d+) LU", summary)
    return {"lufs": float(i.group(1)) if i else None,
            "tp": float(tp.group(1)) if tp else None,
            "lra": float(lra.group(1)) if lra else None}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--episodes", required=True)
    ap.add_argument("--skip-join", action="store_true")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    log = os.path.join(REPO, "logs", f"finish_{time.strftime('%Y%m%d_%H%M')}.log")
    print(f"log: {log}", flush=True)
    env = gpu_env()

    for ep in [e.strip() for e in args.episodes.split(",") if e.strip()]:
        chap, sub = ep.split(".")
        work = os.path.join(REPO, f"ep{int(chap):02d}_{sub}")
        eid = ep.replace(".", "_")
        plans = glob.glob(os.path.join(REPO, "scripts", f"Ep {ep} *SFX plan.json"))
        chunks = sorted(glob.glob(os.path.join(work, "c??.wav")))
        if not os.path.isdir(work) or len(chunks) < 2:
            print(f"{ep}: takes not ready ({len(chunks)} chunks)", flush=True)
            state_update(ep, status="waiting_takes", chunks=len(chunks))
            continue
        if not plans:
            print(f"{ep}: no SFX plan", flush=True)
            state_update(ep, status="no_plan")
            continue
        plan = plans[0]
        body = ",".join(os.path.basename(c)[:-4] for c in chunks[1:])

        align = os.path.join(work, "c01.align.json")
        if args.force or not os.path.exists(align):
            if sh([VENV, os.path.join(TOOLS, "align_words.py"), "--workdir", work,
                   "--chunks", "c01", "--model", "large-v3"], log, env) != 0:
                state_update(ep, status="align_failed", log=log)
                continue
        sh(["python3", os.path.join(TOOLS, "fix_anchors.py"), "--workdir", work,
            "--plan", plan], log)
        rc = sh(["python3", os.path.join(TOOLS, "mix_from_plan.py"), "--workdir", work,
                 "--chunk", "c01", "--plan", plan, "--check-only"], log)
        if rc != 0:
            state_update(ep, status="anchors_unresolved", log=log)
            print(f"{ep}: anchors unresolved - see {log}", flush=True)
            continue
        if args.force or not os.path.exists(os.path.join(work, "sfx", "_c01_mixed.wav")):
            if sh(["python3", os.path.join(TOOLS, "mix_from_plan.py"), "--workdir", work,
                   "--chunk", "c01", "--plan", plan], log) != 0:
                state_update(ep, status="mix_failed", log=log)
                continue
        sh(["python3", os.path.join(TOOLS, "qc_layer.py"), "--workdir", work, "--step", "20"], log)

        if args.skip_join:
            state_update(ep, status="mixed", log=log)
            continue
        out = os.path.join(work, f"ep{eid}_full_sfx.mp3")
        if args.force or not os.path.exists(out):
            if sh(["python3", os.path.join(TOOLS, "join_episode.py"), "--workdir", work,
                   "--episode", ep, "--body", body], log) != 0:
                state_update(ep, status="join_failed", log=log)
                continue
        m = lufs(out)
        state_update(ep, status="done", out=out, **m)
        print(f"{ep}: done {m}", flush=True)

    print("\nstate:", json.dumps(json.load(open(STATE)), indent=1)[:1500], flush=True)


if __name__ == "__main__":
    main()
