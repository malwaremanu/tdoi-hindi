# Ep 6.4 — SFX plan (cold open)

Cold open = script ka `## Cold open` se `## Ab tak` ke pehle tak — **335 narration shabd**
(chunk `c01`, kareeb 2:04). House rule wahi hai: **SFX, ambience aur score sirf cold open
par; ident ke baad poora episode saaf narration.**

Purane `scripts/Ep 6 — SFX plan.md` ke cue naam (B1, B2, S1–S5, M1) yahan naye dhaanche mein
dobara lagaye gaye hain — wahi kaam, naye id, nayi timeline (6.4 ka cold open 6 ka purana
cold open hai, naye shabdon mein). Sab kuch **phrases** par tika hai: cue ka `phrase` cold
open ke asli shabdon ka ek tukda hai (Devanagari), aur mixer `tools/audio/mix_from_plan.py`
align se uska asli waqt nikalta hai. Har cue ke saath `fallback_at` bhi hai — align na mile
to wahi sambhalta hai.

Neeche diye seconds 160 shabd/prati-minute ke andaaze par hain (cold open ≈ 2:04); asli take
par align inhe khud re-time karega, isliye sab kuch phrase-locked rakha gaya hai.

Level convention (jaise Ep 4.1): narration hi anchor hai; ambience beds −21…−27 dB,
foley/spot −18…−24 dB, score −22…−26 dB. Is scene ka ek hi ooncha cue hai (kitaab ki thap,
−16 dB) — uska oopar kuchh nahi.

## Cast (source files)

| id | file | kya hai |
|---|---|---|
| B1 `hall` | `ep01/sfx/raw_fs/b1_bed.mp3` | Fatehpur Sikri ke daalan ki garam, shaant hawa — koi chidiya nahi (bed) |
| B2 `darbar` | `ep03/sfx/raw_fs/crowd.mp3` | door ka darbar — dhundhli gunjan, koi samajh aane wala shabd nahi (bed) |
| S1 `qadam` | `ep03/sfx/raw_fs/steps.mp3` | patthar par do-teen halke qadam (kale chogon wale andar aate hain) |
| S2–S4 `tohfa`/`panna1`/`panna2` | `ep01/sfx/raw_fs/s8_paper.mp3` | lipti kitaab ka haath badalna, phir do bhaari panne palatna |
| S5 `thap` | `ep05/sfx/raw_fs/cup.mp3` + `ep01/sfx/raw_fs/s8_paper.mp3` | bhaari, dhimmi thap — kitaab ek taraf rakh di jaati hai (thap + kagaz ki ek patli chit) |
| naya `hawa` | `synth:gust` | sookhi hawa — sawal jis hawa mein latak gaya |
| naya `kothri` | `ep01/sfx/raw_fs/s6_latch.mp3` | door ki jail — ek sookha latch, bahut door |
| M1 `tanpura` | `ep03/sfx/raw_fs/tanpura.mp3` | ek hi score, ek hi swell |

Synthesised cue (`synth:gust`) plan mein `synth:` naam se hai; mix script use khud banata hai.
Koi naya download nahi — sab repo ke pool se.

## Cue table

Anchors Devanagari phrase hain (mixer ke liye), aur Roman line sirf padhne ke liye. Times
fallback hain (align inhe khiska dega).

