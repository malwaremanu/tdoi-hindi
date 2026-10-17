# Ep 5.2 — SFX plan (cold open)

Cold open = `## Cold open` .. teen sawaal (316 narration shabd, chunk `c01`).
Scene: Allahabad, 1944. Ek bhara kamra. Iran se aaya ek mehmaan — cultural mission ka leader.
Wo apni baat kitaabon se nahi, ek kahani se shuru karta hai: do bhai, ek purab ek pashchim, aur ek
purani dhun jo dono gharon mein bachi rahi. Shape wahi hai jo Ep 3 / Ep 4.1 / Ep 5 ka hai:
narration anchor hai, har bed uske neeche, host intro dry, aur aakhri bed ka kat ek chhota sa
sannata chhod jaata hai. Sirf cold open par sound hai — `## Ab tak` se aage poora episode saaf.

## Cast (source files)

| id | file | what it is |
|---|---|---|
| ROOM | `ep01/sfx/raw_fs/b1_bed.mp3` | bhare kamre ki dheemi room tone (bed) |
| CROWD | `ep03/sfx/raw_fs/crowd.mp3` | baithi bheed ki halki gunj, kabhi samajh na aane wale shabd (bed) |
| WICKER | `ep02/sfx/raw_fs/wicker.mp3` | ek chhoti reed/wood ki cheekh — kursi gisatne ki aawaaz |
| DOOR | `ep03/sfx/raw_fs/door.mp3` | door se aayi hui ek halki darwaze ki aawaaz (mehmaan) |
| PAPER | `ep01/sfx/raw_fs/s8_paper.mp3` | pannon ki ek chhoti si chhap (kitaab) |
| STEPS | `ep03/sfx/raw_fs/steps.mp3` | floor par kadam |
| SARANGI | `ep03/sfx/raw_fs/sarangi.mp3` | ek bowed phrase — is episode ki "dhun" |
| SHRUTI | `ep03/sfx/raw_fs/shruti.mp3` | shruti-box ka sustain — score ka floor |

**Dhun ka instrument:** repo pool mein bansuri nahi hai, is liye "purani dhun" ka motif SARANGI ke
ek hi bowed phrase se bajta hai — sookha, purana, ek saans, koi melody nahi. Dhun teen baar bajti
hai (chhoti / poori hokar ruk jaati hai / aakhri baar sabse saaf) aur kabhi do baar ek saath nahi.

## Cue table (anchors phrase-locked hain; fallback second sirf safety net hain)

