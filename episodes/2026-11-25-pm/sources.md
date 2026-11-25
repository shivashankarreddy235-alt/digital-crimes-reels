# Sources: EP06 "Boss Scam: when your MD's real WhatsApp asks for an urgent transfer" (CORPORATE CYBER BRIEF)

Every page below was opened by this run (25 Nov 2026) unless marked otherwise. Quotes are short; the rest is paraphrase.

---

## How the scam works

- **The "real WhatsApp" route: malware hijacks an active WhatsApp Web session; fraudsters then use the genuine account (or save their
  own number as "CEO").** VERIFIED (I4C via PIB; SEBI).
  - PIB (MHA / I4C), 7 Aug 2026, "I4C cautions corporates and finance professionals against 'Boss Scam'": a .zip named e.g.
    "Statement of Account.zip", "RBI.zip" or "MCA.zip" carries a .exe and a .dll; on a Windows PC a Trojan "hijacks the victim's
    active WhatsApp Web session"; fraudsters then use "the genuine WhatsApp account of a senior executive" or "covertly save an
    attacker-controlled number under the name of the 'CEO'" to order urgent transfers to mule accounts. Targets: CAs, company
    directors, CFOs, finance and accounts staff. Source: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2295889
  - SEBI PR No. 40/2026, 17 Jul 2026 (after I4C alerted SEBI): "The malware hacks the system and hijacks the active Web WhatsApp
    session tokens"; also deepfake voice/video and "false groups"; staff told not to share the transaction as it "may be Unpublished
    Price Sensitive Information". Source: https://www.sebi.gov.in/sebi_data/attachdocs/jul-2026/1784288188963.pdf
  - Business Standard, 23 Jun 2026 (the I4C advisory of 22 Jun 2026): "As seen in multiple cases, the CEO forwards the message to
    finance officer." Source: https://www.business-standard.com/india-news/boss-scam-ceo-impersonation-fraud-govt-advisory-i4c-126062300353_1.html
  - Business Today, 11 Aug 2026: the newer method removes the old check of "whether the message came from the CEO's usual number".
    Source: https://www.businesstoday.in/india/story/whatsapp-boss-scam-explained-received-a-fake-rbi-or-mca-file-heres-how-scammers-can-target-you-548542-2026-08-11
  - Script: concept only (fake notice → ZIP → malware on a Windows PC → logged-in session taken over). No file names beyond those
    the advisory itself publishes, no tool names, no steps. Explain, never enable.

- **I4C's response and numbers.** VERIFIED (PIB, 7 Aug 2026, above).
  - More than 58,000 potential victims alerted in the last 30 days by SMS (header "I4CMHA-G"); "more than 10,000" protected,
    including by geo-blocking command-and-control servers through the Sahyog Portal; indicators shared with CERT-In and antivirus
    vendors. On screen: "58,000+ alerted in 30 days · Source: I4C via PIB, 7 Aug 2026".

- **Safety steps (official).** VERIFIED.
  - PIB/I4C: verify urgent transfer or account-change requests "through a direct voice call or in-person confirmation"; do not open
    .zip or executables from unverified sources; regulators "never distribute software updates, security fixes or account
    statements through WhatsApp attachments"; check Linked Devices and log out unused WhatsApp Web sessions; report on 1930 or
    www.cybercrime.gov.in.
  - SEBI: "Do not transfer funds solely on the basis of instructions received on any social media platforms"; "cross-check
    requests … by calling their seniors"; "Log out any Web WhatsApp sessions that are not being actively used"; report on 1930
    or www.cybercrime.gov.in.
  - "Two people approve every big payment" (maker-checker / dual approval): general internal-control practice; quoted from experts
    (Quick Heal, Fortinet) in Business Standard, 23 Jun 2026 — not an I4C or SEBI instruction. Shown as advice, not attributed.

