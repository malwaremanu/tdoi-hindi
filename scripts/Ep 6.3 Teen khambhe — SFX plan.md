# Ep 6.3 — SFX plan (cold open)

Cold open = `## Cold open` se `## Ab tak` tak: **348 narration shabd** (heading aur `[SFX: ...]`
lines ke bina gina), chunk `c01`. Ise poora score kiya gaya hai; ident ke baad ka 1944 wala para
aur poora body ("Ab tak" se aage) **bilkul saaf** hai.

House convention wahi hai jo Ep 3 / Ep 4.1 / Ep 5 / Ep 6 mein thi: narration anchor hai, har bed
uske neeche, host intro dry, aur score ek hi baar uthta hai. Is episode mein ek hi phrase-marker
hai jise theek se lagaya ja sakta hai — **"Kis taaqat se?"** — aur uske turant baad ident aa jaata
hai, isliye score ki jagah chhoti hai (neeche "Score" dekhein).

**Anchors (zaroori):** har cue ka anchor Devanagari mein hai aur us cold open ke **lagataar shabd**
hain. Ye teen niyam se chune gaye (teens phraselist se verify kiye gaye):

1. Phrase cold open mein **ek hi baar** aata hai (`occurrence: 1`), aur `Ab tak` wale para mein
   bhi dobara nahi aata (mixer poore `c01.align.json` mein dhoondhta hai, sirf cold open mein nahi).
2. Phrase ka **aakhri shabd vaakya ke ant mein nahi hai** — mixer ka `norm()` "।" (U+0964) ko nahi
   hataata kyunki wo Devanagari range ke andar hai, isliye `है।` ka skeleton `ह।` ban jaata hai aur
   `है` se `difflib` ratio **0.67** aata hai — jo 0.7 ki degaari se kam hai, yaani phrase **match hi
   nahi hoti**. Har phrase ka aakhri shabd is plan mein vaakya ke beech ka hai (danda/question mark
   se pehle), aur ye baat `find_phrase()` se simulate kar ke check ki gayi.
3. Comma se koi farq nahi padta (comma strip ho jaata hai), aur **nukta se bhi farq nahi padta** —
   mixer ka `norm()` U+093C bhi hata deta hai, isliye `ताकत`/`ताक़त` aur `दरवाजा`/`दरवाज़ा` dono
   match hote hain. Chhote shabd par sirf danda/question mark hi khatarnak hai (rule 2), isliye
   phrases mein nukta ke bina likha gaya hai.

`fallback_at` / `end_fallback` ke seconds "andaaza" hain — model: **0.395 s prati shabd + 0.6 s
vaakya-viraam par**, jo Ep 6 ke `c01` (271 shabd / 110.3 s) aur Ep 4.2 ke `c01` (444 shabd /
182.6 s) par calibrate kiya gaya hai. Asli anchor **phrase** hai; seconds sirf `--no-align` ke liye
safety net hain (in dono ka farq is file mein 0.05 s se zyada nahi hai).

## Cast (source files)

| id | file | kya hai |
|---|---|---|
| WIND | `ep03/sfx/raw_fs/wind.mp3` | dhool bhari shaam ki hawa (godhuli ki sadak) — bed |
| VILLAGE | `ep03/sfx/raw_fs/b1_village.mp3` | gaon ke bahar ki raat: khet aur jhingur — bed |
| AANGAN | `ep01/sfx/raw_fs/b1_bed.mp3` | aangan/baithak ka room tone — bed |
| TANPURA | `ep03/sfx/raw_fs/tanpura.mp3` | ek lamba sur (score, ek hi swell) |
| CROW | `ep01/sfx/raw_fs/s5_crow.mp3` | ek door ka kauwa (kati fasal ke khaali khet) |
| STEPS | `ep03/sfx/raw_fs/steps.mp3` | dhool par kadam — utarna aur door jaati fauj |
| PAPER | `ep01/sfx/raw_fs/s8_paper.mp3` | kagaz aage badhana |
| LATCH | `ep01/sfx/raw_fs/s6_latch.mp3` | phaatak ki zanjeer (hilti hai, phir ruk jaati hai) |
| CROWD | `ep03/sfx/raw_fs/crowd.mp3` | door ki baithak ki dheemi awaaz — koi samajh aane wale shabd nahi |
| WICKER | `ep02/sfx/raw_fs/wicker.mp3` | charpai ki rassi ki chik-chik |
| synth | `tools/audio/mix_from_plan.py` ke andar | `sand_trickle`, `gust` |