| # | id | cue (line) | sound | lands on the phrase | t (fallback) | level under voice | pan | fades |
|---|---|---|---|---|---|---|---|---|
| A1 | room | poori scene: "Allahabad. 1944." se "Kamra chup ho jaata hai." tak | ROOM | — (start 0.0; end `कमरा चुप हो जाता` +0.35 s) | 0.0 → 76.2 | -25 dB | centre (0.0) | in 2.5 s, hush par cut |
| A2 | crowd | "Ek kamra hai. Kamre mein log baithe hain." | CROWD | — (start 0.0; end `कमरा चुप हो जाता`) | 0.0 → 75.85 | -26 dB | centre (0.0) | in 2.5 s, out 2.6 s |
| B1 | chair | "Kuch kursiyon par, kuch zameen par." | WICKER | `कुछ कुर्सियों पर` | 5.35 | -22 dB | -0.25 | in 0.01 / out 0.15 |
| B2 | guest_door | "Wo mehmaan door se aaya hai. Iran se." | DOOR | `मेहमान दूर से आया` | 10.70 | -24 dB | +0.45 | in 0.15 / out 0.6 |
| B3 | book | "...apni baat kitabon se nahi shuru karta." | PAPER | `किताबों से नहीं शुरू करता` | 21.72 | -23 dB | -0.30 | in 0.01 / out 0.12 |
| C1 | tune1 | "Wo ek kahani se shuru karta hai." | SARANGI (3.0 s) | `एक कहानी से शुरू करता` | 23.72 | -24 dB | centre (0.0) | in 0.35 / out 0.9 |
| C2 | step_east | "Ek purab ki taraf chala gaya" | STEPS | `एक पूरब की तरफ चला गया` | 29.40 | -23 dB | -0.35 | in 0.02 / out 0.3 |
| C3 | step_west | "doosra pashchim ki taraf" | STEPS | `दूसरा पश्चिम की तरफ` | 30.73 | -23 dB | +0.45 | in 0.02 / out 0.35 |
| C4 | shruti | "Bas ek cheez dono gharon mein bachi rahi." → hush tak | SHRUTI (score) | `दोनों घरों में बची` | 44.77 → 75.85 | -25 dB, swell par -22 dB | centre (0.0) | in 3 s, ek swell, out |
| C5 | fragment | "Kuch tukde." | SARANGI (0.8 s cut) | `कुछ टुकड़े` | 47.78 | -24 dB | centre (0.0) | in 0.02 / out 0.25 |
| C6 | tune2 | "Aur phir ek din, sadiyon baad, wahi dhun kisi ne bajayi." | SARANGI | `वही धुन किसी ने बजाई` | 58.80 | -23 dB | centre (0.0) | in 0.2 / out 0.5, phir ruk |
| D1 | hush_duck | "Kamra chup ho jaata hai." | duck 0.30 | `कमरा चुप हो जाता` | 75.85 | — | — | pre 1.3 / post 2.2 |
| E1 | tune3 | hush ke 2.6 s baad, apne sannate mein | SARANGI | `कमरा चुप हो जाता` +2.6 s | 78.45 | -20 dB | centre (0.0) | in 0.4 / out 1.5 |
| F1 | questions | "Ek sawal wahin khada ho jaata hai… to rishta tootaa kaise?" | kuch nahi | — | — | — | — | dhun kareeb 83 s par ghul chuki hai |
| G1 | ident | "Namaskar, main hoon Asha…" | kuch nahi | — | — | — | — | host intro poora dry |
| H1 | body | `## Ab tak` se aage | dead air | — | — | — | — | 1.3 s sannata, phir pehla shabd |

9 spot cues, 2 beds, 1 score layer, 1 duck. Sabse oonchi cue `tune3` (-20 dB) hai — cap -16 se
4 dB neeche. Koi cue host intro ko cross nahi karta.

**Anchor note.** Har `phrase` cold open ke asli shabdon ki tarah Devanagari mein hai, aur us
transliteration se hai jo `c01` ke liye use hui. Har phrase cold open mein **ek hi baar** aati hai
(occurrence 1), aur poori phrase 2–6 shabd ki hai. Do cheezein dhyan mein rakhi gayi hain: (1)
phrase ka aakhri shabd kisi chhote dande-wale shabd par nahi rakha (mixer matra strip karta hai,
par `।` bacha rehta hai, is liye `है।` jaise 1-akshar shabd par match 0.7 se neeche chala jaata
hai); (2) `fallback_at` sirf us waqt kaam aata hai jab `align.json` na ho — asli time hamesha
alignment se aata hai, aur fallback ke seconds ~3 shabd/second ke andaaze par hain.

## Score (ek hi swell)

Ek hi score layer hai — SHRUTI ka sustain (koi melody nahi, koi dhol ya taal nahi, koi bansuri nahi).
- **Entry:** `दोनों घरों में बची` par, teesri baar ki dhun se pehle — "do gharon mein bachi hui
  ek cheez" hi score ka mauqa hai. 3 s mein -25 dB par aata hai (points 0 → 3 s).
- **Swell:** sirf ek, `एक दूसरे को पहचान लिया` par: +3 dB, yaani -25 → **-22 dB**, plateau ke saath
  (points mein 15.5 s se 20.5 s tak ka window — chhota timing error kuch nahi bigaadta).
- **Exit:** `कमरा चुप हो जाता` par score khatam — kamra chup hone ke saath drone bhi chala jaata
  hai. Ye "नमस्कार" se kareeb 11 s pehle hai, is liye host intro ke liye 0.25 s ki shart bahut
  pehle poori ho jaati hai.
