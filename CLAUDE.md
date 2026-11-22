# Digital Crimes — daily reel production

Instructions for Claude. This repository produces and hosts the daily reels for the Instagram channel
**@digital_crimes** (cyber law and cyber forensics awareness, India). The owner is a practising advocate,
so every reel is also bound by the Bar Council of India's rules (see "Legal rules"). The repository is
public: never put client information, personal data or secrets in it.

- Instagram posting: **Windsor.ai for Social Media** connector — connector `instagram`,
  account `17841412954133912` (digital_crimes), action `create_video_post`.
- Public file host: GitHub Pages, `https://shivashankarreddy235-alt.github.io/digital-crimes-reels/`
- Owner's decisions: review before every post · posts go live at **1:00 PM IST** · odd episodes in
  **English**, even episodes in **Hinglish** (Hindi in Latin script) · original synthesized music only.

## Layout

```
engine/reel_template.html   visual engine + EP01 scenes (copy per episode; keep the ENGINE section)
engine/render.py            stills | build | voice  (see its docstring)
engine/audio.py             original score + sound effects, driven by window.TIMELINE
content/calendar.md         episode schedule (date, language, topic, hook, law) + topic bank
episodes/YYYY-MM-DD/        reel.html, reel.mp4, cover.jpg, caption.txt, script.md, sources.md, status.json
```

`status.json`: `{"episode": n, "date": "YYYY-MM-DD", "topic": "...", "language": "English|Hinglish",
"status": "pending|approved|posted|skipped", "approved_at": null, "posted_at": null, "media_id": null}`

## Run A — make tomorrow's reel (evening run)

1. D = tomorrow's date in IST. Take D's row in `content/calendar.md`. If there is none, take the next
   topic from the topic bank, add a row (next episode number, alternate language) and use it.
   If `episodes/D/status.json` already exists with status pending/approved/posted, stop and tell the owner.
2. **Verify the law first.** For every section, Act and claim you plan to use, open (WebFetch) a bare-Act
   page and at least one reputable source (LiveLaw, Bar & Bench, SCC Online, India Code, PIB, MHA/I4C,
   RBI). Search for news from the last 30 days that changes the law or gives a better hook. Old law
   (IPC, CrPC, Evidence Act) is cited only as "old law". If a point cannot be verified, drop it.
   Write `episodes/D/sources.md` listing every page opened, with what it supports.
