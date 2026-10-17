# Ep 5.3 — SFX plan (cold open)

Cold open = `## Cold open` se host ident tak — 1789 ka chhapa-khana, samundar par jaati kitaab,
Goethe ka kamra, aur Europe ka purana sawal (327 narration shabd, chunk `c01`).

House convention wahi hai: **effects, ambience aur score sirf cold open par; baaki episode saaf
narration.** Narration anchor hai, har bed uske neeche baithta hai, host intro sookha rehta hai,
aur aakhri bed ke baad body se pehle sannate ka pocket.

**Anchor note (zaroori).** `ep05_3/c01.txt` abhi bana nahi hai, isliye yahan ke Devanagari
phrases maine khud script ke Roman cold open se translit kiye hain (spelling ep04_1/c01.txt jaisi:
`है।`, `पढ़े-लिखे`, `नमस्कार,`). Har phrase 2–6 shabd ka hai aur mixer ke `norm()` + 0.7 similarity
niyam se poore cold open mein **ek hi baar** aata hai — ek apwaad `शकुंतला` hai: wo do baar aata
hai (ident mein "शकुंतला का सफर"), isliye us cue par `occurrence: 1` hai; wo akela shabd ka
anchor hai kyunki uske aas-paas ke shabd `है।` / `नाम।` jaise punctuation ke saath aate hain, aur
5 akshar ka skeleton punctuation ke saath bhi match kar jaata hai. Har anchor ke saath `fallback_at`
(second) diya hai; wo ~2.3 shabd/second ke hisaab se nikala gaya hai (Ep 4.1 ki asli take se calibrate kiya),
isliye alignment na mile to bhi cue jagah par baithega — par asli mix `align.json` se hi hona chahiye.

## Cast (source files)
| id | file | what it is |
|---|---|---|
| ROOM | `ep01/sfx/raw_fs/b1_bed.mp3` | room tone — chhapa-khane ka kamra (bed) |
| SEA | `synth:river_wash` | gehri samundar ki dhulai (jahaz ka safar) |
| WIND | `ep03/sfx/raw_fs/wind.mp3` | Germany ke bahar ki sard, khadakti hawa (bed) |
| DRONE | `ep02/sfx/raw_fs/drone.mp3` | neeche ka sust tone — hulchul se sawal tak (bed) |
| TANPURA | `ep03/sfx/raw_fs/tanpura.mp3` | score — ek hi swell |
| THUD | `synth:brick_thud` | chhapa-khane ka dabaav (press ka thap) |
| INK | `ep01/sfx/raw_fs/s9_writing.mp3` | kagaz par syaahi |
| SARANGI | `ep03/sfx/raw_fs/sarangi.mp3` | do naam ke do jhuke hue sur |
| WICKER | `ep02/sfx/raw_fs/wicker.mp3` | jahaz ki rassi/lakdi ki chir |
| GUST | `synth:gust` | khidki ke bahar ek jhonka |
| PAPER | `ep01/sfx/raw_fs/s8_paper.mp3` | panne, aur chhap ke pule |
| LOWTONE | `synth:low_tone` | "wo ruk jaata hai" ka neeche wala tone |
| CELLO | `ep02/sfx/raw_fs/cello.mp3` | "baat samajh aa gayi" ka ek sur |
| CROWD | `ep03/sfx/raw_fs/crowd.mp3` | Europe ki hulchul (bheed ki awaaz, shabd samajh nahi aate) |

Synthesised cues (`synth:…`) mix script se generate hote hain; baaki saare files repo ke pool se hain.
Kuch bhi download nahi kiya gaya.

