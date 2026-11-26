# EP09 sources — Phone seized: the hash value that proves nothing changed

Every legal section, technical claim and number in the reel and caption, with the pages opened (26 Nov 2026, evening build).

## Law

**Bharatiya Sakshya Adhiniyam, 2023 — Section 63(4) and the Schedule certificate** (law card; caption)
- Bare Act, The Schedule [See section 63(4)(c)], AdvocateKhoj:
  https://www.advocatekhoj.com/library/bareacts/bharatiyaaakshya2023/b.php — opened. Part A (to be filled by the Party) and
  Part B (to be filled by the Expert) both identify the device: "Make & Model", "Color", "Serial Number",
  "IMEI/UIN/UID/MAC/Cloud ID" (as applicable), and both state: "I state that the HASH value/s of the electronic/digital record/s
  is ____, obtained through the following algorithm:-" SHA1 / SHA256 / MD5 / Other, "(Hash report to be enclosed with the
  certificate)". Part B is signed with "Name, designation and signature".
  Supports: "the certificate names the device (make, model, IMEI) and records the hash value"; "Part B: signed by an expert".
- K&S Partners note on Section 63 (4 Jan 2025, updated 22 Oct 2026): https://ksandk.com/litigation/section-63-bharatiya-sakshya-adhiniyam-2023/
  — opened; paraphrases s.63(4): certificate "signed by the person in charge of the computer and an expert".
  (The s.63 bare-Act page itself, advocatekhoj …/63.php, did not load; the claim rests on the Schedule text and the SC ruling below.)

**Supreme Court — Pune Bar Association v. Union of India, W.P.(C) No. 599 of 2026, order of 22 May 2026** (CJI Surya Kant,
Joymalya Bagchi J., Vipul M. Pancholi J.) (on-screen source line; caption)
- LiveLaw, 28 May 2026, 2026 LiveLaw (SC) 551: https://www.livelaw.in/top-stories/supreme-court-rejects-challenge-to-s634-bsa-mandating-hash-value-disclosure-for-electronic-evidence-535950
  — opened (paywalled after the lead). Quotes the Court: "Hash value of an electronic data is synonymous with an electronic
  fingerprint and provides a sure way of identifying and verifying digital data"; s.63(4) read with the Schedule has a
  "clear and rational nexus with the object of the law"; Part B gives "an additional layer of authenticity".
- Verdictum, 28 May 2026: https://www.verdictum.in/supreme-court/qualification-section-39-bsa-not-restricted-section-79a-it-act-examiners-forensics-sign-part-b-certificate-1614860
  — opened, full text. Same holding; besides s.79A IT Act examiners, a person with "special skill and expertise in computer
  science and cyber forensics" may sign Part B if the Court is satisfied "on the basis of unimpeachable material".
- SCC Online (SCC Times), 8 Jul 2026, 2026 SCC OnLine SC 1297: https://www.scconline.com/blog/post/2026/07/08/sc-upholds-admissibility-of-electronic-evidence-under-section-63-4-bsa/
  — opened (partly). Headline: "Hash value is an electronic fingerprint; Section 63(4) BSA certificate requirement is valid".
  Supports the on-screen line "Supreme Court, 22 May 2026: hash value = an 'electronic fingerprint'". The Court's words are quoted
  only as "electronic fingerprint".

**Bharatiya Nagarik Suraksha Sanhita, 2023 — Section 105** (caption only; on screen only as "seizure recorded on video")
- LiveLaw article by Justice Narayana Pisharadi (former Kerala HC judge), 19 Jan 2025, reproducing s.105:
  https://livelaw.in/articles/recording-of-search-and-seizure-electronic-mode-section-105-bnss-281366 — opened. The search or
  taking of possession, including the preparation of the list of seized things and its signing by witnesses, shall be recorded
  through audio-video electronic means, "preferably mobile phone"; the recording is forwarded without delay to the District
  Magistrate, SDM or Judicial Magistrate First Class.
- Nyaaya, 24 Jan 2025: https://nyaaya.org/nyaaya-weekly/electronic-recording-of-search-and-seizure-processes-is-mandatory-now/
  — opened. Same reading (recording "preferably a cell phone", list signed by witnesses, forwarded to the Magistrate).
- Allahabad HC (Lucknow), Naseeb Ahmad v. State of U.P., LiveLaw 24 Aug 2026:
  https://www.livelaw.in/high-court/allahabad-high-court/allahabad-high-court-police-non-compliance-section-105-bnss-videography-search-seizure-547230
  — opened; context only (the court noted the requirement was "practically not implemented" in UP). Not used on screen.
