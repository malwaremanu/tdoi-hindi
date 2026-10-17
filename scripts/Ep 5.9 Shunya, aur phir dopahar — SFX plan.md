# Ep 5.9 — SFX plan (cold open)

Cold open = `## Cold open` .. "To chaliye." (**356 narration shabd**, chunk `c01`).
Drishya: Madras, ek daftar, dopahar — chhat par ek purana pankha, saamne ek khula
register, ek clerk jo ginti likhta hai, aur shaam ko uski apni diary. House style wahi
hai (Ep 4.1 ka schema): narration anchor hai, har bed uske neeche, host intro saaf, aur
aakhri cut intro se pehle dead-air pocket chhodta hai.

**Is episode mein score bhi host intro se pehle khatam ho jaata hai.** Brief ka niyam:
ek hi swell, aur wo "नमस्कार" se 0.25 s pehle out. Isliye host intro aur uske teen sawal
bina kisi SFX/score ke bolenge (Ep 4.1 mein tanpura sawalon ke neeche chalta tha — yahan
jaan-boojh kar nahi, kyunki "koi cue host intro ko cross nahi karega").

**Anchor note.** Is episode ka `ep05_9/c01.txt` abhi maujood nahi hai, isliye niche ke
Devanagari anchors Roman script se khud transliterate kiye gaye hain (jaise baaki
episodes ka c01 Devanagari hota hai). Jab c01 ban jaaye to ek baar milaan kar lena. Do
baatein dhyan mein:
(a) koi bhi anchor aise shabd par khatam na ho jahan sentence-ending danda laga ho —
mixer ka `norm()` danda nahi hataata, isliye `है।` aur `है` ka match 0.7 se neeche gir
jaata hai (is plan mein sabhi phrases jaan-boojh kar is tarah chune gaye hain);
(b) `गणित-शास्त्री` jaisa hyphenated shabd kisi anchor mein nahi hai, kyunki hyphen ke
dono taraf ke shabd mixer mein ek hi token ban jaate hain.
Neeche ke sabhi phrases 2–6 shabd ke hain aur cold open mein **ek hi baar** aate hain —
mixer ke apne `norm()` + fuzzy (ratio ≥ 0.7) log se check kiya gaya, har phrase ka sirf
ek hit hai.

## Cast (source files)

| id | file | what it is |
|---|---|---|
| ROOM | `ep01/sfx/raw_fs/b1_bed.mp3` | sookhi, garam daftar ki hawa (bed) |
| FAN | `ep03/sfx/raw_fs/wind.mp3` (lowpass) | chhat ke pankhe ki dheemi hawa (bed) |
| TANPURA | `ep03/sfx/raw_fs/tanpura.mp3` | ek hi swell — verdict line se intro tak |
| WICKER | `ep02/sfx/raw_fs/wicker.mp3` | pankhe ki dheemi chataq |
| ENGINE | `ep02/sfx/raw_fs/engine.mp3` | neeche kisi machine ki halki kharkhadahat |
| WRITING | `ep01/sfx/raw_fs/s9_writing.mp3` | register par ankhon ki sar-sarahat |
| CUP | `ep05/sfx/raw_fs/cup.mp3` | register band hone ki thap, aur lakdi ke dabbe ki thap |
| PAPER | `ep01/sfx/raw_fs/s8_paper.mp3` | diary jeb se nikalna, lifafa |
| PEN | `ep01/sfx/raw_fs/s8b_pen.mp3` | raat ki diary, ruk-ruk kar likhna |
| CROW | `ep01/sfx/raw_fs/s5_crow.mp3` | agli subah, door ek kauwa |
| synth | `synth:low_tone` | door duniya ka halka, neecha sura (cue) |

Pool mein alag "pankha" recording nahi hai, isliye pankha do cheezon se banta hai: dheemi
hawa (lowpass kiya hua wind) + WICKER ki chataq. Yahi ek jagah hai jahan plan pool ke
bahar kuch maangta hai — aur wo bhi nahi maangta, sirf jodta hai.

## Cue table

Anchors phrase-locked hain (Devanagari), time sirf `fallback_at` hai. `offset` ka matlab:
phrase ke **aakhri shabd** ke baad se ginti (minus = cue pehle shuru hota hai).

