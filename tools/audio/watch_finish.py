#!/usr/bin/env python3
"""Watch for finished takes and run the post-take stage on them automatically.

The audio batch produces episodes one at a time; this loop polls every few minutes, runs
`finish_episodes.py` for the whole set (it skips episodes whose takes are not ready and
those already done), and stops once every episode of the set is `done`.

  python3 tools/audio/watch_finish.py [--episodes 4.1,...] [--every 240] [--max-hours 36]
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time

REPO = "/home/itcell/audiobooks/tdoi"
TOOLS = os.path.join(REPO, "tools", "audio")
STATE = os.path.join(REPO, "logs", "finish_state.json")
DEFAULT = ["4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "5.1", "5.2", "5.3", "5.4", "5.5",
           "5.6", "5.7", "5.8", "5.9", "6.1", "6.2", "6.3", "6.4", "6.5", "6.6"]


def statuses():
    try:
        return json.load(open(STATE))
    except Exception:  # noqa: BLE001
        return {}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--episodes", default=",".join(DEFAULT))
    ap.add_argument("--every", type=int, default=240)
    ap.add_argument("--max-hours", type=float, default=36.0)
    args = ap.parse_args()
    eps = [e.strip() for e in args.episodes.split(",") if e.strip()]
    deadline = time.time() + args.max_hours * 3600
    log = os.path.join(REPO, "logs", "finish_watch.log")

    while time.time() < deadline:
        with open(log, "a") as f:
            f.write(f"\n===== watch pass {time.strftime('%Y-%m-%d %H:%M:%S')} =====\n")
            f.flush()
            subprocess.run(["python3", os.path.join(TOOLS, "finish_episodes.py"),
                            "--episodes", ",".join(eps)], cwd=REPO, stdout=f,
                           stderr=subprocess.STDOUT, text=True)
        st = statuses()
        done = [e for e in eps if st.get(e, {}).get("status") == "done"]
        waiting = [e for e in eps if st.get(e, {}).get("status") in (None, "waiting_takes")]
        print(f"{len(done)}/{len(eps)} done, {len(waiting)} waiting for takes", flush=True)
        if not waiting and len(done) == len(eps):
            print("every episode is finished", flush=True)
            break
        time.sleep(args.every)
    print("watch loop exiting", flush=True)


if __name__ == "__main__":
    main()