| # | script cue | id | cue | sound | lands on (phrase — Roman line) | level | pan | fades |
|---|---|---|---|---|---|---|---|---|
| 1 | B1 | `hall` | daalan ki garam, shaant hawa (bed) | `ep01/sfx/raw_fs/b1_bed.mp3` | pehle shabd se: "Dopahar hai. Fatehpur Sikri." | −25 dB | 0.0 | in 2.5 s; out "darbar agle kaam par chala jaata hai" (~79.4 s) |
| 2 | B2 / B2-hush | `darbar` | door ka darbar (bed) | `ep03/sfx/raw_fs/crowd.mp3` | "दरबार भरा" — "Darbar bhara hai." (~12.0 s) | −27 dB | 0.0 | in 3 s; hush (−3 dB) "अकबर अपने ज़माने" se pehle (~44 s); out "ये बनी कैसे" se 1.6 s pehle (~68.9 s) |
| 3 | S1 | `qadam` | patthar par halke qadam | `ep03/sfx/raw_fs/steps.mp3`, 1.6 s | "अजनबी काले चोगों में" — "…kuch ajnabi, kaale chogon mein…" | −20 dB | −0.25 | in 0.02 / out 0.30 |
| 4 | S2 | `tohfa` | kapde mein lipti kitaab haath badalti hai | `ep01/sfx/raw_fs/s8_paper.mp3`, 1.1 s | "लिपटी एक मोटी किताब" — "Kapde mein lipti ek moti kitaab." | −22 dB | −0.20 | in 0.02 / out 0.25 |
| 5 | S3 | `panna1` | pehla bhaari panne palatna | `ep01/sfx/raw_fs/s8_paper.mp3`, 0.6 s | "वो एक पन्ना" — "Wo ek panna palatte hain." | −20 dB | −0.15 | in 0.005 / out 0.15 |
| 6 | S4 | `panna2` | doosra panne palatna | `ep01/sfx/raw_fs/s8_paper.mp3`, 0.45 s | "फिर दूसरा" — "Phir doosra." | −21 dB | −0.10 | in 0.005 / out 0.12 |
| 7 | S5 | `thap` | kitaab ek taraf: bhaari, dhimmi thap | `ep05/sfx/raw_fs/cup.mp3` (lowpass 2 kHz), 0.5 s | "किताब एक तरफ़ रख" — "Kitaab ek taraf rakh di jaati hai." | **−16 dB** (scene ka sabse ooncha) | −0.10 | in 0.005 / out 0.30 |
| 8 | S5 (chit) | `thap_paper` | thap ke baad kagaz ki patli sarasarahat | `ep01/sfx/raw_fs/s8_paper.mp3`, 0.4 s (+0.30 s baad) | "किताब एक तरफ़ रख" (wahi lamha) | −24 dB | −0.20 | in 0.02 / out 0.15 |
| 9 | naya | `hawa` | sookhi hawa ka jhonka | `synth:gust`, 3.2 s | "हवा में लटक" — "Ek chhota sa sawal hawa mein latak reh jaata hai." | −24 dB | +0.40 | in 1.0 / out 1.2 |
| 10 | naya | `kothri` | door ka sookha latch | `ep01/sfx/raw_fs/s6_latch.mp3`, 0.8 s | "एक जेल की कोठरी" — "…ek jail ki kothri mein baithe Nehru…" | −24 dB | +0.45 | in 0.01 / out 0.30 |
| 11 | M1 | `tanpura` | score: tanpura (ek hi entry) | `ep03/sfx/raw_fs/tanpura.mp3` | "तीन सौ साल बाद" — "Teen sau saal baad…" (~81.4 s) | −25 dB → −22 dB (ek swell) | 0.0 | in 3.5 s; out ~95.9 s, "नमस्कार" se 0.25 s pehle |
| 12 | — | `sawal_duck` | duck — koi cue nahi (jaan-boojh kar) | — (beds par lagta hai) | "ये बनी कैसे" — "Ye bani kaise?" | beds/cues ×0.30, pre 1.2 s, post 2.2 s | — | — |
| 13 | — | ident | ident par sab out | — | "नमस्कार" | — | — | ident se aage kuchh nahi bajta |

**Kul 8 spot cue** (id 3–10). Baaki do rows bed, score, duck aur ident ke hai. Pan ka rule:
qadam/kagaz thoda baayein (−0.10…−0.25), door/khuli hawa wali cheezein daayein (+0.40, +0.45),
beds aur score centre par.

## Score (M1) — ek hi entry, ek hi swell

Ek hi instrument: tanpura, Pa–Sa–Sa–Sa loop, `ep03/sfx/raw_fs/tanpura.mp3` (high-pass 70 Hz,
low-pass 6 kHz). Koi melody nahi, koi dhoons nahi, koi reverb nahi, koi doosra instrument nahi.
Score sirf ek baar aata hai — Nehru ki jail wali line par — ek baar chadhta hai aur chala jaata hai.

| samay | M1 | kya hota hai |
|---|---|---|
| 80.0–81.4 s | −60 (chup) | darbar ka daalan chala gaya; "Teen sau saal baad" par kitabhi nahi bajta |
| 81.4–84.9 s | −60 → −25 | tanpura dheere se uthta hai: "ek jail ki kothri mein baithe Nehru…" |
| 84.9–89.6 s | −25 | thehra rehta hai — "theek isi pal par ruk jaate hain" |
| 89.6–91.9 s | −25 → **−22** | **yahi ek swell**: "jismein ek bada sawal chhupa hai" par chadhta hai |
| 91.9–93.8 s | −22 | swell thehrta hai — "Europe aage kaise nikal gaya" iske oopar |
| 93.8–95.9 s | −22 → −60 | neeche utarta hai, "aur Bharat peeche kyun reh gaya?" ke aakhir par khatam |
| 95.9 s ke baad | −60 | "नमस्कार" se 0.25 s pehle poori tarah chup — ident saaf |

Rules: swell sirf ek (89.6–91.9 s), score ka peak −22 dB (band −22…−26 se bahar nahi),
"ये बनी कैसे" par koi score nahi, aur ident ke baad (16–17 wale paragraph) bilkul kuchh nahi.

## Kahan chup rehna hai

