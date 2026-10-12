#!/usr/bin/env python3
"""Write the remaining episode scripts, one chapter at a time, with Claude Code.

For every book chapter that has no script yet:
  1. run `claude -p` with the style reference (Ep 1) + that chapter's source text
  2. validate the produced script (structure + word count)
  3. rebuild the HTML site, commit, push to GitHub — chapter by chapter
If Claude reports a 5-hour usage limit, sleep until it resets and retry the same chapter.

Usage: python3 tools/make_scripts.py [--only N]
Logs:  logs/make_scripts.log   Status: logs/progress.json
"""
import datetime
import glob
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(ROOT, "logs", "make_scripts.log")
STATUS = os.path.join(ROOT, "logs", "progress.json")
REPO = "malwaremanu/tdoi-hindi"
CLAUDE_TIMEOUT = 40 * 60

SHORT = {
    "ch01": "Ahmadnagar ka Qila",
    "ch02": "Badenweiler Lausanne",
    "ch03": "The Quest",
    "ch04": "The Discovery of India",
    "ch05": "Through the Ages",
    "ch06": "New Problems",
    "ch07": "The Last Phase Consolidation",
    "ch08": "Nationalism versus Imperialism",
    "ch09": "World War II",
    "ch10": "Ahmadnagar Fort Again",
}

PROMPT = """You are writing Episode {n} of a Hindi audiobook podcast called 'The Discovery of India, Hindi mein' (narrator: Asha). Read these two files first: 1) STYLE REFERENCE: '{ref}' 2) SOURCE TEXT: '{src}' (Chapter {n} of Nehru's The Discovery of India: {title} — sections: {sections}). Then write the Episode {n} script to '{out}' following the Ep 1 format EXACTLY: same header shape (# Ep {n}: <title> — Script, then a date line with 'Oct 13, 2026 · @Manupal Choudhary'), an '## Episode info' section, a 'Book ka sub-section | Script mein kahan' markdown table mapping every sub-section, then a '## Cold open' and numbered '## Part N: <Hindi part title>' sections. Rules: (a) narration text in Roman Hindi (Latin script, like Ep 1 — NOT Devanagari); (b) total roughly 4,000 words, 28-30 minutes of audio; (c) no sentence from the original book may be copied — retell everything in your own words, and where Nehru quotes poets or writers, only mention that he quotes; (d) your own ordering: open with a vivid cold-open scene drawn from the chapter (the most arresting moment), then work through the sub-sections; (e) keep Ep 1's tone: plain, concrete, short sentences, dates and places named precisely, no academic language. When done print only a 3-line summary with the word count."""

FIX_PROMPT = """The script you just wrote at '{out}' is not acceptable: {reason}. Rewrite the whole file so it follows these requirements exactly: {req}"""


def log(msg):
    line = f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] {msg}"
    print(line, flush=True)
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def status(**kw):
    os.makedirs(os.path.dirname(STATUS), exist_ok=True)
    data = {}
    if os.path.exists(STATUS):
        try:
            data = json.load(open(STATUS))
        except Exception:
            data = {}
    data.update(kw)
    data["updated"] = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"
    json.dump(data, open(STATUS, "w"), indent=2)


def existing_script(n):
    hits = glob.glob(os.path.join(ROOT, "scripts", f"Ep {n} *.md"))
    return hits[0] if hits else None


def script_out_path(n, title):
    return os.path.join(ROOT, "scripts", f"Ep {n} {title} — Script.md")


def run_claude(prompt, allow_tools="Read,Write", turns=20, timeout=CLAUDE_TIMEOUT):
    cmd = ["claude", "-p", prompt, "--allowedTools", allow_tools,
           "--max-turns", str(turns)]
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    try:
        p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True,
                           timeout=timeout, env=env)
    except subprocess.TimeoutExpired:
        return -1, "", "timeout"
    return p.returncode, (p.stdout or "") + (p.stderr or ""), ""


def limit_hit(out):
    return bool(re.search(r"(usage limit|rate.?limit|limit reached|5-hour|5 hour|try again later|overloaded)",
                          out, re.I))


