# Ep 6.2 — SFX plan (cold open)

Cold open = `## Cold open` .. `## Ab tak` (script ki line 43 se 79 tak), yaani **315 narration
shabd** (12 cold-open para = 198, host ident = 29, uske baad ke do body para = 88) — chunk `c01`.
Scene jo score hota hai wo pehle ~65 second hai: barsaat ki pehli shaam se lekar
"Raja badalte rahe. To aam zindagi kyun nahi badli?" tak. Uske baad kuch bhi SFX nahi.

House convention wahi hai jo Ep 3 / Ep 5 / Ep 4.1 mein hai: narration anchor hai, har bed uske
neeche baithta hai, host intro dry hai, aur aakhri bed ke katne ke baad dead-air pocket bachta hai.

Anchors **phrase par tike hain, second par nahi.** Dono bed, score, duck aur saare 12 cue apne
Devanagari phrase se judte hain (JSON dekhiye). Phrase ka aakhri shabd dhoondh kar mixer us shabd
ka asli audio time nikaal leta hai, isliye take dobara render hone par bhi sab apni jagah rehta
hai. `fallback_at` / `end_fallback` sirf safety net hain (`--no-align` ke liye), 0.33 s prati shabd
ke andaaze par.

> Phrase aise chune gaye hain ki unka **aakhri shabd** kisi 1-vyanjan wale sentence-final shabd
> (`है।`, `हैं।`, `में।`) par na ruke — mixer ka `norm()` danda (।) nahi hataata, aur `है।` vs `है`
> ka score 0.667 reh jaata hai (limit 0.7). Isliye "बरसात की पहली शाम" (…है से pehle), "ऊपर जाती"
> (…हैं से pehle) jaise chhote runs use hue hain. Har phrase c01 mein **ek hi baar** aata hai —
> grep se check kiya gaya hai.

## Cast (source files)

| id | file | kya hai |
|---|---|---|
| RAIN | `synth:rain` | barish ki chadar (bed + pehli barsaat ka dhamaka) |
| VILLAGE | `ep03/sfx/raw_fs/b1_village.mp3` | gaon ka bed — sookhi hawa, ped ke pichhe ki goonj |
| GUST | `synth:gust` | thandi hawa ka jhonka |
| DROP | `synth:sand_trickle` | sookhi mitti/patton par girti boondon ka chhitka |
| WICKER | `ep02/sfx/raw_fs/wicker.mp3` | rassi aur jhoole ki chik-chik (chaar jagah) |
| CROWD | `ep03/sfx/raw_fs/crowd.mp3` | door ladkiyon ka gaana (bheed ki goonj, koi saaf shabd nahi) |
| SARANGI | `ep03/sfx/raw_fs/sarangi.mp3` | naam wala moment — ek kamand ki bhari awaaz |
| PEN | `ep01/sfx/raw_fs/s9_writing.mp3` | Nehru ki kalam kaagaz par |
| STEPS | `ep03/sfx/raw_fs/steps.mp3` | dhool par door ke kadam — gaddi ki taraf ka juloos |
| LOW | `synth:low_tone` | badalte sultanon ka bhara hua neecha sur |
| TANPURA | `ep03/sfx/raw_fs/tanpura.mp3` | score — sirf ek swell (neeche) |

Synth chalane wale paanch cue/bed JSON mein `synth:<naam>` ke roop mein likhe hain. Dhyan:
mixer synth cues par `filter` **nahi** lagata (`resolve_sound` sirf `fn(dur)` call karta hai),
isliye synth cues par filter nahi maanga gaya — recipe hi utni saaf chuni gayi hai.

## Cue table (level, pan, fade — anchors JSON mein Devanagari phrases ke saath)

