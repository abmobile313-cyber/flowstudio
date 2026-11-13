#!/usr/bin/env python3
"""usage: still2vid.py src.jpg dst-id [...]  -> samples/<dst>.jpg (poster+badge) and samples/<dst>.mp4 (5 s push-in + badge)"""
import subprocess, sys, os
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); B = Image.open(D + '/badge.png').convert('RGBA')
args = sys.argv[1:]
for src, dst in zip(args[::2], args[1::2]):
    im = Image.open(src).convert('RGB'); w, h = im.size
    W, H = (1280, 852) if w > h else (720, 1280)
    im = im.resize((W, H), Image.LANCZOS)
    bw = round(W * (0.30 if W > H else 0.42)); bh = round(B.height * bw / B.width); m = max(8, round(W * 0.012))
    b = B.resize((bw, bh), Image.LANCZOS); im.save('/tmp/_base.png'); b.save('/tmp/_b.png')
    p = im.copy(); p.paste(b, (W - bw - m, H - bh - m), b); p.save(f'samples/{dst}.jpg', quality=90)
    vf = f"[0:v]scale={W*2}:{H*2},zoompan=z='1+0.0016*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=125:s={W}x{H}:fps=25[v];[v][1:v]overlay={W-bw-m}:{H-bh-m},format=yuv420p"
    subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-loop', '1', '-i', '/tmp/_base.png', '-i', '/tmp/_b.png', '-filter_complex', vf, '-t', '5', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-movflags', '+faststart', '-an', f'samples/{dst}.mp4'], check=True)
    print(dst)
