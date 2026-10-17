# Ep 5.5 — SFX plan (cold open)

Cold open = `## Cold open` .. `## Ab tak` — **362 narration shabd**, chunk `c01`.
Uske teen hisse hain: **Paris ka kamra** (barsaat, do aadmi, Malraux ka sawal — shabd 230),
**1944, Ahmadnagar ki kothri** (Nehru us sawal ko kitaab mein utaar rahe hain — shabd 82),
aur **ident + do sawal** (Asha ka namaskar — shabd 50).

Chain wahi hai jo Ep 3 / Ep 4.1 ka hai: narration anchor hai, har bed uske neeche rehta hai,
host intro dry hai, aur aakhri bed ke baad body se pehle sannata hai. Har cue phrase-locked hai
(Devanagari anchors), isliye take dobara render hone par bhi cue apne shabd par hi land karega;
har anchor ke saath ek `fallback_at` (andaaza, 160 shabd/min) bhi diya gaya hai.

## Cast (source files)

| id | file | what it is |
|---|---|---|
| ROOM | `ep01/sfx/raw_fs/b1_bed.mp3` | Paris ke kamre ka sannata (bed) |
| RAIN | `synth:rain` | kheeki ke sheeshay par barsaat (bed) |
| DRONE | `ep02/sfx/raw_fs/drone.mp3` | 1944 ki kothri ka dabaav (bed) |
| TANPURA | `ep03/sfx/raw_fs/tanpura.mp3` | ek lamba, dheema sur (score) |
| ENGINE | `ep02/sfx/raw_fs/engine.mp3` | neeche sadak se kisi gaadi ka door ka shor |
| WICKER | `ep02/sfx/raw_fs/wicker.mp3` | kursi ki chare-mar |
| STAB | `ep01/sfx/raw_fs/s3_stab.mp3` | talwar ka zor — scene ka ek hi sabse ooncha cue |
| CROWD | `ep03/sfx/raw_fs/crowd.mp3` | jalte shehar ka door ka shor (kabhi shabd nahi) |
| RIVER | `synth:river_wash` | khoon ki nadiyon ka gehra bahav |
| PEN | `ep01/sfx/raw_fs/s8b_pen.mp3` | kitaab par qalam |
| STEPS | `ep03/sfx/raw_fs/steps.mp3` | dhool par kadam |
| LATCH | `ep01/sfx/raw_fs/s6_latch.mp3` | darwaze ki chitkani |

Synthesised cues (`synth:rain`, `synth:river_wash`) mix script mein bante hain — koi nayi file
download nahi hui, sab kuch repo pool se hai.

## Scene map (waqt andaaze se: 0.30 s prati shabd + 0.5 s prati para)

| hissa | script lines | shabd | andaaza waqt | kya bajta hai |
|---|---|---|---|---|
| Paris ka kamra, barsaat aur sawal | 36–62 (p00–p13) | 230 | 0–75 s | ROOM + RAIN, ENGINE, WICKER, STAB/CROWD/RIVER |
| 1944, Ahmadnagar ki kothri | 66–70 (p14–p16) | 82 | 76–102 s | DRONE + PEN + STEPS + LATCH, aur TANPURA chadhta hai |
| ident + do sawal | 74–78 (p17–p19) | 50 | 102–119 s | **kuch nahi** — poora dry |

## Beds (poore hisse ke neeche)

| id | sound | start | end | level | envelope |
|---|---|---|---|---|---|
| ROOM | `ep01/sfx/raw_fs/b1_bed.mp3` | 0.0 s | `पक्की हैं` (p13 ka ant, ~75.2 s) | −25 dB | 2 s mein aata hai; p05 par −8, p10 par −9; 73.0 s se girta hai, 76.0 s par −60 (chala jaata hai) |
| RAIN | `synth:rain` (highpass=120,lowpass=7000) | 0.0 s | `पक्की हैं` (~75.2 s) | −23 dB | 1.6 s mein aata hai; wahi do hush (−10/−11); 71.0 s se dheema, 73.8 s −3, 75.0 s −8, 75.9 s par −60 — "phir ek saath band" |
| DRONE | `ep02/sfx/raw_fs/drone.mp3` (lowpass=900) | `उन्नीस सौ चवालीस` −0.3 s | `नमस्कार` (doosra) −0.25 s | −26 dB | 3 s mein aata hai; tanpura ke liye −5 dB; intro ke shabd par khatam |

