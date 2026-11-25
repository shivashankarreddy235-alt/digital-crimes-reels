# Sources: EP07 "The invisible layer over your UPI app: how APK malware sees your PIN" (TECH DECODED)

Every page below was opened by this run (25 Nov 2026) unless marked otherwise. Quotes are short; the rest is paraphrase.
Explain, never enable: the reel shows the idea of an overlay, Accessibility misuse and SMS reading. It names no malware tools, no
code, no servers and no steps.

---

## How the invisible layer works

- **Overlay ("Ghost Overlay"): a transparent layer over the genuine UPI app's keypad records each digit tapped and passes the tap
  on to the real app, so nothing looks wrong.** VERIFIED (Cyble research via CXOToday; NPCI–Google reports).
  - CXOToday, 16 Oct 2026, citing Cyble Research and Intelligence Labs (CRIL): the malware lays a transparent layer over the real
    keypad, logs each digit and "replays the same tap into the app"; "Nothing on screen looks wrong as the user never leaves the
    real app"; "People have learned to look for a fake login page, and this malware never shows one." The victim must grant the fake
    app Android's Accessibility permission; it is pushed as a fake government transport app from outside the Play Store via SMS
    links about unpaid e-challans. Source: https://cxotoday.com/cybersecurity/cyble-alert-fake-traffic-challan-apps-steal-upi-pins-overlaying-genuine-google-pay/
  - Business Today, 17 Nov 2026: overlay malware ("Ghost Overlays", GhostBat RAT variants) can "place invisible layers over
    legitimate payment apps and capture users' UPI PINs".
    Source: https://www.businesstoday.in/technology/story/npci-upi-apps-seek-googles-intervention-to-curb-cyber-fraud-report-567919-2026-11-17
  - MediaNama, 19 Nov 2026: the "display over other apps" permission lets overlays "place invisible layers over legitimate
    applications"; they "can intercept the information and transmit it to hackers" when UPI PINs are entered.
    Source: https://www.medianama.com/2026/11/223-npci-upi-google-sideloading-apks/
  - Script: on screen "Invisible layer · records each tap · passes it on" and "Source: Cyble research, reported Oct 2026". The real
    app is shown as a generic UPI app (no brand); the two apps Cyble names are not named in the reel.

- **Accessibility misuse: reading keypad input on 60 banking, UPI, wallet and fintech apps.** VERIFIED (Cyble via CXOToday, above).
  - The same Accessibility access is used to read keypad input; the article says this covers 60 apps by default.
  - Google (India blog, 3 Oct 2024): Accessibility, SMS and notification permissions are "frequently abused by fraudsters to
    intercept one-time passwords via SMS or notifications, as well as spy on screen content".
    Source: https://blog.google/intl/en-in/products/launching-enhanced-fraud-protection-pilot-in-india/
  - Accessibility's legitimate purpose (helping people who need the screen read out or need help using the phone) is general
    Android knowledge, stated without a figure.
  - On screen (data card): "60 banking, UPI and wallet apps — keypad input read by one malware family · Source: Cyble research,
    via CXOToday, 16 Oct 2026".

- **SMS: OTPs and bank alerts go to the scammer.** VERIFIED.
  - CXOToday / Cyble (above): the malware reads incoming SMS, including OTPs and bank alerts (it can also change call forwarding and
    send texts from the SIM — not shown in the reel).
  - Free Press Journal, updated 31 Mar 2026, on a CERT-In alert: once details are entered, the app can read SMS and OTPs are "sent
    to the attacker's server"; it asks for "access to SMS and phone calls" and to run in the background.
    Source: https://www.freepressjournal.in/mumbai/cert-in-issues-alert-on-apk-malware-fraud-used-by-cybercriminals-to-steal-financial-data-via-fake-e-challan-bill-alerts
  - Script: "PIN + OTP = payments in your name" (concept; no steps).

- **The lure: a bill/disconnection message with an APK, sent on WhatsApp or SMS.** VERIFIED.
  - CERT-In alert (FPJ, above): a message about an unpaid e-challan "or a gas bill payment update" carrying an APK or a link.
  - Mumbai case (FPJ, 26 Jun 2026, below): a message about gas disconnection asked the victim to download an APK and pay ₹10 to
    update the bill.
  - The reel's scenario is DRAMATISED: "Sunita, 58, Nagpur", the gas-bill message, "Bill_Update.apk", the ₹500 payment and the
    ₹49,999 debits are invented and illustrative. No real company, bank or app is named.

## Why now (the peg)

- **NPCI and UPI apps have asked Google for Android-level safeguards; the industry wants accessibility services, device
  administration and overlay permissions restricted for apps installed outside verified stores.** VERIFIED (reported, four outlets).
  - Business Today 17 Nov 2026 (above); Outlook Money 18 Nov 2026 ("citing three people in the payments industry"):
    https://www.outlookmoney.com/banking/npci-in-talks-with-google-to-strengthen-android-security-against-upi-frauds ;
    MediaNama 19 Nov 2026 (Payments Council of India chairman: payment apps raised concerns with Google);
    The420, 22 Nov 2026: https://the420.in/npci-google-android-upi-fraud-security/
  - All rest on an Economic Times report (not opened). No Google response is reported. On screen: "Reported: Business Today,
    17 Nov 2026 · The420, 22 Nov 2026" and "Talks reported; no Google decision yet."
  - Newer Android versions already have "restricted settings" for sideloaded apps (Business Today, Outlook Money). Not used on
    screen.