3. **Script** (`episodes/D/script.md`): 40–55 seconds, 6–8 scenes. Hook in the first 2 seconds (the
   scammer's words, a myth, or a shocking fact). One legal point per scene, section numbers on screen.
   Close with the action viewers should take (1930 / cybercrime.gov.in / the right forum, where relevant),
   then the outro "Save this · Share it ..." and the disclaimer. For each scene give: time range,
   on-screen text, and the voiceover in the episode's language (about 2.5 words per second).
4. **Build the reel.** Copy `engine/reel_template.html` to `episodes/D/reel.html`. Leave the ENGINE
   section untouched. Rewrite the SCENES section and `window.TIMELINE` (bounds must equal the SCENES
   start times; every visual beat gets a sound `pop`; impacts get `shake` + `impacts`). Reuse the
   existing components: `tag`, `head`, `card`, the step timeline (sHow), the statute card with typing
   (sLaw), the section cards (sOff), the red-flag rows (sFlags), the big number (sAct), the outro (sOut).
   Update the outro's "Laws cited" line to the Acts actually used.
5. **Look before rendering:** `python3 engine/render.py stills episodes/D <4–8 busiest times>` and Read
   `episodes/D/.work/stills/sheet.jpg`. Fix overlaps, overflow and safe-zone problems: key content stays
   between y=250 and y=1520; nothing important below y=1560 or right of x=980 below y=1100
   (Instagram's caption and buttons sit there). Text must be readable on a phone: body ≥ 30 px.
6. `python3 engine/render.py build episodes/D` → `reel.mp4` (about 10 MB) + `cover.jpg`. Extract and
   look at 3 frames from the finished video.
7. Write `caption.txt` (format below) and `status.json` (status `pending`).
8. Run the **pre-post checklist**. Then `git add` (never `.work/`), commit
   `EPnn: <topic> (pending review)`, push to `main`.
9. Send the owner the reel and cover (SendUserFile), then one message (SendUserMessage) with: the
   caption, the voiceover script in the episode's language, and: "Reply **post** to approve it for
   1:00 PM tomorrow, tell me what to change, or send a voice note reading the script and I'll add your
   voice. Reply **skip** to skip tomorrow."
10. When the owner replies in that session:
    - **post / approve** → status `approved`, `approved_at` = now; commit and push. If it is already
      past 1:00 PM IST on D, publish now (Run B, steps 3–6).
    - **changes** → edit, rebuild, re-send, wait again.
    - **a voice file** → it must be ≤ TIMELINE.T − 0.5 s; if longer, stretch scene timings in
      reel.html and rebuild first. Then `python3 engine/render.py voice episodes/D <file>`, check it,
      commit, push, re-send for approval. A recording of the owner is a real voice: no AI label.
      If an AI-cloned voice is ever used, add "AI voiceover in my own voice." to the caption and remind
      the owner to switch on Instagram's AI label (required by Meta and the IT Amendment Rules 2026).
    - **skip** → status `skipped`; commit and push.

## Run B — publish the approved reel (12:59 PM IST)

1. D = today's date in IST. Read `episodes/D/status.json`.
2. Status `posted` → stop (never post twice). Status not `approved` → do not post; tell the owner
   "Today's reel isn't approved yet. Open last evening's review and reply post, or skip." and stop.
3. `video_url` = `https://shivashankarreddy235-alt.github.io/digital-crimes-reels/episodes/D/reel.mp4`,
   `cover_url` = the same folder's `cover.jpg`.
4. Windsor.ai `execute_action`: connector `instagram`, account `17841412954133912`, action
   `create_video_post`, params `{"video_url": ..., "cover_url": ..., "caption": <caption.txt exactly>,
   "share_to_feed": true}`. Post only the approved file and caption, nothing else.
5. Success → status `posted`, `posted_at`, `media_id` (and permalink if returned). `git rm` the
   `reel.mp4` (Instagram keeps its own copy; keep everything else), commit `EPnn posted`, push.
   Tell the owner it is live, with the link.
6. Failure → retry once at most. Then tell the owner the exact error and leave status `approved`.

## Legal rules (non-negotiable)

The owner is an advocate: BCI Rule 36 and the BCI social media circular of 17 July 2026 allow only
accurate, non-promotional, non-sensational legal awareness.

- No solicitation: no "DM me", "contact us", phone/WhatsApp numbers, "book a consultation", case wins,
  client stories or testimonials, "guaranteed" outcomes, "best lawyer" claims. Never mention the
  owner's practice or cases.
- No paid promotions, sponsorships, collaborations or affiliate links.
- No court content: nothing filmed in or about specific hearings; no clips of live-streamed proceedings.
- No client facts, names, documents or account details — use hypotheticals and reported judgments.
- No synthetic real people: never depict a real judge, court, officer, advocate or litigant.
  No photos of real people. Mock phone screens only, with "Unknown number" — never a real number.
- No State Emblem, police/CBI/ED or other official logos, uniforms or seals.
- Never identify victims of sexual offences (BNS s.72, POCSO s.23) — including sextortion and
  deepfake-abuse victims. No minors' details.
- Pending matters: allegations stay allegations; no prejudging; no naming private accused persons.
- Explain red flags and the law, never the method (no hacking steps, mule-account set-ups, evasion).
- Copyright: original visuals and the engine's own music only; quote Acts and judgments with
  commentary; never copy database headnotes or another creator's script, visuals or audio.
- Every reel ends with "Legal awareness only · Not legal advice" and the Acts cited.

## Caption format (caption.txt, 80–130 words, plain text)

```
<line 1: the hook, repeated>

<2–3 sentences: the law, with section numbers>

<1 action line: 1930 / cybercrime.gov.in / Sanchar Saathi (Chakshu) / right forum>

Save this and send it to someone who needs it.

Legal awareness only. Not legal advice.

#Topic #CyberLaw #CyberSafety #<Hindi/Hinglish or second topic tag> #DigitalCrimes
```

Exactly 5 hashtags. Hinglish episodes: caption in Hinglish (Latin script), same structure.

## Pre-post checklist (run before every push for review)

1. Every section number and Act name verified against a bare Act page (sources.md).
2. Nothing asks viewers to contact, hire or message the owner.
3. No identifiable client, victim, accused person, judge or officer; no real numbers or accounts.
4. No emblem or agency logo; no real people; no crime how-to.
5. Disclaimer and "Laws cited" on the outro; caption has the disclaimer and 5 hashtags.
6. Safe zones respected; frames checked by eye; length 40–60 s; file ≤ 100 MB.

## Housekeeping

- `.work/` folders are never committed (see .gitignore).
- Videos are removed after posting, so the repository stays small. If it ever passes 800 MB,
  tell the owner.
- Keep `content/calendar.md` status column current (pending → approved → posted / skipped).
