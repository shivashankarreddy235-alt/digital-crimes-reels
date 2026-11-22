# Digital Crimes — daily reel production

Instructions for Claude. This repository produces and hosts the daily reels for the Instagram channel
**@digital_crimes**: cyber law, cyber forensics and the technology behind cyber crime, explained for India.
The owner is a practising advocate, so every reel is bound by the Bar Council of India's rules
(see "Legal rules"). The repository is public: never put client information, personal data, voice
recordings or secrets in it.

- Instagram posting: **Windsor.ai for Social Media** — connector `instagram`, account
  `17841412954133912` (digital_crimes), action `create_video_post`.
- Public file host: GitHub Pages, `https://shivashankarreddy235-alt.github.io/digital-crimes-reels/`
- Owner's decisions: review before every post · posts go live at **7:00 AM IST** · reels are
  **90–120 seconds** · on-screen text always **English** · voice alternates: odd episodes **English
  voice**, even episodes **Hindi voice** · voice = the owner's own ElevenLabs voice clone (see "Voice") ·
  original synthesized music only · the owner's logo in `assets/logo.png` when present.

## Content mix

Follow `content/calendar.md`. The rhythm is two technology/forensics episodes, then one client topic:
- **Technology**: how GPS, cell towers, SIM cards, IMEI, walkie-talkies, IP addresses, UPI, encryption etc.
  actually work, explained simply with diagrams.
- **Forensics**: how investigators catch criminals (CDR, tower dumps, IPDR, device extraction, hash values,
  metadata) and how evidence is proved in court.
- **Client topics** (every third episode): digital arrest scams and bank account freezing / getting a
  frozen account released — general legal awareness only, never the owner's own cases.

**Explain, never enable.** Explain how a technology works and how investigators use it. Never give
steps to tamper with an IMEI, spoof a caller ID, clone a SIM, intercept signals, hide from tracing or
evade investigation. Where tampering is itself an offence (e.g. telecom identifiers under the
Telecommunications Act, 2023 — verify the section), say so.

## Layout

```
engine/reel_template.html  engine v2 + EP01 (tower) scenes and the component library — copy per episode
engine/render.py           vo | stills | build | finish | voice   (see its docstring)
engine/audio.py            original score + sound effects, driven by window.TIMELINE
engine/voice_action.py     run by .github/workflows/voiceover.yml (ElevenLabs TTS + mixing, on GitHub)
assets/logo.png            owner's logo (optional; engine falls back to the shield)
content/calendar.md        schedule (date, voice language, type, topic, hook, facts) + topic bank
episodes/YYYY-MM-DD/       reel.html, vo_request.json, voice/durations.json, mix/, reel.mp4, cover.jpg,
                           caption.txt, script.md, sources.md, status.json
```

`status.json`: `{"episode": n, "date": "YYYY-MM-DD", "topic": "...", "language": "...",
"status": "pending|approved|posted|skipped", "approved_at": null, "posted_at": null, "media_id": null}`

## Run A — make tomorrow's reel (evening run, 6:40 PM IST)

1. D = tomorrow's date in IST. Take D's row in `content/calendar.md` (if none, take the next topic
   from the topic bank keeping the 2:1 rhythm, add a row, alternate the voice language).
   If `episodes/D/status.json` exists: `approved`/`posted` → stop and tell the owner; `pending` →
   re-send it for review (step 11) instead of rebuilding. Exception: if it went out music-only and its
   `voice/durations.json` says `ok: false`, retry the voice (step 5, bump `"attempt"`); if the voice now
   works, continue from step 6 and re-send the voiced version.
2. **Verify first.** For every legal section, technical claim and number, open (WebFetch) a bare-Act page
   or primary source and at least one reputable source (LiveLaw, Bar & Bench, SCC Online, India Code,
   PIB, DoT, TRAI, MHA/I4C, RBI, ISRO, manufacturer or standards docs). Search the last 30 days for news
   that changes the law or gives a better hook. Old law (IPC, CrPC, Evidence Act) only as "old law".
   Unverifiable → drop it. Write `episodes/D/sources.md` (every page opened, what it supports).