| # | cue | kahan land karta hai | sound | phrase (Devanagari) | level | pan | envelope |
|---|---|---|---|---|---|---|---|
| A1 | bed ROOM | "Madras. Ek daftar. Dopahar." se intro tak | `ep01/sfx/raw_fs/b1_bed.mp3` | — (start 0.0) | -23 dB | 0.0 | in 2 s, "नमस्कार" se 0.25 s pehle out |
| A2 | bed FAN | poora open (pankha chhat par) | `ep03/sfx/raw_fs/wind.mp3` (lowpass) | — (start 0.0) | -26 dB | 0.0 | in 3 s, intro se pehle out |
| S1 | pankhe ki chataq | "Madras. Ek daftar. Dopahar." | `ep02/sfx/raw_fs/wicker.mp3` | एक दफ़्तर दोपहर | -22 dB | 0.2 (upar-right) | 0.9 s, out 0.35 s |
| S2 | klark ki sar-sarahat | "Register ke panno par ank chalte jaate hain" | `ep01/sfx/raw_fs/s9_writing.mp3` | रजिस्टर के पन्नों पर अंक | -20 dB | -0.25 | 2.6 s, in 0.3 / out 0.5 |
| S3 | machine (neeche) | "jaise koi lamba silsila, jiska koi ant nahi" | `ep02/sfx/raw_fs/engine.mp3` (lowpass) | जिसका कोई अंत | -24 dB | 0.4 (door) | 3.0 s, in 0.8 / out 1.2 |
| S4 | register band | "Shaam ko register band ho jaata hai." | `ep05/sfx/raw_fs/cup.mp3` (lowpass) | शाम को रजिस्टर बंद | -18 dB | -0.15 | 0.9 s, out 0.25 s |
| S5 | diary jeb se | "apni jeb se ek chhoti si diary nikalta hai" | `ep01/sfx/raw_fs/s8_paper.mp3` | जेब से एक छोटी सी डायरी | -22 dB | -0.35 | 0.8 s, out 0.2 s |
| S6 | raat ki diary | "Wo unhe raat bhar likhta rehta hai." | `ep01/sfx/raw_fs/s8b_pen.mp3` | उन्हें रात भर लिखता | -21 dB | -0.3 | 1.4 s, in 0.05 / out 0.35 |
| S7 | door ek kauwa | "Aur agli subah kuch panno ko..." | `ep01/sfx/raw_fs/s5_crow.mp3` | और अगली सुबह | -24 dB | 0.55 (door, right) | 1.1 s, out 0.3 s |
| S8 | duniya ka neecha sura | "jinpar us waqt duniya ke sabse bade ganit-shastri kaam kar rahe the" | `synth:low_tone` | उस वक़्त दुनिया के | -26 dB | 0.4 (door) | 4.0 s, in 1.4 / out 1.8 |
| S9 | lifafa | "ek clerk apni diary mein akele likh raha tha." ke ant par | `ep01/sfx/raw_fs/s8_paper.mp3` | अकेले लिख रहा | -19 dB | 0.2 | 0.9 s, out 0.2 s |
| S10 | lakdi ka dabba | lifafe ke turant baad, intro se pehle | `ep05/sfx/raw_fs/cup.mp3` (lowpass) | अकेले लिख रहा | -20 dB | 0.25 | 0.7 s, out 0.2 s |

**10 spot cues, dher saare narration ke neeche.** Duniya ki loudest cheez S4 ka
register-band hona (-18 dB) hai; usse oopar kuch nahi jaata. S8 ka sura jaan-boojh kar
score-wale window (-26) par hai, kyunki wo score nahi, ek door ki duniya ka nishaan hai.
S9/S10 usi phrase ("अकेले लिख रहा") par hain — ek hi drishya, do awaazein (lifafa girta
hai, dabba leta hai), jaise Ep 6 ka book-set-down cue cup + paper se bana tha.

## Score — ek hi swell

`ep03/sfx/raw_fs/tanpura.mp3`, highpass 70 / lowpass 6000, pan 0.0. Ye **ek hi** gesture
hai: veredict line ("Ek taraf wo nishaan...") ke aakhri shabd ke baad -26 dB par aata hai,
"lifafa dabbe mein girta hai" wale beat par +4 dB (yaani -22 dB) par peak karta hai, aur
"नमस्कार" se 0.25 s pehle -60 par chala jaata hai. Koi doosra instrument nahi, koi melody
nahi, koi reverb nahi. Score ka koi hissa host intro ke neeche nahi rehta.

| score ka beat | kab | level | kya hota hai |
|---|---|---|---|
| entry | "एक तरफ़ वो निशान" ke baad (-26 par in, 1.2 s) | -26 dB | tanpura chupchap bichhta hai — wo cheez jo ghar chhod chuki thi, wapas kamre mein |
| hold | "दुनिया भर का हिसाब बदल चुका था। दूसरी तरफ़, उसके पैदा होने की जगह पर" | -26 dB | neeche, kuch nahi kar raha |
| **swell** | "एक clerk apni diary mein akele likh raha tha" + lifafa/dabba (S9/S10) | **-22 dB** | ek hi baar +4 dB: warm-up nahi, riser nahi, bas uthna |
| out | "नमस्कार" se 0.25 s pehle | -60 dB | host intro se pehle bilkul khatam |

