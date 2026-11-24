# Sources: EP04 "Your money doesn't vanish, it splits" (UPI fraud → mule-account layering → 1930 freeze)

Research date: Tue 24 Nov 2026 (IST). Every page below was opened with WebFetch unless it is marked "search result only".
Status key: **VERIFIED** = the primary source was opened and says this. **PARTLY** = only a secondary source, or the wording differs, or there is a caveat. **NOT VERIFIED / drop**.
Pages that failed to open:
- newkerala.com lead article (permission timed out), so the same ANI copy on webindia123 was used instead.
- MHA Lok Sabha PDF 5124 of 24 Mar 2026 (site error), so the matching PIB release was used.
- aninews.in (error).
- RBI draft KYC PDF on rbidocs (captcha), so the HTML version on rbi.org.in was used.
- npci.org.in (robots-blocked).
- thestatesman.com SC article (error).
- India Code PDFs opened fine via WebFetch. curl was blocked by the proxy.

---

## The law

- **BNS s.318(4): cheating and dishonestly inducing delivery of property.** VERIFIED (India Code bare text).
  - Wording: "Whoever cheats and thereby dishonestly induces the person deceived to deliver any property to any person … shall be punished with imprisonment of either description for a term which may extend to seven years, and shall also be liable to fine."
  - s.318(1) defines "cheat" as "by deceiving any person, fraudulently or dishonestly induces the person so deceived to deliver any property…".
  - Source: https://www.indiacode.nic.in/bitstream/123456789/20062/1/a202345.pdf (BNS, 2023; read in full).
  - Old law: IPC s.420.
  - No separate secondary source fetched for the bare text. The CBI's Operation Chakra-V mule FIR is reported as invoking "criminal conspiracy, cheating, forgery" (The Statesman/IANS, undated page): https://www.thestatesman.com/india/mule-accounts-cbi-continues-crackdown-on-cybercrimes-with-searches-in-five-states-nine-held-1503450148.html

- **BNS s.317: stolen property.** VERIFIED (India Code).
  - **Property obtained by cheating IS included.** s.317(1): "Property, the possession whereof has been transferred by theft or extortion or robbery or cheating, and property which has been criminally misappropriated or in respect of which criminal breach of trust has been committed is designated as stolen property … within or without India…". It "ceases to be stolen property" once it comes back into the possession of the person legally entitled to it.
  - s.317(2): "Whoever dishonestly receives or retains any stolen property, knowing or having reason to believe the same to be stolen property, shall be punished with imprisonment of either description for a term which may extend to three years, or with fine, or with both."
  - Source: same India Code PDF.
  - Old law: IPC s.410/411.
  - Script caution: the offence needs "knowing or having reason to believe". Say "can be charged", not "will be jailed".

- **BNS s.61: criminal conspiracy.** VERIFIED (India Code).
  - s.61(1): when two or more persons "agree … to do, or cause to be done— (a) an illegal act; or (b) an act which is not illegal by illegal means".
  - s.61(2)(a): for offences punishable with death, life or RI of two years or more, the conspirator is punished "in the same manner as if he had abetted such offence" (unless a specific provision applies).
  - s.61(2)(b): other conspiracies get up to 6 months, or fine, or both.
  - Old law: IPC s.120A/120B.

- **BNS s.111: organised crime.** VERIFIED (India Code), but **use with care**.
  - s.111(1) lists "economic offence, cyber-crimes" among continuing unlawful activities that constitute organised crime when committed by or for an "organised crime syndicate".
  - Explanation (iii): "economic offence" includes "mass-marketing fraud or running any scheme to defraud several persons or doing any act in any manner with a view to defraud any bank or financial institution…".
  - s.111(2)(b) (no death caused): "not less than five years but which may extend to imprisonment for life" + fine "not less than five lakh rupees".
  - s.111(3): whoever "abets, attempts, conspires or knowingly facilitates" organised crime gets min 5 yrs to life + fine ≥ ₹5 lakh.
  - **Precondition (Explanation (ii)):** a "continuing unlawful activity" needs a cognizable offence punishable with 3+ years, done as or for a syndicate, "in respect of which more than one charge-sheets have been filed before a competent Court within the preceding period of ten years and that Court has taken cognizance".
  - Script: "Running mule networks can even be charged as **organised crime** (BNS s.111) when the legal conditions are met." Don't imply every account-renter faces s.111.

