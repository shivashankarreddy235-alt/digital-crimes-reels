"""Digital Crimes reel renderer (engine v2).

  python3 engine/render.py vo     EP            # write EP/vo_request.json from the scenes' `vo` lines
  python3 engine/render.py stills EP t1 t2 ...  # look at frames before a full render
  python3 engine/render.py build  EP            # render; see below
  python3 engine/render.py finish EP            # after the Action mixed the voice: -> reel.mp4 + cover.jpg
  python3 engine/render.py voice  EP FILE       # owner's own recorded voiceover (one file) instead of AI voice

build:
  - If EP/voice/durations.json exists with ok:true and matches EP/vo_request.json, every scene is set
    to max(its `min`, voice clip + 0.8 s), the "AI VOICE" tag is shown, and the build writes
    EP/mix/music.m4a + EP/mix/mix_request.json. Commit and push those; the GitHub Action mixes the voice
    and commits EP/mix/mixed.m4a; then run `finish`.
  - Otherwise it makes a music-only EP/reel.mp4 + EP/cover.jpg directly.
Intermediate files go to EP/.work (git-ignored).
"""
import base64
import functools
import hashlib
import http.server
import threading
import json
import os
import subprocess
import sys

from playwright.sync_api import sync_playwright

ENGINE = os.path.dirname(os.path.abspath(__file__))
FPS = 30
VO_LEAD = 0.3   # voice starts this long after its scene starts
VO_TAIL = 0.5   # breathing room after the clip ends
X264 = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "22", "-maxrate", "4M", "-bufsize", "8M",
        "-pix_fmt", "yuv420p", "-r", str(FPS)]


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"command failed: {' '.join(cmd[:6])}...\n{r.stderr[-2000:]}")
    return r.stdout


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]


def voice_plan(ep):
    """Return per-scene clip durations if the AI voice is ready for the current request, else None."""
    req, d = os.path.join(ep, "vo_request.json"), os.path.join(ep, "voice", "durations.json")
    if not (os.path.exists(req) and os.path.exists(d)):
        return None
    info = json.load(open(d))
    if not info.get("ok") or info.get("request_hash") != sha(req):
        return None
    return info["durations"]


_SERVER = None


def page_url(ep):
    """Serve the repository over local HTTP so the logo images don't taint the canvas (file:// does)."""
    global _SERVER
    root = os.path.dirname(ENGINE)
    if _SERVER is None:
        class Quiet(http.server.SimpleHTTPRequestHandler):
            def log_message(self, *a):
                pass
        _SERVER = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=root))
        threading.Thread(target=_SERVER.serve_forever, daemon=True).start()
    rel = os.path.relpath(os.path.abspath(os.path.join(ep, "reel.html")), root)
    return f"http://127.0.0.1:{_SERVER.server_address[1]}/{rel}"


def open_page(p, ep):
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto(page_url(ep))
    pg.wait_for_function("window.ready===true")
    vd = voice_plan(ep)
    if vd:
        base = pg.evaluate("window.EPISODE.scenes.map(s=>[s.dur, s.min || s.dur])")
        new = [max(mn, v + VO_LEAD + VO_TAIL) if v else d for (d, mn), v in zip(base, vd + [0] * len(base))]
        pg.evaluate(f"applyDurations({json.dumps(new)})")
        pg.evaluate("setAiVoice(true)")
    return b, pg, vd


def frame(pg, t):
    d = pg.evaluate(f"renderFrame({t})")
    return base64.b64decode(d.split(",")[1])


def vo(ep):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = b.new_page()
        pg.goto(page_url(ep))
        pg.wait_for_function("window.ready===true")
        info = pg.evaluate("({voice:window.EPISODE.voice,segs:window.EPISODE.scenes.map(s=>({scene:s.id,text:s.vo||''}))})")
        b.close()
    req = {"model_id": "eleven_multilingual_v2", "language": "hi" if info["voice"] == "Hindi" else "en",
           "segments": info["segs"]}
    json.dump(req, open(os.path.join(ep, "vo_request.json"), "w"), ensure_ascii=False, indent=1)
    words = sum(len(s["text"].split()) for s in info["segs"])
    print(f"vo_request.json written: {len(info['segs'])} segments, {words} words")