## Cue table (anchor phrases Devanagari mein; second sirf andaaza hain — asli mix `c01.align.json` se)
| # | cue | sound | lands on the phrase | level | pan | fades |
|---|---|---|---|---|---|---|
| 1 `press1` | chhapa-khane ka pehla dabaav | `synth:brick_thud` | `शहर में एक छापाखाना` (~4.2 s) | -16 dB | -0.15 | 0.005 in / 0.25 out |
| 2 `press2` | doosra dabaav | `synth:brick_thud` | `किताब छप रही` (~6.7 s) | -18 dB | -0.10 | 0.005 in / 0.25 out |
| 3 `ink` | kagaz par syaahi | `ep01/sfx/raw_fs/s9_writing.mp3` | `पहले पन्ने पर एक नाम` (~9.6 s) | -24 dB | -0.35 | 0.03 in / 0.4 out |
| 4 `name1` | pehla naam: Shakuntala | `ep03/sfx/raw_fs/sarangi.mp3` | `शकुंतला` (~11.8 s) | -23 dB | 0.0 | 0.35 in / 1.4 out |
| 5 `name2` | doosra naam: Kalidasa | `ep03/sfx/raw_fs/sarangi.mp3` | `नाम कालिदास` (~15.5 s) | -24 dB | +0.15 | 0.3 in / 1.2 out |
| 6 `rope` | jahaz ki rassi ki chir | `ep02/sfx/raw_fs/wicker.mp3` | `किताब एक जहाज पर` (~18.5 s) | -23 dB | +0.40 | 0.15 in / 0.8 out |
| 7 `gust` | bahar ka jhonka | `synth:gust` | `बाहर सर्द हवा` (~33.2 s) | -24 dB | +0.50 | 0.8 in / 1.5 out |
| 8 `page` | panne palatna | `ep01/sfx/raw_fs/s8_paper.mp3` | `पन्ने पलटे जाते` (~43.5 s) | -22 dB | -0.30 | 0.02 in / 0.3 out |
| 9 `stop` | wo ruk jaata hai | `synth:low_tone` | `और फिर वो रुक जाता` (~46.7 s) | -21 dB | 0.0 | 0.06 in / 1.2 out |
| 10 `idea` | baat samajh aa gayi | `ep02/sfx/raw_fs/cello.mp3` | `एक बात समझ आ गई` (~59.6 s) | -24 dB | -0.10 | 0.5 in / 1.4 out |
| 11 `hulchul` | Europe ki hulchul | `ep03/sfx/raw_fs/crowd.mp3` | `हलचल मच` (~84.5 s) | -22 dB | +0.45 | 0.5 in / 1.2 out |
| 12 `editions` | chhap ke pule | `ep01/sfx/raw_fs/s8_paper.mp3` | `छापे कई बार निकले` (~86.8 s) | -23 dB | -0.25 | 0.05 in / 0.5 out |

**Beds** (sab 0.0 pan, sab narration ke neeche)
| id | sound | kab se kab tak | level |
|---|---|---|---|
| `room` | `ep01/sfx/raw_fs/b1_bed.mp3` | shuru (0 s) → `वही किताब एक जहाज` +2.0 s (~21.3 s), 1.6 s fade in | -25 dB |
| `sea` | `synth:river_wash` | `वही किताब एक जहाज` (~19.3 s) → `छोटा कमरा` +0.8 s (~28.3 s) | -26 dB |
| `wind` | `ep03/sfx/raw_fs/wind.mp3` | `छोटा कमरा` (~27.5 s) → `महसूस नहीं होती` +0.4 s (~57.9 s) | -24 dB |
| `drone` | `ep02/sfx/raw_fs/drone.mp3` | `लोगों में एक हलचल` (~84.2 s) → `पुराने नाटक की नकल` +0.6 s (~116.1 s) | -25 dB |

## Score — ek hi swell
Sirf **ek** entry: `tanpura` (`ep03/sfx/raw_fs/tanpura.mp3`, filter `highpass=70,lowpass=6000`)
- **Chadhta hai:** `आज का सवाल यही` (~117.9 s) — yani aaj-ka-sawal wali line par, do sawalon ke
  theek pehle, 1.8 s ka fade in (host ke namaskar se kareeb 14.4 s pehle).
- **Rehta hai:** dono sawalon ke neeche, -24 dB par (voice ke neeche, kabhi oopar nahi).
- **Nikalta hai:** `नमस्कार` par `end_offset: -0.25` — yani host intro ki pehli awaaz se 0.25 s pehle
  poora out (~132.3 s). **Host intro sookha hai.**
- Yehi poore cold open ka ekmaatra swell hai; drone bed ke swar nahi uthte (wo flat rehta hai), taaki
  sirf tanpura hi "chadhta" lage.

## Kahan chup rehna hai
- **Shuruaat:** pehli line — "साल सत्रह सौ नवासी है…" — bina kisi spot cue ke chalti hai; pehle ~3.5 s
  par sirf `room` bed hai. Pehla dabaav tab aata hai jab "छापाखाना" bola jaata hai.