Koi download nahi. Sab kuch repo ke pool se hai (licences settled). Ek bhi nayi file nahi maangi gayi.

## Cue table (9 spot cues)

| id | cue (kis line par) | sound | lands on the phrase (Devanagari) | level | pan | fades | fallback (s) |
|---|---|---|---|---|---|---|---|
| C1 | "Sadak par dhool uthi hui hai." — sadak se uthti bareek dhool | `synth:sand_trickle` (2.6 s) | सड़क पर धूल उठी | -22 | -0.35 | in 0.6 / out 0.8 | 4.9 |
| C2 | "Khet khaali pade hain." — fasal kat chuki, khaali khet | `s5_crow.mp3` (0.43 s) | खेत खाली पड़े | -24 | +0.5 | in 0.02 / out 0.15 | 13.1 |
| C3 | "Wo neeche utarta hai." — ghode se utar kar do kadam | `steps.mp3` (atrim 0.4–2.2) | वो नीचे उतरता | -22 | -0.3 | in 0.02 / out 0.3 | 48.0 |
| C4 | "Kagaz aage badhata hai." — mantri ki mohar wala kagaz | `s8_paper.mp3` (atrim 0.05–1.5) | कागज आगे बढ़ाता | -21 | -0.2 | in 0.05 / out 0.35 | 50.4 |
| C5 | "Phaatak ki zanjeer hilti hai — aur phir ruk jaati hai." | `s6_latch.mp3` (atrim 11.2–12.1) | फाटक की जंजीर हिलती | **-16** | 0.0 | in 0.005 / out 0.3 | 77.1 |
| C6 | "Bas hawa ki awaaz reh jaati hai." — zanjeer rukne ke baad | `synth:gust` (3.0 s) | हवा की आवाज रह जाती | -23 | +0.35 | in 0.2 / out 0.5 | 81.4 |
| C7 | "kuch log charpai par baithte hain" — baithak shuru | `crowd.mp3` (atrim 0.5–5.5) | कुछ लोग चारपाई पर बैठते | -25 | 0.3 | in 0.8 / out 1.5 | 95.2 |
| C8 | "Ek rassi halki si chik-chik karti hai." — charpai ki rassi | `wicker.mp3` (atrim 2.75–4.15) | एक रस्सी हल्की | -22 | -0.15 | in 0.02 / out 0.5 | 99.0 |
| C9 | "Ek fauj kahin aur ja rahi hai." — doosre gaon ki taraf | `steps.mp3` (atrim 1.4–3.4) | एक फौज कहीं और | -26 | +0.55 | in 0.5 / out 0.9 | 115.4 |

Levels: foley/spot cues -21 … -26 par hain, aur **ek hi cue -16 par** hai — C5, yaani phaatak ki
zanjeer, jo is scene ka sabse ooncha block hai (spine ka object: gaon ka darwaza). Iske oopar kuch
nahi jaata; score bhi -17 par rukta hai.

## Beds (3)

| id | sound | kab se kab tak | level | pan | envelope |
|---|---|---|---|---|---|
| B1 WIND | `ep03/sfx/raw_fs/wind.mp3` (HPF 120 / LPF 7000) | 0.0 → `नमस्कार` -0.25 (141.9) | -24 | 0.0 | points (absolute, kyunki start 0.0): 81.0–84.0 par **+3 dB** ("bas hawa ki awaaz reh jaati hai"), 85.5 par wapas 0, 141.85 par -60 |
| B2 VILLAGE | `ep03/sfx/raw_fs/b1_village.mp3` (HPF 200 / LPF 9000) | 0.0 → `गांव सो जाता` +0.5 (107.4) | -26 | 0.0 | points: 93.0 tak flat, 96–101 par **-4 dB** (baithak: jhingur dheere), 105–106.2 par -9, phir -60 |
| B3 AANGAN | `ep01/sfx/raw_fs/b1_bed.mp3` (HPF 100 / LPF 8000) | `अंदर आंगन में` (95.0) → `गांव सो जाता` +0.2 (107.1) | -26 | 0.0 | koi points nahi → mixer ka default (2 s in, 1.2 s out) |

