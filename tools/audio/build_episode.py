#!/usr/bin/env python3
"""Build a full episode audio file from a script, in as few TTS requests as possible.

Hard constraints (Gemini 3.8 Flash TTS): 8,192 input tokens per request and
~655 s of audio per response — a 30-minute episode cannot be one request, so the
text is packed into paragraph-aligned chunks that stay well under both limits and
then joined into a single continuous file.

  python3 tools/audio/build_episode.py --script "scripts/Ep 1 ... — Script.md" \
      --text /path/narration_dev.txt --voice Fola --out ep01/ep01_full.mp3

--text skips the extraction/transliteration step when a prepared Devanagari
narration already exists (that is the normal flow: transliterate once with the
local gateway, never with a paid/free TTS request).
"""
import argparse
import json
import base64
import os
import re
import struct
import subprocess
import sys
import time
import urllib.error
import urllib.request

FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
FP = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffprobe"
ENV = "/home/itcell/.hermes/.env"
HOST = "generativelanguage.googleapis.com"
PAUSE = 0.6            # breath between takes
REQUESTS_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
                            "logs", "tts_requests.jsonl")


POOL = os.path.expanduser("~/.hermes/keys/gemini_pool.json")
FREE_LIMIT_PER_DAY = 10     # free tier: requests per key per day


def _pool_load():
    data = json.load(open(POOL))
    today = time.strftime("%Y-%m-%d")
    if data.get("day") != today:                 # reset the daily counters
        for k in data["keys"]:
            k["used_today"] = 0
        data["day"] = today
    return data


def _pool_save(data):
    data["updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
    tmp = POOL + ".tmp"
    json.dump(data, open(tmp, "w"), indent=1)
    os.replace(tmp, POOL)


def pick_key():
    """Least-used usable key of the day; None when every key is spent."""
    data = _pool_load()
    usable = [k for k in data["keys"]
              if k.get("valid") and not k.get("exhausted_today")
              and k.get("used_today", 0) < FREE_LIMIT_PER_DAY]
    if not usable:
        return None
    usable.sort(key=lambda k: k.get("used_today", 0))
    return usable[0]["key"]


def mark_key(key, status):
    data = _pool_load()
    for k in data["keys"]:
        if k["key"] == key:
            k["used_today"] = k.get("used_today", 0) + 1
            k["last_used"] = time.strftime("%Y-%m-%d %H:%M:%S")
            if status in (429, 403):
                k["exhausted_today"] = True
    _pool_save(data)


def api_key():
    k = pick_key()
    if not k:
        raise SystemExit("every key in the pool is spent for today")
    return k


def wav_bytes(pcm: bytes, rate: int = 24000) -> bytes:
    return (b"RIFF" + struct.pack("<I", 36 + len(pcm)) + b"WAVEfmt "
            + struct.pack("<IHHIIHH", 16, 1, 1, rate, rate * 2, 2, 16)
            + b"data" + struct.pack("<I", len(pcm)) + pcm)


def log_request(**kw):
    kw["ts"] = f"{time.time():.0f}"
    os.makedirs(os.path.dirname(REQUESTS_LOG), exist_ok=True)
    with open(REQUESTS_LOG, "a") as f:
        f.write(json.dumps(kw) + "\n")


def synthesize(text: str, voice: str, model: str, out_wav: str, timeout=600):
    payload = {
        "contents": [{"parts": [{"text": text}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}},
        },
    }
    key = api_key()
    req = urllib.request.Request(
        f"https://{HOST}/v1beta/models/{model}:generateContent",
        data=json.dumps(payload).encode(),
        headers={"x-goog-api-key": key, "Content-Type": "application/json"},
        method="POST")
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:400]
        mark_key(key, e.code)
        log_request(model=model, voice=voice, status=e.code, words=len(text.split()),
                    key=key[-6:], error=body[:200])
        raise RuntimeError(f"HTTP {e.code}: {body}") from None
    mark_key(key, 200)
    log_request(model=model, voice=voice, status=200, words=len(text.split()),
                key=key[-6:], chars=len(text), seconds=round(time.time() - t0, 1))
    cand = data.get("candidates") or []
    if not cand:
        raise RuntimeError(f"no candidates: {json.dumps(data)[:300]}")
    part = (cand[0].get("content") or {}).get("parts") or [{}]
    inline = part[0].get("inlineData") or {}
    raw = base64.b64decode(inline.get("data") or "")
    if not raw:
        raise RuntimeError("empty audio in response: " + json.dumps(data)[:300])
    mime = (inline.get("mimeType") or "").lower()
    if "wav" not in mime:
        raw = wav_bytes(raw)
    with open(out_wav, "wb") as f:
        f.write(raw)
    return time.time() - t0