def stills(ep, times):
    out = os.path.join(ep, ".work", "stills")
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b, pg, _ = open_page(p, ep)
        paths = []
        for t in times:
            f = os.path.join(out, f"t{t:06.2f}.jpg")
            open(f, "wb").write(frame(pg, t))
            paths.append(f)
        tl = pg.evaluate("window.TIMELINE")
        b.close()
    from PIL import Image
    ims = [Image.open(f).resize((540, 960)) for f in paths]
    cols = min(4, len(ims))
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (540 * cols, 960 * rows))
    for i, im in enumerate(ims):
        sheet.paste(im, ((i % cols) * 540, (i // cols) * 960))
    sheet.save(os.path.join(out, "sheet.jpg"), quality=85)
    print(os.path.join(out, "sheet.jpg"))
    print("scene starts:", [(s["id"], round(s["start"], 2)) for s in tl["scenes"]], "T =", round(tl["T"], 2))


def build(ep):
    work = os.path.join(ep, ".work")
    os.makedirs(work, exist_ok=True)
    files = []
    with sync_playwright() as p:
        b, pg, vd = open_page(p, ep)
        tl = pg.evaluate("window.TIMELINE")
        json.dump(tl, open(os.path.join(work, "timeline.json"), "w"))
        bounds = tl["bounds"]
        for i in range(len(bounds) - 1):
            f0, f1 = round(bounds[i] * FPS), round(bounds[i + 1] * FPS)
            out, tmp = os.path.join(work, f"scene{i:02d}.mp4"), os.path.join(work, f"scene{i:02d}.tmp.mp4")
            ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS),
                                   "-c:v", "mjpeg", "-i", "-", *X264, tmp], stdin=subprocess.PIPE)
            for f in range(f0, f1):
                ff.stdin.write(frame(pg, f / FPS))
            ff.stdin.close()
            if ff.wait() != 0:
                sys.exit(f"ffmpeg failed on scene {i}")
            os.replace(tmp, out)
            files.append(os.path.abspath(out))
            print(f"scene {i} done", flush=True)
        b.close()
    with open(os.path.join(work, "list.txt"), "w") as fh:
        fh.writelines(f"file '{f}'\n" for f in files)
    video = os.path.join(work, "video_only.mp4")
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", os.path.join(work, "list.txt"),
         "-c", "copy", video])
    raw, music = os.path.join(work, "music_raw.wav"), os.path.join(work, "music.wav")
    run([sys.executable, os.path.join(ENGINE, "audio.py"), os.path.join(work, "timeline.json"), raw])
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", "loudnorm=I=-15:TP=-1.5:LRA=11", "-ar", "44100", music])
    if vd:
        mix = os.path.join(ep, "mix")
        os.makedirs(mix, exist_ok=True)
        run(["ffmpeg", "-y", "-loglevel", "error", "-i", music, "-c:a", "aac", "-b:a", "160k", os.path.join(mix, "music.m4a")])
        req = {"request_hash": sha(os.path.join(ep, "vo_request.json")), "T": tl["T"],
               "offsets": [round(s["start"] + VO_LEAD, 3) for s in tl["scenes"]]}
        json.dump(req, open(os.path.join(mix, "mix_request.json"), "w"), indent=1)
        print("WAITING_FOR_MIX: commit + push mix/music.m4a and mix/mix_request.json, wait for mix/mixed.m4a, then run finish")
    else:
        mux(ep, video, music)
        cover(ep, tl["cover"])
        print("MUSIC_ONLY: reel.mp4 + cover.jpg written")


def finish(ep):
    work, mix = os.path.join(ep, ".work"), os.path.join(ep, "mix")
    req = os.path.join(mix, "mix_request.json")
    done = json.load(open(os.path.join(mix, "mixed.json")))
    if not done.get("ok") or done.get("mix_hash") != sha(req):
        sys.exit(f"mix not ready or failed: {done}")
    tl = json.load(open(os.path.join(work, "timeline.json")))
    mux(ep, os.path.join(work, "video_only.mp4"), os.path.join(mix, "mixed.m4a"))
    cover(ep, tl["cover"])
    print("reel.mp4 + cover.jpg written with voice")


def mux(ep, video, audio):
    tmp = os.path.join(ep, ".work", "reel.tmp.mp4")
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-i", audio, "-map", "0:v", "-map", "1:a",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", tmp])
    os.replace(tmp, os.path.join(ep, "reel.mp4"))


def cover(ep, t):
    run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t), "-i", os.path.join(ep, "reel.mp4"), "-frames:v", "1",
         "-q:v", "2", os.path.join(ep, "cover.jpg")])


def voice(ep, vfile):
    work = os.path.join(ep, ".work")
    video, music = os.path.join(work, "video_only.mp4"), os.path.join(work, "music.wav")
    if not (os.path.exists(video) and os.path.exists(music)):
        sys.exit("run build first (needs .work/video_only.mp4 and .work/music.wav)")
    mixed = os.path.join(work, "mixed.wav")
    fc = ("[1:a]aresample=44100,aformat=channel_layouts=stereo,highpass=f=80,"
          "loudnorm=I=-16:TP=-2:LRA=9,adelay=250|250,apad,asplit=2[v1][v2];"
          "[0:a]volume=0.55[m];[m][v1]sidechaincompress=threshold=0.03:ratio=6:attack=15:release=350[md];"
          "[md][v2]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", music, "-i", vfile, "-filter_complex", fc, "-map", "[a]",
         "-ar", "44100", mixed])
    mux(ep, video, mixed)


if __name__ == "__main__":
    cmd, ep = sys.argv[1], sys.argv[2]
    {"vo": lambda: vo(ep), "stills": lambda: stills(ep, [float(x) for x in sys.argv[3:]]), "build": lambda: build(ep),
     "finish": lambda: finish(ep), "voice": lambda: voice(ep, sys.argv[3])}.get(cmd, lambda: sys.exit(__doc__))()