B1 aur B2 ke `points` **absolute** hain (unka `start` 0.0 hai, isliye `env()` ke liye t=0 wahin
padta hai). B3 aur score ke points apne-apne start se **relative** hain — dekh "Mix notes" ka
point 5.

## Score (ek hi swell)

Instrument: **tanpura hi**. Koi melody nahi, koi doosra instrument nahi, koi percussion nahi.

| step | kya hota hai | level |
|---|---|---|
| entry | `अपना दरवाजा बंद कर सकता` par fade-in (0.5 s) — yani line "phir bhi ek gaon apna darwaza band kar sakta tha" ke aakhri shabdon par | -24 se shuru |
| base | 0.9 s par +3 — kanoon/faisle wali line ke neeche bich jaata hai | -21 |
| swell | 1.15–1.55 s par **+7 dB** — ye peak theek **"किस ताकत से?"** par girdta hai (fallback par 140.1–140.5 s, sawal 140.8 s) | **-17** |
| exit | 1.95 s par -60; layer `नमस्कार` -0.25 par khatam hota hai (141.9), isliye tanpura host intro se **0.5–1.2 s** pehle (take ke pace par) poori tarah chup hai | — |

`points` apne start se relative: `[[0,-60],[0.5,0],[0.9,3],[1.15,7],[1.55,7],[1.95,-60]]`.

Kyun itna chhota swell? Kyunki is cold open mein score ke liye sirf **ek hi khaali jagah** hai:
"kis taaqat se?" ke turant baad ident shuru ho jaata hai, aur score ko `नमस्कार` se 0.25 s pehle
poori tarah chup hona hai. Isliye tanpura ek tez, saaf gesture hai — "ek lamba sur" jo sawal par
uthta hai aur host ko jagah de deta hai. (Script ke inline marker mein tanpura "panchayat" par likha
hai; wo shabd is cold open mein **bolaa hi nahi jaata**, isliye swell us sawal par anchored hai
jiska jawab panchayat hai — Part 2 mein wahi baithak khulti hai.)

**Ek duck** (`faisla_duck`): `ये गांव आज रात` par, pre 1.3 s / post 2.3 s, gain **0.30**. Yani
faisle wali line — "Ye gaon aaj raat ye darwaza nahi kholega." — par dono beds 0.30 par dab jaate
hain aur line akeli girti hai. Ye scene ka ek hi duck hai; score is window ke bahut baad aata hai,
isliye swell par koi asar nahi padta.

## Kahan chup rehna hai

1. **"Ye gaon aaj raat ye darwaza nahi kholega."** (duck ke saath) — yahan koi cue nahi. Beds
   -10.5 dB neeche chale jaate hain; line sach mein akeli hoti hai, uske baad hi "sawaar kuch der
   khada rehta hai" aata hai.
2. **"Mohar acchi lagi hui hai. Kagaz saaf hai. Sab kuch theek hai — sirf ek cheez kam hai."** —
   poora beat khaali. Koi paper, koi mohar, koi music nahi; kami narrations mein hai, SFX mein nahi.
3. **"Andar se koi jawab nahi aata."** — zanjeer ke hit se pehle ka khali sunnaa. C5 ko akela aane
   dena; uske pehle kuch bhi nahi (yahi scene ka sabse bada mauka hai).
4. **"Us fauj ka raasta is gaon se nahi jaata… jahan phaatak khula hai, ya jahan phaatak hai hi
   nahi."** — fauj aur raaste bayaan hote hain, chalte nahi. Iss beat mein sirf hawa (B1) rehti hai;
   fauj ka cue usse pehle line par hai, isse aage nahi.