- **IT Act 2000 s.66D: cheating by personation using a computer resource.** VERIFIED (text reproduced on UNODC SHERLOC; India Code page not opened).
  - Wording: "Whoever, by means of any communication device or computer resource cheats by personation, shall be punished with imprisonment of either description for a term which may extend to three years and shall also be liable to fine which may extend to one lakh rupees."
  - Source: https://sherloc.unodc.org/cld/fr/legislation/ind/the_information_technology_act_2000/chapter_xi/sections_66c66d/sections_66c-66d.html
  - Caution: 66D fits the scammer who impersonates (bank, police, etc.). It is not the natural section for a mule account-holder.

- **BNSS s.106: power of police officer to seize certain property.** VERIFIED (India Code). **Legal position on bank "debit freeze" is unsettled (PARTLY).**
  - s.106(1): "Any police officer may seize any property which may be alleged or suspected to have been stolen, or which may be found under circumstances which create suspicion of the commission of any offence."
  - s.106(3): the officer "shall forthwith report the seizure to the Magistrate having jurisdiction".
  - Source: https://indiacode.nic.in/bitstream/123456789/20099/3/A2023-46.pdf
  - Old law: CrPC s.102.
  - The High Courts are split on bank-account debit freezes:
    - Kerala HC (*Headstar Global*, 2025), Bombay HC (*Kartik Yogeshwar Chatur*, 2025) and Delhi HC (*Malabar Gold*, 2026) say that attaching proceeds of crime needs a Magistrate's order under s.107. Source: SCC Online blog, 24 Jul 2026: https://www.scconline.com/blog/post/2026/07/24/bnss-debit-freezing-bank-accounts-legality-analysis/
    - Karnataka HC (Justice M. Nagaprasanna, 2026 LiveLaw (Kar) 287) says police **can** debit-freeze under s.106 as an investigative step without prior Magistrate approval, subject to reporting under s.106(3). It follows *IIFL Finance* and Allahabad HC DB *Ashish Rawat*. Source: LiveLaw, 12 Aug 2026: https://www.livelaw.in/high-court/karnataka-high-court/karnataka-high-court-rules-debit-freeze-require-prior-magistrate-approval-545521
    - Delhi HC (20 Nov 2026) noted that clause 10.2 of the MHA SOP ties seizure or suspension directions to BNSS s.106 "or other applicable laws". Source: LiveLaw: https://www.livelaw.in/high-court/delhi-high-court/cyber-fraud-sop-cant-be-used-to-undo-voluntary-money-transfers-between-known-parties-delhi-high-court-559221
  - **Script:** don't say "police freeze under s.106" as settled law. Say "Police can seize or seek attachment of suspected proceeds under BNSS ss.106–107", or leave sections off the freeze scene.

- **BNSS s.107: attachment, forfeiture or restoration of property (proceeds of crime).** VERIFIED (India Code).
  - s.107(1): "Where a police officer making an investigation has reason to believe that any property is derived or obtained, directly or indirectly, as a result of a criminal activity or from the commission of any offence, he may, with the approval of the Superintendent of Police or Commissioner of Police, make an application to the Court or the Magistrate … for the attachment of such property."
  - s.107(2): the Court or Magistrate issues a notice to show cause within fourteen days. s.107(4) proviso allows an ex parte order.
  - s.107(6): "If the Court or the Magistrate finds the attached or seized properties to be the proceeds of crime, the Court or the Magistrate shall by order direct the District Magistrate to rateably distribute such proceeds of crime to the persons who are affected by such crime."
  - s.107(7): distribution "within a period of sixty days". s.107(8): unclaimed or surplus proceeds "shall stand forfeited to the Government".
  - Secondary: Kerala HC, "Police Cannot Attach Bank Account Under S.107 BNSS Without Magistrate's Approval" (LiveLaw, search result only): https://www.livelaw.in/high-court/kerala-high-court/kerala-high-court-rules-police-cannot-freeze-bank-account-section-107-bnss-295027
  - Gist for screen: "BNSS s.107: a Magistrate can attach proceeds of crime and order them returned to victims."

