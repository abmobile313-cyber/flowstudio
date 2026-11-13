import json, os, subprocess
from PIL import Image
U = '/tmp/claude-0/-home-claude/b87108f0-499a-542f-82a0-30ba3fa58006/scratchpad/'
S = '/home/claude/flowstudio/samples/'
badge = Image.open(U + 'badge.png').convert('RGBA')
res = json.load(open(U + 'wmres.json'))
R = set(json.load(open(U + 'remove2.json')))
def bsize(W, H):
    bw = round(W * (0.30 if W >= H else 0.42)); bh = round(badge.height * bw / badge.width); m = max(8, round(W * 0.012))
    return bw, bh, m
done = []
for n, (t, si, sv) in res.items():
    if n in R: continue
    import re
    need_img = si >= 21 and not re.search(r'-u\d\d$', n)
    need_vid = t == 'video' and sv is not None and sv >= 21 and not re.search(r'-u\d\d$', n)
    if need_img:
        p = S + n + '.jpg'; im = Image.open(p).convert('RGB'); W, H = im.size; bw, bh, m = bsize(W, H)
        b = badge.resize((bw, bh), Image.LANCZOS); im.paste(b, (W - bw - m, H - bh - m), b); im.save(p, quality=90)
    if need_vid:
        p = S + n + '.mp4'
        W, H = map(int, subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', p]).decode().strip().split(','))
        bw, bh, m = bsize(W, H); badge.resize((bw, bh), Image.LANCZOS).save('/tmp/_b.png')
        tmp = p + '.wm.mp4'
        r = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', p, '-i', '/tmp/_b.png', '-filter_complex', f'[0:v][1:v]overlay=W-w-{m}:H-h-{m},format=yuv420p',
                            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-c:a', 'copy', '-movflags', '+faststart', tmp])
        if r.returncode == 0: os.replace(tmp, p)
        else: print('fail', n)
    if need_img or need_vid: done.append((n, need_img, need_vid))
print(len(done), 'files watermarked')
json.dump(done, open(U + 'wm_done.json', 'w'))
