# Ep 6.5 — SFX plan (cold open)

Cold open = `## Cold open` .. `## Ab tak` (364 narration words, chunk `c01`, ep06_5). Score sirf
cold open par; `नमस्कार` ke baad poora episode sookha (dry voice) rehta hai.
House style Ep 1 / 3 / 4.1 / 6 jaisa hi: narration anchor hai, har bed uske neeche, ident dry,
aur aakhri bed cut ke baad body se pehle dead-air pocket.

**Scene:** Calcutta, 1757, dopahar dhal rahi hai. Nadi ke kinaare do-manzila kothi; upar ek kamra,
ek lambi mez, mez par kaagaz aur khaali register, haath mein pankh wali kalam. Ek naujawan clerk
samjhauta utaar raha hai. Ek panna — uspar ek rakam, aur us rakam ke neeche ek naam (doosre khane
mein dobara). Bahar door do topon ki dheemi garaj. Lifafa mom ki mohar ke saath kashti par nikal
jaata hai; kamre mein ek band register reh jaata hai. Faisla aaj nahi hoga.

## Cast (source files)

| id | file | what it is |
|---|---|---|
| RIVER | `synth:river_wash` (`synth_seconds: 240`) | nadi ka paani — dheemi, saans jaisi thapak (bed) |
| ROOM | `ep01/sfx/raw_fs/b1_bed.mp3` | kothi ke kamre ka room tone (bed) |
| TANPURA | `ep03/sfx/raw_fs/tanpura.mp3` | tanpura loop — ek hi swell (score) |
| PEN | `ep01/sfx/raw_fs/s9_writing.mp3` | kalam ka kaagaz par chalna |
| PAPER | `ep01/sfx/raw_fs/s8_paper.mp3` | panna / panno ka bundle / band register |
| TICK | `ep01/sfx/raw_fs/s8b_pen.mp3` | halki chhoti tik (ginne wali) |
| KNOCK | `ep05/sfx/raw_fs/cup.mp3` | lakdi ki mez par dabi thap (sikka / register) |
| NAME | `ep03/sfx/raw_fs/sarangi.mp3` | ek hi bowed phrase — naam ka lamha |
| BOOM | `ep01/sfx/raw_fs/s3_stab.mp3` | hard impact, low-pass karke door ki top |
| SUB | `ep02/sfx/raw_fs/bass.mp3` | sub-bass — doosri top ki garaj |
| SEAL | `ep01/sfx/raw_fs/s6_latch.mp3` | dabaav/clack — mom ki mohar |
| BOAT | `ep02/sfx/raw_fs/wicker.mp3` | lakdi ki chikat/reed — kashti ki aawaaz |

Synth cues (`synth:river_wash`) mix script mein bante hain; baaki sab repo pool se hain, koi
download nahi.

## Cue table (anchors phrase-locked; Devanagari phrase = cold open ke asli shabd)

Times `ep06_5/c01.align.json` ke hisaab se apne aap shift hote hain; neeche jo `~MM:SS` diya hai wo
andaaza hai (2.45 shabd/second), sirf fallback ke liye.