- Delhi Police BNSS handbook, Edition I, Jan 2024: https://training.delhipolice.gov.in/PDF/PublicData/NOTICE_20240614145643825.pdf
  — opened (index only): "105 (Fresh Addition) Recording of search and seizure through audio video electronic means".

## Technology

**Hash values (SHA-256): one change gives a different digest**
- NIST FIPS 180-4, Secure Hash Standard: https://csrc.nist.gov/files/pubs/fips/180-4/final/docs/fips180-4.pdf — opened.
  "The digests are used to detect whether messages have been changed since the digests were generated."; "it is computationally
  infeasible ... to find two different messages that produce the same message digest."; "Any change to a message will, with a
  very high probability, result in a different message digest." SHA-256 = 256-bit digest (Figure 1), shown as 64 hex characters.
- Own demonstration (run in this build, `sha256sum`, UTF-8, no newline) — the two hashes shown on screen are real:
  "Meet me at 7 PM." → b4a83b2b6afe7d41e0789d509bc1c8f05215dde03ae854d26ddd0b63fd3f1be5
  "Meet me at 8 PM." → 87b00585df24d8af972b99912058a17674accbe8b584921e58f60482cad2675d
  (one character changed; only 3 of 64 positions coincide).
- Bar & Bench (S.S. Rana & Co., 13 Aug 2024): https://www.barandbench.com/law-firms/view-point/tech-savvy-evidence-system-step-by-step-guide-hash-function-value-electronic-evidence
  — opened; hash value shows that data in electronic records "is safe and unaltered".

**Forensic copy of a phone; examination on the copy**
- NIST SP 800-101 Rev. 1, Guidelines on Mobile Device Forensics (May 2014):
  https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-101r1.pdf — opened (front matter and §1–2.3 verbatim; later
  sections in summary): acquired data is hashed with a cryptographic hash to maintain the integrity of an acquisition (§3.4), and
  the acquired image is then examined with forensic tools (§3.1, §5.3.3). The reel says only "the lab makes a full copy and
  takes its hash"; it does not claim a phone can always be copied without any change to the device.
- Legal Republic, "Police seized your phone or laptop — getting it back" (24 Aug 2026):
  https://www.legalrepublic.in/everyday-law/getting-seized-phone-back/ — opened; context: "a forensic mirror copy with a hash
  signature". Not quoted on screen.

**IMEI: dial *#06#** (the one-minute phone check)
- Samsung India FAQ: https://www.samsung.com/in/shop-faq/exchange-and-upgrade/how-do-i-find-my-imei-number-to-exchange-my-mobile-phone/
  — opened: "Dial *#06# on the phone ... to identify its IMEI number." (*#06# is the standard GSM code on Android and iPhone.)
- The Schedule (above) lists "IMEI/UIN/UID/MAC/Cloud ID" among the device fields — supports "the certificate names your phone by it".
- CEIR / Sanchar Saathi home page (https://ceir.sancharsaathi.gov.in/Home/index.jsp) opened; it doesn't mention *#06#, so it is not
  cited for that claim.

## News (hook context, review email; not on screen)
- The Guardian Chronicle, 26 Nov 2026 (16:56 IST): https://theguardianchronicle.com/jamtara-police-arrest-10-cyber-criminals-seize-16-phones-17-sims/
  — opened: Jamtara police seized 16 mobile phones, 17 SIM cards and a laptop in two raids (alleged fake customer-care racket).
  Accused are named in the report; not repeated anywhere. Allegations only.
- Kerala HC on BNSS s.94 and phones (LiveLaw, 24 Nov 2026) — opened; trend scan only (see trends.md).

## Dropped / not used
- "Phones can be copied without any change" — not supported for mobile devices; not claimed.
- Copy of the seizure list for the person searched (BNSS s.103) — not verified this run; left out of the checklist.
- Forensic-lab backlog numbers (ThePrint, Deccan Herald) — not opened; not used.
- Tandfonline article on mobile forensics under the BSA (2026) — page failed; not used.

Scenario: dramatised. The phone, the chat line, the masked IMEI (35XX XXXX XX4417) and the seizure scene are invented; no real
case, person, number or device. No police logo, uniform, emblem or official seal is drawn (plain tamper tape only).