- **PMLA and mule networks.** PARTLY. Usable as "PMLA is also used against cyber-fraud money trails". There is **no official statement found that an individual who rents out an account will face PMLA**.
  - PIB/MHA, 24 Mar 2026 (Lok Sabha reply): ED "has taken up around 257 cases related to cybercrime for investigation" under PMLA (as of 28.02.2026), "resulting in identification of Proceeds of Crime (PoC) worth 35,925.58 crore rupees". Source: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2244499&reg=3&lang=2
    - Secondary: Inc42, 25 Mar 2026: https://inc42.com/buzz/cybercrime-proceeds-worth-%e2%82%b936k-cr-under-eds-radar-govt/
  - ED press release, 05.03.2026 (part-time job scam, about ₹641 crore). Proceeds were first credited to "mule accounts managed and operated by members of certain Telegram groups", then moved through "a web of dummy/shell entities across India to fragment and obscure the source of funds". From there they went via a UAE prepaid-card platform and were converted into crypto, through "a complex chain of custodial and non-custodial wallets". Source: https://www.enforcementdirectorate.gov.in/media/press-release-documents/5b4e9432-6a23-4a25-91a0-cc974c65624a_Press%20Release_Part%20Time%20Job%20Scam_5%2003%202026%203.pdf
    - Pending case. Don't name the accused.
    - Secondary: Moneylife: https://moneylife.in/article/ed-arrests-2-cas-in-641-crore-cyber-fraud-money-laundering-case/79857.html (search result only)
  - Bombay HC (*Nagani Akram Mohammad Shafi v. UoI*, Jul 2025): BNS offences corresponding to scheduled IPC offences can be "scheduled offences" under PMLA even without an amendment to the schedule. Source: Bar & Bench, 8 Jul 2025: https://www.barandbench.com/news/litigation/bns-offences-can-be-scheduled-offences-under-pmla-after-ipc-repeal-bombay-high-court
  - Safe script line: "Big fraud money trails are also probed under the money-laundering law (PMLA). ED has taken up about 257 cyber-crime cases." Drop any "you will face PMLA" line.

---

## Mule accounts & layering

- **What a mule account is: RBI's definition (draft).** VERIFIED as a DRAFT.
  - RBI draft KYC Amendment Directions, 2026: Money Mule Account = "an account used, knowingly or unknowingly, to receive, layer or transfer proceeds of cyber-enabled financial fraud". Source: https://www.rbi.org.in/scripts/BS_ViewContent.aspx?Id=5170
  - Press release of 11 Sep 2026; comments closed 2 Oct 2026: https://rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=63587
  - Secondary: Inc42, 14 Sep 2026: https://inc42.com/buzz/rbi-floats-draft-rules-to-standardise-account-blocking-in-cyber-fraud-cases/
  - The same draft provides:
    - A temporary debit hold on a flagged "Suspected Money Mule Transaction" of "₹1000 and above".
    - A hold on the whole account only "as a last resort and only in exceptional circumstances".
    - A maximum hold of 60 days without contrary instruction.
    - Notice to the account holder.
    - Proposed effective date "April 1, 2027". RBI later told the SC it would notify by 30 Nov and bring them into force by 31 Dec 2026 (MediaNama, 11 Nov 2026).
  - On screen, say **"RBI's proposed rules"**.

- **MHA/I4C description of mule accounts.** VERIFIED (via ThePrint/PTI report of the MHA Lok Sabha reply, 9 Dec 2025).
  - Mule accounts are used to launder proceeds, opened with incorrect KYC or without the owner's knowledge of misuse, and funds move "through multiple layers of mule accounts". This is ThePrint's paraphrase of the reply.
  - Source: https://theprint.in/india/special-i4c-registry-led-to-blocking-of-rs-8031-cr-cyber-fraud-funds-govt/2802007
  - Earlier RBI wording (6 Dec 2024): "Use of money mule accounts is a common method adopted by fraudsters to channel proceeds of frauds." Source: https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=59245