5. **`नमस्कार` ke baad sab kuch saaf.** Ident dry hai (uske neeche tanpura ya bed nahi), 1944 wala
   para dry hai, aur `Ab tak` se aage poore episode mein ek bhi SFX nahi. Taanpura `नमस्कार` se
   0.5–1.2 s pehle chup ho jaata hai (layer `नमस्कार` -0.25 par khatam hota hai), beds bhi wahin
   katte hain, isliye intro mein **1.2 s ki sachchi khamoshi** hai
   (`dead_air.before_body_seconds`).

## Sound list (exact paths)

Beds:
`ep03/sfx/raw_fs/wind.mp3` (27.1 s) · `ep03/sfx/raw_fs/b1_village.mp3` (9:05) ·
`ep01/sfx/raw_fs/b1_bed.mp3` (5:58)

Foley:
`ep01/sfx/raw_fs/s5_crow.mp3` (0.43 s) · `ep03/sfx/raw_fs/steps.mp3` (3.41 s) ·
`ep01/sfx/raw_fs/s8_paper.mp3` (32.7 s) · `ep01/sfx/raw_fs/s6_latch.mp3` (13.3 s) ·
`ep03/sfx/raw_fs/crowd.mp3` (2:57) · `ep02/sfx/raw_fs/wicker.mp3` (15.6 s)

Score:
`ep03/sfx/raw_fs/tanpura.mp3` (46.4 s)

Synth (mix script online banata hai, koi file nahi):
`synth:sand_trickle` (2.6 s) · `synth:gust` (3.0 s)

Jo pool mein tha par **jaan-boojh kar nahi liya**: `ep03/sfx/raw_fs/field.mp3` (17.3 s — itni
chhoti file mixer tile kar deta hai, 107 s ke bed par 6 baar, yaani saaf loop sunai deta), `s1_dig`
/ `s1b_dig` / `s2_gravel` / `s4_brush` / `s3_stab` / `s9_writing` / `door.mp3` / `cup.mp3` /
`engine.mp3` / `drone.mp3` / `bass.mp3` / `sarangi.mp3` / `cello.mp3` / `shruti.mp3` / `tanpura2.mp3`.

## Mix notes aur QC

1. **File head hi bajta hai.** Mixer kisi cue ka koi start-offset nahi leta — `seconds` sirf file
   ke **head** se kaat ta hai. Isliye jin do files ka hit head par nahi hai, unke liye `filter` mein
   `atrim` + `asetpts` lagaya gaya hai: `s6_latch.mp3` ka sabse bada transient **11.68 s** par hai
   (head par sirf 0.026 RMS ki halki awaaz) aur `wicker.mp3` ka gehra creak **2.86 s** par. Filter
   strings: `atrim=start=11.2:end=12.1,asetpts=N/SR/TB,highpass=80` (C5) aur
   `atrim=start=2.75:end=4.15,asetpts=N/SR/TB,highpass=150` (C8). Baaki sab ki hit head par hai
   (kauwa 0.14 s, kagaz 0.08–0.31 s, kadam 0.65 s, crowd 0.02 s).
2. **Loop.** `wind.mp3` 27.1 s ki hai — 141.9 s ke bed ke liye tile karni padegi (~5 baar).
   Ye `ep02/sfx/raw_fs/air.mp3` ke saath **bilkul ek hi file** hai (dono ka md5
   `0e1687e50ad830415b3b658fee3dfd5a`) — yani "dry air" aur "gritty wind" ek hi recording hain, do
   alag beds nahi ban sakte. Seam sunai de to 2 s equal-power crossfade se loop banayein aur points
   ka slow ±1.5 dB modulation (jo plan mein hai) rakhein. `b1_village.mp3` (9:05) aur `b1_bed.mp3`
   (5:58) itni lambi hain ki unka loop dikhta nahi.