def dur(path):
    r = subprocess.run([FP, "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(r.stdout.strip())


def extract_narration(script_path):
    text = open(script_path, encoding="utf-8").read()
    body = text[text.index("## Cold open"):]
    if "## Sources" in body:
        body = body[:body.index("## Sources")]
    body = re.sub(r"^##\s+.*$", "", body, flags=re.M)
    body = re.sub(r"\*\*|\*", "", body)
    body = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", body)
    return re.sub(r"\n{3,}", "\n\n", body).strip()


def split_chunks(text, target_words):
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks, cur = [], []
    n = 0
    for p in paras:
        w = len(p.split())
        if cur and n + w > target_words:
            chunks.append("\n\n".join(cur))
            cur, n = [], 0
        cur.append(p)
        n += w
    if cur:
        chunks.append("\n\n".join(cur))
    return chunks


def join(chunks_dir, names, out_wav, out_mp3, pause=PAUSE):
    tmp = os.path.join(chunks_dir, "_norm")
    os.makedirs(tmp, exist_ok=True)
    normed = []
    for n in names:
        src = os.path.join(chunks_dir, n + ".wav")
        dst = os.path.join(tmp, n + ".wav")
        subprocess.run([FF, "-y", "-i", src, "-af",
                        "dynaudnorm=f=200:g=5:p=0.95,aresample=48000",
                        "-ac", "1", "-ar", "48000", dst],
                       capture_output=True, check=True)
        normed.append((n, dst))
    inputs, filters, offset = [], [], 0.0
    for i, (_, p) in enumerate(normed):
        inputs += ["-i", p]
        d = dur(p)
        ms = int(round(offset * 1000))
        filters.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=mono,"
                       f"adelay={ms}|{ms}[a{i}]")
        offset += d + pause
    labels = "".join(f"[a{i}]" for i in range(len(normed)))
    filters.append(f"{labels}amix=inputs={len(normed)}:normalize=0,"
                   f"atrim=0:{offset + 0.8:.3f},asetpts=PTS-STARTPTS[out]")
    subprocess.run([FF, "-y", *inputs, "-filter_complex", ";".join(filters),
                    "-map", "[out]", "-ar", "48000", "-ac", "1", out_wav],
                   capture_output=True, check=True)
    subprocess.run([FF, "-y", "-i", out_wav,
                    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                    "-ar", "44100", "-ac", "1",
                    "-codec:a", "libmp3lame", "-q:a", "2", out_mp3],
                   capture_output=True, check=True)
    return offset


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--script", required=True)
    ap.add_argument("--text", help="prepared (transliterated) narration file")
    ap.add_argument("--workdir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--voice", default="Fola")
    ap.add_argument("--model", default="gemini-3.8-flash-tts")
    ap.add_argument("--words", type=int, default=550, help="target words per request")
    ap.add_argument("--max-requests", type=int, default=10)
    ap.add_argument("--only-generate", action="store_true")
    args = ap.parse_args()

    text = open(args.text, encoding="utf-8").read() if args.text else extract_narration(args.script)
    chunks = split_chunks(text, args.words)
    os.makedirs(args.workdir, exist_ok=True)
    names = []
    for i, c in enumerate(chunks, 1):
        name = f"c{i:02d}"
        names.append(name)
        open(os.path.join(args.workdir, name + ".txt"), "w", encoding="utf-8").write(c)
    total_words = sum(len(c.split()) for c in chunks)
    print(f"{len(chunks)} chunks, {total_words} words, "
          f"~{total_words / 140:.0f} min audio", flush=True)
    for i, (n, c) in enumerate(zip(names, chunks), 1):
        print(f"  {n}: {len(c.split())} words", flush=True)

    made = 0
    for n, c in zip(names, chunks):
        wav = os.path.join(args.workdir, n + ".wav")
        if os.path.exists(wav) and os.path.getsize(wav) > 1000:
            print(f"{n}: already generated", flush=True)
            continue
        if made >= args.max_requests:
            print(f"request budget ({args.max_requests}) reached — stopping", flush=True)
            sys.exit(3)
        for attempt in (1, 2, 3):
            try:
                t = synthesize(c, args.voice, args.model, wav)
                made += 1
                print(f"{n}: ok in {t:.1f}s, {dur(wav):.1f}s audio", flush=True)
                break
            except RuntimeError as e:
                msg = str(e)
                quota = ("HTTP 429" in msg) or ("HTTP 403" in msg)
                if quota:
                    left = sum(1 for k in _pool_load()["keys"]
                               if k.get("valid") and not k.get("exhausted_today"))
                    print(f"{n}: quota hit on a key, {left} keys left in pool", flush=True)
                    if left == 0:
                        print("every key spent for today — stopping", flush=True)
                        sys.exit(4)
                    made += 1
                    time.sleep(5)
                    continue
                print(f"{n}: attempt {attempt} failed — {msg[:250]}", flush=True)
                if attempt == 1:
                    made += 1
                    time.sleep(20)
                else:
                    sys.exit(5)
    if args.only_generate:
        return
    raw = os.path.join(args.workdir, "_full_raw.wav")
    total = join(args.workdir, names, raw, args.out)
    print(f"joined: {dur(args.out):.1f}s -> {args.out}", flush=True)


if __name__ == "__main__":
    main()