- **Ye jaan-boojh kar nahi kiya:** dharmik ya "Iran-vs-Bharat" ka koi musical rang nahi (koi sitar,
  bansuri, santur, ney, daf nahi) — kyunki scene ek kamre ki yaad hai, do sanskritiyon ka mela
  nahi. Score narration ke saath nahi "gaata", bas neeche leta rehta hai.

## Kahan chup rehna hai (sannata sound se zyada zaroori hai)

1. **`कमरा चुप हो जाता` (D1).** Yahi is open ki verdict line hai — koi naam nahi girta, to duck
   isi par hai: room, crowd aur score teenon 0.30 par chale jaate hain, aur line chup kamre mein
   akeli khadi rehti hai. `pre` 1.3 s theek us line ke pehle shabd par shuru hota hai.
2. **Hush ke baad 2.3 second ka poora sannata.** Bed khatam, score khatam, tune3 abhi shuru nahi
   hui — in seconds mein kuch bhi nahi (duck window isi liye `post` 2.2 s hai). Tune3 isi sannate
   ke baad, apne waqt par aati hai.
3. **`सदियाँ गुज़रीं… कोई ख़त नहीं, कोई ख़बर नहीं` (kareeb 11 s).** Yahan koi cue nahi — sirf
   kamre ki tone. Kahani ka "bhool jaana" sound se nahi, sound ke ghatne se dikhta hai.
4. **`एक दूसरे को पहचान लिया` par koi foley nahi.** Recognition ke waqt sirf score ubharta hai;
   koi sting, koi whoosh, koi dhun nahi (tune2 `बजाई` par ruk chuki hai).
5. **Mehmaan ki Aakhri baat (`हम ईरान से अपनी पुरानी धुन बजाने आए हैं…`) poore 11.7 s khaali.**
   Sabse bhaari line par kuch bhi nahi — shabd khud kaam karte hain.
6. **Teen sawaal aur `नमस्कार`.** Tune3 kareeb 83 s par ghul chuki hai; aakhri sawaal
   (`तो रिश्ता टूटा कैसे?`) aur host intro bina kisi bed ke. Body se pehle 1.3 s ka sannata.

## Sound list (exact paths)

- Bed: `ep01/sfx/raw_fs/b1_bed.mp3` (room tone) · `ep03/sfx/raw_fs/crowd.mp3` (bheed, kabhi
  samajh na aane wale shabd)
- Foley: `ep02/sfx/raw_fs/wicker.mp3` (kursi) · `ep03/sfx/raw_fs/door.mp3` (distant darwaza) ·
  `ep01/sfx/raw_fs/s8_paper.mp3` (panna) · `ep03/sfx/raw_fs/steps.mp3` (kadam, dono bhai)
- Dhun / score: `ep03/sfx/raw_fs/sarangi.mp3` (ek bowed phrase; teen baar, teen lambai —
  0.8 s / 3.1 s / 4.6 s) · `ep03/sfx/raw_fs/shruti.mp3` (score ka sustain)
- Koi synth cue nahi, koi download nahi, koi naya file nahi.

## Kya sunayi dega

1. Shuru mein bhare kamre ki dheemi room tone aur baithi hui bheed ki halki gunj; ek kursi ki
   halki cheekh, aur door se aayi darwaze ki ek halki aawaaz — mehmaan aaya hai.
2. Kitaab wali line par bas ek kaagaz ki chhoti si chhap hogi, aur usi ke baad pehli baar ek akeli
   purani dhun (ek hi saans, sarangi par) — kahani shuru.
3. Do bhai alag honge: ek ke kadam left, doosre ke right. Phir sabse pehle dhun ke tukde, aur ek
   dheema shruti ka sustain jo recognition wali line par sirf ek baar oopar uthta hai.
4. Uske baad doosri baar wahi dhun poori bajegi aur "bajayi" par ruk jaayegi; kamra chup hoga, aur
   do second se zyada ka poora sannata hoga.
5. Usi sannate ke baad dhun teesri aur aakhri baar bajegi — sabse saaf; phir sawaalon ke andar ghul
   jaayegi.
6. Teen sawaal aur "Namaskar" bilkul saaf honge (koi bed nahi), aur body se pehle 1.3 second ka
   sannata hoga.
