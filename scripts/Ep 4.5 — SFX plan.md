# Ep 4.5 — SFX plan (cold open)

Cold open = `## Cold open` .. `## Ab tak` (377 narration words, chunk `c01`) — the young man's
departure (dawn village, potli, maa ka haath, darwaaza, raasta) aur aakhir mein 1944 ka
Ahmadnagar qila, jahan Nehru ki shikaayat se aaj ka sawal khulta hai.
Signal chain aur levels wahi hain jo Ep 3 / 4.1 / 5 / 6 mein chale hain: narration anchor hai,
har bed uske neeche baithta hai, host intro sookha rehta hai, aur aakhri bed ka cut body se
pehle 1.2 s ka dead-air pocket chhodta hai.

Anchors phrases par locked hain (Roman Hindi script se Devanagari mein uttere gaye), seconds par
nai — jab take dobara render hoga, cue wahi rahega. Har phrase cold open mein ek hi jagah match
karta hai (maine poore cold open par fuzzy-match se check kiya, wahi logic jo mixer ke `find_phrase`
mein hai, ratio 0.7) — `fallback_at` sirf safety net hai. Do phrases do-kaam karte hain: cue 6
(`["और","चल","पड़ता","है"]`) wahi hai jis par B1 bed out hota hai, aur duck wahi phrase hai jo
cue 8 ko chalata hai — dono jodi jaan-boojh kar ek hi pal par baithi hain.

## Cast (source files)

| id | file | what it is |
|---|---|---|
| VILLAGE | `ep03/sfx/raw_fs/b1_village.mp3` | gaon ka bhor-wala bed (bed) |
| FIELD | `ep03/sfx/raw_fs/field.mp3` | khula maidan, door tak (raaste ka bed) |
| ROOM | `ep01/sfx/raw_fs/b1_bed.mp3` | qile ki kothri ka room tone (bed) |
| DRONE | `ep02/sfx/raw_fs/drone.mp3` | low sustained tone — yahi ek score/swell hai |
| CROW | `ep01/sfx/raw_fs/s5_crow.mp3` | ek door ka kauwa (rehte hue gaon ki subah) |
| WICKER | `ep02/sfx/raw_fs/wicker.mp3` | charmaraahat (kuen ki rassi, bailgaadi ke pahiye) |
| PAPER | `ep01/sfx/raw_fs/s8_paper.mp3` | kapde/kaagaz ki sar-sarahat (gaanth, naqshe) |
| SARANGI | `ep03/sfx/raw_fs/sarangi.mp3` | ek bowed phrase (maa ka haath) |
| DOOR | `ep03/sfx/raw_fs/door.mp3` | purana lakdi ka darwaaza |
| STEPS | `ep03/sfx/raw_fs/steps.mp3` | kachchi mitti par pair (chhote, sookhe) |
| WRITING | `ep01/sfx/raw_fs/s9_writing.mp3` | likhne ki halki kharakh |
| synth | `low_tone` (mix script mein banti hai) | naam se pehle uthne wali sooti awaaz |

Do synthesised/ek hi file se do kaam liye gaye hain, dono yahan declare hain: `synth:low_tone`
(Takshashila ke naam par) aur WICKER do jagah — kuen ki rassi (bhor) aur bailgaadi ke pahiye
(raasta); level, pan aur lambai dono jagah alag hain, isliye ek jaisa nahi sunai dega.

## Cue table (anchors phrase-locked; `fallback_at` sirf tab jab alignment na mile)