| id | narration line | sound | lands on the phrase | level under voice | pan | fades / envelope |
|---|---|---|---|---|---|---|
| S1 `pen1` | "कलम चलती है।" | `ep01/sfx/raw_fs/s9_writing.mp3`, 2.4 s | `कलम चलती है` (~00:44.9) | -20 dB | L -0.15 | in 0.02 s, out 0.4 s; likhna shuru |
| S2 `page1` | "बीच में एक पन्ना आता है" | `ep01/sfx/raw_fs/s8_paper.mp3`, 0.8 s | `बीच में एक पन्ना आता` (~00:46.9) | -22 dB | L -0.20 | in 0.01 s, out 0.15 s |
| S3 `coin1` | "उस रकम के नीचे" | `ep05/sfx/raw_fs/cup.mp3` + `lowpass=2000`, 0.6 s | `उस रकम के नीचे` (~00:51.8) | **-18 dB** | L -0.30 | in 0.005 s, out 0.2 s; scene ka sabse uncha cue |
| S4 `name` | "वही नाम, थोड़ी दूर" | `ep03/sfx/raw_fs/sarangi.mp3`, 3.2 s | `वही नाम थोड़ी दूर` (~00:54.3) | -23 dB | centre | -1.8 s pehle se, in 0.4 s, out 1.5 s |
| S5 `tick2` | "एक नाम, दो बार।" | `ep01/sfx/raw_fs/s8b_pen.mp3`, 0.35 s | `एक नाम दो बार` (~00:58.8) | -21 dB | L -0.35 | in 0.005 s, out 0.12 s; "do baar" = do tik |
| S6 `cannon1` | "बाहर, दूर, कुछ आवाज़ें आती हैं।" | `ep01/sfx/raw_fs/s3_stab.mp3` + `lowpass=180`, 1.1 s | `कुछ आवाज़ें आती हैं` (~01:11.4) | -24 dB | R 0.45 | -0.3 s, in 0.005 s, out 0.5 s; top 1 |
| S7 `cannon2` | "हल्के से सर उठाता है।" | `ep02/sfx/raw_fs/bass.mp3` + `lowpass=200`, 2.2 s | `हल्के से सर उठाता है` (~01:13.9) | -24 dB | R 0.55 | -1.4 s se, in 0.08 s, out 1.0 s; top 2, zyada door |
| S8 `paper2` | "पन्नों को एक-एक कर के जोड़ता है" | `ep01/sfx/raw_fs/s8_paper.mp3`, 1.6 s | `पन्नों को एक-एक कर के` (~01:19.6) | -21 dB | L -0.20 | in 0.02 s, out 0.5 s; bundle |
| S9 `seal` | "मोम की मोहर लगाता है" | `ep01/sfx/raw_fs/s6_latch.mp3` + `lowpass=3500`, 0.5 s | `मोम की मोहर लगाता है` (~01:26.9) | -19 dB | L -0.10 | -0.1 s, in 0.005 s, out 0.25 s |
| S10 `boat` | "लिफ़ाफ़ा एक कश्ती पर जाता है" | `ep02/sfx/raw_fs/wicker.mp3`, 2.6 s | `एक कश्ती पर जाता है` (~01:32.2) | -24 dB | R 0.40 | in 0.5 s, out 1.0 s |
| S11 `register` | "एक बंद रजिस्टर रह जाता है।" | `ep05/sfx/raw_fs/cup.mp3` + `lowpass=1200`, 0.8 s | `एक बंद रजिस्टर रह जाता` (~01:40.4) | -19 dB | L -0.15 | in 0.005 s, out 0.3 s |

**11 spot cues.** Har cue apni line se hi motivated hai: likhna (S1), panna (S2), rakam/sikka (S3),
naam ka lamha (S4), doosri gin (S5), do door ki top (S6-S7), panno ka bundle (S8), mohar (S9),
kashti (S10), band register (S11). Koi cue `नमस्कार` ya uske baad ki lines ko touch nahi karta.

## Score — ek hi swell (TANPURA)

`ep03/sfx/raw_fs/tanpura.mp3`, EQ `highpass=70, lowpass=6000`, loop, centre, base **-24 dB**.
Entry phrase `उस लंबी मेज़ पर` (+ fallback 98.4 s) — yaani jab kahani kamre aur mez par lautta hai;
exit `नमस्कार` par `end_offset: -0.25` (+ end_fallback 112.0 s). Koi melodic line nahi, koi
doosra instrument nahi, tabla/bansuri bilkul nahi.

| t (start se) | ~MM:SS | level | kya ho raha hai |
|---|---|---|---|
| 0 → 2.0 | 01:38.4 → 01:40.4 | -60 → -28 | kamre mein wapsi ke saath halka andar aata hai |
| 5.8 | ~01:44.1 ("बहुत कुछ लिखा गया") | -24 | poora ho jaata hai |
| 6.8 | ~01:45.1 ("एक चीज़ नहीं लिखी गई") | **-22** | **ek hi swell** — jo cheez nahi likhi gayi, wahi uncha |
| 8.2 → 10.0 | ~01:46.5 → 01:48.3 | -25 → -26.5 | neeche utarta hai (verdict ke pehle) |
| 10.0 → 13.65 | 01:48.3 → `नमस्कार` -0.25 | → -60 | khatam; `नमस्कार` se 0.25 s pehle poora out |