- **Official "layer" language and speed.** VERIFIED for "immediately layered". PARTLY for "minutes/seconds".
  - PIB/MHA (I4C alert on illegal payment gateways), 28 Oct 2024: "Funds are immediately layered to another account". Source: https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2069000&reg=48&lang=2
  - "Layer 1 mule accounts" is official MHA/PIB terminology (see Numbers). **No official definition of Layer 2 or Layer 3 was found.** You can explain it descriptively: Layer 1 = the account that first receives the victim's money; Layers 2, 3… = the accounts it is split into.
  - Police/press usage: the Mumbai police statement (FPJ, updated 24 Aug 2026) refers to about 30,000 "first-layer bank accounts" frozen or put under lien over four years: https://www.freepressjournal.in/mumbai/mumbai-police-help-6096-cyber-fraud-victims-recover-397-crore-through-money-restoration-module
  - The Week (16 Aug 2026) describes one investigation in which money moved through "13 layers", "2,487 transactions" and 600+ accounts, with small ₹500 to ₹5,000 splits concentrated in layers 3 to 5 ("smurfing"). Source: https://www.theweek.in/theweek/current/2026/08/14/the-mule-network-how-cybercriminals-exploit-bank-accounts-for-money-laundering.html
    - Real people are named there. Use only the pattern, with no names.
  - **Speed:** Karnataka HC (Aug 2026) observed that money can move through mule accounts "within seconds". This is LiveLaw's report of the judgment, not a verbatim quote I could confirm. Source: https://www.livelaw.in/high-court/karnataka-high-court/karnataka-high-court-rules-debit-freeze-require-prior-magistrate-approval-545521
  - **No official MHA/I4C/RBI statement giving "minutes" or "hours" was found.**
  - Safe wording: "within minutes, the money is split again and again". Attribute it as a pattern, or say "almost instantly", not a sourced number.

- **Official "golden hour" statement.** PARTLY. **No central (MHA/I4C/RBI) definition was found.**
  - Rajasthan Police (official X post, reported by Patrika, 11 Sep 2026): act "within the Golden Hour" and call 1930 "as soon as fraud occurs". No duration is given. Source: https://www.patrika.com/en/jaipur-news/rajasthan-police-alert-dont-panic-if-cyber-fraud-happens-take-this-step-in-the-golden-hour-20899239
  - Hyderabad DCP Cyber Crimes (Telangana Today, 29 Jul 2024): "Every minute matters in financial frauds". The article says to report "at least between 1 hour and 3 hours". Source: https://telanganatoday.com/golden-hour-rule-to-rescue-of-cyber-fraud-victims-in-hyderabad
  - Script: "Police call it the golden hour: report immediately." Don't state "1 hour" as an official rule.

- **Recruitment of students / "₹5,000 a month for your account".** PARTLY (reported, not official).
  - The Week (Aug 2026): mules are offered "₹5,000 to ₹40,000" upfront plus 1.5 to 2% of proceeds. Students and unemployed youth are common targets.
  - Onmanorama (9 Sep 2026): in the Kasaragod "Operation Cy-Hunt", 26 cases were booked, and one account-holder reportedly got ₹5,000 commission. Source: https://www.onmanorama.com/news/kerala/2026/09/09/rent-out-your-bank-account-land-in-a-cybercrime-case-kasaragod-police-book-26.html
  - Use "₹5,000" only as a **hypothetical offer** on screen, not as an official figure.

- **Official warning: don't sell or rent your account; you can be arrested.** VERIFIED.
  - PIB/MHA (I4C), 28 Oct 2024: I4C "advises all citizens not to sell/rent their bank accounts", and the same goes for company registration and Udhyam Aadhaar certificates. "Illicit funds deposited in such bank accounts can lead to legal consequences, including arrest." Accounts are "scouted through social media", mainly Telegram and Facebook. Source: https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2069000&reg=48&lang=2
    - Secondary: News On AIR, 29 Oct 2024: https://www.newsonair.gov.in/cybercrime-coordination-centre-issued-alert-against-illegal-payment-gateways
    - Secondary: Deccan Herald: https://deccanherald.com/india/cybercrime-alert-centre-warns-people-against-selling-or-renting-bank-accounts-company-registration-certificates-others-3252430
  - Kerala Police (News On AIR, 8 Aug 2026): students and low-income people are targeted with commissions, and "account holders bear full responsibility for transactions carried out through their bank accounts." Source: https://newsonair.gov.in/keralam-police-cautions-the-public-against-mule-account-fraud/
  - Hyderabad police (Telangana Today, 29 Jun 2026): "lending a bank account, even for a small commission, is a serious criminal offence". The same report says more than 200 mule account holders were arrested in the city over five months. Source: https://telanganatoday.com/hyderabad-police-intensify-crackdown-on-mule-account-networks