| # | cue | sound | lands on the phrase (Devanagari) | level | pan | fades / seconds |
|---|---|---|---|---|---|---|
| B1 | bhor ka gaon — bed | VILLAGE | poora scene, `["और","चल","पड़ता","है"]` par out (+0.6 s) | -25 dB | 0.0 | 2.5 s in; 28.4–33.6 s par -13 dB ka dip (khaali haath wala beat) |
| B2 | raasta — bed | FIELD | `["उसका","रास्ता","लंबा","है"]` se, `["अहमदनगर","का","किला"]` par out (-0.4 s) | -26 dB | 0.0 | 3.0 s in / 6.0 s out |
| B3 | 1944, qila — bed | ROOM | `["अहमदनगर","का","किला"]` se, `["नमस्कार","मैं","हूँ"]` par out (-0.75 s) | -27 dB | 0.0 | 2.5 s in / 3.5 s out |
| 1 | kauwa, suraj se pehle | CROW (lowpass 4000) | `["अभी","सूरज","नहीं","निकला"]` (-1.0 s) | -24 dB | 0.55 | 0.05 / 0.25 s; 0.9 s |
| 2 | kuen ki rassi ki charmarahat | WICKER (lowpass 6000) | `["एक","आँगन","जिसमें","चूल्हा"]` (-0.9 s) | -24 dB | -0.35 | 0.08 / 0.30 s; 1.1 s |
| 3 | potli ki gaanth | PAPER | `["गाँठ","बाँध","देता","है"]` (-0.5 s) | -22 dB | -0.25 | 0.02 / 0.20 s; 1.0 s |
| 4 | maa ka haath | SARANGI (hp 90 / lp 6500) | `["बेटे","के","सिर","पर","हाथ","रख"]` (-2.2 s) | -23 dB | -0.15 | 0.6 / 1.8 s; 4.0 s |
| 5 | purana darwaaza khulta hai | DOOR | `["नौजवान","पोटली","कंधे","पर","डालता","है"]` (-1.4 s) | -18 dB | -0.30 | 0.02 / 0.40 s; 1.8 s |
| 6 | chal padta hai — pair | STEPS | `["और","चल","पड़ता","है"]` (-0.25 s) | -21 dB | -0.35 | 0.05 / 0.60 s; 2.6 s |
| 7 | bailgaadi guzarti hai | WICKER (hp 90 / lp 3500) | `["मैदान","नदियाँ","जंगल"]` (-1.4 s) | -22 dB | 0.45 | 0.7 / 1.2 s; 3.4 s |
| 8 | shehar ka naam | synth:low_tone | `["उस","शहर","का","नाम","है","तक्षशिला"]` (-1.0 s) | -20 dB | 0.0 | 0.4 / 1.2 s; 3.2 s |
| 9 | Nehru likh rahe hain | WRITING (hp 200 / lp 7000) | `["पुराने","भारत","पर","लिख"]` (-0.4 s) | -21 dB | -0.30 | 0.3 / 0.8 s; 3.2 s |
| 10 | raajyon ke naqshe | PAPER | `["राज्यों","के","नक़्शे","बनाए","हैं"]` (-0.4 s) | -23 dB | 0.25 | 0.1 / 0.5 s; 1.8 s |
| D1 | naam akela girta hai | duck (ek hi baar) | same phrase as cue 8 | gain 0.30 | — | pre 1.2 s / post 2.2 s |

Kul 10 spot cues (seema ~12 ke andar). Sabse ooncha block cue 5 hai (-18 dB); koi bhi cue
-18 dB se oopar nahi jaata.

## Score (ek hi swell)

Sirf ek score layer hai — `DRONE` (`ep02/sfx/raw_fs/drone.mp3`, hp 60 / lp 6000), -25 dB, pan 0.0.
Ye Takshashila ke naam ke baad enter karta hai (`start` 59.6 s, yani naam ke duck window ke bahar)
aur host intro se 0.25 s pehle out ho jaata hai: `end_phrase ["नमस्कार","मैं","हूँ"]`,
`end_offset -0.75` (ye asal mein "नमस्कार" ke khatm hone se ~0.25 s pehle padta hai — brief wala
`["नमस्कार"]` + `-0.25` hi timing hai, par poora phrase lene se fuzzy match ka jhagda nahi hota).

Envelope mein ek hi swell hai: `["सफ़र","क्यों","कर"]` (yani "Hum ye safar kyun kar rahe hain?")
par +3 dB, phir wapas -25 dB par. Uske baad Nehru ki kothri tak drone dab ke chalta rehta hai aur
intro se pehle chup ho jaata hai. `points` har layer ke apne `start` se gine gaye hain (mixer ka
`env()` layer ke shuru se index karta hai) — ise "theek" karne ki zaroorat nahi.

## Kahan chup rehna hai

Teen jagah jaan-boojh kar koi cue nahi hai:

1. `["बस","इतना","ही","सामान"]` aur uske baad wala paragraph — "koi naukar nahi, koi talwar nahi,
   koi bhala nahi". Yahi scene ka pehla bhaari beat hai, aur yahan awaaz bharni nahi hai: sirf
   gaon ka bed, aur B1 ka envelope is poore paragraph ke liye -13 dB neeche chala jaata hai
   (28.4–33.6 s). Teen "nahi" khud sabse zyada sunai dete hain jab unke neeche kuch na ho.