Points (`[[t, dB], …]`, relative): `[0,-60], [2,-4], [4.5,-2], [5.8,0], [6.8,2], [8.2,-1], [10,-2.5], [13.65,-60]`.

## Continuous beds (RIVER + ROOM)

| t | RIVER (nadi, -25 dB) | ROOM (kamra, -27 dB) |
|---|---|---|
| 0.0 | -60 → 0 (3.5 s mein aata hai) | -60 (bahar hain, kamra abhi nahi) |
| ~12.5 s | 0 (-25) | → -28 (upar kamre mein aate hain) |
| 88 → 94 s | 0 → +1.5 (yaani -25 → -23.5; kashti ke saath paani khulta hai) | -28 → -60 (kamre se bahar nikal jaate hain) |
| 98 s | 0 (-25) | → -30 (mez par lautte hain) |
| 111.4 → 111.95 | 0 → -60 (out) | -30 → -60 (out) |

Dono beds `end_phrase: ["नमस्कार"]`, `end_offset: -0.25` par khatam (host intro ke upar kuch nahi).
Bed pan hamesha `0.0`.

## Kahan chup rehna hai (silence > sound)

1. **~00:54.5 – 01:11.4 — "उस नौजवान को इसका मतलब नहीं पता…"** Yahan koi spot cue nahi; sirf nadi
   aur kamra. Ye cold open ka sabse bada khaali hissa hai — jaan-boojh kar. Jo aadmi hisaab likh
   raha hai, use matlab pata nahi: us par koi awaaz nahi daalni.
2. **~01:15.0 – 01:19.6, top ke baad** "फिर झुक जाता है" — doosri top ki garaj khatam, aur uske baad
   sannata; sar uthaane aur wapas jhukne ke beech kuch nahi.
3. **~01:27.5 – 01:32.2, mohar ke baad** "और किसी के हाथ भेज देता है" — lifafa chala gaya, cue nahi;
   narration ke saath sirf kamra aur nadi.
4. **~01:47.0 – 01:50.4, "फ़ैसला आज नहीं होगा"** Duck: nadi, kamra aur tanpura sab ~0.30 gain par
   gir jaate hain, taaki faisle wali line apne aap, akele khadi ho. Uske baad score laut kar nahi aata.
5. **`नमस्कार` se 0.25 s pehle → ident tak, aur uske baad** — sab out; intro ke neeche kuch nahi.
6. **Cold open ke aakhir se body tak** — 1.3 s asli khamoshi (`dead_air.before_body_seconds`).

## Duck (ek hi baar)

| id | phrase | pre | post | gain |
|---|---|---|---|---|
| `verdict_duck` | `फ़ैसला आज नहीं होगा` (fallback 108.2 s) | 1.2 s | 2.2 s | 0.30 |

## Sound list (exact paths, repo pool — kuch download nahi)

Beds / score: `synth:river_wash`, `ep01/sfx/raw_fs/b1_bed.mp3`, `ep03/sfx/raw_fs/tanpura.mp3`.
Foley: `ep01/sfx/raw_fs/s9_writing.mp3`, `ep01/sfx/raw_fs/s8_paper.mp3`,
`ep01/sfx/raw_fs/s8b_pen.mp3`, `ep01/sfx/raw_fs/s6_latch.mp3`, `ep01/sfx/raw_fs/s3_stab.mp3`,
`ep05/sfx/raw_fs/cup.mp3`, `ep03/sfx/raw_fs/sarangi.mp3`, `ep02/sfx/raw_fs/bass.mp3`,
`ep02/sfx/raw_fs/wicker.mp3`.