**Envelope note (zaroori).** Score/bed ke `points` **layer ke start se** gine jaate hain
(layer-local), absolute seconds nahi — poori list `[[0,-60],…]` se shuru hoti hai. Ye isliye
zaroori hai ki mixer `np.interp` se envelope banata hai: agar pehla point layer ke shuru
se bahut aage ho, to poora layer chup (`-60`) bajta hai. Final `points` ka aakhri point
jaan-boojh kar `end` se ~1 s pehle -60 par rakha gaya hai, taaki take thoda chhota/lamba
hone par bhi cue ek jhatke par (click par) khatam na ho. **QC mein ek baar check karna:**
score "नमस्कार" se pehle poora khatam hai, aur uske peak ka waqt lifafe/dabbe wale beat
par hai; agar `c01` ka wahan ka window 10 s se chhota hai to peak/fade ko 1 s pehle kheench lena.

## Kahan chup rehna hai

1. **"Pata England ka." (line 61)** — teen shabd, koi cue nahi, koi swell nahi, koi
   "whoosh" nahi. Sirf daftar ki hawa. Yahi is cold open ka pehla sannata hai: pata
   England ka hai, aur us par kuch nahi bajta.
2. **"Uska kaam hai ginti likhna."** — bed ke alawa kuch nahi. Machine aur kalam dono
   apni-apni line par aate hain, is par nahi.
3. **"Umar kam. Kapde sadhe hue. Aankhon mein wo thakan, jo neend se nahi jaati."** —
   thakan par koi awaaz nahi. Yahan pehla beat hai jo sirf hawa par chalta hai.
4. **Shunya ka moment** — "गिनती का वो निशान, जो देखने में कुछ भी नहीं लगता" par beds
   duck ho jaate hain (`duck`, 0.30 gain, pre 1.4 / post 2.2). Ek line jo dekhne mein kuch
   bhi nahi lagti, uske neeche kuch bhi nahi hona chahiye.
5. **Intro se pehle ka pocket** — S10 ke baad aur "नमस्कार" ke beech kuch nahi; beds aur
   score dono out. Host intro aur uske teen sawal bilkul saaf (jaan-boojh kar: is episode
   mein sawalon ke neeche tanpura nahi hai).
6. **"तो चलिए।" ke baad** — 1.2 s poora sannata, phir body ka pehla shabd.

## Sound list (exact paths)

| file | kahan |
|---|---|
| `ep01/sfx/raw_fs/b1_bed.mp3` | bed ROOM, 0.0 → "नमस्कार" -0.25 |
| `ep03/sfx/raw_fs/wind.mp3` | bed FAN (lowpass=520), 0.0 → "नमस्कार" -0.25 |
| `ep02/sfx/raw_fs/wicker.mp3` | S1 pankhe ki chataq |
| `ep01/sfx/raw_fs/s9_writing.mp3` | S2 register par likhna |
| `ep02/sfx/raw_fs/engine.mp3` | S3 machine (lowpass=1500) |
| `ep05/sfx/raw_fs/cup.mp3` | S4 register band (lowpass=2200) + S10 dabba (lowpass=1800) |
| `ep01/sfx/raw_fs/s8_paper.mp3` | S5 diary/paper + S9 lifafa |
| `ep01/sfx/raw_fs/s8b_pen.mp3` | S6 raat ki diary |
| `ep01/sfx/raw_fs/s5_crow.mp3` | S7 door ka kauwa |
| `synth:low_tone` | S8 door duniya ka sura (mix script mein banta hai) |
| `ep03/sfx/raw_fs/tanpura.mp3` | score (ek hi swell) |

Sab kuch repo pool se hai; koi download nahi. Reference ke liye backup: agar S3 ka
`engine.mp3` (lowpass ke baad bhi) gaadi jaisa lage, to usi jagah `ep02/sfx/raw_fs/drone.mp3`
`filter: "highpass=45,lowpass=800"` ke saath use karna — ek hi cue, ek hi level.

## Kya sunayi dega

1. शुरू में एक थकी हुई, गरम दफ़्तर की हवा और ऊपर पुराने पंखे की धीमी चरमराहट — बस इतना, कोई संगीत नहीं।
2. रजिस्टर पर कलम चलने की हल्की सरसराहट, नीचे से किसी मशीन की थप-थप, और शाम को रजिस्टर बंद होने की एक दबी हुई थाप।
3. जेब से डायरी निकलने की फुसफुस, फिर रात भर रुक-रुक कर लिखने की आवाज़, और अगली सुबह दूर एक कौवे की आवाज़।
4. "उस वक़्त दुनिया के सबसे बड़े गणित-शास्त्री काम कर रहे थे" पर दूर एक भारी, नीची गूँज आएगी — मानो बाहर दुनिया चल रही हो।
5. "गिनती का वो निशान, जो देखने में कुछ भी नहीं लगता" पर बैकग्राउंड दब जाएगा, और "एक तरफ़ वो निशान…" पर धीमा तानपूरा नीचे बिछ जाएगा।
6. लिफ़ाफ़ा लकड़ी के डब्बे में गिरेगा, तानपूरा उसी वक़्त ऊपर उठेगा, और "नमस्कार" से ठीक पहले सब कुछ ख़त्म हो जाएगा — आशा के नमस्कार और तीन सवाल बिल्कुल साफ़।
