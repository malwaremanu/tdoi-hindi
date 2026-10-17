# Ep 4.6 — SFX plan (cold open)

Cold open = `## Cold open` se host ident aur uske baad ke roadmap tak — **442 narration shabd**,
chunk `c01`. Sirf yahi scene scored hai: "Ab tak" se aage poora episode sookha (dry) rehta hai.

Anchors: `ep04_6/c01.txt` abhi maujood nahi, is liye saare phrase is episode ki script se
transliterate kiye gaye Devanagari shabd hain (wahi tool, `tools/audio/transliterate.py`), aur
har phrase cold open mein sirf ek baar aata hai. Ek hi phrase do jagah aata hai — `भर पत्ते` —
aur wahan `occurrence: 1` diya gaya hai, kyunki pehli jagah cold open ki image hai aur doosri
jagah host ident ka episode-naam ("मुट्ठी भर पत्ते, एक तलवार") hai.
JSON ke `fallback_at` sirf safety net hain (3.1 shabd/sekond se banaye gaye andaze); asli
landing align.json se hoti hai.

## Cast (source files)

| id | file | what it is |
|---|---|---|
| JHINGUR | `ep03/sfx/raw_fs/b1_village.mp3` | village bed ka oopri hissa — raat ke jhingur/keede (bed) |
| RAAT_HAWA | `ep02/sfx/raw_fs/air.mp3` | khaali aangan ki sookhi hawa (bed) |
| KOTHRI | `ep01/sfx/raw_fs/b1_bed.mp3` | room tone — kothri ka andar (bed) |
| KALAM | `ep01/sfx/raw_fs/s8b_pen.mp3` | kalam uthane ki chhoti khurak |
| LIKHNA | `ep01/sfx/raw_fs/s9_writing.mp3` | kaagaz par likhne ki sookhi khurak |
| DRONE | `ep02/sfx/raw_fs/drone.mp3` | dheema sust sur — "ajeeb sanyog" wala beat |
| PATT | `ep01/sfx/raw_fs/s4_brush.mp3` | sookhe patte ki sarsarahat (brush sweep se) |
| STAB | `ep01/sfx/raw_fs/s3_stab.mp3` | talwar ki ek tez tankar (hard impact, 523 Hz ki dhaatu) |
| TANPURA | `ep03/sfx/raw_fs/tanpura.mp3` | score — ek hi swell, naam ke beat par |
| synth | mix script mein banega | `low_tone` (door ki ghanti + sawal ka saans), `gust` (garmi ki hawa) |

Do jagah library mein seedha file nahi hai, is liye sabse kareeb ka rasta liya gaya:
raat ke jhingur = village bed ka high band (koi cricket file nahi hai), aur door ki mandir ki
ghanti = `synth:low_tone` (dheema, door se aayi ek tankar). Dono cue table mein saaf likhe hain.

## Cue table (id | cue | sound | lands on the phrase | level under the voice | pan | fades)

| # | cue (line) | sound | lands on (Devanagari phrase) | level | pan | fades |
|---|---|---|---|---|---|---|
| A1 | "Ahmadnagar ka qila. Raat. Aangan mein chaandni…" | JHINGUR bed | `start 0.0` → `नमस्कार` −0.25 s | −24 dB | centre | in 2.0 s (default envelope), out 1.2 s |
| A2 | same paragraph | RAAT_HAWA bed | `start 0.0` → `नमस्कार` −0.25 s | −27 dB | centre | in 2.0 s, out 1.2 s |
| A3 | "Ek kothri ki khidki se roshni aati hai" … "Bahar aangan khaali hai" | KOTHRI room tone | `कोठरी की खिड़की` → `बाहर आंगन खाली` | −25 dB | centre | in 2.0 s, out 1.2 s |
| B1 | "Wo kalam uthata hai." | KALAM | `वो कलम उठाता` (−0.1 s) | −24 dB | −0.25 (left) | in 0.03 s, out 0.30 s |
| B2 | "Sirf jhingur, aur door kisi mandir ki ghanti." | synth low_tone (2.8 s) | `दूर किसी मंदिर की घंटी` (−0.8 s) | −26 dB | +0.50 (right, door) | in 0.25 s, out 1.4 s |
| B3 | "Aaj Vaishakh ki poornima hai." | synth gust (3.2 s) | `वैशाख की पूर्णिमा` (+0.1 s) | −25 dB | +0.35 (wide, right) | in 0.8 s, out 1.2 s |
| C1 | "Nehru ke saamne ek ajeeb sangyog khada ho jaata hai" | DRONE (lowpass 900, 7 s) | `अजीब संयोग खड़ा` (−0.5 s) | −25 dB | centre | in 2.0 s, out 2.5 s |
| D1 | "Nehru likhna shuru karte hain." | LIKHNA (highpass 180, 2.6 s) | `लिखना शुरू` (−0.3 s) | −21 dB | −0.15 (left) | in 0.02 s, out 0.50 s |
| D2 | "…jise log Buddha kehte hain." | TANPURA — **score** | `जिसे लोग बुद्ध कहते हैं` (−1.5 s) | −24 dB (swell −22.5) | centre | in 2.5 s, out ~3 s (neeche "score") |
| E1 | "Ek haath mein mutthi bhar patte." | PATT (highpass 300, 1.6 s) | `भर पत्ते` (occ. 1) (−0.4 s) | −22 dB | −0.30 (left, haath) | in 0.05 s, out 0.50 s |
| E2 | "Doosre haath mein ek talwar." | STAB (highpass 120, 1.3 s) | `दूसरे हाथ में एक तलवार` (−0.15 s) | **−16 dB** (scene ka sabse ooncha) | −0.10 | in 0.005 s, out 0.60 s |
| E3 | "Asli jeet kya hai — talwar ki, ya apne aap ki?" | synth low_tone (1.8 s) | `असली जीत क्या है` (−0.9 s) | −25 dB | centre | in 0.4 s, out 1.0 s |
| F1 | "Namaskar, main hoon Asha…" | saare beds out | `नमस्कार` −0.25 s | — | — | hard out, host ident dry |
| G1 | "Aaj hum pehle ek samrajya ki kala dekhenge…" | koi cue nahi | — | — | — | ident + roadmap poori tarah sookhe |
| H1 | cold open → body | dead air | 1.4 s | — | — | chuppi, phir body ka pehla shabd |