Filters: RIVER — koi filter nahi (synth filter ignore karta hai, `synth_seconds` hi kaam karta hai);
ROOM `highpass=90`; TANPURA `highpass=70,lowpass=6000`; BOOM `lowpass=180`; SUB `lowpass=200`;
KNOCK `lowpass=2000` (sikka) aur `lowpass=1200` (register); SEAL `lowpass=3500`.

## Mix notes

- Chalao: `python3 tools/audio/mix_from_plan.py --workdir ep06_5 --chunk c01 --plan "scripts/Ep 6.5 Company kyun jeeti — SFX plan.json"`.
- Har cue par `fallback_at` diya hai, par asli anchor Devanagari phrase hi hai (align par chalta hai).
  Narration dobara render ho to sirf phrase anchors bharose ke hain, seconds nahi.
- Levels: spot cues **-18 se -24 dB** ke beech (sabse uncha sikka -18, sabse neeche doosri top aur kashti -24);
  beds -23.5 … -27 (nadi -25, kamra -27); score -22 … -26 (base -24, swell -22). -16 dB wala cue jaan-boojh kar
  nahi diya — ye ek aadmi ke likhne ka scene hai, sabse bhaari cheez bhi chhoti rakhi gayi.
- Voice dead centre; foley thoda baayein (-0.10 … -0.35), door/wide cheezein daayein (0.40 … 0.55),
  beds/score centre.
- Kabhi bhi 12 se zyada spot cue nahi: yahan 11 hain, aur har cue apni line ke andar hi khatam hota hai
  (koi cue paragraph boundary cross nahi karta).
- Koi reverb nahi, koi whoosh/riser nahi, koi music `नमस्कार` ke baad nahi; body bilkul sookha.
- QC: ek baar phone speaker par halki volume mein — agar nadi ya tanpura shabd se pehle sunayi de,
  dono ko 2 dB neeche. Phir headphones par check: 01:47 ke duck mein line akele sunayi de, aur
  `नमस्कार` se 0.25 s pehle sab out ho.
- Shanka (unsure, agar QC mein kharab lage): (a) "sikka" ke liye pool mein asli metal tick nahi hai
  — `cup.mp3` + `lowpass=2000` dabi wooden thap deta hai, `s8b_pen.mp3` halki tik; agar dono
  jaisa hi lage to sikka cue ke do 0.25 s slices `s8b_pen.mp3` se lein. (b) `wicker.mp3` kashti ki
  chikat jaisa hai — paani ka lapka RIVER bed ke +1.5 dB rise se aata hai, isliye BOAT ko solo
  bhaari nahi lagta; agar kashti "lakdi" jaisi lage to BOAT ko -26 dB kar den.

## Kya sunayi dega

1. शुरू में सिर्फ़ नदी का पानी — धीमी, साँस जैसी थपक; और जैसे ही "ऊपर एक कमरा" आता है, कमरे की शांत हवा उसके अंदर आ जाती है.
2. कलम का काग़ज़ पर चलना, बीच में एक पन्ना खुलना, और उस रकम के नीचे एक दबी थप — बस इतना, कोई शोर नहीं.
3. "एक नाम, दो बार" पर एक हल्की सी टिक, और "वही नाम, थोड़ी दूर" पर एक ठहरी हुई सारंगी की साँस.
4. बाहर, दूर, दो बारी-बारी तोपों की दबी गड़गड़ाहट — जैसे किसी और इलाक़े में; नायक सर उठाता है और फिर झुक जाता है.
5. पन्नों का जुड़ना, मोम की मोहर की दबी क्लिक, और फिर कश्ती की लकड़ी की चटक के साथ पानी खुल जाता है; कमरा पीछे छूट जाता है.
6. आख़िर में लंबी मेज़ पर रजिस्टर बंद होता है, धीमा तानपूरा एक बार ऊपर उठता है, और "फ़ैसला आज नहीं होगा" कहने से ठीक पहले हवा, पानी और सुर — तीनों एक साथ झुक जाते हैं. फिर नमस्कार से पहले पूरा सन्नाटा.
