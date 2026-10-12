#!/usr/bin/env python3
"""Render the repo (book text + episode scripts) as a static HTML site into site/.

Usage: python3 tools/build_site.py
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")

CSS = """
:root {
  --bg: #0f1115; --panel: #161a21; --panel2: #1c2129; --ink: #e7e4dc;
  --dim: #9aa3af; --accent: #e0a458; --line: #262c36; --link: #7fb3ff;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0; background: var(--bg); color: var(--ink);
  font-family: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  font-size: 18px; line-height: 1.7;
}
.wrap { max-width: 820px; margin: 0 auto; padding: 0 22px 80px; }
header.site {
  border-bottom: 1px solid var(--line); background: var(--panel);
  position: sticky; top: 0; z-index: 5;
}
header.site .wrap { display: flex; align-items: center; gap: 18px; padding: 14px 22px; }
header.site a { color: var(--ink); text-decoration: none; }
.brand { font-weight: 700; letter-spacing: .02em; }
.brand span { color: var(--accent); }
nav.top { margin-left: auto; display: flex; gap: 16px; font-family: system-ui, sans-serif; font-size: 14px; }
nav.top a { color: var(--dim); }
nav.top a:hover, nav.top a.on { color: var(--accent); }
h1, h2, h3 { line-height: 1.25; font-weight: 700; }
h1 { font-size: 2.1rem; margin: 46px 0 10px; }
h2 { font-size: 1.45rem; margin: 44px 0 12px; color: var(--accent); }
h3 { font-size: 1.12rem; margin: 30px 0 8px; }
p { margin: 0 0 18px; }
a { color: var(--link); }
.meta { color: var(--dim); font-family: system-ui, sans-serif; font-size: 14px; }
.lead { font-size: 1.12rem; color: #cfd3da; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 14px; margin: 26px 0; }
.card {
  background: var(--panel); border: 1px solid var(--line); border-radius: 12px;
  padding: 16px 16px 14px; text-decoration: none; color: var(--ink); display: block;
  transition: border-color .15s, transform .15s;
}
.card:hover { border-color: var(--accent); transform: translateY(-2px); }
.card .n { font-family: system-ui, sans-serif; font-size: 12px; letter-spacing: .12em;
  text-transform: uppercase; color: var(--accent); }
.card .t { font-weight: 700; margin-top: 6px; }
.card .d { color: var(--dim); font-family: system-ui, sans-serif; font-size: 13px; margin-top: 6px; }
.badge { display: inline-block; font-family: system-ui, sans-serif; font-size: 12px;
  border: 1px solid var(--line); border-radius: 999px; padding: 2px 10px; color: var(--dim); }
.badge.done { color: #86d3a0; border-color: #2c4a37; }
.badge.wip { color: var(--accent); border-color: #4a3a24; }
.toc { list-style: none; padding: 0; margin: 20px 0; }
.toc li { border-bottom: 1px dashed var(--line); padding: 10px 2px; display: flex; gap: 12px; align-items: baseline; }
.toc .num { font-family: system-ui, sans-serif; font-size: 13px; color: var(--dim); min-width: 34px; }
.toc .w { margin-left: auto; font-family: system-ui, sans-serif; font-size: 13px; color: var(--dim); }
nav.pager { display: flex; justify-content: space-between; gap: 16px; margin-top: 56px;
  border-top: 1px solid var(--line); padding-top: 18px; font-family: system-ui, sans-serif; font-size: 15px; }
table { border-collapse: collapse; width: 100%; margin: 20px 0; font-family: system-ui, sans-serif; font-size: 15px; }
th, td { border: 1px solid var(--line); padding: 9px 11px; text-align: left; vertical-align: top; }
th { background: var(--panel2); color: var(--accent); font-weight: 600; }
blockquote { margin: 22px 0; padding: 4px 18px; border-left: 3px solid var(--accent); color: #c9cdd4; font-style: italic; }
code { background: var(--panel2); padding: 1px 6px; border-radius: 5px; font-size: .9em; }
hr { border: 0; border-top: 1px solid var(--line); margin: 40px 0; }
footer.site { border-top: 1px solid var(--line); color: var(--dim);
  font-family: system-ui, sans-serif; font-size: 13px; padding: 22px; text-align: center; }
.section-label { font-family: system-ui, sans-serif; font-size: 12px; letter-spacing: .14em;
  text-transform: uppercase; color: var(--dim); margin-top: 40px; }
"""

PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><link rel="stylesheet" href="{css}">
</head><body>
<header class="site"><div class="wrap">
  <a class="brand" href="{base}index.html">The Discovery of India <span>· Hindi mein</span></a>
  <nav class="top">
    <a href="{base}book/index.html"{bookon}>Book</a>
    <a href="{base}scripts/index.html"{scripson}>Scripts</a>
    <a href="https://github.com/{repo}" target="_blank" rel="noopener">GitHub</a>
  </nav>
</div></header>
<main class="wrap">{body}</main>
<footer class="site">The Discovery of India · Jawaharlal Nehru — narration by Asha · rendered by tools/build_site.py</footer>
</body></html>
"""


def esc(s):
    return html.escape(s, quote=False)


def inline(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def render_markdown(text):
    """Small markdown subset: h1-h3, paragraphs, lists, tables, blockquote, hr."""
    out, i, lines = [], 0, text.split("\n")
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if ln.startswith("# "):
            out.append(f"<h1>{inline(ln[2:].strip())}</h1>")
        elif ln.startswith("## "):
            out.append(f"<h2>{inline(ln[3:].strip())}</h2>")
        elif ln.startswith("### "):
            out.append(f"<h3>{inline(ln[4:].strip())}</h3>")
        elif ln.strip() == "---":
            out.append("<hr>")
        elif ln.lstrip().startswith(">"):
            buf = []
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                buf.append(lines[i].lstrip()[1:].strip())
                i += 1
            out.append("<blockquote>" + " ".join(inline(b) for b in buf if b) + "</blockquote>")
            continue
        elif ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head, body = rows[0], rows[1:]
            if body and all(set(c) <= set("- :") for c in body[0]):
                body = body[1:]
            t = ["<table><thead><tr>"] + [f"<th>{inline(c)}</th>" for c in head] + ["</tr></thead><tbody>"]
            for r in body:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue
        elif re.match(r"^\s*[-*] ", ln):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*] ", lines[i]):
                items.append(re.sub(r"^\s*[-*] ", "", lines[i]))
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            continue
        else:
            buf = []
            while i < len(lines) and lines[i].strip() and not re.match(
                r"^(#|\||>|---|\s*[-*] )", lines[i]
            ):
                buf.append(lines[i].strip())
                i += 1
            out.append("<p>" + inline(" ".join(buf)) + "</p>")
            continue
        i += 1
    return "\n".join(out)


def txt_to_html(text):
    """Book chapters: '# title' and '## section' markers, blank-line paragraphs."""
    out, paras, buf = [], [], []

    def flush():
        if buf:
            paras.append("<p>" + inline(" ".join(buf)) + "</p>")
            buf.clear()

    for ln in text.split("\n"):
        if not ln.strip():
            flush()
        elif ln.startswith("# "):
            flush()
            out.append(f"<h1>{inline(ln[2:].strip())}</h1>")
        elif ln.startswith("## "):
            flush()
            out.append(f"<h2 id=\"{slug(ln[3:].strip())}\">{inline(ln[3:].strip())}</h2>")
        elif ln.startswith(">"):
            flush()
            out.append(f"<blockquote>{inline(ln.lstrip('> ').strip())}</blockquote>")
        else:
            buf.append(ln.strip())
    flush()
    return "\n".join(out)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def write(rel, title, body, base="", bookon="", scripson=""):
    path = os.path.join(SITE, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    css = base + "assets/style.css"
    with open(path, "w", encoding="utf-8") as f:
        f.write(PAGE.format(title=esc(title), css=css, base=base, body=body,
                            bookon=bookon, scripson=scripson, repo=REPO))


REPO = "malwaremanu/tdoi"

CH_TITLES = {}
TOC = json.load(open(os.path.join(ROOT, "book", "toc.json"), encoding="utf-8"))
CH_META = {t["id"]: t for t in TOC}
BOOK_IDS = [t["id"] for t in TOC if t["id"].startswith("ch")]

def ep_number(name):
    m = re.match(r"Ep\s*(\d+)", name)
    return int(m.group(1)) if m else 999


SCRIPTS = sorted(
    (f for f in os.listdir(os.path.join(ROOT, "scripts")) if f.endswith(".md")),
    key=ep_number,
)


def script_meta(name, text):
    m = re.search(r"^#\s*(.+?)\s*—\s*Script", text, re.M)
    title = m.group(1) if m else name
    words = len(re.sub(r"[|#*]", " ", text).split())
    return title, words


def main():
    os.makedirs(os.path.join(SITE, "assets"), exist_ok=True)
    open(os.path.join(SITE, "assets", "style.css"), "w").write(CSS)

    # ---- book index ----
    items = []
    for i, cid in enumerate(BOOK_IDS, 1):
        meta = CH_META[cid]
        items.append(
            f'<a class="card" href="{cid}.html"><div class="n">Chapter {i}</div>'
            f'<div class="t">{esc(meta["title"])}</div>'
            f'<div class="d">{meta["words"]:,} words · {len(meta["sections"])} sections</div></a>'
        )
    body = (
        "<h1>The Discovery of India</h1>"
        '<p class="lead">Jawaharlal Nehru · Ahmadnagar Fort, 1942–45. Full text, split into '
        "the book\'s own chapters.</p>"
        f'<p class="meta">{sum(t["words"] for t in TOC):,} words · {len(TOC)} parts · '
        'source: <a href="../book/the-discovery-of-india.pdf">PDF</a> / '
        '<a href="../book/the-discovery-of-india.txt">plain text</a></p>'
        '<div class="grid">' + "".join(items) + "</div>"
    )
    write("book/index.html", "Book · The Discovery of India", body, base="../", bookon=' class="on"')

    # ---- book chapters ----
    for i, cid in enumerate(BOOK_IDS):
        meta = CH_META[cid]
        text = open(os.path.join(ROOT, "book", "chapters", cid + ".txt"), encoding="utf-8").read()
        secs = "".join(
            f'<li><span class="num">{n:02d}</span><a href="#{slug(s)}">{esc(s)}</a></li>'
            for n, s in enumerate(meta["sections"], 1)
        )
        prev_h = (
            f'<a href="{BOOK_IDS[i-1]}.html">← {esc(CH_META[BOOK_IDS[i-1]]["title"])}</a>'
            if i else '<a href="index.html">← Contents</a>'
        )
        nxt = (
            f'<a href="{BOOK_IDS[i+1]}.html">'
            f'{esc(CH_META[BOOK_IDS[i+1]]["title"])} →</a>'
            if i + 1 < len(BOOK_IDS)
            else '<a href="index.html">Contents →</a>'
        )
        body = (
            f'<p class="section-label">Chapter {i+1} of {len(BOOK_IDS)}</p>'
            f"<h1>{esc(meta['title'])}</h1>"
            f'<p class="meta">{meta["words"]:,} words · {len(meta["sections"])} sections · '
            f'narrated as Episode {i+1}</p>'
            f'<ul class="toc">{secs}</ul>'
            + txt_to_html(text)
            + f'<nav class="pager">{prev_h}{nxt}</nav>'
        )
        write(f"book/{cid}.html", f"{meta['title']} · The Discovery of India", body,
              base="../", bookon=' class="on"')

    # ---- scripts index ----
    cards = []
    for name in SCRIPTS:
        text = open(os.path.join(ROOT, "scripts", name), encoding="utf-8").read()
        title, words = script_meta(name, text)
        num = re.match(r"Ep\s*(\d+)", name)
        n = num.group(1) if num else "?"
        ep_id = "ep" + n.zfill(2)
        cards.append(
            f'<a class="card" href="{ep_id}.html"><div class="n">Episode {n}</div>'
            f'<div class="t">{esc(title)}</div>'
            f'<div class="d">{words:,} words · <span class="badge done">script ready</span></div></a>'
        )
    body = (
        "<h1>Episode scripts</h1>"
        '<p class="lead">Every chapter of the book, retold as one podcast episode in Roman Hindi, '
        "read by Asha. Scripts first — audio is generated later, all in one pass.</p>"
        '<div class="grid">' + "".join(cards) + "</div>"
        '<p class="meta">Audio for these scripts is not generated yet; when it is, the whole '
        "season goes out as a single batch.</p>"
    )
    write("scripts/index.html", "Scripts · The Discovery of India", body, base="../",
          scripson=' class="on"')

    for name in SCRIPTS:
        text = open(os.path.join(ROOT, "scripts", name), encoding="utf-8").read()
        title, words = script_meta(name, text)
        num = re.match(r"Ep\s*(\d+)", name)
        n = int(num.group(1)) if num else 0
        prev_h = (
            f'<a href="ep{n-1:02d}.html">← Episode {n-1}</a>' if n > 1
            else '<a href="index.html">← All scripts</a>'
        )
        nxt = f'<a href="ep{n+1:02d}.html">Episode {n+1} →</a>' if (n + 1) <= len(SCRIPTS) else '<a href="index.html">All scripts →</a>'
        body = (
            f'<p class="section-label">Episode {n} · script</p>'
            + render_markdown(text)
            + f'<nav class="pager">{prev_h}{nxt}</nav>'
        )
        write(f"scripts/ep{n:02d}.html", f"Episode {n} · {title}", body, base="../",
              scripson=' class="on"')

    # ---- home ----
    chapters_cards = "".join(
        f'<a class="card" href="book/{cid}.html"><div class="n">Chapter {i}</div>'
        f'<div class="t">{esc(CH_META[cid]["title"])}</div>'
        f'<div class="d">{CH_META[cid]["words"]:,} words</div></a>'
        for i, cid in enumerate(BOOK_IDS, 1)
    )
    script_cards = []
    for s in SCRIPTS:
        n = ep_number(s)
        text = open(os.path.join(ROOT, "scripts", s), encoding="utf-8").read()
        title, _w = script_meta(s, text)
        script_cards.append(
            f'<a class="card" href="scripts/ep{n:02d}.html">'
            f'<div class="n">Episode {n}</div>'
            f'<div class="t">{esc(title)}</div>'
            f'<div class="d"><span class="badge done">script ready</span></div></a>'
        )
    script_cards = "".join(script_cards)
    body = (
        "<h1>The Discovery of India, Hindi mein</h1>"
        '<p class="lead">Nehru\'s 1946 classic, chapter by chapter, rewritten in plain Roman Hindi '
        "as a podcast read by <strong>Asha</strong> — no line of the original is copied, only its "
        "story.</p>"
        '<p class="meta">10 chapters · '
        f'{sum(t["words"] for t in TOC):,} words of source · {len(SCRIPTS)} script(s) written · '
        "audio pending</p>"
        '<p><a class="badge done" href="book/index.html">Read the book</a> &nbsp;'
        '<a class="badge done" href="scripts/index.html">Episode scripts</a></p>'
        '<div class="section-label">Episodes</div><div class="grid">' + script_cards + "</div>"
        '<div class="section-label">Book · chapter by chapter</div><div class="grid">'
        + chapters_cards + "</div>"
    )
    write("index.html", "The Discovery of India, Hindi mein", body)

    n_scripts = len(SCRIPTS)
    print(f"site built: {1 + 2 + len(BOOK_IDS) + n_scripts} pages, {n_scripts} scripts")


if __name__ == "__main__":
    main()