- **Mule-network busts showing the cash-out step.** VERIFIED as reported. Use anonymised.
  - Karnataka Cyber Command (Deccan Herald, page undated; operation Dec 2025 to Feb 2026): 68 "mule herders" arrested, 869 mule accounts, ₹85.05 crore routed, ₹13.43 crore on hold or frozen. Money was "withdrawn in cash or converted to cryptocurrency". Source: https://www.deccanherald.com/india/karnataka/karnataka-cyber-command-arrests-68-mule-herders-uncovers-rs-85-crore-scam-network-2-3904753

---

## Numbers (for a data card)

- **Suspect Registry launch date: 10 Sep 2024.** VERIFIED.
  - PIB/MHA, 24 Mar 2026: "A Suspect Registry of identifiers of cyber criminals has been launched by I4C on 10.09.2024". Source: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2244499&reg=3&lang=2
  - The Lok Sabha reply of 11 Aug 2026 (ANI via webindia123 and FPJ) also gives "September 10, 2024, with banks and financial institutions". The PIB release of 12 Aug 2026 that I opened did not restate the date.
  - Secondary: ThePrint/PTI, 9 Dec 2025: https://theprint.in/india/special-i4c-registry-led-to-blocking-of-rs-8031-cr-cyber-fraud-funds-govt/2802007

- **"27.37 lakh Layer-1 mule accounts shared as of 31 Jan 2026".** VERIFIED, but SUPERSEDED.
  - PIB/MHA, 24 Mar 2026 (Lok Sabha reply): "Till 31.01.2026, more than 23.05 lakh suspect identifier data received from Banks", and "27.37 lakh Layer 1 mule accounts have been shared with the participating entities of Suspect Registry". Source: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2244499&reg=3&lang=2
  - Secondary: Inc42, 25 Mar 2026. News On AIR, 11 Mar 2026 (Rajya Sabha): "over 27 lakh", with ₹9,518 crore declined: https://www.newsonair.gov.in/govt-saves-over-%e2%82%b98600-crore-in-cyber-fraud-cases-mos-home-affairs-b-sanjay-kumar
  - Lead article (ANI via webindia123, 26 Jul 2026): https://news.webindia123.com/news/articles/Business/20260726/4479444.html

- **NEWER figure (use this): as of 30 Jun 2026.** VERIFIED.
  - PIB/MHA, 12 Aug 2026 (PRID 2298336): "more than 30.48 lakh suspect identifier data received from banks". "32.08 lakh Layer 1 mule accounts have been shared with the participating entities of Suspect Registry". "declined transactions worth Rs. 25,698 crores." Source: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2298336&reg=48&lang=1
  - Secondary: Free Press Journal / ANI, Lok Sabha reply of 11 Aug 2026 by MoS Home: https://www.freepressjournal.in/india/centre-blocks-3718-fraudulent-apps-saves-11158-crore-from-cyber-fraud
  - Secondary: webindia123 / ANI, 11 Aug 2026: https://news.webindia123.com/news/Articles/India/20260811/4485786.html
  - Note: the declined amount rose from ₹9,518 crore (Jan 2026) to ₹25,698 crore (Jun 2026). That is what the PIB release says. Quote it exactly and attribute it, "as of 30 June 2026".

- **CFCFRMS / 1930: amount saved.** VERIFIED.
  - PIB/MHA, 12 Aug 2026: "till 30.06.2026, financial amount of more than Rs. 11,158 Crore has been saved in more than 32.80 lakh complaints." Source: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2298336&reg=48&lang=1
  - Secondary: FPJ (12 Aug 2026), webindia123/ANI (11 Aug 2026), Aaj Tak (28 Jul 2026).
  - Earlier: ₹8,690 crore / 24.65 lakh complaints till 31.01.2026 (PIB, 24 Mar 2026).
  - Same reply (secondary only): 15.75 lakh SIMs and 5.77 lakh IMEIs blocked as reported by police. The "Money Restoration Module" and "Grievance Redressal Module" became operational in April 2026.

- **CFCFRMS launch: 2021.** VERIFIED.
  - PIB, 17 Jun 2021: helpline 155260 and reporting platform "soft launched on 1st April, 2021". Source: https://www.pib.gov.in/PressReleasePage.aspx?PRID=1727990&reg=48&lang=2
  - Later releases say CFCFRMS was "launched in 2021". The helpline number is now **1930**: News On AIR, 17 Dec 2025 (Rajya Sabha): "toll-free number 1930 has been operationalised". Source: https://www.newsonair.gov.in/over-rs-7000-crore-saved-through-citizen-financial-cyber-fraud-reporting-and-management-system/
  - I found no exact date for the switch from 155260 to 1930, so don't state one.