- Google's own measures (background, not on screen): the India pilot blocks internet-sideloaded apps that declare RECEIVE_SMS,
  READ_SMS, notification-listener or Accessibility permissions (Google blog, 3 Oct 2024, above); developer verification went live
  on 30 Sep 2026 in Indonesia, Singapore and Thailand and is to expand globally in 2027 (Google support page,
  https://support.google.com/android-developer-console/answer/16561738 ; Android Authority, 1 Oct 2026, lists Brazil too:
  https://androidauthority.com/android-sideloading-developer-verification-first-wave-rollout-3717921). India is not named, so the
  reel makes no claim about it.

## The trail (reported case)

- **Mumbai Cyber Police (West Region): six arrested; an interstate network allegedly linked to about ₹43 crore and 3,206
  complaints on the National Cyber Crime Reporting Portal; 111 fake APK files found in forensic examination; 8,609 people
  downloaded the apps.** VERIFIED as reported (one outlet; figures attributed to officials; allegations).
  - Free Press Journal, 26 Jun 2026: https://www.freepressjournal.in/mumbai/6-arrested-as-mumbai-cyber-police-bust-43-crore-fake-apk-based-cyber-fraud-network-linked-to-3200-cases-video
  - The APKs were disguised as bank, gas-company and other apps; once installed they let the operators intercept OTPs and banking
    SMS. About 1.24 crore SMS were received through the apps' servers.
  - On screen: "Mumbai case · Reported: Free Press Journal, 26 Jun 2026" and "Allegations — not yet proved in court." No names of
    accused persons, victims, officers or companies.
  - The investigation chain shown (phone examined → fake app found → its server traced → arrests) is a simplified concept of what
    the report describes (forensic examination of the APK files; servers that received the SMS); it does not describe police
    methods beyond that.

## The law

- **IT Act 2000 s.43(c) and s.66.** VERIFIED (bare text).
  - s.43: "If any person without permission of the owner …" … (c) "introduces or causes to be introduced any computer contaminant or
    computer virus into any computer, computer system or computer network"; liable to pay damages by way of compensation.
    Explanation (i): "computer contaminant" means "any set of computer instructions that are designed" to "modify, destroy, record,
    transmit data or programme residing within a computer…" or to usurp its normal operation.
    Source: https://incometaxindia.gov.in/Acts/Information%20Technology%20Act,%202000/102120000000005390.htm
  - s.66: "If any person, dishonestly or fraudulently, does any act referred to in section 43, he shall be punishable with
    imprisonment for a term which may extend to three years or with fine which may extend to five lakh rupees or with both."
    Source: https://vidhijudicial.com/sec-65-to-78-chapter-xi-(offences)-the-information-technology-act,-2000.html
  - On screen: "IT Act, 2000 · s.66 with s.43: dishonestly planting malware on a phone: up to 3 years, or fine up to ₹5 lakh, or
    both." (A phone is a "computer" in the Act's broad sense; stated as commentary, not quoted.)

- **IT Act 2000 s.66C: identity theft.** VERIFIED (bare text, vidhijudicial page above).
  - "Whoever, fraudulently or dishonestly make use of the electronic signature, password or any other unique identification feature
    of any other person" — imprisonment up to three years and fine up to one lakh rupees.
  - On screen: "Using another person's password or unique ID feature (such as a UPI PIN): up to 3 years and fine up to ₹1 lakh."
    "Such as a UPI PIN" is commentary.
  - (s.66D, cheating by personation using a computer resource, is on the same page; not used in this reel.)

- **BNS 2023 s.318(4): cheating and dishonestly inducing delivery of property: up to 7 years and fine.** VERIFIED.
  - This run: apnilaw.com bare-Act page (third-party; last updated 13 Aug 2025): s.318(1) "Whoever, by deceiving any person,
    fraudulently or dishonestly induces the person so deceived…"; s.318(4) "shall be punished with imprisonment of either
    description for a term which may extend to seven years" and fine.
    Source: https://www.apnilaw.com/bare-act/bns/section-318-bharatiya-nyaya-sanhita-bns-cheating
  - India Code PDF (official text) was read in full by the EP04 run on 24 Nov 2026 (see episodes/2026-11-24-pm/sources.md); this
    run's re-open of India Code and devgan.in failed with fetch-permission errors.
  - Old law: IPC s.420.

## Do this now

- **Install apps only from the Play Store; never install an APK sent on WhatsApp, SMS or Telegram; never turn on Accessibility for
  an unknown app; keep Play Protect on; if installed, switch off data and Wi-Fi, uninstall, change passwords and the UPI PIN, check
  the bank statement; report on 1930 or cybercrime.gov.in.** VERIFIED (CERT-In alert via FPJ, 31 Mar 2026, above; Cyble via
  CXOToday: install only from official stores, alert the bank, 1930 / cybercrime.gov.in).
- 1930 and cybercrime.gov.in for money already lost: verified in EP04's sources.md (News On AIR, 17 Dec 2025; PIB).

## Dropped or not used

- "Digital payment fraud cases rose to 3.58 lakh in September" (The420, 22 Nov 2026): the report and year are not identified.
  Dropped.
- RBI compensation for small-value digital frauds from January 2027 (The420; Inc42 search result): not opened at a primary
  source. Not used.
- Supreme Court on cyber fraud (Telangana Today/PTI, 24 Jul 2026): outside the window; not relevant to this topic.