| # | cue | sound | kis phrase par | level | pan | fade |
|---|---|---|---|---|---|---|
| A1 | `rain_bed` | synth:rain | poore scene par (0.0 se), `बिल्कुल वही` par kat | −21 dB | 0.0 | in 2 s, out 0.27 s (hard) |
| A2 | `rain_arrive` | synth:rain | `बरसात की पहली शाम` | **−17 dB** (scene ka loudest block) | 0.0 | in 1.2 s, out 2.5 s |
| A3 | `village_bed` | `b1_village.mp3` | `गांव के बाहर` se `बिल्कुल वही` +0.35 s | −26 dB | 0.0 | in 1.6 s, out 1.05 s |
| A4 | `boond` | synth:sand_trickle | `सूखी मिट्टी पर बूंद गिरती` | −21 dB | −0.2 | in 0.15 s, out 0.6 s |
| A5 | `thandak` | synth:gust | `हवा में ठंडक` | −24 dB | +0.4 | in 0.8 s, out 1.2 s |
| B1 | `rassi1` | wicker | `दो रस्सी के झूले बंधे` | −21 dB | −0.3 | in 0.05 s, out 0.35 s |
| B2 | `creak_up` | wicker | `ऊपर जाती` | −20 dB | −0.2 | in 0.05 s, out 0.4 s |
| B3 | `creak_down` | wicker | `नीचे आती` | −21 dB | −0.25 | in 0.05 s, out 0.45 s |
| B4 | `gaana` | crowd | `और गाती` | −25 dB | +0.5 | in 0.9 s, out 1.6 s |
| C1 | `name` | sarangi | `नाम अमीर खुसरो` (1.9 s pehle se, offset −1.9) | −23 dB | 0.0 | in 0.4 s, out 1.6 s |
| C2 | `lekhan` | `s9_writing.mp3` | `नेहरू लिखते हैं` | −23 dB | −0.35 | in 0.3 s, out 0.8 s |
| D1 | `steps` | `steps.mp3` | `कितने बादशाह` | −24 dB | +0.45 | in 0.6 s, out 1.0 s |
| D2 | `sultans` | synth:low_tone | `सुल्तान बदले` | −21 dB | 0.0 | in 0.5 s, out 1.2 s |
| E1 | `vapsi` | wicker | `गाना वही` | −20 dB | −0.25 | in 0.05 s, out 0.35 s |
| E2 | **hard cut** | — | `बिल्कुल वही` | — | — | barsaat 0.27 s mein out, phir sannata |

Sabse tez level −17 dB hai (A2), aur wo bhi us waqt jab bed −23 dB par jaa raha hai — mil kar
−16 dB se oopar nahi jaata. Koi cue −16 dB se oopar nahi hai. Foley baayein (−0.2 … −0.35),
door/chaude cheezein daayein (+0.4 … +0.5), beds, score aur naam 0.0 par — voice beech mein
khuli rehti hai.

## Score — sirf ek swell

Ek hi layer: `tanpura` (`ep03/sfx/raw_fs/tanpura.mp3`), −23 dB, pan 0.0.

- **Andar:** `छह सौ साल पहले` par (Khusrau wali line ka pehla aadha) — 2.6 s ka fade in.
- **Choti:** `एक शब्द भी बदले बिना` par (chhah sau saal → aaj tak, ek shabd nahi badla).
- **Bahar:** `बिल्कुल वही` par — barsaat ke saath, ek saans mein. Host intro `नमस्कार` se pehle
  poora out (score aur dono bed teenon `बिल्कुल वही` par hi khatam ho jaate hain, uske baad kuch
  nahi), yaani us rule se kaafi pehle ki koi cheez intro ko na chhue.
- Swell sirf ek baar hai: entry, ek crest `एक शब्द भी बदले बिना`, aur ek exit. Beech mein koi
  doosra surge nahi. Points JSON mein `[[0,-60],[2.6,-4],[crest-3,-1],[crest,-1.5],…,-60]]` hain.

## Duck — sirf ek baar

`name_duck`: phrase `नाम अमीर खुसरो`, `pre` 1.2 s, `post` 2.4 s, `gain` 0.30. Ye episode ka
naam-wala moment hai — Khusrau ka naam akela khada hota hai, baaki sab (beds, score aur khud
`name` cue) 0.30 par jhuk jaate hain. Poore cold open mein doosra duck nahi.

Aakhir ka sawal ("Raja badalte rahe…") duck se **nahi** sheeshe par rakha gaya — wo bilkul nange
mein padta hai (neeche dekhiye).

## Kahan chup rehna hai (silence > sound)

1. **Ped par kuch nahi.** `गांव के बाहर … पीपल पर भी एक` par sirf do beds hain, koi spot cue nahi —
   jagah khud ko sunaayi de, awaaz se nahi.
2. **Naam se pehle ki khamoshi.** `बोल इतने पुराने हैं … पर धुन आज की है` par kuch nahi. Gaana
   khatam, saaz ruk gaya — aur phir naam aata hai. Duck window isi gali se khulti hai.