3. **Script** (`episodes/D/script.md`): 90–120 s, 10–13 scenes. Hook in the first 2 seconds. One idea
   per scene; show the technology as a diagram, not just text. Section numbers on screen. Close with a
   takeaway, the outro and the disclaimer. Per scene: id, default length, on-screen text, voiceover.
   Voiceover runs about 2.5 words per second (≈ 230–280 words in total).
   Hindi-voice episodes: write the `vo` lines in **Hindi (Devanagari)**, natural spoken Hindi; keep
   technical/legal terms in English where people say them that way (CDR, IMEI, Section 94, BNSS).
4. **Build the reel.** Copy `engine/reel_template.html` to `episodes/D/reel.html`. Keep the ENGINE
   section unchanged; rewrite the EPISODE section: scene functions (local time `lt`, length `D`) and
   `window.EPISODE` (title, voice 'English'|'Hindi', laws, cover, scenes with `dur`, sounds and `vo`).
   Reuse the components: tower, sector, waves, phone, sim, mapPanel, dataTable, lawCard, pill, card,
   iPin and the icons; add new drawing helpers inside the EPISODE section when a topic needs them.
   Every visual beat gets a `pop`; big reveals get an `impact`.
5. `python3 engine/render.py vo episodes/D` → `vo_request.json`. Commit it with reel.html and push:
   the GitHub Action makes the voice clips (about 1–3 minutes) and commits `voice/durations.json`.
   Poll with `git pull` every 20 s for up to 10 minutes.
   - durations `ok: true` → the voice is ready.
   - `ok: false` (e.g. secrets missing) or no answer → continue music-only and tell the owner why.
   To retry later, change `"attempt"` in vo_request.json (add it if missing) and push.
6. **Look before rendering:** `python3 engine/render.py stills episodes/D <6–12 busiest times>`
   (scene starts are printed; they already include the voice stretch). Read the sheet. Fix overlaps,
   overflow and safe zones: key content between y=250 and y=1520; nothing important below y=1560 or
   right of x=980 below y=1100. Body text ≥ 30 px.
7. `python3 engine/render.py build episodes/D`.
   - Voice ready → it writes `mix/music.m4a` + `mix/mix_request.json`. Commit both, push, poll for
     `mix/mixed.json` (ok + matching hash, usually under 2 minutes), then
     `python3 engine/render.py finish episodes/D` → `reel.mp4` + `cover.jpg`.
   - No voice → it writes a music-only `reel.mp4` + `cover.jpg` directly.
   Extract and look at 3 frames from the finished video; check the length is 90–125 s.
8. Write `caption.txt` (format below) and `status.json` (status `pending`). If the AI voice is in the reel,
   the caption must include the line `Voiceover: AI-generated in my own voice.` (the reel also shows
   an "AI VOICE" tag automatically).
9. Run the **pre-post checklist**. Commit `EPnn: <topic> (pending review)` (never `.work/`), push.
10. Update the Status column in `content/calendar.md`.
11. Send the owner the reel and cover (SendUserFile), then one message (SendUserMessage): the caption,
    the voiceover script, whether the AI voice is in it, and: "Reply **post** to approve it for 7:00 AM
    tomorrow, tell me what to change, or send a voice note and I'll use your real voice instead.
    Reply **skip** to skip tomorrow."