## Score — sirf ek swell

TANPURA, −24 dB, centre. **Ek hi baar** aata hai, **ek hi baar** chadhta hai, phir chala jaata hai:

- `छह दरवाजे हैं` (script ka "darwaze par shuru") se 0.8 s pehle enter,
- `पांच दरवाजे आज खुलेंगे` par poore zor par (yahi cold open ka sabse ooncha shabd-moment hai),
- `नमस्कार` (doosra — yaani Asha ka ident) se 0.25 s pehle out. Intro aur dono sawal par koi
  score nahi; `points` (layer ke shuru se): 0 s −60 · 1.4 s 0 · 4.0 s 0 · 5.6 s −60.

Anchor `छह दरवाजे हैं` par `"occurrence": 1`, aur `end_phrase` `["नमस्कार"]` par
`"end_occurrence": 2` — kyunki "नमस्कार" cold open mein **do baar** aata hai (p05 "namaskar se
pehle" aur p17 ident). Ye likhna zaroori hai, warna bed/cue pehle wale "namaskar" par ruk jaayega.

## Duck — sirf ek

Malraux ke sawal par: `किस ताकत ने एक बड़े` (p11), `pre` 1.2 s, `post` 2.4 s, `gain` 0.30.
Iske pehle jang ka poora zor hai (STAB/CROWD/RIVER) aur turant baad "aur yahan?" wala hush —
duniya neeche jaati hai aur sawal akela khada rehta hai. Yahi cold open ka naam/faisla wala
lamha hai: "kis taaqat ne ek bade, phaile hue dharm ko bina yuddh ke andar ghula diya?"

## Cue table (anchors phrase-locked)

| id | cue (script ki line) | sound | lands on the phrase | level | pan | fades |
|---|---|---|---|---|---|---|
| car | "Ek kamra hai. Paris ka." / neeche sadak se gaadi | ENGINE | `पेरिस का` | −24 dB | +0.55 (dayen = door) | in 0.5 s, out 1.0 s, 2.6 s |
| chair | "Ek aadmi Nehru ke saamne baithta hai." | WICKER | `सामने बैठता है` | −22 dB | −0.30 | 1.3 s, in 0.02 s, out 0.3 s |
| sword | "Talwarein." | STAB | `तलवारें` | **−16 dB** (scene ka ek hi ooncha cue) | −0.12 | 1.0 s, in 0.005 s, out 0.45 s |
| burn_city | "Jalte shehar." | CROWD | `जलते शहर` | −21 dB | +0.45 | 3.4 s, in 0.4 s, out 1.1 s |
| blood_river | "Khoon ki nadiyan." | RIVER (`synth:river_wash`) | `खून की नदियां` | −24 dB | +0.30 | 5 s, in 1.0 s, out 1.2 s |
| pen | "…ek qaidi apni kitaab mein utaar raha hai" | PEN | `उतार रहा है` | −22 dB | −0.20 | 2 s, in 0.05 s, out 0.5 s |
| steps | "To aaj hum us sawal ke peeche chalenge." | STEPS | `हम उस सवाल के पीछे` | −24 dB | −0.30 | 2.2 s, out 0.6 s |
| door | "Paanch darwaze aaj khulenge." | LATCH | `पांच दरवाजे आज खुलेंगे` | −21 dB | −0.35 | 1.4 s, out 0.4 s |

Aath spot cues — sab aapni line se hi paida hote hain, aur ek bhi cue paragraph ki seema nahi
todta. Har anchor cold open mein **sirf ek baar** aata hai (check kiya gaya, fuzzy matcher se
bhi), isliye `"occurrence": 1` kaafi hai.

## Kahan chup rehna hai

- **p05 — "Bilkul shuru mein. Namaskar se pehle. Chai se pehle."** Koi cue nahi: na cup, na
  chai ka pour, na swagat ka koi sound. ROOM aur RAIN dono −8/−10 dB par chale jaate hain.
  Mazaaq yahi hai — sawal chai se bhi pehle aata hai, to chai ki awaaz bhi nahi honi chahiye.
- **p06 — "Sawal ye hai."** Nangi line; koi cue nahi. Bed apni aawaaz par laut aate hain.
- **p10 — "Aur yahan? Yahan koi badi jang nahi hui."** Jang ka block khatam, phir kuch bhi nahi.
  STAB bas 1.5 s pehle baj chuka hai — duniya ke jangon ka jawab yahan sannata hai (beds −9/−11).
- **p13 ke ant se p14 tak** — RAIN "ek saath band", ROOM chala jaata hai, aur DRONE 1944 par hi
  shuru hota hai: do hisson ke beech ek chhota, khaali pul.
- **p17–p19 (ident + dono sawal)** — poora dry: ek bhi bed ya score nahi. Tanpura `नमस्कार` se
  pehle nikal jaata hai, isliye Asha ki aawaaz aur dono sawal poori tarah saaf sunayi dete hain.
- `dead_air.before_body_seconds` = **1.3 s** — ident ke baad, body ke pehle shabd se pehle.

## Script ke `[SFX: …]` cues ka hisaab

| script ki SFX line | plan mein kahan |
|---|---|
| "kheeki ke sheeshay par barsaat ki thaap; kamre ka sannata; neeche sadak se kisi gaadi ka door ka shor" | RAIN bed + ROOM bed + ENGINE cue (`car`) |
| "barsaat dheemi hoti hai; phir ek saath band" | RAIN ke points: 70.8 s se −1 dB, 74.0 s par −4 dB, 75.2 s par band |
| "tanpura ka ek lamba, dheema sur, 'darwaze' par shuru" | score `छह दरवाजे हैं` se 0.8 s pehle (`darwaze` wala beat) |
| "tanpura dheere-dheere ghulta hai; ident se pehle sannata" | score `नमस्कार` se 0.25 s pehle out + `dead_air` 1.3 s |

**Dhyan dijiye:** aakhri line ka pehla hissa (tanpura ka ghulna) house rule ki wajah se ident se
*pehle* shift ho gaya hai — score intro se 0.25 s pehle nikal jaata hai, isliye ident aur dono
sawal dry hain. "Ident se pehle sannata" wala hissa waisa hi hai (`dead_air` 1.3 s).

## Sound list (exact paths)

- Beds: `ep01/sfx/raw_fs/b1_bed.mp3` · `synth:rain` · `ep02/sfx/raw_fs/drone.mp3`
- Score: `ep03/sfx/raw_fs/tanpura.mp3`
- Foley/spot: `ep02/sfx/raw_fs/engine.mp3` · `ep02/sfx/raw_fs/wicker.mp3` ·
  `ep01/sfx/raw_fs/s3_stab.mp3` · `ep03/sfx/raw_fs/crowd.mp3` · `synth:river_wash` ·
  `ep01/sfx/raw_fs/s8b_pen.mp3` · `ep03/sfx/raw_fs/steps.mp3` · `ep01/sfx/raw_fs/s6_latch.mp3`

## Kya sunayi dega

Pehle ek kamre ka sannata — kheeki par barsaat ki thaap, aur neeche sadak se kisi gaadi ka door ka shor.
Us kamre mein do kursiyan, ek halki chare-mar, aur phir sawal — jiske saamne poori duniya neeche chali jaati hai.
Ek line par talwaren, jalte shehar aur khoon ki nadiyan: duniya ne dharm badalne ke liye kya-kya kiya. Aur uske turant baad sirf sannata — "aur yahan?"
Phir 1944, Ahmadnagar ki kothri: ek dheema, gehri sura, aur kisi ke qalam ki kharach — Jaise ek qaidi apna hi sawal likh raha ho.
Aakhir mein paanch darwaze khulte hain, tanpura ek baar chadhta hai; Asha ke "namaskar" se thoda pehle sab chup ho jaata hai, aur body se pehle 1.3 second ka poora sannata.