def wait_out_limit(out):
    """Sleep until Claude's limit resets; fall back to 45 minutes."""
    m = re.search(r"reset[s]? at (\d{1,2})(?::(\d{2}))?\s*(am|pm)", out, re.I)
    minutes = 45
    if m:
        h, mi, ap = int(m.group(1)), int(m.group(2) or 0), m.group(3).lower()
        if ap == "pm" and h != 12:
            h += 12
        if ap == "am" and h == 12:
            h = 0
        now = datetime.datetime.now()
        target = now.replace(hour=h, minute=mi, second=0, microsecond=0)
        if target <= now:
            target += datetime.timedelta(days=1)
        minutes = max(2, int((target - now).total_seconds() // 60) + 1)
    log(f"usage limit hit — sleeping {minutes} min")
    status(state="waiting-for-limit", minutes=minutes)
    time.sleep(minutes * 60)


def validate(path):
    if not os.path.exists(path):
        return "file was not written"
    text = open(path, encoding="utf-8").read()
    words = len(re.sub(r"[|#*]", " ", text).split())
    if "## Cold open" not in text:
        return "missing '## Cold open' section"
    if "|" not in text or "Book ka sub-section" not in text:
        return "missing the sub-section mapping table"
    if not re.search(r"## Part 1", text):
        return "missing numbered Part sections"
    if words < 2500:
        return f"too short: {words} words (need ~4000)"
    if len(re.findall(r"[ऀ-ॿ]", text)) > 0:
        return "contains Devanagari — must be Roman Hindi"
    return None


def git_push():
    env = dict(os.environ,
               GIT_ASKPASS="/home/itcell/.local/bin/gh-askpass.sh",
               GIT_TERMINAL_PROMPT="0")
    subprocess.run(["git", "add", "-A"], cwd=ROOT, check=False, env=env)
    subprocess.run(["git", "commit", "-qm", "update"], cwd=ROOT, check=False, env=env)
    p = subprocess.run(["git", "push", "origin", "HEAD"], cwd=ROOT,
                       capture_output=True, text=True, env=env, timeout=300)
    return p.returncode == 0, (p.stdout + p.stderr).strip()[-300:]


def publish(n, title):
    subprocess.run([sys.executable, os.path.join(ROOT, "tools", "build_site.py")],
                   cwd=ROOT, check=False, capture_output=True, timeout=180)
    subprocess.run(["git", "add", "-A"], cwd=ROOT, check=False)
    subprocess.run(["git", "commit", "-qm", f"Ep {n}: {title} script + site"],
                   cwd=ROOT, check=False)
    ok, msg = git_push()
    log(f"push for Ep {n}: {'ok' if ok else 'FAILED — ' + msg}")
    return ok


def main():
    only = None
    if "--only" in sys.argv:
        only = int(sys.argv[sys.argv.index("--only") + 1])

    toc = {t["id"]: t for t in json.load(open(os.path.join(ROOT, "book", "toc.json")))}
    ref = os.path.join(ROOT, "scripts", "Ep 1 Ahmadnagar ka Qila — Script.md")
    os.makedirs(os.path.dirname(LOG), exist_ok=True)

    for n in range(1, 11):
        if only and n != only:
            continue
        cid = f"ch{n:02d}"
        if existing_script(n):
            log(f"Ep {n}: already written, skipping")
            continue
        meta = toc[cid]
        out = script_out_path(n, SHORT[cid])
        src = os.path.join(ROOT, "book", "chapters", cid + ".txt")
        prompt = PROMPT.format(
            n=n, ref=ref, src=src, title=meta["title"],
            sections=", ".join(meta["sections"]), out=out,
        )
        req = ("header + date line, '## Episode info', a 'Book ka sub-section | Script mein kahan' "
               "table covering every sub-section, '## Cold open', numbered '## Part N:' sections, "
               "Roman Hindi (Latin script), ~4,000 words, no copied sentences")

        attempt = 0
        while True:
            attempt += 1
            log(f"Ep {n} ({meta['title']}): claude attempt {attempt} starting")
            status(state="writing", episode=n, title=meta["title"], attempt=attempt)
            rc, out_txt, err = run_claude(prompt)
            if err == "timeout":
                log(f"Ep {n}: claude timed out after {CLAUDE_TIMEOUT}s")
                continue
            if rc != 0 and limit_hit(out_txt):
                wait_out_limit(out_txt)
                continue
            if limit_hit(out_txt) and not os.path.exists(out):
                wait_out_limit(out_txt)
                continue
            reason = validate(out)
            if reason is None:
                words = len(re.sub(r"[|#*]", " ",
                          open(out, encoding="utf-8").read()).split())
                log(f"Ep {n}: READY ({words} words) -> {os.path.basename(out)}")
                status(state="script-ready", episode=n, words=words)
                publish(n, meta["title"])
                break
            log(f"Ep {n}: invalid script — {reason}")
            if attempt >= 3:
                log(f"Ep {n}: giving up after 3 attempts")
                status(state="failed", episode=n, reason=reason)
                break
            prompt = prompt + "\n\nPREVIOUS ATTEMPT WAS REJECTED: " + reason + ". " + FIX_PROMPT.format(
                out=out, reason=reason, req=req)

    remaining = [n for n in range(1, 11) if not existing_script(n)]
    status(state="done" if not remaining else "incomplete", remaining=remaining)
    log(f"all done, remaining episodes: {remaining or 'none'}")


if __name__ == "__main__":
    main()
