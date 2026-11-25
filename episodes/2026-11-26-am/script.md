# EP07 — The invisible layer over your UPI app: how APK malware sees your PIN

**Series:** TECH DECODED (teal badge) · **Primary audience:** Android users who pay by UPI (second audience: their parents — the
closing line says "Send this to your parents").
Slot: 2026-11-26 am (7:00 AM IST) · on-screen text English · voice **Hindi** (AI voice: the ElevenLabs voice set in the owner's
account) · section numbers and 1930 written as English words so they are spoken in English (owner's EP03 rule).
Scenario: **dramatised** — "Sunita, 58, Nagpur", the gas-bill WhatsApp message, "Bill_Update.apk", the ₹500 payment to "Ramesh
Dairy" and the two ₹49,999 debits are invented and illustrative; all numbers, IDs and references are masked. No real bank, app,
gas company or person. Not any client or case. Built from the CERT-In alert (gas-bill / e-challan APKs), Cyble's "Ghost Overlay"
research and a reported Mumbai case.
Reported case on screen by city, outlet and date only (Mumbai Cyber Police — Free Press Journal, 26 Jun 2026); no names; "Allegations
— not yet proved in court" shown twice.
Why today: NPCI and UPI apps have asked Google to restrict the permissions overlay malware abuses (reported 17–22 Nov 2026) — see
trends.md.
Explain, never enable: the overlay, Accessibility misuse and SMS reading are shown as concepts. No malware names on screen beyond the
researchers' label "Ghost Overlay", no code, no servers, no steps.
Voiceover: 267 words (Hindi). Length: 114.4 s (scenes fitted to the voice).

Five-part spine: 01 THE SCAM (scenes 2–4) · 02 HOW IT WORKS (5–8) · 03 THE TRAIL (9–10) · 04 THE LAW (11) · 05 DO THIS NOW (12).
Tech Decoded weighting: part 2 carries the most time (about 37 s); part 1 about 26 s, part 3 about 15 s, part 4 about 12.5 s,
part 5 about 12.6 s. Chapter cards open scenes 2, 5, 9, 11 and 12 (wipe + sting).

| # | Scene | Length (voiced) | On screen | Voiceover (Hindi) |
| --- | --- | --- | --- | --- |
| 1 | hook | 5.8 s | "You typed your PIN" · "in the REAL app." (teal) · generic UPI PIN screen, dots filling as keys light up · a red dashed layer with an eye slides over it · stamp RECORDED · "Someone saw it." (red) · "The last step in this reel is the one that stops it." | PIN आपने असली UPI app में डाला। फिर भी किसी ने देख लिया। कैसे, और इसे कैसे रोकें? |
| 2 | scam (01 THE SCAM) | 10.3 s | DRAMATISED tag · "Sunita, 58, Nagpur · a fictional example" · mock WhatsApp from +91 9XXXX XXX41: "Dear customer, your gas connection will be disconnected TONIGHT. Bill not updated." / "Install the bill-update app below and pay ₹10 to avoid disconnection." / file Bill_Update.apk (3.2 MB · APK file) / "Ok, installing" · captions DISCONNECTED TONIGHT · PAY ONLY ₹10 · AN APK FILE | Sunita जी को WhatsApp: आज रात gas connection कटेगा। ये app install करके दस रुपये भरिए। साथ में एक APK file। |
| 3 | grant | 8.1 s | DRAMATISED tag · fake app "Bill Update": "To continue, allow:" Accessibility ("Bill Helper" service) toggle · Display over other apps ("Draw on top of any app") toggle · "Needed to update your bill." · two taps turn both on · stamp FULL ACCESS · captions ACCESSIBILITY: ON · DRAW OVER OTHER APPS: ON · TWO TAPS | App बोला: Accessibility on कीजिए, और दूसरे apps के ऊपर दिखने की permission दीजिए। बस दो taps। |
| 4 | paid | 7.2 s | NEXT MORNING · the real UPI app: "Paying Ramesh Dairy ₹500", PIN typed, success screen · then two bank notifications "₹49,999 debited — UPI to xxxxxx88@upi" / "xxxxxx17@upi" · stamp SHE NEVER SENT THESE · DRAMATISED · illustrative amounts · captions EVERYTHING LOOKED NORMAL · ₹99,998 GONE | अगली सुबह, असली app से पाँच सौ का payment। सब normal। फिर account से पैसे कटने लगे। |
| 5 | how (02 HOW IT WORKS) | 12.8 s | "The invisible layer" · 3D exploded view: the real UPI app (teal) below, a red dashed transparent layer "OVERLAY" with an eye lifting off it · four taps on the top layer: each digit lands in a RECORDED box (4 7 1 9) and a dashed line carries the tap down to the real keypad, whose PIN dots fill · labels INVISIBLE LAYER · ON TOP / THE REAL UPI APP · captions INVISIBLE LAYER · RECORDS EVERY TAP · PASSES IT ON · "Nothing on screen looks wrong." · "Source: Cyble research ("Ghost Overlay"), reported Oct 2026" | ये है overlay: असली app के ऊपर एक invisible परत। आप जो digit दबाते हैं, परत उसे record करके tap असली app तक भेज देती है। Screen पर सब normal दिखता है। |
| 6 | eyes | 9.3 s | "The second eye: Accessibility" · phone with a scanning line and an eye · BUILT TO HELP: "Reads the screen aloud for people who need it." · IN A FAKE APP: "Reads what's on your screen — and what you type." · data card 60 apps — banking, UPI and wallet apps whose keypad one malware family can read (Source: Cyble research, via CXOToday, 16 Oct 2026) · captions ACCESSIBILITY · READS YOUR SCREEN | दूसरी आँख: Accessibility. ये feature screen पढ़कर सुनाने के लिए बना है। पर fake app इससे आपकी screen और keypad पढ़ लेता है। |
| 7 | sms | 7.4 s | "Then your SMS" · SMS card "AD-XXBANK: XXXX21 is your OTP for a UPI transaction…" · envelopes flow from "Your phone" to "Scammer's server" · YOUR PIN + YOUR OTP = PAYMENTS IN YOUR NAME · "CERT-In alert, via Free Press Journal (Mar 2026) · Cyble (Oct 2026)" · captions OTPs + BANK ALERTS · SENT TO THE SCAMMER | और SMS भी: OTP और bank alerts सीधे ठग के server पर। PIN और OTP, दोनों उसके पास। |
| 8 | news | 8.1 s | "Why this matters now" · "Reported: Business Today, 17 Nov 2026 · The420, 22 Nov 2026" · NPCI + UPI APPS → GOOGLE: "Restrict these for apps installed from outside the Play Store:" · locked chips ACCESSIBILITY SERVICES · DEVICE ADMIN · DISPLAY OVER OTHER APPS · "Talks reported; no decision by Google yet." · captions NPCI ASKED GOOGLE · LOCK THESE PERMISSIONS | इसीलिए NPCI और UPI apps ने Google से कहा है: Play Store के बाहर वाले apps को ये permissions आसानी से न मिलें। |
| 9 | trail (03 THE TRAIL) | 9.1 s | "The trail they leave" · 3,206 COMPLAINTS ON THE PORTAL ↓ 111 FAKE APK FILES EXAMINED ↓ SERVERS THAT GOT THE SMS · stamp 6 ARRESTED · SERVER LOG (illustrative, masked): 08:21:04 AD-XXBANK OTP XXXX21 / Debited ₹49,999 ×2 · "Mumbai Cyber Police · Reported: Free Press Journal, 26 Jun 2026" · "Allegations — not yet proved in court." · captions FAKE APPS EXAMINED · SERVERS TRACED | पर ये apps निशान छोड़ते हैं। Mumbai में fake apps और उनके servers की जाँच से छह लोग पकड़े गए; आरोप अभी साबित नहीं हुए। |
| 10 | data | 5.8 s | "One network, allegedly" · data card 8,609 people installed the fake apps (Mumbai case · Reported: Free Press Journal, 26 Jun 2026) · data card 3,206 complaints across India · about ₹43 crore (National Cyber Crime Reporting Portal, as reported) · "Allegations — not yet proved in court." · captions 8,609 INSTALLS · 3,206 COMPLAINTS | आरोप है: आठ हज़ार से ज़्यादा installs, और तीन हज़ार से ज़्यादा शिकायतें। |
| 11 | law (04 THE LAW) | 12.5 s | "What the law says" · IT ACT, 2000 · s.66 WITH s.43(c): "Dishonestly planting malware on a phone: up to 3 years, or fine up to ₹5 lakh, or both." · IT ACT, 2000 · SECTION 66C: "Using another person's password or unique ID feature (such as a UPI PIN): up to 3 years and fine up to ₹1 lakh." · BNS, 2023 · SECTION 318(4): "Cheating someone into handing over money: up to 7 years and fine." (Old law: IPC s.420) · captions s.66: MALWARE · s.66C: IDENTITY THEFT · s.318(4): UP TO 7 YEARS | Malware डालना: IT Act Section sixty six. किसी का PIN इस्तेमाल करना: Section sixty six C. और धोखे से पैसा लेना: BNS Section three eighteen four, सात साल तक। |
| 12 | act (05 DO THIS NOW) | 12.6 s | SCREENSHOT THIS card (holds 6 s+): RED FLAGS — an app sent on WhatsApp or SMS (an .apk file) · it asks for Accessibility or "display over other apps" · a bill, KYC or fine to pay "right now"; DO THIS NOW — install apps only from the Play Store · never turn on Accessibility for an unknown app · money gone? Call 1930 and your bank at once · "Installed one? Data off · uninstall · change your UPI PIN · call your bank" · SEND THIS TO YOUR PARENTS | Screenshot लीजिए। WhatsApp या SMS पर आया app कभी install मत कीजिए। अनजान app को Accessibility कभी नहीं। पैसा गया, तो तुरंत one nine three zero। ये अपने parents को भेजिए। |
| 13 | outro | 5.5 s | Logo + wordmark · Save this · Share it · Legal awareness only · Not legal advice · Laws cited: IT Act 2000 (ss.43, 66, 66C) · BNS 2023 (s.318(4)) | (none) |

Studio elements used: series badge (header + cover) · 5 chapter cards with stings · dramatised mock WhatsApp chat, a fake-app
permission screen, a generic UPI PIN screen and success screen, bank debit notifications and an SMS (all masked, DRAMATISED tag) ·
animated 3D overlay diagram (invisible layer over the real keypad, taps recorded and passed on) · phone-to-server SMS flow ·
investigation chain with a masked, illustrative server log · data cards with outlet / researcher and date · law cards · kinetic
English captions · screenshot checklist (3 red flags, 3 actions) · original score, stings, chimes, risers and impacts.

Cover hooks considered: REAL APP. REAL PIN. / SOMEONE SAW IT. · AN INVISIBLE LAYER / OVER YOUR UPI APP · NEVER INSTALL AN APP /
SENT ON WHATSAPP · YOUR UPI PIN / HAD A WITNESS · THE SCREEN LOOKED NORMAL. / IT WASN'T. Rendered: the first three (A = cover.jpg,
matches the reel's first line). Owner's photo: black_suit_side.png (not used in any earlier reel).