1. **38.3–56.6 s, "ये छपी हुई है" se "sab behas karte hain" tak.** Chhape akshar aur Akbar
   ka chitra. Yahan ek bhi spot cue nahi: na panne, na qadam, na hawa. Sirf hushi hui darbar
   ki gunjan aur daalan ki hawa. Ye cold open ka sabse saaf hissa hai — narration hi sab kuch
   keh rahi hai.
2. **70.5–79.9 s, "ये bani kaise?" aur uske baad ka anuchhed.** Episode ka thesis sawal. Darbar
   pehle hi out, daalan ki hawa duck par 30% (≈ −35 dB) — aur agla cue "kothri" 80.98 s par.
   Beech mein koi sting, koi drone, koi whoosh nahi.
3. **56.6–60.8 s, "Akbar kitaab band karte hain. Shukriya kehte hain."** Kitaab band karna
   awaaz se nahi dikhaya jaata — kriya awaaz mein hai, illustration mein nahi.
4. **79.4 s se aage poora jail ka hissa.** Darbar ki hawa "darbar agle kaam par chala jaata hai"
   par khatam ho jaati hai; aage sirf tanpura, phir sannata. Do jagah ke beech koi cheez nahi.
5. **"नमस्कार" se pehle 0.25 s aur ident ke baad poora episode.** Ident clean studio mein
   aata hai, aur uske baad ("Aaj ka sawal yahi hai…", "Panipat ke maidan se…") ek bhi cue nahi —
   wo do paragraph saaf narration par chalte hain.
6. **Cold open ke aakhir par 1.3 s dead air** (aakhri shabd ke baad, `## Ab tak` se pehle).
   Ise bharna nahi hai.

## Sound list (exact paths)

| id | path | kya lena hai |
|---|---|---|
| `hall` | `ep01/sfx/raw_fs/b1_bed.mp3` (357 s) | static, garam hawa; koi chidiya/traffic nahi. filter `highpass=120,lowpass=9000` |
| `darbar` | `ep03/sfx/raw_fs/crowd.mp3` (176 s) | door ki bheed: dhundhli gunjan, koi samajh aane wala shabd nahi. filter `highpass=150,lowpass=5000` |
| `qadam` | `ep03/sfx/raw_fs/steps.mp3` (3.4 s) | do-teen halke qadam, pehle 1.6 s |
| `tohfa` | `ep01/sfx/raw_fs/s8_paper.mp3` (32.7 s) | kagaz/kapda ek baar, pehle 1.1 s |
| `panna1` | `ep01/sfx/raw_fs/s8_paper.mp3` | pehle 0.6 s — bhaari panne ka ek palatna |
| `panna2` | `ep01/sfx/raw_fs/s8_paper.mp3` | pehle 0.45 s — doosra palatna, thoda halka |
| `thap` | `ep05/sfx/raw_fs/cup.mp3` (5.1 s) | pehle 0.5 s, `lowpass=2000` — dhimmi thap, slam nahi |
| `thap_paper` | `ep01/sfx/raw_fs/s8_paper.mp3` | pehle 0.4 s — thap ke baad ek patli chit |
| `hawa` | `synth:gust` (`synth_seconds: 3.2`) | sookhi hawa; mix script khud banata hai |
| `kothri` | `ep01/sfx/raw_fs/s6_latch.mp3` (13.3 s) | pehle 0.8 s — ek sookha latch, bahut door |
| `tanpura` | `ep03/sfx/raw_fs/tanpura.mp3` (46.4 s) | Pa–Sa–Sa–Sa drone; loop ke liye kaafi lamba. filter `highpass=70,lowpass=6000` |

Sab files repo ke pool mein pehle se hain — koi download nahi.

## Kya sunayi dega

1. Shuru mein Fatehpur Sikri ke khaali daalan ki garam, shaant hawa — koi chidiya nahi; "darbar bhara hai" par door ki dhundhli gunjan jud jaati hai.
2. Kale chogon wale paadri andar aate hain: patthar par halke qadam, kapde mein lipti kitaab ka haath badalna, aur do bhaari panne palatne ki awaaz — bas itna hi.
3. Jab Akbar kitaab ek taraf rakh dete hain, ek bhaari dhimmi thap aati hai (scene ka sabse ooncha pal), uske baad kagaz ki ek patli chit; chhape akshar aur Akbar ke chitr par poori tarah chup.
4. "Ye bani kaise?" se pehle darbar chala jaata hai aur hawa dab jaati hai — sawal sirf ek sookhi hawa ke jhonke par poochha jaata hai, us hawa mein jo latak gaya.
5. Tees sau saal baad ek door ka sookha latch bajta hai, phir tanpura dheere se uthta hai, "jismein ek bada sawal chhupa hai" par ek baar chadhta hai.
6. "Aur Bharat peeche kyun reh gaya?" ke saath tanpura neeche utarta hai aur "namaskar" se pehle bilkul chup ho jaata hai — host ka swagat saaf studio mein, aur uske baad poore episode mein kuchh nahi bajta.