- **Jaise hi sona khatam:** `वही किताब एक जहाज` par room tone fade hone lagta hai aur ~21.3 s par
  poora out (19.3–28.3 s samundar ka bed; wind 27.5 s par shuru hota hai, isliye 0.8 s ka crossfade).
  In dono ke beech koi spot cue na daalein.
- **Parda/Faust wala poora paragraph** (— "इस नाटक के शुरू में एक पर्दा उठता है… जैसे इस नाटक में था।")
  **jaan-boojh kar khaali hai.** Wind bed wahin khatam ho gaya, koi spot cue nahi — sirf awaaz aur
  `room`-less khamoshi. Yahi cold open ka sabse khaamosh hissa hai.
- **Europe ka purana sawal** — `पुराने नाटक की नकल` (~115.5 s) par drone bhi nikal jaata hai; agla 2.4
  second sirf awaaz, phir tanpura chadhta hai.
- **Ident ke baad:** `dead_air.before_body_seconds = 1.4` — ident ke aakhri shabd ke baad poora sannata,
  phir "Ab tak" ka pehla shabd (script ki `[SFX: tanpura ghulta hai; sannata]` line).

## Sound list (exact paths / recipes)
Beds: `ep01/sfx/raw_fs/b1_bed.mp3` · `ep03/sfx/raw_fs/wind.mp3` · `ep02/sfx/raw_fs/drone.mp3` ·
`synth:river_wash`
Score: `ep03/sfx/raw_fs/tanpura.mp3`
Cues: `synth:brick_thud` · `ep01/sfx/raw_fs/s9_writing.mp3` · `ep03/sfx/raw_fs/sarangi.mp3` ·
`ep02/sfx/raw_fs/wicker.mp3` · `synth:gust` · `ep01/sfx/raw_fs/s8_paper.mp3` · `synth:low_tone` ·
`ep02/sfx/raw_fs/cello.mp3` · `ep03/sfx/raw_fs/crowd.mp3`

## Kya sunayi dega
Chhapa-khane mein pehle do bhaari dabaav, phir kagaz par syaahi ki lakeer. Jaise hi "शकुंतला" bola
jaata hai, saara mahaul dab jaata hai aur ek sarangi ka jhuka hua sur naam ko akela kar deta hai.
Uske baad samundar, aur ek lakdi ki chir — kitaab jahaz par hai. Germany ke chhote kamre mein bahar
sard hawa chalti hai, panne palatte hain, aur phir sab ruk jaata hai: ek neeche wala tone, ek cello
ka sur. Europe ki bheed mein hulchul machti hai, kagaz ke pule nikalte hain. Phir ek lambi khamoshi,
aur "आज का सवाल यही है" par tanpura chadhta hai — jo host ke namaskar se theek pehle chup ho jaata
hai. Namaskar ke baad 1.4 second poora sannata.

## Rules jo nibhaye gaye
- Sab cues anchor-locked hain (2–6 Devanagari shabd, cold open mein ek hi baar — apwaad `शकुंतला`),
  aur har cue ke saath `fallback_at` hai.
- Levels: beds -24…-26 dB, spot cues -18…-24 dB, score -24 dB — sirf chhapa-khane ke pehle dabaav
  (`press1`) ko -16 dB ki chhoot hai (scene ka sabse loud block). -16 dB se oopar kuch nahi.
- Voice hamesha centre; foley thoda baayen (-0.1…-0.35), door/chaudi cheezein daayen (+0.4…+0.5);
  beds aur score 0.0 par.
- Ek hi score swell, aur wo host intro se 0.25 s pehle out. Koi cue intro ko cross nahi karta.
- Ek hi duck: naam ke lamhe par (`शकुंतला`), pre 1.5 s, post 2.5 s, gain 0.3.
- **Script ki do inline SFX lines** (`[SFX: chhapai; kagaz par syaahi]` aur `[SFX: samundar; jahaz ki
  rassi]`) poore cover hain. Teesri `[SFX: tanpura ka dheema sur]` + chauthi `[SFX: tanpura ghulta
  hai; sannata]` — dono ek hi swell ban jaati hain: tanpura `आज का सवाल यही` par chadhta hai aur
  `नमस्कार` se 0.25 s pehle out hota hai, kyunki house rule kehta hai host intro sookha rehta hai;
  "sannata" ident ke baad ka 1.4 s dead air hai.
- Body saaf rehta hai — cold open ke baad koi SFX nahi.