- **This week's peg: I4C (NCTAU) advisory on safe use of WhatsApp Web.** VERIFIED (news reports; the I4C PDF itself not opened).
  - Outlook India, 23 Nov 2026 ("an advisory dated November 18"): log out manually after every session; closing the tab is not
    logging out; avoid public/shared computers; avoid sensitive work on WhatsApp Web.
    Source: https://www.outlookindia.com/national/whatsapp-web-security-warning-i4c-account-misuse-safety-advisory
  - ETV Bharat, 23 Nov 2026: "Simply closing the browser window or WhatsApp Web tab should not be considered sufficient to
    terminate an authenticated session"; avoid government, organisational, financial or confidential information on WhatsApp Web.
    Source: https://www.etvbharat.com/en/technology/whatsaapp-web-security-threat-whatsapp-apk-fraud-i4cs-nctau-enn26112305521
  - Organiser, 24 Nov 2026 (embeds @MIB_India's X post of 23 Nov 2026): risks — reading messages, impersonation, fraud.
    Source: https://organiser.org/2026/11/24/428701/bharat/beware-of-whatsapp-web-misuse-i4c-warns-of-unauthorised-access-impersonation-and-online-fraud/
  - tmv.in, 24 Nov 2026 (links it to the Boss Scam): https://tmv.in/article/avoid-official-or-sensitive-work-on-whatsapp-india-issues-cyber-advisory-warns-of-account-misuse
  - On screen: "I4C advisory, Nov 2026 (reported 23 Nov)". Voice: "हाल ही में" (recently), not "this week".

## Reported cases (no names of people or companies on screen)

- **Mumbai firm: ₹10.4 crore, 63 transfers, 3–15 Jun 2026; a new number with the director's photo; "in a meeting".** VERIFIED.
  - Business Today, 18 Jun 2026: ₹10,40,71,924; 63 transfers between 3 and 15 June; "a WhatsApp message from an unknown number"
    that "used the executive director's photograph as the display picture"; the scammer was "attending an urgent meeting and would
    be unable to take calls"; discovered when the employee contacted the real director through official channels.
    Source: https://businesstoday.in/latest/trends/story/63-transactions-rs10-crore-gone-how-a-fake-whatsapp-message-fooled-a-company-537698-2026-06-18
  - ThePrint, 1 Jul 2026: a bank branch in Delhi alerted police to suspicious cash withdrawal attempts; Delhi Police arrested five;
    DCP: proceeds were routed, layered and withdrawn "through commission-based account holders".
    Source: https://theprint.in/india/a-whatsapp-message-from-your-ceo-rs-1-5-crore-gone-how-the-boss-scam-is-tricking-indian-executives/2973626/
  - On screen: "Reported: Business Today, 18 Jun 2026 · ThePrint, 1 Jul 2026" and "allegations — not yet proved in court".
    The company and the director are not named (the reports name them; this reel does not).

- **Ahmedabad firm: ₹1.5 crore in one transfer, after a fake "RBI" notice ZIP opened on WhatsApp Web; FIR under BNS 318(4), 319(2)
  and the IT Act.** VERIFIED (ThePrint, 1 Jul 2026, above).
  - The accountant opened a "3.3 MB ZIP file" (a notice claiming to be from the RBI) on WhatsApp Web on his desktop; the transfer
    request came from "an account that had my profile picture", with an instruction "not to call back"; the fraudster had read the
    owner–accountant chats. Case "under Bharatiya Nyaya Sanhita Sections 318(4) (cheating), 319(2) (cheating by personation) and
    under the IT Act" (IT Act sections not given). No arrest reported.

## The law

- **BNS 2023 s.319 — cheating by personation.** VERIFIED (bare text, two sources agree).
  - s.319(1): "A person is said to cheat by personation if he cheats by pretending to be some other person, or by knowingly
    substituting one person for another, or representing that he or any other person is a person other than he or such other
    person really is." Explanation: the offence is committed "whether the individual personated is a real or imaginary person."
  - s.319(2): "Whoever cheats by personation shall be punished with imprisonment of either description for a term which may extend
    to five years, or with fine, or with both."
  - Sources: https://devgan.in/bns/section/319/ · https://www.advocatekhoj.com/library/bareacts/bharatiyanyayasanhita/319.php
  - Old law: IPC s.419.

- **BNS 2023 s.318(4) — cheating and dishonestly inducing delivery of property: up to 7 years and fine.** VERIFIED by the EP04 run
  against India Code (https://www.indiacode.nic.in/bitstream/123456789/20062/1/a202345.pdf); not re-opened this run.
  Applied in the reported Ahmedabad FIR (ThePrint). Old law: IPC s.420.

- **IT Act 2000 s.66 read with s.43 — computer-related offences (e.g. introducing a virus, access without permission, done
  dishonestly or fraudulently): up to 3 years, or fine up to ₹5 lakh, or both.** VERIFIED (bare text).
  - s.43: "If any person without permission of the owner or any other person who is in charge of a computer, computer system or
    computer network, — (a) accesses or secures access to such computer …; (c) introduces or causes to be introduced any computer
    contaminant or computer virus into any computer, computer system or computer network; …"
  - s.66: "If any person, dishonestly or fraudulently, does any act referred to in section 43, he shall be punishable with
    imprisonment for a term which may extend to three years or with fine which may extend to five lakh rupees or with both."
  - Sources: https://prsindia.org/files/bills_acts/bills_parliament/2021/IT%20Act,%202000.pdf · https://lawgist.in/information-technology-act-2000/66
  - Script: "Planting malware / taking over an account without permission" → s.66 read with s.43. Not claimed as the section in any
    specific FIR.

- **IT Act 2000 s.66D — cheating by personation by means of a communication device or computer resource: up to 3 years and fine up
  to ₹1 lakh.** VERIFIED by the EP04 run (UNODC SHERLOC bare text); this run's re-open of SHERLOC timed out, and the PRS PDF's
  summary (opened this run) gives the same offence and punishment.
  - Wording (EP04 sources.md): "Whoever, by means of any communication device or computer resource cheats by personation, shall
    be punished with imprisonment of either description for a term which may extend to three years and shall also be liable to
    fine which may extend to one lakh rupees."

- **Not used:** IT Act s.66C (identity theft) — verbatim text not re-opened this run, and no source ties it to these cases.
  CERT-In's 6-hour reporting Directions (28 Apr 2022) — the Annexure I wording could not be checked, and EP10 covers it.

## Reporting

- **1930 / www.cybercrime.gov.in.** VERIFIED (PIB 7 Aug 2026 and SEBI 17 Jul 2026, above).
- "Golden hour": no official duration (see EP04 sources.md). Script says "immediately", not "within one hour".

## Dramatised scenario (invented)
- "Meera, 39, accounts head, Indore", the MD "Rajiv Sir", the ₹48,50,000 transfer, the masked account ••7730 and the chat are
  invented and illustrative, built from the pattern in the I4C/SEBI advisories and the reported cases. Not any client or case.
