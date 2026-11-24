"""Original, royalty-free score + sound design for a Digital Crimes reel (synthesised, no samples).

Usage: python3 audio.py timeline.json out.wav
timeline.json is window.TIMELINE from the episode's reel.html (render.py writes it).
"""
import json
import sys
import wave

import numpy as np
from scipy.signal import butter, lfilter

TL = json.load(open(sys.argv[1]))
A = TL.get("audio", {})
SR = 44100
T = float(TL["T"])
N = int(T * SR)
t = np.arange(N) / SR
rng = np.random.default_rng(3)
L = np.zeros(N)
R = np.zeros(N)


def add(sig, start, gain=1.0, pan=0.0):
    i = int(start * SR)
    if i >= N or i < 0:
        return
    sig = sig[: N - i]
    L[i:i + len(sig)] += sig * gain * (1 - max(0, pan))
    R[i:i + len(sig)] += sig * gain * (1 + min(0, pan))


def env_exp(n, k):
    return np.exp(-np.arange(n) / SR * k)


def kick(f0=150, f1=45, dur=0.45, k=9):
    n = int(dur * SR)
    tt = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-tt * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env_exp(n, k)


def noise(dur):
    return rng.standard_normal(int(dur * SR))


def bp(x, lo, hi):
    b, a = butter(2, [lo / (SR / 2), hi / (SR / 2)], btype="band")
    return lfilter(b, a, x)


def hp(x, f):
    b, a = butter(2, f / (SR / 2), btype="high")
    return lfilter(b, a, x)


def lp(x, f):
    b, a = butter(2, f / (SR / 2), btype="low")
    return lfilter(b, a, x)


BEAT = 0.6  # 100 BPM
b0, b1 = A.get("beat", [TL["bounds"][1], T - 2.1])
beats = np.arange(b0, b1 + 0.01, BEAT)

# sidechain envelope from kicks
duck = np.ones(N)
for b in beats:
    i = int(b * SR)
    n = int(0.5 * SR)
    seg = 1 - 0.55 * env_exp(n, 9)
    duck[i:i + n] = np.minimum(duck[i:i + n], seg[: len(duck[i:i + n])])

# drone (A1 + E2), swells in before the beat starts
intensity = np.clip((t - (b0 - 1.6)) / 1.6, 0.35, 1.0) * np.clip((T - t) / 2.5, 0, 1)
drone = np.sin(2 * np.pi * 55 * t) + 0.5 * np.sin(2 * np.pi * 82.41 * t + 1) + 0.25 * np.sin(2 * np.pi * 110.3 * t)
drone *= 0.8 + 0.2 * np.sin(2 * np.pi * 0.25 * t)
L += drone * 0.11 * intensity * duck
R += drone * 0.11 * intensity * duck

# pad: Am F Dm E, two bars each
chords = [[220.0, 261.63, 329.63], [174.61, 220.0, 261.63], [146.83, 174.61, 220.0], [164.81, 207.65, 246.94]]
pad = np.zeros(N)
for ci, start in enumerate(np.arange(0, T, 4.8)):
    ch = chords[ci % 4]
    i0 = int(start * SR)
    i1 = min(N, int((start + 5.2) * SR))
    tt = t[i0:i1] - start
    e = np.clip(tt / 0.8, 0, 1) * np.clip((5.2 - tt) / 0.8, 0, 1)
    s = np.zeros(len(tt))
    for f in ch:
        for det in (-0.6, 0.6):
            for h, a in ((1, 1), (2, 0.35), (3, 0.15)):
                s += a * np.sin(2 * np.pi * (f + det) * h * tt + h)
    pad[i0:i1] += s * e
pad = lp(pad, 1800)
pg = 0.022 * duck * np.clip(intensity, 0.5, 1)
L += pad * pg
R += np.roll(pad, 300) * pg

# drums
hats_from = A.get("hats_from", b0)
snare_from = A.get("snare_from", b0)
for i, b in enumerate(beats):
    add(kick(), b, 0.55)
    if b >= hats_from:
        add(hp(noise(0.035), 7000) * env_exp(int(0.035 * SR), 90), b + BEAT / 2, 0.10, pan=0.3)
    if b >= snare_from and i % 2 == 1:
        add(bp(noise(0.18), 900, 5000) * env_exp(int(0.18 * SR), 22), b, 0.16, pan=-0.1)