Kul 8 spot cue + 3 bed + 1 score + 1 duck — brief ki ~12 cue ki hadd ke andar.

## Score (exactly one swell)

- Ek hi score: **TANPURA** (`ep03/sfx/raw_fs/tanpura.mp3`, `highpass=70,lowpass=6000`), −24 dB,
  centre. Andar aata hai naam se **1.5 s pehle** (`जिसे लोग बुद्ध कहते हैं`) — yaani wahi jagah
  jahan script ki apni SFX line kehti hai "'Buddha' par shuru, phir dheere ghulta hai".
- Envelope: 0 → −60, 2.5 s par −2, 6 s tak −2, 11 s par **+1.5 (swell)**, 13.5 s par −3,
  15 s par −60. Yaani sabse oonchi jagah −22.5 dB — score ki band ke andar.
- Score `लौट कर आएंगी` ("Ye dono baatein aaj ke aakhir mein laut kar aayengi") ke 1.0 s baad out
  ho jaata hai, yaani host ke "नमस्कार" se bahut pehle chup hai. Do baatein (khud ko jeetne wala
  vijeta / jeet nafrat ko janm deti hai) sirf isi tanpura par baithti hain — unke neeche koi
  doosra cue jaan-boojh kar nahi rakha, kyunki yahi pair Part 8 mein laut kar aata hai.

## Duck (sirf ek)

- `naam_duck` on `जिसे लोग बुद्ध कहते हैं` — `pre` 1.2 s, `post` 2.4 s, `gain` 0.30. Naam ka
  pal hi cold open ka faisla hai (wo aadmi kaun hai), aur poore cold open mein chuppi/duck
  sirf yahin lagti hai. Cold open mein koi doosra duck nahi.

## Kahan chup rehna hai (silence > sound)

- **Teen beats jaan-boojh kar cue-free hain:** (1) `ये गिनती आज की नहीं है…` aur uske baad
  teenon `इसी पूर्णिमा` wali lines (janm, gyaan, ant) — sirf do beds, koi spot cue nahi;
  (2) `लिखने से पहले रुक जाता है` — kalam ka cue wahin khatam ho jaata hai, aur
  "Kyunki usne aaj ka din gina hai" bilkul saaf baithta hai; (3) `एक दिन। एक चांद। जन्म, ज्ञान,
  और अंत।` — is line par kuch nahi, aur uske turant baad hi score shuru hota hai.
- **Host ident aur roadmap dry hain:** beds `नमस्कार` se 0.25 s pehle out; "Namaskar, main hoon
  Asha…" aur "Aaj hum pehle ek samrajya ki kala dekhenge…" par ek bhi cue nahi.
- **Cold open ke baad:** `dead_air.before_body_seconds` = **1.4 s** — poora sookha, phir body
  ("Ab tak") ka pehla shabd.

## Sound list (exact paths / recipes jo istemaal hue)

- Beds: `ep03/sfx/raw_fs/b1_village.mp3` · `ep02/sfx/raw_fs/air.mp3` · `ep01/sfx/raw_fs/b1_bed.mp3`
- Spot: `ep01/sfx/raw_fs/s8b_pen.mp3` · `ep01/sfx/raw_fs/s9_writing.mp3` ·
  `ep02/sfx/raw_fs/drone.mp3` · `ep01/sfx/raw_fs/s4_brush.mp3` · `ep01/sfx/raw_fs/s3_stab.mp3`
- Score: `ep03/sfx/raw_fs/tanpura.mp3`
- Synth recipes (mix script): `synth:low_tone` (door ki ghanti, sawal), `synth:gust` (garmi ki hawa)

## Niyam jo nibhaye gaye

- Voice dead centre; foley left (`−0.10 … −0.30`), door/wide cheezein right (`+0.35 … +0.50`),
  beds aur score `0.0`.
- Bed −21…−27, score −22…−26, spot −16…−26 (jitne bhi −25/−26 par hain wo dheeme/tone wale hain);
  scene ka sabse ooncha block ek hi cue hai — talwar ka −16 dB.
- Koi cue host intro ko cross nahi karta; beds `नमस्कार` −0.25 s par khatam.
- Beds ke liye `points` nahi diye: mixer khud phrase se resolve hui lambai par 2.0 s fade-in aur
  1.2 s fade-out banata hai (seconds guess karne se behtar).

## Kya sunayi dega

1. Shuruaat: raat ka khaali aangan — door jhingur, halki sookhi hawa, aur ek lambi chuppi.
2. Kothri ke andar room tone, kalam ki chhoti khurak, phir sab tham jaata hai — kyunki usne din gina hai.
3. Bahar lautte hi door ki mandir ki ghanti ek baar, garmi wali hawa, aur "ajeeb sanyog" par ek dheema sust sur.
4. "Buddha" naam par sab peeche hat jaata hai, aur tanpura ek hi baar ubharta hai — do baatein isi ke neeche.
5. Patte ki sarsarahat left se, aur talwar ki ek tez tankar — cold open ka sabse ooncha lamha.
6. "Namaskar…" se pehle sab chup; ident aur roadmap sookhe, phir 1.4 s ki chuppi aur body shuru.
