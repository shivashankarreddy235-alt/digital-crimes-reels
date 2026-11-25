# Sources: EP07 "Can a WhatsApp call be traced? How investigators follow the IP trail" (FORENSICS FILE)

Rebuilt on 25 Nov 2026 (night) after the owner's email reply to the first EP07 review: "Change the topic to something
interesting to cyber forensics". In the session the owner picked "Tracing a WhatsApp call" from four forensics options.
The earlier EP07 (Tech Decoded, UPI overlay malware) and its sources stay in git history (commit 991dc56) and go back to the topic bank.

Every page below was opened by this run (25 Nov 2026) unless marked otherwise. Quotes are short; the rest is paraphrase.
Explain, never enable: the reel explains what metadata a call leaves and how it is lawfully obtained and proved. It gives no
way to hide, no tools and no steps. All numbers, IPs, ports, SIMs and IMEIs on screen are masked and invented.

---

## The technology

- **A WhatsApp call is end-to-end encrypted: "No one outside of the chat, not even WhatsApp, can read, listen to, or share them."**
  VERIFIED. WhatsApp Help Center, "About end-to-end encryption": "End-to-end encryption keeps your personal messages and calls
  between you and the person you're communicating with." / "No one outside of the chat, not even WhatsApp, can read, listen to,
  or share them." Source: https://whatsapp.com/faq/general/28030015 (quoted on screen with attribution).
- **A normal call is logged as a CDR; internet sessions are logged as IPDR (IP Detail Records), which hold metadata, not content.**
  VERIFIED. Telangana Today, 21 Jul 2026 (Asif Yar Khan): CDR "records voice calls and SMS"; IPDR "captures metadata such as the IP
  address assigned to a device", servers accessed, session timings, ports used and data volume, and does not reveal contents;
  "Even if communication is encrypted, every internet session leaves behind a digital trail" (an official, quoted).
  Source: https://telanganatoday.com/how-ipdr-is-transforming-cybercrime-investigations-in-india
- **What an IPDR holds; many phones share one public IP behind NAT, so the port and the exact time tell them apart.** VERIFIED.
  DoT, Data Services Cell, letter No 8520-01/98-LR/Vol.(IX) Pt.I, 16 Nov 2021, "Revised IPDR format", in force 31 Mar 2022.
  Table (i) IPDR parameters: name of subscriber (photo ID and address proof kept separately), address, contact number,
  MSISDN, user ID, "Source IP address with Source Port", static/dynamic allocation, "Destination IP with destination port",
  IST start and end time (hh:mm:ss) and dates, "Source MAC Address/IMEI/Other device identification number", "IMSI and SIM type".
  Table (ii) NAT SYS LOG: start/end date and time, source IP, source port, translated IP, translated port, destination IP, destination port.
  Source: https://dotws.cdot.in/sites/default/files/Revised%20IPDR%20fromat%2016-11-21.pdf?download=1
  - Script: "Thousands of phones. One IP." The word "thousands" is the general CGNAT idea that the NAT log's translated-port field
    exists to solve; no figure is given on screen.
- **Operators must keep IPDR for at least two years (earlier one year).** VERIFIED. DoT, Access Services Wing, letter No. 20-271/2010
  AS-I (Vol.-III), 21 Dec 2021, amending the Unified Licence: clause 39.20 records "shall be archived for at least two years for
  scrutiny by the Licensor for security reasons" (was one year); Part II Chapter IX clause 7.1: "The Licensee shall maintain CDR/IPDR
  for Internet including Internet Telephony Service for a minimum period of two years." Clause 7.2 (log-in/log-out) also two years.
  Source: https://dot.gov.in/sites/default/files/21122021%20UL%20CDR%20two%20years.pdf?download=1
  Also: Communications Today, 24 Dec 2021, https://www.communicationstoday.co.in/dot-amends-ul-to-increase-storage-time-of-cdr-edr-ipdr/ ;
  Deccan Herald, https://www.deccanherald.com/india/govt-mandates-two-year-storage-period-for-all-calls-over-normal-networks-internet-1076199.html
  - Script avoids saying the licence obliges disclosure "to security agencies on request" (the letters say "scrutiny by the Licensor").
    Disclosure in the reel rests on BNSS s.94 and IT Rules r.3(1)(j), below.
