# EP02 sources (checked 23 Nov 2026)

## How GPS works
- Constellation: the US commits to at least 24 operational GPS satellites 95% of the time; medium Earth orbit at about
  20,200 km; each satellite circles the Earth twice a day: https://www.gps.gov/systems/gps/space
  (count pages there are dated 2017/2023, so the reel says "at least 24", not a live count).
- Satellites are one-way beacons; "the GPS satellites themselves do not track anything on the ground" and the operators
  "cannot locate your phone/device": https://www.gps.gov/faq
- Satellites carry precise atomic clocks and continuously broadcast their position and the time the signal was sent;
  the receiver turns travel time into distance; one signal gives a circle, more narrow it down; at least four are used
  to account for receiver clock drift; the sat-nav does not send anything to the satellites:
  https://www.iflscience.com/your-sat-nav-does-not-ping-any-satellites-so-how-does-gps-actually-work-75331
  ("Advanced atomic clocks" also listed for Block IIF on the gps.gov space page above.)
- Travel time × speed of light = (pseudo)range; at least 4 satellites needed for three coordinates plus the receiver
  clock offset (ESA Navipedia): https://gssc.esa.int/navipedia/index.php/An_intuitive_approach_to_the_GNSS_positioning
- Arithmetic shown on screen (not a sourced figure): 20,200 km ÷ 299,792 km/s ≈ 0.067 s; a 1-microsecond clock
  error × speed of light ≈ 300 m.
- Accuracy: "GPS-enabled smartphones are typically accurate to within a 4.9 m (16 ft.) radius under open sky";
  accuracy worsens near buildings, bridges and trees, indoors, and with signals reflected off buildings (multipath):
  https://www.gps.gov/node/70 (canonical https://www.gps.gov/gps-accuracy)
- A-GPS: the network supplies satellite orbit data (ephemeris/almanac) and time, which improves time to first fix;
  standalone GPS "does not depend on the network" but can be slower to the first fix:
  https://en.wikipedia.org/wiki/Assisted_GNSS
- Tower location is an area, not an exact spot (tighter in cities, wider in villages): EP01 sources
  (episodes/2026-11-23-am/sources.md).

## NavIC
- NavIC (formerly IRNSS) is ISRO's regional system; coverage is India and up to 1,500 km beyond its boundary;
  designed position accuracy better than 20 m (2σ); new satellites broadcast in L1, L5 and S bands:
  https://www.isro.gov.in/SatelliteNavigationServices.html
- NVS-03 launched on GSLV-F18 from Sriharikota on 30 Oct 2026 at 23:51 IST into its intended GTO; carries L1, L5 and
  S-band navigation payloads and an indigenously developed atomic clock alongside procured clocks; NVS-02 (Jan 2025)
  could not reach its slot after an oxidiser-valve problem: PIB backgrounder, 1 Nov 2026,
  https://www.pib.gov.in/PressReleasePage.aspx?PRID=2331077&reg=48&lang=1
- Second source for the launch and the L1 signal / indigenous clock:
  https://organiser.org/2026/10/31/422606/sci-tech/isro-nvs-03-launch-news-gslv-f18-places-next-gen-navigation-satellite-in-orbit-strengthening-navic/ ;
  https://indianmasterminds.com/news/isro-nvs-03-satellite-navic-248540/ (orbit manoeuvres completed 4 Nov 2026).
  Not used: any count of NavIC satellites now in service (no source gives one).

## Law
- BNSS, 2023, s.94: a Court, or the officer in charge of a police station by a written order (physical or electronic),
  can require production of any document, electronic communication or communication device likely to contain digital
  evidence: https://www.writinglaw.com/section-94-bnss/ ; use for location/CDR data also in EP01 sources (SCC Online,
  LiveLaw).
- BSA, 2023, s.63: electronic records are admissible on conditions; s.63(4) certificate must accompany the record:
  https://www.advocatekhoj.com/library/bareacts/bharatiyaaakshya2023/63.php
- Supreme Court, 8 July 2024 (Google Maps PIN bail-condition case, 2024 LiveLaw (SC) 441): "There can't be a bail
  condition enabling the police to constantly track the movement of the accused"; such a condition would let police
  "virtually peep into the private life of the accused" (Article 21); the PIN condition was deleted:
  https://livelaw.in/supreme-court/bail-condition-enabling-police-to-constantly-track-movement-of-accused-cant-be-imposedsupremecourt-262556 ;
  https://www.barandbench.com/news/sharing-google-pin-location-as-bail-condition-hit-by-right-to-privacy-under-article-21-supreme-court
  (parties not named in the reel).

## Recent news (last 30 days)
- NVS-03 launch (30 Oct 2026) used as the NavIC news peg (above). No change in the law on location data found.
