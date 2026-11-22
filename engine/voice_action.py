"""Voiceover step, run by .github/workflows/voiceover.yml on GitHub Actions (which has internet access).

Two jobs, picked automatically:
  tts  - episodes/D/vo_request.json changed -> ElevenLabs TTS, one clip per scene, kept only in the
         private Actions cache (clean voice clips are never committed to this public repo);
         commits episodes/D/voice/durations.json (clip lengths, used to time the scenes).
  mix  - episodes/D/mix/mix_request.json changed -> places the clips at the scene offsets, ducks
         the music under the voice, commits episodes/D/mix/mixed.m4a (voice + music only).

Needs repo secret ELEVENLABS_API_KEY and repo variable ELEVENLABS_VOICE_ID (the owner's own
cloned voice). Without them it writes ok:false with the reason, and the reel goes out music-only.

  python3 engine/voice_action.py plan   -> prints key=value lines for $GITHUB_OUTPUT
  python3 engine/voice_action.py run    -> does the job chosen by plan
"""
import glob
import hashlib
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

CACHE = ".vocache"


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]


def load(path, default=None):
    try:
        return json.load(open(path))
    except Exception:
        return default


def plan():
    for ep in sorted(glob.glob("episodes/*"), reverse=True):
        req = os.path.join(ep, "vo_request.json")
        mreq = os.path.join(ep, "mix", "mix_request.json")
        if os.path.exists(req):
            h = sha(req)
            done = load(os.path.join(ep, "voice", "durations.json"), {})
            if done.get("request_hash") != h or not done.get("ok"):
                return {"mode": "tts", "ep": ep, "hash": h}
            if os.path.exists(mreq):
                mh = sha(mreq)
                mdone = load(os.path.join(ep, "mix", "mixed.json"), {})
                if mdone.get("mix_hash") != mh:
                    return {"mode": "mix", "ep": ep, "hash": h, "mix_hash": mh}
    return {"mode": "none"}


def tts_clips(ep, h):
    """Make (or reuse cached) one MP3 per non-empty segment. Returns list of paths or None per segment."""
    req = json.load(open(os.path.join(ep, "vo_request.json")))
    key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    voice = os.environ.get("ELEVENLABS_VOICE_ID", "").strip()
    out_dir = os.path.join(CACHE, h)
    os.makedirs(out_dir, exist_ok=True)
    clips = []
    for i, seg in enumerate(req["segments"]):
        text = (seg.get("text") or "").strip()
        if not text:
            clips.append(None)
            continue
        f = os.path.join(out_dir, f"seg{i:02d}.mp3")
        if not os.path.exists(f) or os.path.getsize(f) < 1000:
            if not key or not voice:
                raise RuntimeError("ELEVENLABS_API_KEY secret or ELEVENLABS_VOICE_ID variable is not set")
            body = {"text": text, "model_id": req.get("model_id", "eleven_multilingual_v2"),
                    "voice_settings": req.get("voice_settings", {"stability": 0.45, "similarity_boost": 0.85,
                                                                 "style": 0.15, "use_speaker_boost": True})}
            r = urllib.request.Request(
                f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128",
                data=json.dumps(body).encode(), method="POST",
                headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"})
            try:
                with urllib.request.urlopen(r, timeout=180) as resp:
                    open(f, "wb").write(resp.read())
            except urllib.error.HTTPError as e:
                raise RuntimeError(f"ElevenLabs HTTP {e.code}: {e.read()[:300].decode('utf-8', 'replace')}")
        clips.append(f)
    return clips


def dur(f):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                         capture_output=True, text=True).stdout.strip()
    return round(float(out), 3)


def run():
    p = plan()
    if p["mode"] == "none":
        print("nothing to do")
        return
    ep, h = p["ep"], p["hash"]
    if p["mode"] == "tts":
        os.makedirs(os.path.join(ep, "voice"), exist_ok=True)
        res = {"request_hash": h, "ok": False, "durations": [], "error": None}
        try:
            clips = tts_clips(ep, h)
            res["durations"] = [dur(c) if c else 0 for c in clips]
            res["ok"] = True
        except Exception as e:  # report, never crash: the reel can still go out music-only
            res["error"] = str(e)
        json.dump(res, open(os.path.join(ep, "voice", "durations.json"), "w"), indent=1)
        print(json.dumps(res))
        return
    # mix
    mreq = json.load(open(os.path.join(ep, "mix", "mix_request.json")))
    res = {"mix_hash": p["mix_hash"], "ok": False, "error": None}
    try:
        clips = tts_clips(ep, h)
        music = os.path.join(ep, "mix", "music.m4a")
        inputs, parts, labels = ["-i", music], [], []
        n = 0
        for i, c in enumerate(clips):
            if not c:
                continue
            n += 1
            ms = int(round(mreq["offsets"][i] * 1000))
            inputs += ["-i", c]
            parts.append(f"[{n}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={ms}|{ms}[c{n}]")
            labels.append(f"[c{n}]")
        T = float(mreq["T"])
        fc = ";".join(parts) + ";" + "".join(labels) + (
            f"amix=inputs={n}:normalize=0,highpass=f=80,loudnorm=I=-16:TP=-2:LRA=9,apad,asplit=2[v1][v2];"
            "[0:a]volume=0.55[m];[m][v1]sidechaincompress=threshold=0.03:ratio=6:attack=15:release=350[md];"
            f"[md][v2]amix=inputs=2:duration=first:normalize=0,atrim=0:{T},loudnorm=I=-14:TP=-1.5:LRA=11[a]")
        out = os.path.join(ep, "mix", "mixed.m4a")
        r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", fc, "-map", "[a]",
                            "-c:a", "aac", "-b:a", "192k", "-ar", "44100", out], capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError("ffmpeg: " + r.stderr[-500:])
        res["ok"] = True
    except Exception as e:
        res["error"] = str(e)
    json.dump(res, open(os.path.join(ep, "mix", "mixed.json"), "w"), indent=1)
    print(json.dumps(res))


if __name__ == "__main__":
    if sys.argv[1] == "plan":
        for k, v in plan().items():
            print(f"{k}={v}")
    else:
        run()
