# Ep 4.3 — SFX plan (cold open)

Cold open = `## Cold open` se "Namaskar, main hoon Asha…" ke aakhri line tak — **412 narration shabd**,
chunk `c01`. Signal chain aur levels wahi hain jo Ep 4.1 / 3 / 5 / 6 mein hain: narration anchor hai,
har bed uske neeche baithta hai, host intro sookha (dry) hai, aur kothri ka bed intro se 0.25 s pehle
kat jaata hai.

Anchors **phrase-locked** hain — `phrase` hamesha Devanagari hai aur cold open ke ek hi jagah aata hai
(`occurrence: 1`). JSON ke `fallback_at` seconds sirf safety net hain (alignment na mile to mixer wahin
bajata hai), isliye take dobara banne par bhi har cue apni jagah par laut aata hai.

Cold open ka dhaancha do hisson mein hai: **jashn** (dhol, diye, jhande, chowk ki bheed) aur **qila**
(Ahmadnagar, kothri, mez par akhbaar, ek sawal). Beech mein dhol ek jhatke mein kat jaate hain — wahi
scene ka sabse bada mod hai.

## Cast (source files)

| id | file | kaam |
|---|---|---|
| BHEED | `ep03/sfx/raw_fs/crowd.mp3` | jashn wali bheed ka halka shor (bed) |
| VILLAGE | `ep03/sfx/raw_fs/b1_village.mp3` | shehron ki aam hawa / room tone (bed) |
| KOTHRI | `ep01/sfx/raw_fs/b1_bed.mp3` | qile ki kothri ka room tone (bed) |
| SHRUTI | `ep03/sfx/raw_fs/shruti.mp3` | score — shruti-box drone (ek hi entry, ek hi swell) |
| SHEHNAI | `ep02/sfx/raw_fs/cello.mp3` | door ki sooti lehar — shehnai ki jagah (repo mein shehnai nahi hai) |
| TANPURA | `ep03/sfx/raw_fs/tanpura.mp3` | naye hazaar saal par ek chheda hua taar |
| SARANGI | `ep03/sfx/raw_fs/sarangi.mp3` | ek sooti phrase — naam ka lamha |
| CROW | `ep01/sfx/raw_fs/s5_crow.mp3` | sannate mein door ek akela kauva |
| PAPER | `ep01/sfx/raw_fs/s8_paper.mp3` | akhbaar ka panna, aur panna modna |
| WICKER | `ep02/sfx/raw_fs/wicker.mp3` | purani jildon / almari ki halki cheenk |
| synth | mix script | `brick_thud` (dhol/nagaade), `gust` (kahaniyon ka phailav) |

Kuch bhi download nahi kiya gaya — sab repo pool se hai. Do jagah pool ki khaas shaklein hain, aur wo
plan mein saaf likhi hain: **dhol/nagaade** ke liye `synth:brick_thud` (105 Hz body + click — dhol ki
tarah), aur **shehnai ki lehar** ke liye `ep02/.../cello.mp3` (repo mein koi shehnai/reed nahi hai;
door se aati sooti lehar ka kaam chalti hai).

## Cue table

