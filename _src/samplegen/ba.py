#!/usr/bin/env python3
"""Before/after colour-grade samples for Flow Studio's Video Editing folder.
landscape source -> 1280x720 with a moving wipe; portrait source -> two 9:16 panes side by side."""
import subprocess, sys, os
from PIL import Image
import os
S = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'samples')) + '/'
OUT = os.path.dirname(os.path.abspath(__file__)) + '/out/'
os.makedirs(OUT, exist_ok=True)
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FL = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BADGE = os.path.dirname(os.path.abspath(__file__)) + '/badge.png'
# badge sized for 1280 wide frames (30% of width)
b = Image.open(BADGE); bw = 330; b.resize((bw, round(b.height * bw / b.width)), Image.LANCZOS).save(OUT + '_badge1280.png')
FLAT = "eq=contrast=0.72:saturation=0.42:brightness=0.05:gamma=1.12,curves=all='0/0.08 1/0.92'"
GRADE = "eq=contrast=1.07:saturation=1.12:gamma=0.98,unsharp=5:5:0.7,vignette=PI/5"
def label(txt, x, y, size=26, box='0x101218@0.62'):
    return f"drawtext=fontfile={F}:text='{txt}':x={x}:y={y}:fontsize={size}:fontcolor=white:box=1:boxcolor={box}:boxborderw=12"

def land(src, out, dur):
    fc = (f"[0:v]scale=1280:720:force_original_aspect_ratio=increase:flags=lanczos,crop=1280:720,fps=25,split[a][b];"
          f"[a]{FLAT}[raw];[b]{GRADE}[fin];"
          f"color=black:s=1280x720:r=25:d={dur},format=gray,geq=lum='if(lt(X,W*(0.5-0.38*cos(2*PI*T/{dur}))),255,0)'[m];"
          f"color=black:s=1280x720:r=25:d={dur},format=rgba,geq=r=255:g=255:b=255:a='if(lt(abs(X-W*(0.5-0.38*cos(2*PI*T/{dur}))),2),235,0)'[ln];"
          f"[raw][fin][m]maskedmerge[mm];[mm][ln]overlay=0:0,format=yuv420p,"
          + label('AFTER · FLOW STUDIO GRADE', 28, 28) + ',' + label('BEFORE · RAW', 'w-tw-40', 28) +
          "[v];[v][1:v]overlay=W-w-14:H-h-14")
    return fc

def port(src, out, dur):
    fc = (f"[0:v]scale=404:718:force_original_aspect_ratio=increase:flags=lanczos,crop=404:718,fps=25,split[a][b];"
          f"[a]{FLAT}[raw];[b]{GRADE}[fin];"
          f"color=0x0b0c12:s=1280x720:r=25:d={dur}[bg];"
          f"[bg][raw]overlay=196:1[t1];[t1][fin]overlay=680:1,"
          f"drawbox=x=196:y=1:w=404:h=718:color=white@0.25:t=2,drawbox=x=680:y=1:w=404:h=718:color=0xff3d9a@0.9:t=3,"
          + label('BEFORE · RAW', 210, 16, 20) + ',' + label('AFTER · GRADED', 694, 16, 20, '0xff3d9a@0.85') + ','
          f"drawtext=fontfile={F}:text='→':x=618:y=330:fontsize=46:fontcolor=white,format=yuv420p[v];[v][1:v]overlay=W-w-14:H-h-14")
    return fc

def run(name, src):
    p = S + src + '.mp4'
    w, h, d = subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height:format=duration', '-of', 'csv=p=0:s=,', p]).decode().split()[0:2] + [None]
    W, H = map(int, subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', p]).decode().strip().split(','))
    dur = min(8.0, float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]).decode().strip()))
    fc = land(p, name, dur) if W > H else port(p, name, dur)
    subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-t', str(dur), '-i', p, '-i', OUT + '_badge1280.png', '-filter_complex', fc, '-t', str(dur),
                    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-an', OUT + name + '.mp4'], check=True)
    subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-ss', str(dur * 0.62), '-i', OUT + name + '.mp4', '-frames:v', '1', '-q:v', '3', OUT + name + '.jpg'], check=True)
    print('ok', name)

if __name__ == '__main__':
    for pair in sys.argv[1:]:
        n, s = pair.split('=')
        run(n, s)
