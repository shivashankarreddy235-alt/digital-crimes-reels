"""Digital Crimes reel renderer.

  python3 engine/render.py stills EPISODE_DIR t1 t2 ...   # look at frames before a full render
  python3 engine/render.py build  EPISODE_DIR             # -> EPISODE_DIR/reel.mp4 + cover.jpg (music only)
  python3 engine/render.py voice  EPISODE_DIR VOICE_FILE  # mix a voiceover in, video untouched

EPISODE_DIR must contain reel.html (a copy of engine/reel_template.html with new SCENES + TIMELINE).
Intermediate files go to EPISODE_DIR/.work (git-ignored).
"""
import base64
import json
import os
import subprocess
import sys

from playwright.sync_api import sync_playwright

ENGINE = os.path.dirname(os.path.abspath(__file__))
FPS = 30
X264 = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "22", "-maxrate", "4M", "-bufsize", "8M",
        "-pix_fmt", "yuv420p", "-r", str(FPS)]


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"command failed: {' '.join(cmd[:6])}...\n{r.stderr[-2000:]}")


def open_page(p, ep):
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto("file://" + os.path.abspath(os.path.join(ep, "reel.html")))
    pg.wait_for_function("window.ready===true")
    return b, pg


def frame(pg, t):
    d = pg.evaluate(f"renderFrame({t})")
    return base64.b64decode(d.split(",")[1])


def stills(ep, times):
    out = os.path.join(ep, ".work", "stills")
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b, pg = open_page(p, ep)
        paths = []
        for t in times:
            f = os.path.join(out, f"t{t:05.2f}.jpg")
            open(f, "wb").write(frame(pg, t))
            paths.append(f)
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


def build(ep):
    work = os.path.join(ep, ".work")
    os.makedirs(work, exist_ok=True)
    files = []
    with sync_playwright() as p:
        b, pg = open_page(p, ep)
        tl = pg.evaluate("window.TIMELINE")
        json.dump(tl, open(os.path.join(work, "timeline.json"), "w"))
        bounds = tl["bounds"]
        for i in range(len(bounds) - 1):
            f0, f1 = round(bounds[i] * FPS), round(bounds[i + 1] * FPS)
            out = os.path.join(work, f"scene{i}.mp4")
            tmp = os.path.join(work, f"scene{i}.tmp.mp4")
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
    raw = os.path.join(work, "music_raw.wav")
    run([sys.executable, os.path.join(ENGINE, "audio.py"), os.path.join(work, "timeline.json"), raw])
    music = os.path.join(work, "music.wav")
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", "loudnorm=I=-15:TP=-1.5:LRA=11", "-ar", "44100", music])
    mux(ep, video, music)
    cover(ep, tl["cover"])


def mux(ep, video, audio_wav):
    tmp = os.path.join(ep, ".work", "reel.tmp.mp4")
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-i", audio_wav, "-map", "0:v", "-map", "1:a",
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
    if cmd == "stills":
        stills(ep, [float(x) for x in sys.argv[3:]])
    elif cmd == "build":
        build(ep)
    elif cmd == "voice":
        voice(ep, sys.argv[3])
    else:
        sys.exit(__doc__)