| # | cue (line) | sound | lands on the phrase (Devanagari) | level | pan | fades |
|---|---|---|---|---|---|---|
| A1 | "Sochiye, April 1944." … "…us ek naam ko dhoondhta hai." | BHEED (bed) | `0.0` se `उस एक नाम को` +1.4 s tak | -25 dB | centre | 2.5 s fade in; sannate par jhatka cut |
| A2 | wahi jashn wala hissa | VILLAGE (bed) | `0.0` se `उस एक नाम को` +1.4 s tak | -26 dB | centre | 2.5 s fade in; jhatka cut |
| B1 | "Desh ke kai shehron mein dhol baj rahe hain." | DHOL = `synth:brick_thud` | `शहरों में ढोल बज` (-0.15 s) | -16 dB | L 0.25 | 5 ms in, 0.25 s out |
| B2 | "Galiyon mein jhande hain…" | DHOL2 = `synth:brick_thud` | `गलियों में झंडे` | -18 dB | L 0.12 | 5 ms in, 0.25 s out |
| B3 | "…aur chowk par log jama hain." | NAGAADA = `synth:brick_thud` | `और चौक पर लोग` | -20 dB | L 0.18 | 5 ms in, 0.25 s out |
| C1 | "Kis baat ka jashn hai?" | SHEHNAI = `ep02/…/cello.mp3` (5 s) | `किस बात का जश्न` (-1.0 s) | -23 dB | R 0.35 | 1.5 s in, 2.0 s out |
| D1 | "Ek naya hazaar saal shuru ho raha hai." | TANPURA = `ep03/…/tanpura.mp3` (3.5 s) | `एक नया हजार साल` | -25 dB | centre | 0.5 s in, 1.5 s out |
| E1 | "…ek hi naam. Vikram. Ya poora naam, Vikramaditya…" | SARANGI = `ep03/…/sarangi.mp3` (4.2 s) | `सालों पर एक ही नाम` (-1.9 s) | -23 dB | centre | 0.4 s in, 1.6 s out → naam akela (duck) |
| F1 | "…Asia ke kai deshon tak gayi. Aur baad mein Europe tak." | PHAILAV = `synth:gust` (5 s) | `एशिया के कई देशों तक` (-0.6 s) | -24 dB | R 0.45 | 1.2 s in, 2.5 s out |
| F2 | "…us ek naam ko dhoondhta hai." → sannata → "door kahin ek akela kauva" | CROW = `ep01/…/s5_crow.mp3` | `उस एक नाम को` (+1.6 s) | -24 dB | R 0.50 | 0.02 s in, 0.18 s out |
| G1 | "Ab Ahmadnagar ka qila." se intro tak | KOTHRI (bed) | `अब अहमदनगर` (+0.2 s) se `नमस्कार` -0.25 s tak | -26 dB | centre | 2.5 s fade in; intro par hard out |
| G2 | "…kalpana kijiye, ek akhbaar." | AKHBAAR = `ep01/…/s8_paper.mp3` (1.8 s) | `कल्पना कीजिए एक अखबार` (+0.2 s) | -21 dB | L 0.10 | 0.05 s in, 0.3 s out |
| H1 | "Par wo panna mod kar rakh dete hain." | PANNA = `ep01/…/s8_paper.mp3` (1.4 s) | `पन्ना मोड़ कर रख देते` (-0.2 s) | -22 dB | L 0.25 | 0.03 s in, 0.25 s out |
| H2 | "Wo kitaabein palatte hain. Purane grant. Purani soochiyan." | JILD = `ep02/…/wicker.mp3` (2 s) | `वो किताबें पलटते` (+0.15 s) | -24 dB | L 0.35 | 0.08 s in, 0.4 s out |
| Z1 | "Namaskar, main hoon Asha…" (host intro) | — | `नमस्कार` -0.25 s par sab beds out | — | — | hard out; intro dry |

**11 spot cues** (B1–B3, C1, D1, E1, F1–F2, G2, H1, H2) — brief ki ~12 ki seema ke andar, aur har cue
apni line se hi motivated hai. Scene ka sabse ooncha cue B1 dhol hai (-16 dB, brief ki ek-cue chhoot);
baaki sab -18 dB ya uske neeche.

## Score (ek hi entry, ek hi swell)

SHRUTI (`ep03/sfx/raw_fs/shruti.mp3`) — ek hi baar uthta hai, **`और एक सवाल उनके मन में`** par
(≈ 108 s), thoda halka rehta hai, aur **`ये विक्रम थे कौन?` / `और थे कब?`** wale hook par apna
ek hi swell leta hai (nominal -25 dB se +2.5 dB, yaani kareeb -22.5 dB — "Vikram the kaun?" ke neeche
bas ek poora saans). Uske baad wo niche utarta hai aur **30 s par poori tarah chup** ho jaata hai;
layer `नमस्कार` -0.25 s par band ho jaati hai, yaani score host intro se pehle out hai
(audibly ~1.5 s pehle hi chup ho chuka hota hai). Swell sirf ek hai — cue table ka gust foley hai,
score ka swell nahi.

## Kahan chup rehna hai

1. **Dhol ka jhatka.** "…us ek naam ko dhoondhta hai." ke aakhir par dhol, bheed aur sheher — teeno
   ek jhatke mein kat jaate hain (beds `उस एक नाम को` +1.4 s par out). Uske 0.2 s baad **ek akela
   kauva** (F2, +1.6 s) bolta hai, phir "Ab Ahmadnagar ka qila." — KOTHRI room tone `अब अहमदनगर` +0.2 s
   par hi shuru hota hai, yaani sannate ke baad.
