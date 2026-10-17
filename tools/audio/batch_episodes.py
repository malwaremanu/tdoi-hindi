#!/usr/bin/env python3
"""Batch the audio stage for a list of episodes: Devanagari -> takes -> QC.

For each episode, in order:
  1. prep narration (script -> cleaned Roman text + cold-open-aware chunk plan)
  2. transliterate to Devanagari via the local gateway (cached per batch)
  3. TTS takes + joined clean master (build_episode.py)
  4. QC: LLM transcript (verify_gemini.py) + sentence audit (check_sentences.py)

Resume-safe: every step is skipped when its output already exists, per-episode state
is mirrored to logs/batch_state.json, and the run stops cleanly (exit 0) when the
TTS key pool is spent for the day so it can be re-launched after the reset.

  python3 tools/audio/batch_episodes.py --episodes 4.2,4.3,4.4 [--no-verify]
                                        [--reserve-requests 0]
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
PY = sys.executable or "python3"
POOL = os.path.expanduser("~/.hermes/keys/gemini_pool.json")
LIMIT = 10                      # requests per key per day (free tier)
REQUESTS_PER_EPISODE = 5        # cold open + ~4 body chunks at 1,300 words per request
STATE = os.path.join(REPO, "logs", "batch_state.json")


def sh(cmd, log):
    with open(log, "a") as f:
        f.write(f"\n$ {' '.join(cmd)}\n")
        f.flush()
        p = subprocess.run(cmd, cwd=REPO, stdout=f, stderr=subprocess.STDOUT, text=True)
    return p.returncode


def pool_remaining():
    try:
        data = json.load(open(POOL))
    except Exception:  # noqa: BLE001
        return 0
    if data.get("day") != time.strftime("%Y-%m-%d"):
        return LIMIT * len(data.get("keys", []))
    return sum(max(0, LIMIT - k.get("used_today", 0)) for k in data.get("keys", [])
               if k.get("valid") and not k.get("exhausted_today"))


def state_update(ep, **kw):
    data = {}
    if os.path.exists(STATE):
        data = json.load(open(STATE))
    rec = data.setdefault(ep, {})
    rec.update(kw)
    rec["updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
    tmp = STATE + ".tmp"
    json.dump(data, open(tmp, "w"), indent=1)
    os.replace(tmp, STATE)


def script_for(ep):
    hits = glob.glob(os.path.join(REPO, "scripts", f"Ep {ep} * — Script.md"))
    return hits[0] if hits else None


def cold_open_words(script):
    text = open(script, encoding="utf-8").read()
    m = re.search(r"^## Cold open\s*$", text, re.M)
    if not m:
        return 0
    nxt = re.search(r"^## ", text[m.end():], re.M)
    body = text[m.end():m.end() + nxt.start()] if nxt else text[m.end():]
    lines = [l for l in body.split("\n") if l.strip() and not l.strip().startswith("[SFX")]
    return len(" ".join(lines).split())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--episodes", required=True, help="comma-separated ids, e.g. 4.2,4.3")
    ap.add_argument("--no-verify", action="store_true")
    ap.add_argument("--reserve-requests", type=int, default=0,
                    help="keep this many requests for later work")
    ap.add_argument("--words-per-request", type=int, default=1300)
    ap.add_argument("--translit-backend", choices=["local", "api"], default="local")
    args = ap.parse_args()

    os.makedirs(os.path.join(REPO, "logs"), exist_ok=True)
    log = os.path.join(REPO, "logs", f"batch_{time.strftime('%Y%m%d_%H%M')}.log")
    print(f"log: {log}", flush=True)

    for ep in [e.strip() for e in args.episodes.split(",") if e.strip()]:
        script = script_for(ep)
        if not script:
            print(f"{ep}: script not found", flush=True)
            state_update(ep, status="no_script")
            continue
        chap, sub = ep.split(".")
        work = os.path.join(REPO, f"ep{int(chap):02d}_{sub}")   # ep04_2, ep05_9 ...
        os.makedirs(work, exist_ok=True)
        state_update(ep, status="running", workdir=work)

        remaining = pool_remaining()
        if remaining - args.reserve_requests < REQUESTS_PER_EPISODE:
            print(f"{ep}: stopping, only {remaining} TTS requests left "
                  f"(reserve {args.reserve_requests}, need ~{REQUESTS_PER_EPISODE})", flush=True)
            state_update(ep, status="quota_wait", requests_left=remaining)
            break

        dev = os.path.join(work, "narration_dev.txt")
        rom = os.path.join(work, "narration_rom.txt")
        cold = cold_open_words(script)
        first = int((cold * 1.02) // 10 * 10 + 10)          # round up past the cold open
        print(f"\n=== Ep {ep}: cold open {cold} words -> --first-chunk-words {first} ===", flush=True)

        if not os.path.exists(rom) or os.path.getsize(rom) < 1000:
            if sh([PY, os.path.join(TOOLS, "prep_narration.py"), "--script", script,
                   "--workdir", work, "--first-chunk-words", str(first),
                   "--words", str(args.words_per_request)], log) != 0:
                state_update(ep, status="prep_failed")
                continue

        if not os.path.exists(dev) or os.path.getsize(dev) < 1000:
            if sh([PY, os.path.join(TOOLS, "transliterate.py"), "--rom", rom,
                   "--out", dev, "--backend", args.translit_backend], log) != 0:
                state_update(ep, status="translit_failed")
                continue
        latin = len(re.findall(r"[A-Za-z]", open(dev, encoding="utf-8").read()))
        if latin:
            print(f"{ep}: {latin} Latin characters left in the Devanagari narration", flush=True)
            state_update(ep, status="translit_latin_left", latin=latin)
            continue

        master = os.path.join(work, f"ep{ep.replace('.', '_')}_full_clean.mp3")
        rc = sh([PY, os.path.join(TOOLS, "build_episode.py"), "--script", script,
                 "--text", dev, "--workdir", work, "--out", master,
                 "--first-chunk-words", str(first), "--words", str(args.words_per_request),
                 "--max-requests", str(REQUESTS_PER_EPISODE + 1)], log)
        if rc != 0:
            tail = open(log).read()[-400:]
            if "spent for today" in tail:
                print(f"{ep}: TTS pool spent for today — stop", flush=True)
                state_update(ep, status="quota_wait", requests_left=pool_remaining())
                break
            state_update(ep, status="build_failed", log=log)
            continue

        words = len(open(dev, encoding="utf-8").read().split())
        state_update(ep, status="audio_ok", words=words, master=master,
                     requests_left=pool_remaining())

        if args.no_verify:
            continue
        chunks = sorted(glob.glob(os.path.join(work, "c??.txt")))
        names = ",".join(os.path.basename(c)[:-4] for c in chunks)
        ok = sh([PY, os.path.join(TOOLS, "verify_gemini.py"), "--workdir", work,
                 "--chunks", names], log) == 0
        if ok:
            sh([PY, os.path.join(TOOLS, "check_sentences.py"), "--workdir", work,
                "--chunks", names], log)
            state_update(ep, status="verified", words=words, master=master)
        else:
            state_update(ep, status="verify_pending", words=words, master=master)
        print(f"Ep {ep}: audio ok ({words} words), requests left {pool_remaining()}", flush=True)

    print("\nstate:", json.dumps(json.load(open(STATE)), indent=1)[:1200], flush=True)


if __name__ == "__main__":
    main()
