# The Discovery of India — Hindi mein

Jawaharlal Nehru's *The Discovery of India* (1946), chapter by chapter, retold as a Hindi
podcast read by **Asha**. Scripts first; audio is generated afterwards, in one pass for the
whole season.

## Layout

| Path | What it is |
| --- | --- |
| `book/` | Source text: `the-discovery-of-india.pdf`, full `the-discovery-of-india.txt`, `toc.json`, and one file per chapter in `chapters/` |
| `scripts/` | Episode scripts — one per book chapter, `Ep N <chapter title> — Script.md` |
| `tools/` | `build_site.py` renders `site/`, `make_scripts.py` drives Claude Code chapter by chapter, `audio/` holds the TTS/join pipeline used for Ep 1 |
| `ep01/` | Working dir of the Ep 1 audio experiment (chunk texts kept, wav/mp3 gitignored) |
| `site/` | Generated static HTML — open `site/index.html` |

## Episode format

Every script follows the Ep 1 shape: header + date line, `## Episode info`, a
`Book ka sub-section | Script mein kahan` mapping table, a `## Cold open`, then
`## Part N:` sections. Narration is **Roman Hindi** (Latin script), ~4,000 words ≈ 28–30 min,
and never copies a sentence from the original.

## Rebuild the site

```bash
python3 tools/build_site.py
```