# phone ring (generic two-tone + vibration buzz)
for a, b in A.get("ring", []):
    n = int((b - a) * SR)
    tt = np.arange(n) / SR
    f = np.where(np.floor(tt * 12) % 2 == 0, 1318.5, 1046.5)
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.5 + 0.2 * np.sin(4 * np.pi * np.cumsum(f) / SR)
    edge = np.clip(tt / 0.02, 0, 1) * np.clip((b - a - tt) / 0.03, 0, 1)
    buzz = lp(np.sign(np.sin(2 * np.pi * 150 * tt)), 400) * 0.6
    add((tone * 0.16 + buzz * 0.10) * edge, a)

# risers
for at in A.get("riser", []):
    n = int(0.6 * SR)
    tt = np.arange(n) / SR
    add(bp(noise(0.6), 600, 6000) * (tt / 0.6) ** 2, at, 0.18)


def impact(at, g=1.0):
    add(kick(120, 32, 1.2, 4), at, 0.8 * g)
    add(lp(noise(0.25), 3000) * env_exp(int(0.25 * SR), 16), at, 0.35 * g)
    add(hp(noise(0.9), 2500) * env_exp(int(0.9 * SR), 5), at, 0.07 * g, pan=0.4)


for at, g in A.get("impacts", []):
    impact(at, g)


def whoosh(at):
    d = 0.55
    n = int(d * SR)
    tt = np.arange(n) / SR
    e = np.where(tt < 0.3, (tt / 0.3) ** 2, np.exp(-(tt - 0.3) * 14))
    x = noise(d)
    mix = bp(x, 300, 2500) * (1 - tt / d) + bp(x, 2500, 9000) * (tt / d)
    add(mix * e, at - 0.3, 0.22, pan=0.2)
    add(np.roll(mix, 400) * e, at - 0.3, 0.12, pan=-0.6)


for b in TL["bounds"][1:-1]:
    whoosh(b)


def pop(at, f=880, g=0.13):
    n = int(0.09 * SR)
    tt = np.arange(n) / SR
    fr = f * (1 + 0.5 * np.clip(tt / 0.04, 0, 1))
    add(np.sin(2 * np.pi * np.cumsum(fr) / SR) * env_exp(n, 40), at, g)


def sting(at, g=1.0):
    """Chapter-card sting: short noise rise into an A-minor stab with a low thud (fits the Am score)."""
    m = int(0.28 * SR)
    tr = np.arange(m) / SR
    add(bp(noise(0.28), 1500, 8000) * (tr / 0.28) ** 3, at - 0.28, 0.10 * g, pan=0.2)
    d = 0.9
    n = int(d * SR)
    tt = np.arange(n) / SR
    s = np.zeros(n)
    for f in (220.0, 440.0, 523.25, 659.25):
        s += np.sign(np.sin(2 * np.pi * f * tt)) * 0.25 + 0.3 * np.sin(2 * np.pi * f * 2 * tt)
    s = lp(s, 3200) * env_exp(n, 4.5)
    add(s, at, 0.075 * g, pan=-0.25)
    add(np.roll(s, 380), at, 0.06 * g, pan=0.35)
    add(kick(95, 38, 0.6, 7), at, 0.5 * g)


for at in A.get("sting", []):
    sting(at)


def chime(at, g=1.0):
    """Generic notification chime (two soft sine notes, E6 then A6)."""
    for k, f in enumerate((1318.5, 1760.0)):
        n = int(0.35 * SR)
        tt = np.arange(n) / SR
        add((np.sin(2 * np.pi * f * tt) + 0.2 * np.sin(4 * np.pi * f * tt)) * env_exp(n, 9), at + k * 0.09, 0.07 * g, pan=0.15)


for at in A.get("chime", []):
    chime(at)

for p in A.get("pops", []):
    pop(p[0], p[1] if len(p) > 1 else 880, p[2] if len(p) > 2 else 0.13)

for a, b in A.get("typing", []):
    for at in np.arange(a, b, 0.055):
        if rng.random() < 0.8:
            add(hp(noise(0.012), 3000) * env_exp(int(0.012 * SR), 300), at, 0.045, pan=rng.uniform(-0.3, 0.3))

# master
fade = np.clip((T - t) / 1.2, 0, 1) * np.clip(t / 0.05, 0, 1)
mx = np.stack([L * fade, R * fade], 1)
mx = np.tanh(mx * 1.3) / np.tanh(1.3)
mx /= np.max(np.abs(mx)) / 0.89
pcm = (mx * 32767).astype(np.int16)
with wave.open(sys.argv[2], "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