- **How the 1930 hold works (general).** VERIFIED (PIB 17 Jun 2021).
  1. Police log the complaint as a ticket in CFCFRMS.
  2. The ticket goes to the victim's bank and the receiving bank or wallet.
  3. The bank checks its systems and, "if the money is still there", puts a hold.
  4. If the money has moved on, "the ticket is escalated to that bank", and "This process is repeated until the money is saved from reaching into the hands of the fraudsters."
  - The victim must file full details on cybercrime.gov.in "within 24 hours" using the acknowledgement number. The system acts "in almost real time".
  - Release of held money to the victim needs legal process. Mumbai police (Aug 2026): only money "found eligible for refund after financial and judicial scrutiny" is restored. In general BNSS s.107(6) allows a Court or Magistrate to order distribution, and the 2026 Money Restoration Module exists.
  - Don't promise refunds.

- **Total cyber-fraud loss 2025.** PARTLY. Not on a primary page I could open.
  - ThePrint (21 Feb 2026, "data sourced from the Ministry of Home Affairs"): "Indians lost at least Rs 22,495 crore to cyber fraud in 2025", vs ₹22,845 crore in 2024. 28.15 lakh cases in 2025. Source: https://theprint.in/india/cybercrime-saw-24-spike-in-2025-indians-lost-rs-22495-crore-mainly-in-investment-scams/2859930
  - FPJ (18 Feb 2026) gives the same ₹22,495 crore but "over 24 lakh" complaints, so the complaint count is inconsistent. Source: https://www.freepressjournal.in/amp/mumbai/over-24-lakh-cyber-complaints-22495-crore-fraud-reported-in-2025
  - Prefer the PIB figures above. If used, say "₹22,495 crore reported lost in 2025 (MHA data, as reported)".