3. **Aakhri sawal nange mein.** `आज का सवाल यही है` aur `राजा बदलते रहे…` par **koi cue, koi bed,
   koi score** nahi. Barsaat `बिल्कुल वही` par ek dum kat jaati hai (script ka [SFX] nirdesh),
   village bed 0.35 s baad dam todta hai — aur phir sirf awaaz. Yahi is cold open ka sabse bada
   design faisla hai: barsaat ke baad ka sannata accent hai, kami nahi.
4. **`dead_air.before_body_seconds`: 1.2 s** — host ident ke ant aur body ke pehle shabd
   (`उन्नीस सौ चवालीस`) ke beech. Host intro aur uske baad ka poora hissa dry hai: is episode mein
   cold open ke baad koi SFX nahi (script ke Episode info mein bhi yahi likha hai).

## Sound list (exact paths jo use hue)

```
synth:rain                     (bed + pehli barsaat)
synth:sand_trickle             (sookhi mitti par boondein)
synth:gust                     (thandi hawa)
synth:low_tone                 (badalte sultanon ka sur)
ep03/sfx/raw_fs/b1_village.mp3 (gaon ka bed)
ep02/sfx/raw_fs/wicker.mp3     (jhoole ki rassi — chaar cues)
ep03/sfx/raw_fs/crowd.mp3      (door ladkiyon ka gaana)
ep03/sfx/raw_fs/sarangi.mp3    (Amir Khusrau)
ep01/sfx/raw_fs/s9_writing.mp3 (Nehru ki kalam)
ep03/sfx/raw_fs/steps.mp3      (door ke kadam)
ep03/sfx/raw_fs/tanpura.mp3    (score)
```

Naya kuch download nahi hua — poora pool repo ke andar ka hai. Kuch bhi repo ke is pool se bahar
nahi hai.

## Jokhim (imaandari se)

- **Phrase spelling.** `ep06_2/c01.txt` abhi bana hi nahi, isliye Devanagari anchors repo ke
  apne transliterator (`tools/audio/transliterate.py`) se banaye gaye hain. Mixer matra aur
  anusvara hata kar sirf vyanjan se milaan karta hai, isliye `गई/गयी`, `गाँव/गांव`, `बूँद/बूंद`
  jaise antar se koi farq nahi padta. Jis din c01 banega, ek hi cheez dekhni hai: har phrase
  ka **ek hi baar** hona (aaj ke text par 18/18 phrase ek hi baar aate hain).
- **Aakhri sawal nange mein.** Yahan koi bed nahi, isliye agar take mein background noise ya
  kam room tone hai to ye ~6 s thoda `khaali` lagega. Agar QC mein wo khali lage, to ek hi
  minimal ilaaj hai: `village_bed` ka `end_offset` 0.35 se badha kar ~3.5 s karna (aakhir tak
  −26 dB par hi rehta hai) — lekin main aaj nahi maang raha, kyunki script khud "uske baad
  sannata" kehta hai.
- **`sultans` ka low tone** ek hi dhakke mein teen jumlon ke neeche chalta hai (5.5 s). Agar wo
  bhaari lage to sirf ek jumle par kar dena — par teen tabdeeliyan ek hi sur par hi asar deti hain,
  isliye plan mein ek hi rakha hai.
- **Estimated times** (±1–1.5 s). Anchors phrase par hain, isliye mix se pehle alignment chalane
  par sab apne-asli shabd par baithega; `fallback_at` sirf `--no-align` ke liye hai.

## Kya sunayi dega (4–6 lines)

1. Pehle sirf barsaat — pehli barsaat ka ek bada dhamaka, aur uske neeche gaon ki goonj.
2. Sookhi mitti par boondein girti hain, thandi hawa ka jhonka aata hai, aur ped pichhe chala jaata hai.
3. Do rassi ke jhoole chik-chik karte hain — oopar, neeche — aur door kuch ladkiyan gaati hain; shabd samajh nahi aate.
4. Beech mein saaz chup ho jaata hai, aur "Amir Khusrau" naam akela girta hai — ek kamand, ek naam.
5. Kalam chalti hai, door kadam aate hain, aur badalte sultanon ke neeche ek bhara hua neecha sur bajta rehta hai.
6. Aakhir mein barsaat ek dum ruk jaati hai. Aakhri sawal poore sannate mein padta hai. Uske baad, host ke naam se lekar episode ke ant tak, awaaz saaf — koi SFX nahi.