2. `["इतना","ही","सामान"]` par koi foley nahi — potli ki gaanth (cue 3) se pehle ek khaali pal.
3. `["सफ़र","क्यों","कर"]` wala sawal aur "Kyunki Nehru ki ek shikayat thi." — yahan sirf drone
   hai, koi spot cue nahi. Sawal narration ke paas rehna chahiye.
4. Intro ke baad ke do paragraph (aaj ka sawal, "Jawab us potli ke saath-saath chalega") poore
   sookhe hain — koi bed, koi score, koi cue nahi.

Dead air: aakhri line ke baad 1.2 s ka sannata, phir "Ab tak" ka pehla shabd.

## Sound list (exact paths, sirf yahi)

- Bed: `ep03/sfx/raw_fs/b1_village.mp3`, `ep03/sfx/raw_fs/field.mp3`, `ep01/sfx/raw_fs/b1_bed.mp3`
- Score: `ep02/sfx/raw_fs/drone.mp3`
- Foley: `ep01/sfx/raw_fs/s5_crow.mp3`, `ep02/sfx/raw_fs/wicker.mp3` (do cue),
  `ep01/sfx/raw_fs/s8_paper.mp3` (do cue), `ep03/sfx/raw_fs/sarangi.mp3`, `ep03/sfx/raw_fs/door.mp3`,
  `ep03/sfx/raw_fs/steps.mp3`, `ep01/sfx/raw_fs/s9_writing.mp3`
- Synth: `synth:low_tone` (Ek 8)
- Kuch bhi download nahi hua; repo pool hi use hua.

## Teen baatein QC ke liye

- **Anchors ek-ek baar resolve hote hain.** Maine plan ke saare phrases ko mixer ke apne
  `find_phrase` (ratio 0.7) se, cold open ke Devanagari par, chalaya: plan ke 15 anchor slots
  (12 alag phrases) mein se koi unresolved nahi, aur har `fallback_at` anchored waqt se 0.4 s ke
  andar hai. Jab `c01.align.json` ban jaye, ek baar ye chala lena: `python3 tools/audio/mix_from_plan.py --workdir ep04_5
  --chunk c01 --plan "scripts/Ep 4.5 — SFX plan.json" --check-only` (0 unresolved chahiye).
  Dhyan: akele `["नमस्कार"]` par anchor karna theek nahi — "नौकर" usse 0.7 par match kar jaata hai
  aur bed 100 s pehle kat jaata. Isliye end-anchor `["नमस्कार","मैं","हूँ"]` hai (wahi timing).
- **Duck pura buffer dabata hai.** `mix_from_plan.py` duck gain ko narration sameta hue poore
  buffer par lagata hai, isliye cue 8 ka window (56.0–59.4 s) sunne mein poora mix ~10.5 dB
  neeche jaata hai — sirf beds nahi, awaaz bhi. Yani "naam akela girta hai" filhaal volume-pull
  ki tarah aayega. Agar intent beds-only duck hai, mixer ke duck block ko `layer` par lagana padega.
- **Beds ka loop aur file ke shuru ka sannata.** `field.mp3` sirf 17.3 s ka hai aur raaste ka bed
  ~50 s chalta hai, to mixer use ~3 baar tile karega (Foley beds 545 s / 357 s hain, unme ye dikkat
  nahi). Aur `door.mp3` ka pehla ~1.0 s lagbhag khaali hai — asli charmaraahat 1.0–1.25 s par hai,
  isliye cue 5 ka offset -1.4 s hai taaki creak "डालता है" par hi gire (44.3 s + 1.0 s ≈ 45.3 s).
  `synth:*` cues aur baaki file windows (crow 0.4 s, steps 3.4 s) isi tarah ek baar check kar lena.

## Kya sunayi dega

Suraj se pehle gaon: door kahin ek kauwa, kuen par rassi ki charmarahat, aur ek naujawan kapde par
saamaan rakh raha hai — gaanth ki halki sar-sarahat. Phir sannata, jab wo ginta hai ki saath koi
naukar nahi, kamar par talwar nahi, haath mein bhala nahi. Maa ke haath par sarangi ki ek bow,
lakdi ka purana darwaaza, mitti par pair, aur raaste par se guzarti ek bailgaadi ki charr-charr.
"Takshashila" akela girta hai, uske baad dheema drone jo "hum ye safar kyun kar rahe hain?" par ek
baar ubharta hai. 1944, qile ki kothri: room tone, likhne ki kharakh, naqshon ki sar-sarahat — aur
intro se 0.25 s pehle sab chup.
