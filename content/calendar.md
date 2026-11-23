# Episode calendar

Two reels a day: slot `am` posts at 7:00 AM IST, slot `pm` at 8:00 PM IST; each reel's folder is
`episodes/<date>-<slot>/`. Every reel: on-screen text in English, 90–120 seconds. Voice: Hindi for
every episode (owner's instruction, 23 Nov 2026, until he says otherwise; replaces the English/Hindi alternation). Mix: technology explainers, forensics (how criminals get caught), and a
client topic (digital arrest or bank account freeze/release) every third episode. The law/fact column is
a starting point: every run verifies it before scripting (see CLAUDE.md). Keep the Status column current.

| EP | Date | Slot | Voice | Type | Topic | Hook (first 2 s) | Facts and law to verify | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 2026-11-23 | am | English | Forensics | How a mobile tower can catch a criminal | Your phone is never really alone. | Cell sectors, CDR, IMEI, tower dump; BNSS s.94; DoT 2-year CDR retention; BSA s.63 | posted |
| 02 | 2026-11-23 | pm | Hindi | Technology | How GPS knows exactly where you are | No signal? GPS still knows where you are. | Satellites, signal timing, trilateration; GPS vs NavIC; GPS vs tower location | posted |
| 03 | 2026-11-24 | am | Hindi | Client: digital arrest | Digital arrest: how the scam works and how callers are traced | "You are under digital arrest." | BNSS s.43; BNS s.204, 308, 318, 319, 336; IT Act s.66D; CDR/IPDR/mule-account trail | approved |
| 04 | 2026-11-24 | pm | Hindi | Technology | What an IMEI number is, and why changing it is a crime | Your phone has a fingerprint. 15 digits. | IMEI basics; CEIR / Sanchar Saathi blocking; Telecommunications Act 2023 (tampering with identifiers) — explain, never show how |  |
| 05 | 2026-11-25 | am | Hindi | Technology | How a SIM card connects you to the network | This tiny chip proves who you are. | IMSI, SIM authentication, why SIM swap is dangerous; IT Act s.66C |  |
| 06 | 2026-11-25 | pm | Hindi | Client: account freeze | Why an innocent person's bank account gets frozen | Your account is frozen. You did nothing wrong. | NCRP complaint, bank lien on disputed amount; BNSS s.106 (general explainer only) |  |
| 07 | 2026-11-26 | am | Hindi | Forensics | Tower dump: finding one phone among thousands | Thousands of phones. One criminal. | Tower dump data, time windows, cross-matching; BNSS s.94 |  |
| 08 | 2026-11-26 | pm | Hindi | Technology | How a walkie-talkie works without any tower | No SIM. No tower. Still talking. | Radio frequencies, push-to-talk, range; WPC licensing and licence-exempt band (verify) |  |
| 09 | 2026-11-27 | am | Hindi | Client: account freeze | Account frozen: the legal route to get it released | Frozen account? There is a legal way out. | Bank, investigating officer, Magistrate route under BNSS (verify sections); general process only |  |
| 10 | 2026-11-27 | pm | Hindi | Forensics | How police trace a WhatsApp or internet call | No phone number? Still traceable. | IPDR, IP address, platform data requests (BNSS s.94); DoT IPDR retention |  |
| 11 | 2026-11-28 | am | Hindi | Technology | What your IP address reveals (and what it doesn't) | Every click carries an address. | IP basics, ISP logs, VPN limits (no evasion tips); IPDR |  |
| 12 | 2026-11-28 | pm | Hindi | Client: account freeze | Mule accounts: why renting your account gets it frozen | "₹5,000 a month just for your account." | Money trail, lien, BNS abetment/conspiracy; PMLA exposure |  |
| 13 | 2026-11-29 | am | Hindi | Forensics | Phone seized: how forensic experts extract data | Your phone is in a sealed packet. | Extraction, hash values, chain of custody; BNSS s.105 video recording; BSA s.63 |  |
| 14 | 2026-11-29 | pm | Hindi | Technology | How UPI money moves in seconds, and where it can be stopped | ₹50,000 gone in 4 seconds. | UPI flow, layering across accounts; 1930, lien by banks |  |
| 15 | 2026-11-30 | am | Hindi | Client: digital arrest | Fake CBI notices and video "courtrooms" | A Supreme Court order on WhatsApp? Fake. | BNS s.336 forgery, s.204; SC suo motu directions on digital arrest scams |  |
| 16 | 2026-11-30 | pm | Hindi | Forensics | Deleted chats: can they be recovered? | You deleted it. Is it gone? | Storage basics, backups, forensic recovery limits; BSA s.63 |  |
| 17 | 2026-12-01 | am | Hindi | Technology | How end-to-end encryption works | Not even WhatsApp can read this message. | Encryption keys explained simply; what metadata still exists |  |
| 18 | 2026-12-01 | pm | Hindi | Client: account freeze | Account frozen without notice: your rights | No notice. No explanation. Account frozen. | Bank and police obligations; grievance routes (verify) |  |
| 19 | 2026-12-02 | am | Hindi | Forensics | Hash values: proving evidence wasn't changed | One changed pixel changes everything. | Hashing explained; BSA s.63 certificate; Arjun Panditrao Khotkar (2020) |  |
| 20 | 2026-12-02 | pm | Hindi | Technology | How fake caller IDs work, and how telecoms block them | That call showed a police number. It wasn't. | Caller-ID spoofing concept only; DoT/telecom blocking systems (verify); IT Act s.66D |  |
| 21 | 2026-12-03 | am | Hindi | Client: digital arrest | Already paid a scammer? The first-hour plan | You've just paid a scammer. Now act fast. | 1930, cybercrime.gov.in, bank lien process |  |
| 22 | 2026-12-03 | pm | Hindi | Forensics | Photo metadata: a photo can reveal where it was taken | This photo knows where you were. | EXIF data, GPS tags, forensic use; privacy tips |  |
| 23 | 2026-12-04 | am | Hindi | Technology | How CCTV and number-plate cameras track vehicles | Your car's number plate is being read. | ANPR basics, footage retention, BSA s.63 (verify) |  |
| 24 | 2026-12-04 | pm | Hindi | Client: account freeze | Got money from a stranger? Why your account may freeze | ₹10,000 from an unknown sender. Careful. | Disputed funds, lien, how to respond |  |
| 25 | 2026-12-05 | am | Hindi | Forensics | How a fake app steals OTPs, and how it's traced | One APK. All your OTPs. | Malicious apps concept (no how-to); IT Act s.43, 66, 66C; tracing via servers and payments |  |
| 26 | 2026-12-05 | pm | Hindi | Technology | How satellite phones work, and why they're restricted in India | No tower for 1,000 km. Still connected. | Satellite links; licensing restrictions in India (verify) |  |
| 27 | 2026-12-06 | am | Hindi | Client: digital arrest | Why "CBI on a video call" is always fake | Real police don't arrest on video calls. | BNSS s.43 arrest; notices and summons process (verify); BNS s.204 |  |
| 28 | 2026-12-06 | pm | Hindi | Forensics | Crypto isn't anonymous: tracing on the blockchain | Crypto is anonymous? Not really. | Public ledgers, exchange KYC, PMLA reporting (verify) |  |
| 29 | 2026-12-07 | am | Hindi | Technology | How mobile number porting and SIM replacement work | Someone just got a new SIM with your number. | Porting/SIM replacement safeguards (verify); SIM swap red flags |  |
| 30 | 2026-12-07 | pm | Hindi | Client: recap | Five rules against digital arrest and account freezes | Five rules. Every scam this month broke one. | Recap of the series |  |

Earlier pilot (46 s, old format): Digital arrest — skipped, replaced by EP03; kept in `episodes/pilot-2026-11-23/`. On 23 Nov EP01 was posted a day early, and from that evening the channel posts two reels a day.

## Topic bank (use in order when the calendar runs out; keep the 2 tech/forensics : 1 client rhythm)

- Technology: how 5G differs from 4G for location; how Wi-Fi location works; how OTPs are generated
- Forensics: voice-clone scam calls and how they're detected; CCTV + CDR together; email header tracing
- Client: Supreme Court's 2026 directions on digital arrest scams; account freeze after a UPI refund scam;
  what to tell your bank when your account is frozen