- **WhatsApp collects IP addresses and shares information in response to legal process.** VERIFIED (WhatsApp's own policy).
  WhatsApp Privacy Policy (effective 4 Jan 2021), "Device And Connection Information": "...language and time zone, IP address,
  device operations information, and identifiers..."; "Law, Our Rights, And Protection": "We access, preserve, and share your
  information..." to "respond pursuant to applicable law or regulations, legal process, or government requests".
  Source: https://www.whatsapp.com/legal/privacy-policy/
  - Meta's law-enforcement guidelines (general, not WhatsApp-specific): for end-to-end encrypted chats Meta "will continue to provide
    message and call logs, as well as IP data"; content may need an MLAT request. Source: https://meta.com/safety/communities/law/guidelines/
  - WhatsApp's law-enforcement request portal exists ("Law Enforcement Online Requests"): https://www.whatsapp.com/records/
  - NOT VERIFIED and not claimed: that the app always logs the source port. The reel's "app's record" card marks the port column
    "*where the app logs it". WhatsApp's law-enforcement FAQ (faq.whatsapp.com/800085810452992) could not be fetched (robots).
- **Investigators join IPDR with CDR, subscriber details, device identifiers and tower data.** VERIFIED. Telangana Today, 21 Jul 2026:
  "Investigators match IPDR data with CDR, subscriber details, device identifiers, tower location data, Wi-Fi logs, open-source
  intelligence and CCTV footage"; ISPs share IPDR "only after lawful requests". (Same URL as above; credited on screen.)
  - The Wire, 10 Aug 2026, "Delhi Police prepare SOP for tracking internet activity of users through IPDR analysis" — only the
    headline and description loaded (IPDR "can be matched with call detail records (CDRs), customer application forms (KYC details),
    and mobile tower data"). Not used on screen. https://thewire.in/tech/delhi-police-prepare-sop-for-tracking-internet-activity-of-users-through-ipdr-analysis

## What changes next: SIM binding

- **DoT's SIM-binding direction: messaging apps must keep the account tied to the active SIM in the device; compliance deadline
  31 Dec 2026, operational from 1 Jan 2027.** VERIFIED (news reports; the DoT direction itself was not opened).
  - Business Standard, 23 Oct 2026: "January 1, 2027, is being cited as the operational start date, while December 31, 2026, is the
    stated compliance deadline"; an app's functionality "will stop if the registered SIM card is removed, replaced or deactivated";
    aim: "curb cross-border cyber fraud, phishing and digital arrest scams involving Indian mobile numbers".
    https://www.business-standard.com/industry/news/sim-binding-rules-whatsapp-telegram-to-require-active-sim-from-jan-2027-126102300121_1.html
  - Digit, 22 Oct 2026: requirements take effect from 1 Jan 2027; six-hour web logouts replaced by risk-based logouts.
    https://www.digit.in/news/general/whatsapp-telegram-and-other-apps-to-enforce-sim-binding-from-jan-1-2027-what-it-means.html
  - Inc42, 2 Apr 2026: deadline extended to 31 December; rules called the "Telecommunication Cybersecurity Amendment Rules, 2025".
    https://inc42.com/buzz/govt-extends-deadline-for-sim-binding-compliance-to-dec-31/
  - Outlook Business, 15 Dec 2025: directions issued 28 Nov (2025); accounts to "remain continuously linked to the active SIM".
    https://www.outlookbusiness.com/deeptech/tech/dot-mandates-sim-binding-6-hour-logout-for-whatsapp-telegram-to-combat-cyber-fraud
  - Script: "due to stay tied" / "बंधे रहना है" (not "already"), "DoT SIM-binding direction (Nov 2025, deadline extended)",
    "Aim, as reported". The six-hour logout is not mentioned (it has changed).

## The law

- **BNSS 2023, s.94(1)**: a Court by summons, or "any officer in charge of a police station ... by a written order, either in physical
  form or in electronic form", may require production of "any document, electronic communication, including communication devices,
  which is likely to contain digital evidence or other thing". VERIFIED. https://www.writinglaw.com/section-94-bnss/
  (latestlaws.com returned metadata only.) On screen: "A police officer's written order to produce electronic records and devices."
- **IT (Intermediary Guidelines and Digital Media Ethics Code) Rules 2021, rule 3(1)(j)**: the intermediary shall, "as soon as possible,
  but not later than seventy two hours ... of the receipt of an order, provide information under its control or possession, or
  assistance to the Government agency which is lawfully authorised for investigative or protective or cybersecurity activities";
  the order must be in writing stating the purpose. VERIFIED (consolidated text). https://future.indiankanoon.org/doc/45988656/
  On screen: "On a lawful order, the app shares information it holds within 72 hours."
- **BSA 2023, s.63(4)**: a certificate must be submitted with the electronic record, "signed by a person in charge of the computer or
  communication device or the management of the relevant activities (whichever is appropriate) and an expert", in the form in the
  Schedule. VERIFIED. https://www.advocatekhoj.com/library/bareacts/bharatiyaaakshya2023/63.php
  - Hash value in the Schedule certificate: LiveLaw, 28 May 2026, on Pune Bar Association v Union of India (SC, 22 May 2026; challenge
    to s.63(4) rejected; Part A of the Schedule includes the hash value, Part B is certified by an expert). VERIFIED (free part only).
    https://www.livelaw.in/top-stories/supreme-court-rejects-challenge-to-s634-bsa-mandating-hash-value-disclosure-for-electronic-evidence-535950
    The judgment itself is not mentioned on screen.
- **BNS 2023, s.308**: (1) whoever intentionally puts any person in fear of any injury ... and thereby dishonestly induces the person
  to deliver property commits extortion; (2) punishment: imprisonment "which may extend to seven years, or with fine, or with both".
  VERIFIED. https://www.writinglaw.com/bns-section-308/ (devgan.in failed to load.)
- **1930 / cybercrime.gov.in** (on screen: "Already paid? Call 1930 and your bank at once"; "Report at cybercrime.gov.in or to the
  police"). VERIFIED in earlier runs (PIB 7 Aug 2026; SEBI 17 Jul 2026 — see episodes/2026-11-25-pm/sources.md).

## Dropped or not used

- Reported cases: Deccan Herald, 28 Feb 2024 (Bengaluru: a WhatsApp video call led to a robbery suspect, but the trace came from the
  call recording and CEIR, not IP data) and The Tribune, 17 May 2026 (Delhi: a WhatsApp video-call sextortion case traced by
  "technical surveillance and financial tracking"; no IP detail; sextortion victims must never be identifiable). Neither shows the
  IPDR method, so neither is used. https://www.deccanherald.com/india/karnataka/bengaluru/how-a-whatsapp-video-call-led-the-police-to-trace-habitual-offender-2913144 ·
  https://www.tribuneindia.com/news/delhi/late-night-call-sparks-sextortion-police-arrest-bcom-graduate/amp
- Old law (IPC s.384, CrPC s.91, Evidence Act s.65B) is not on screen: not re-verified tonight.
- No VPN, proxy or "how to hide" content of any kind.