3. **Raat ke jhingur** `b1_village.mp3` se aa rahe hain (uski 1.5–6.5 kHz band mein energy sabse
   zyada hai, jo insects ke saath match karti hai). Mix se pehle 2 s sun kar confirm kar lein ki
   usme koi gaadi/horn/aadmi ki awaaz nahi hai; agar ho to `atrim` se saaf hissa chunein.
4. **Score ko chhota rakha gaya hai** (2.9 s). Teen timelines par simulate kiya gaya: calibrated
   model (0.395 s/shabd) aur 20% tez take — dono mein peak "किस ताकत से?" par girdta hai aur
   `नमस्कार` se pehle layer -60 par chala jaata hai. Agar koi take bahut hi tez ho (lagbhag bina
   pause) to decay `नमस्कार` se poori tarah pehle khatam nahi hota aur cut sunai de sakta hai — us
   case mein `points` ka decay 0.3 s aage sarak dein (peak 0.85–1.25, out 1.65) ya `end_offset`
   -0.45 kar dein.
5. **Points ka convention.** `env()` har layer ke **apne start** se t=0 maanta hai. B1/B2 ke `start`
   0.0 hain, isliye unke points absolute hain. B3 (aangan) aur score ka start phrase se aata hai,
   isliye unke points relative hain (B3 ke koi points nahi, default envelope). Dhyan dein: Ep 4.1 ki
   json mein score ke points **absolute** likhe hue hain (`[[160.3,-60],…,[181.3,-60]]`) aur uska
   start 160.3 s hai — `env()` usse poori tarah -60 dB par le jaata hai, yaani us plan ka tanpura
   bajta hi nahi. Us file ko chhedna nahi hai; yahan ye baat sirf isliye likhi hai ki aage koi
   wahi galti na kare.
6. **Level check:** koi bhi cue -16 se oopar nahi (ek hi cue -16 par: C5), score ka peak -17, beds
   -24/-26. `steps.mp3` bahut dheemi recording hai (peak 0.018) — mixer usse level par laane ke liye
   ~+13 dB dega, to hiss bhi uthegi; isliye dono jagah `atrim` se sirf kadam wala hissa liya gaya hai
   (0.4–2.2 aur 1.4–3.4). QC mein headphones par hiss sunai de to C3/C9 ko 1 dB neeche karein.
7. **Jo hai hi nahi (unsure).** Inline marker mein "[SFX: ghode ki halki saans]" maanga gaya hai,
   par pool mein **ghode ki koi recording nahi hai** (aur download allowed nahi). Isliye ghode ki
   saans chhod di gayi hai — sawaar ko uske **utarne ke do kadam** (C3) aur kagaz (C4) uthaate hain.
   Agar aage koi horse-breath file pool mein aaye to wo C3 se pehle "ghoda aata hai" par lag sakti
   hai. Baaki do "unsure" cheezein: (a) `b1_village.mp3` mein jhingur hain ya nahi (point 3);
   (b) `s6_latch.mp3` ka head khaali hai, isliye C5 ka `atrim` window hi uski jaan hai — mix se pehle
   ek baar sun kar confirm karein ki 11.2–12.1 s mein wahi jhatka hai.

## Kya sunayi dega

1. शुरू में शाम की धूल भरी हवा और दूर के झींगुर — और सड़क पर धूल के हल्के कण उठते हुए।
2. कटे खेतों के ऊपर एक दूर का कौवा, फिर घोड़े से उतरते सवार के दो क़दम और कागज़ की हल्की आवाज़।
3. जब फाटक की जंजीर हिलती है तो सबसे साफ़ आवाज़ वही होगी — हिलती है और रुक जाती है; फिर सिर्फ़ हवा रह जाती है।
4. अंदर आँगन में चारपाई की रस्सी चिक-चिक करेगी, झींगुर धीमे पड़ जाएँगे, और "गाँव सो जाता है" पर सब चुप।
5. आख़िर में तानपूरा एक ही बार ऊपर उठेगा — ठीक "किस ताक़त से?" पर — और नमस्कार से पहले चुप हो जाएगा; उसके बाद पूरा एपिसोड साफ़ आवाज़ में चलेगा।