12. When the owner replies in that session:
    - **post / approve** → status `approved`, `approved_at` = now; commit and push. If it is already past
      7:00 AM IST on D, publish now (Run B, steps 3–6).
    - **changes** → edit, rebuild (re-run `vo` if voice lines changed), re-send, wait again.
    - **a voice file** (the owner's real voice) → `python3 engine/render.py voice episodes/D <file>`
      (needs `.work/` from a music-only build; rebuild music-only first if needed, and stretch scenes if
      the file is longer than the reel). Remove the AI-voice caption line. Commit, push, re-send.
    - **skip** → status `skipped`; commit and push.

## Run B — publish the approved reel (6:59 AM IST)

1. D = today's date in IST. Read `episodes/D/status.json`.
2. `posted` → stop (never post twice). `skipped` → stop silently. Missing or not `approved` → do not
   post; tell the owner "Today's reel isn't approved yet. Open last evening's review and reply post,
   or skip." and stop.
3. `video_url` = `https://shivashankarreddy235-alt.github.io/digital-crimes-reels/episodes/D/reel.mp4`,
   `cover_url` = the same folder's `cover.jpg`.
4. Windsor.ai `execute_action`: connector `instagram`, account `17841412954133912`, action
   `create_video_post`, params `{"video_url": ..., "cover_url": ..., "caption": <caption.txt exactly>,
   "share_to_feed": true}`. Post only the approved file and caption.
5. Success → status `posted`, `posted_at`, `media_id` (and permalink if returned). `git rm` reel.mp4 and
   `mix/music.m4a`, `mix/mixed.m4a` (Instagram keeps its own copy), commit `EPnn posted`, push, update
   the calendar. Tell the owner it is live, with the link. If the reel has the AI voice, remind them that
   Instagram's own "AI info" label can't be set through the API, and they can add it in the app.
6. Failure → retry once at most. Then tell the owner the exact error and leave status `approved`.

## Voice

- The voice is the **owner's own ElevenLabs Instant Voice Clone**, made by the owner from their own
  recording. Never use anyone else's voice, a sound-alike, or a stock voice presented as the owner.
- Generation runs on GitHub Actions (`.github/workflows/voiceover.yml`), using the repository secret
  `ELEVENLABS_API_KEY` and variable `ELEVENLABS_VOICE_ID`, model `eleven_multilingual_v2` (English and
  Hindi). Clean voice clips live only in the private Actions cache; only durations and the final mix
  (voice + music) are committed. Never commit raw voice files or the owner's recordings.
- Disclosure: AI voice → "AI VOICE" tag in the reel + caption line (IT Amendment Rules 2026 on
  synthetically generated information; Meta requires labels on realistic AI audio).

## Legal rules (non-negotiable)

BCI Rule 36 and the BCI social media circular of 17 July 2026 allow only accurate, non-promotional,
non-sensational legal awareness.

- No solicitation: no "DM me", "contact us", phone/WhatsApp numbers, "book a consultation", case wins,
  client stories or testimonials, "guaranteed" outcomes, "best lawyer" claims. Never mention the
  owner's practice or cases.
- No paid promotions, sponsorships, collaborations or affiliate links.
- No court content: nothing filmed in or about specific hearings; no clips of live-streamed proceedings.
- No client facts, names, documents or account details — use hypotheticals and reported judgments.
- No synthetic real people: never depict a real judge, court, officer, advocate or litigant.
  No photos of real people. Mock screens and masked sample data only — never a real number, IMEI,
  account or cell ID.
- No State Emblem, police/CBI/ED or other official logos, uniforms or seals.
- Never identify victims of sexual offences (BNS s.72, POCSO s.23), including sextortion and
  deepfake-abuse victims. No minors' details.
- Pending matters: allegations stay allegations; no prejudging; no naming private accused persons.
- Explain, never enable (see "Content mix").
- Copyright: original visuals and the engine's own music only; quote Acts and judgments with
  commentary; never copy database headnotes or another creator's script, visuals or audio.
- Every reel ends with "Legal awareness only · Not legal advice" and the laws cited.

## Caption format (caption.txt, 80–140 words, plain text, English)

```
<line 1: the hook, repeated>

<2–3 sentences: the key facts and the law, with section numbers>

<1 takeaway or action line: 1930 / cybercrime.gov.in / Sanchar Saathi / the right forum, where relevant>

Save this and send it to someone who needs it.

Legal awareness only. Not legal advice.
[Voiceover: AI-generated in my own voice.]   <- only when the AI voice is used

#Topic #CyberLaw #CyberForensics #<second topic tag> #DigitalCrimes
```

Exactly 5 hashtags.

## Pre-post checklist

1. Every section number, Act name and technical claim verified (sources.md).
2. Nothing asks viewers to contact, hire or message the owner.
3. No identifiable client, victim, accused person, judge or officer; only masked sample data.
4. No emblem or agency logo; no real people; no how-to for tampering, spoofing or evasion.
5. Disclaimer and "Laws cited" on the outro; caption has the disclaimer, AI-voice line if used, 5 hashtags.
6. Safe zones respected; frames checked by eye; length 90–125 s; file ≤ 100 MB.

## Housekeeping

- `.work/` and `.vocache/` are never committed (.gitignore).
- Videos and mixes are removed after posting so the repository stays small. Above 800 MB, tell the owner.
- Keep `content/calendar.md` Status current (pending → approved → posted / skipped).