2. **"Ek calendar ka. Vikram Samvat ka."** — is jawab par koi naya cue nahi; sirf C1 shehnai ki lehar
   apna tail chhodti hai.
3. **"Iska hisaab suraj se chalta hai. Par iske mahine chaand ke hain."** — poora dry; ginti ka hisaab
   shabdon mein hi sunna hai.
4. **"Ye naam har ghar mein jaana-pehchana hai… Anginat kahaniyan is ek naam se chipki hain."** —
   sarangi E1 ke baad, agle naam (F1) tak koi cue nahi.
5. **Hook ke do sawal ("Ye Vikram the kaun? Aur the kab?") aur "Is sawal ka jawab hum aaj ke aakhir mein
   sunenge… pada rahega."** — koi spot cue nahi; sirf score ka drone. Aakhri line ke baad
   **poora sannata** (script ka `[SFX: ident se pehle ek pal ka poora sannata]`), phir dry intro.
6. Cold open ke baad body tak: `dead_air.before_body_seconds` = **1.3 s** — "Aaj ka har kissa ek suraag
   hai…" ke baad 1.3 s ki khoobsoorat khaamoshi, phir "Ab tak".

## Sound list (exact paths)

- Beds: `ep03/sfx/raw_fs/crowd.mp3`, `ep03/sfx/raw_fs/b1_village.mp3`, `ep01/sfx/raw_fs/b1_bed.mp3`
- Score: `ep03/sfx/raw_fs/shruti.mp3`
- Cues (files): `ep02/sfx/raw_fs/cello.mp3`, `ep03/sfx/raw_fs/tanpura.mp3`,
  `ep03/sfx/raw_fs/sarangi.mp3`, `ep01/sfx/raw_fs/s5_crow.mp3`, `ep01/sfx/raw_fs/s8_paper.mp3`,
  `ep02/sfx/raw_fs/wicker.mp3`
- Cues (synth recipes): `synth:brick_thud` (dhol + nagaada, teen jhatke),
  `synth:gust` (kahaniyon ka phailav)
- Filters: hard-high-pass har bed par (bheed `highpass=140,lowpass=6500`, village
  `highpass=90,lowpass=7000`, kothri `highpass=50,lowpass=4000`, shruti `highpass=60,lowpass=5500`),
  taaki narration ki jagah khali rahe.

## Kya sunayi dega

Shuruaat mein gali-gali dhol, halka bheed ka shor, aur door se ek sooti lehar — poora jashn.
"Kis baat ka jashn hai?" par wahi lehar door se guzarti hai; naye hazaar saal par tanpura ek taar chhedta hai.
"Do hazaar saal… ek hi naam" par sarangi bolti hai aur baaki sab dab jaata hai — sirf naam bachta hai.
Kahaniyan Asia tak jaati hain to daayen se ek hawa ka jhonka guzarta hai; phir dhol ek jhatke mein kat jaate hain, aur sannate mein door koi akela kauva bolta hai.
Qile ki kothri mein sookhi sarsaraahat — akhbaar, panna modna, purani jildon ki cheenk.
Aakhir mein shruti ka drone dheere se uthta hai, "Vikram the kaun?" par apni ek saans leta hai, aur "Namaskar" se pehle poora chup ho jaata hai.

## Rules jo nibhaye gaye

- Anchors phrase-locked aur Devanagari; har phrase cold open mein **ek hi baar** aata hai
  (`occurrence: 1`), aur `fallback_at` safety net ke liye diya gaya hai.
- Levels: beds -25…-26 dB, score -25 dB (swell par -22.5 dB), foley -18…-24 dB, ek hi cue -16 dB
  (B1 dhol — scene ka loudest block). Kuch bhi -16 dB se oopar nahi.
- Voice centre; foley left (-0.35…-0.10), door/distance wali cheezein right (0.35…0.50), beds aur score
  `0.0`.
- Ek hi swell (score ki ek hi entry); ek hi duck — naam par.
- Koi cue host intro ko cross nahi karta; beds `नमस्कार` -0.25 s par out, score usse pehle chup.
- JSON ke `points` ki seconds estimates hain (take ki word timings aane par dobara spot karni hain);
  beds ke envelopes sirf fade-in ke hain, isliye unka ant phrase se hi tay hota hai.