- **MuleHunter.AI.** VERIFIED for what it is. PARTLY for the bank count.
  - RBI, 6 Dec 2024 (Statement on Developmental and Regulatory Policies): RBIH, "a subsidiary of Reserve Bank", is piloting "an AI / ML based model called MuleHunter.AI" to detect mule accounts. The pilot with two large public sector banks "has yielded encouraging results". Source: https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=59245
  - Bank count: "over 26 banks" (Business Today, 12 May 2026: https://www.businesstoday.in/technology/story/indian-govt-rbi-innovation-signs-ai-pact-to-tackle-financial-frauds-531090-2026-05-12). No primary figure was found. In Nov 2025 the RBI Governor gave an ambiguous "high double digits" (FPJ, 21 Nov 2025).
  - Script: "an AI tool built by RBI's Innovation Hub to spot mule accounts". Drop the bank count, or attribute "over 26 banks (reported, May 2026)".
  - Related: I4C–RBIH MoU, 12 May 2026, to feed Suspect Registry data into AI fraud detection. Source: News On AIR: https://newsonair.gov.in/cyber-crime-coordination-sign-mou-with-rbi-to-curtail-mule-accounts/

---

## Reporting routes

- **1930 + cybercrime.gov.in when money is already lost; Chakshu for suspected fraud calls, SMS or WhatsApp.** VERIFIED.
  - Sanchar Saathi Chakshu page: "Chakshu facilitates citizens to report the suspected fraud communications" (calls, SMS, WhatsApp). "If you have already lost money, please report at cyber crime helpline 1930", with cybercrime.gov.in also listed. Source: https://sancharsaathi.gov.in/sfc/
  - PIB (6 Oct 2025, Hindi factsheet) names the National Cyber Crime Reporting Portal www.cybercrime.gov.in and helpline 1930. Source: https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/oct/doc2025108661001.pdf
  - 1930 "AI and multilingual" upgrade ordered by the Home Minister (News On AIR, Jun 2026): https://newsonair.gov.in/home-minister-amit-shah-reviews-functioning-of-national-cybercrime-helpline-1930/

- **UPI speed ("money moves in seconds").** PARTLY. I could not open an NPCI primary page (npci.org.in is robots-blocked).
  - Use the Karnataka HC "within seconds" observation (LiveLaw report) or plain "instantly". Don't quote any UPI limit figures.

---

## Dropped / reworded

- **DROP** "official golden hour = 1 hour". There is no MHA/I4C/RBI definition. Reword to "police call it the golden hour: report immediately".
- **DROP** any official "money moves through layers in X minutes" figure, because none exists. Keep "almost instantly", or the HC "within seconds" with attribution.
- **DROP** "renting your account = PMLA case against you". There is no official basis for individuals. Reword to "cyber-fraud money trails are also probed under PMLA (ED: about 257 cases)".
- **DROP** a precise MuleHunter bank count, or attribute it as reported.
- **REWORD** "Layer 1/2/3" as **I4C's term "Layer-1 mule account"** (official) plus a descriptive explanation of later layers. Don't claim official Layer 2/3 definitions.
- **REWORD** "police freeze accounts under BNSS s.106" because the HCs are split. Say "banks put a hold after a 1930 complaint; police and Magistrates can seize or attach proceeds (BNSS ss.106–107)".
- **REWORD** BNS s.111. Use it only as "can be charged as organised crime when the conditions are met".
- **REPLACE** 27.37 lakh (31 Jan 2026) with **32.08 lakh Layer-1 mule accounts, ₹25,698 crore declined, ₹11,158 crore saved in 32.80 lakh complaints (all as of 30 Jun 2026, PIB 12 Aug 2026)**.
- **LABEL** RBI's mule-account debit-hold rules and the 23 Nov 2026 "Stop Switch" as **proposed / draft**.
- Old law appears only in brackets: IPC 420 → BNS 318(4); IPC 411 → BNS 317(2); IPC 120B → BNS 61; CrPC 102 → BNSS 106.

---

## Spot-check by the build run (24 Nov 2026, pages re-opened)
- PIB/MHA, 12 Aug 2026 (PRID 2298336), loaded: "till 30.06.2026, financial amount of more than Rs. 11,158 Crore has been saved in
  more than 32.80 lakh complaints"; "32.08 lakh Layer 1 mule accounts have been shared with the participating entities of
  Suspect Registry"; "Posted On: 12 AUG 2026 4:50PM by PIB Delhi", Ministry of Home Affairs.
- RBI draft KYC Amendment Directions, 2026 (rbi.org.in Id=5170), loaded: "Money Mule Account" means "an account used, knowingly or
  unknowingly, to receive, layer or transfer proceeds of cyber-enabled financial fraud"; Suspected Money Mule Transaction = "a
  transaction of ₹1000 and above, flagged by the bank's transaction-monitoring systems"; maximum temporary debit hold "60 days";
  marked DRAFT ("These Directions shall come into effect from April 1, 2027, or on such earlier date…"); issued following a
  Supreme Court order of 4 Aug 2026.
- I4C alert of 28 Oct 2024 ("Funds are immediately layered to another account"; "not to sell/rent their bank accounts"):
  News On AIR, Moneylife, Deccan Herald and ETV Bharat search results agree with the PIB text opened by the research pass.

## What the reel uses (and how it is worded)
- Mule account = RBI's **draft** definition, labelled "RBI draft KYC directions, Sep 2026".
- "Layer 1" = MHA/I4C term; Layers 2 and 3 explained in plain words (no official definition claimed).
- Speed: "immediately layered" (I4C alert, 2024); the reel's clock is labelled ILLUSTRATIVE.
- Cash-out shown only as ATM cash and crypto (both in the Karnataka Cyber Command and ED reports); cheque and gold dropped
  (not verified for this run).
- 1930 ticket flow bank → bank and hold where the money is found (PIB, 17 Jun 2021).
- Numbers: ₹11,158 crore saved in 32.80 lakh complaints; 32.08 lakh Layer-1 mule accounts shared (both till 30 Jun 2026, PIB 12 Aug 2026).
- Law: BNS s.318(4) (up to 7 years + fine), s.317(1)–(2) (stolen property includes property transferred by cheating; receiving or
  retaining it "knowing or having reason to believe": up to 3 years, or fine, or both), s.61 conspiracy, s.111 organised crime
  "when its conditions are met"; BNSS s.107 (Magistrate can attach proceeds of crime and order them distributed to the persons
  affected). Not used: PMLA line, MuleHunter bank count, golden-hour duration, BNSS s.106 freeze (HCs split).
