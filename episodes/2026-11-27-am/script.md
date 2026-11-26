# EP09 — Your phone is seized. Who proves nothing changed?

**Series:** FORENSICS FILE (blue badge) · **Primary audience:** law students and young advocates (second audience: anyone whose
phone could be seized in an investigation, and their families). Send line: "Send this to a law student."
Slot: 2026-11-27 am (7:00 AM IST, Fri) · on-screen text English · voice **Hindi** (AI voice: the ElevenLabs voice set in the owner's
account) · section numbers and *#06# written as English words so they are spoken in English (owner's EP03 rule).
Format: **35–45 s** (strategy doc, "Reach fixes", 25 Nov 2026). Frame 1 is the hook at full opacity with the voice from 0.1 s (no
fade from black); small corner chapter labels with a sting; one law card; other sections in the caption; the checklist holds for
the screenshot; the send line is spoken and shown in the outro (the last 3 s).
**One idea:** the hash value is the seized data's fingerprint — change one character and the whole hash changes — and the BSA
s.63(4) certificate must record it.
Why this topic today: phones are seized in almost every cyber case — Jamtara police seized 16 on 26 Nov alone — and since May 2026
the Supreme Court has backed the rule that the evidence certificate must carry the data's hash value, its "electronic fingerprint"
(see trends.md).
Scenario: **dramatised** — the phone, the evidence bag, the list of seized items, the chat line "Meet me at 7 PM." and the masked
IMEI (35XX XXXX XXX4417) are invented. No real case, person, device or number; no police logo, uniform, emblem or official seal
(plain tamper tape only). The two hashes on screen are real SHA-256 values of the two sample lines.
Explain, never enable: the reel explains what a hash is and why the certificate carries it. Nothing on defeating forensics or
hiding, wiping or deleting data.

Five-part spine: 01 THE SEIZURE (scene 2) · 02 HOW IT WORKS (3) · 03 THE PROOF (4) · 04 THE LAW (5) · 05 DO THIS NOW (6–7).
Forensics File weighting: part 3 (the proof) and part 2 get the most time.

| # | Scene | Default length | On screen | Voiceover (Hindi) |
| --- | --- | --- | --- | --- |
| 1 | hook | 4.2 s (voice from 0.1 s) | From frame 1, full opacity: "YOUR PHONE IS SEIZED." / "WHO PROVES NOTHING CHANGED?" (blue) · a phone drops into an evidence bag; REC chip; tape "SEALED · DO NOT OPEN" · DRAMATISED · "The answer is a 64-character code." (open loop) | Phone ज़ब्त हुआ — court कैसे जानेगा कि उसमें कुछ बदला नहीं? |
| 2 | seize (01 THE SEIZURE) | 4.6 s | "On video. Listed. Sealed." · camera viewfinder "REC 00:01:12" filming the bag + "LIST OF SEIZED ITEMS — 1. Mobile phone (sealed), IMEI 35XX XXXX XXX4417 — Witness 1 ✓ Witness 2 ✓" · arrow → FORENSIC LAB · captions SEIZURE ON VIDEO · WITNESSES SIGN THE LIST · SEALED → FORENSIC LAB | ज़ब्ती की video बनती है, phone सील होकर lab जाता है। |
| 3 | how (02 HOW IT WORKS) | 5.4 s | "The lab copies everything" · SEIZED PHONE → data stream → FORENSIC COPY (COPYING… → COPY DONE · 100%) → SHA-256 HASH OF THE COPY (64 characters, "Sample value") · fingerprint glyph "= the data's fingerprint" · captions FULL COPY · SHA-256 HASH · = FINGERPRINT | Lab पूरे data की copy बनाकर उसका hash निकालती है — data का fingerprint। |
| 4 | proof (03 THE PROOF) | 5.6 s | "Change one letter…" · "Meet me at 7 PM." → HASH · ORIGINAL b4a83b2b…3fd3f1be5 · "Meet me at 8 PM." (the 8 highlighted) → HASH · ONE LETTER CHANGED 87b00585…cad2675d (changed characters in red) · stamp NEW HASH · card LAB b4a8…1be5 / LATER b4a8…1be5 ✓ SAME HASH = SAME DATA · "Real SHA-256 values of the two lines" · captions ONE LETTER CHANGED · A WHOLE NEW HASH · SAME HASH = SAME DATA | एक अक्षर बदला, तो पूरा hash बदल जाता है। Hash वही, तो data वही। |
| 5 | law (04 THE LAW) | 6.0 s | law card BSA 2023 · SECTION 63(4) — "The certificate for electronic evidence" — "It names the device — make, model, IMEI — and records the hash value. Part B is signed by an expert." · card "ELECTRONIC FINGERPRINT" — "Supreme Court on the hash value, upholding s.63(4)" — Pune Bar Association v. Union of India, 22 May 2026 · "More sections in the caption" | Section sixty three के certificate में ये hash ज़रूरी है — Supreme Court ने इसे electronic fingerprint कहा। |
| 6 | check (05 DO THIS NOW) | 5.4 s | "Check your phone. Now." · mock dialer: *#06# typed → pop-up IMEI 35XX XXXX XXX4417 ("Sample · masked") · "The certificate names your phone by this number" · captions DIAL *#06# · = YOUR IMEI | अभी star hash zero six hash dial कीजिए — certificate आपके phone को इसी IMEI से पहचानता है। |
| 7 | act (screenshot card) | 6.3 s | SCREENSHOT THIS — RED FLAGS: The two hash values don't match · No hash value in the certificate · Seizure not recorded on video — DO THIS NOW: Note your IMEI: dial *#06# · Check the papers name your phone right · Ask a lawyer to compare the hashes · camera flash; holds ≥ 3 s | Hash न मिले, तो data पर सवाल उठता है। ये card save कीजिए। |
| 8 | outro | 3.0 s (voice from 0.1 s) | send line "Send this to a law student." · logo + wordmark · "Legal awareness only · Not legal advice" · "Laws cited: BSA 2023 (s.63(4) & Schedule) · BNSS 2023 (s.105)" | ये video किसी law student को भेजिए। |

Studio elements: series badge (FORENSICS FILE, EP09) · frame-1 hook at full opacity · dramatised cold open (evidence bag, REC chip,
DRAMATISED tag) · camera viewfinder + list of seized items with witness signatures · corner chapter labels with stings · copy →
SHA-256 diagram with a typed 64-character hash · side-by-side hash comparison (real values, changed characters in red) with a
NEW HASH stamp and a SAME HASH = SAME DATA match card · lawCard (one) · dataCard (the Supreme Court's words, with case and date) ·
mock dialer with the *#06# check · kineticCaptions in English · checklistCard (screenshot) with camera flash · send line in the
outro · 3-second outro with disclaimer and laws.

Covers (5 written, 3 rendered): A "YOUR PHONE IS SEIZED. / WHO PROVES NOTHING CHANGED?" (chosen; matches the first line) ·
B "YOUR SEIZED PHONE / GETS A FINGERPRINT." · C "SEIZED PHONE? / ONE CODE GUARDS THE TRUTH." · not rendered: "ONE CHANGED
LETTER. / A WHOLE NEW HASH." (not about "you"), "POLICE HAVE YOUR PHONE? / ITS FINGERPRINT TELLS ALL." (too dramatic).
Person: owner's cut-out black_suit_glasses.png (EP08 used black_suit_side).
