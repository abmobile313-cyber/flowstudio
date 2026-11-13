"""usage: stitch.py out_id clip1.mp4 clip2.mp4 ... -> samples/<out_id>.mp4 (+ .jpg)
Joins 10 s Meta AI clips with 0.6 s crossfades (video + audio), fades in/out, adds the Flow Studio badge."""
import sys, subprocess, os
out, clips = sys.argv[1], sys.argv[2:]
D = os.path.dirname(os.path.abspath(__file__)); S = os.path.join(D, '..', '..', 'samples')
X = 0.6
def dur(f): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
ds = [dur(c) for c in clips]
inp = []; fc = []
for k, c in enumerate(clips):
    inp += ['-i', c]
    fc.append(f'[{k}:v]scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=25,format=yuv420p,setsar=1[v{k}]')
    fc.append(f'[{k}:a]aresample=48000,aformat=channel_layouts=stereo[a{k}]')
vl, al, t = 'v0', 'a0', ds[0]
for k in range(1, len(clips)):
    fc.append(f'[{vl}][v{k}]xfade=transition=fade:duration={X}:offset={t - X}[vx{k}]')
    fc.append(f'[{al}][a{k}]acrossfade=d={X}[ax{k}]')
    vl, al = f'vx{k}', f'ax{k}'; t = t + ds[k] - X
inp += ['-i', os.path.join(D, 'badge.png')]
b = len(clips)
fc.append(f'[{b}]scale=384:-1[bd];[{vl}][bd]overlay=W-w-15:H-h-15,fade=t=in:d=0.4,fade=t=out:st={t-0.8}:d=0.8[vo]')
fc.append(f'[{al}]afade=t=in:d=0.3,afade=t=out:st={t-1.2}:d=1.2,loudnorm=I=-16:TP=-1.5:LRA=9,aresample=48000[ao]')
o = os.path.join(S, out + '.mp4')
subprocess.run(['ffmpeg','-nostdin','-v','error','-y',*inp,'-filter_complex',';'.join(fc),'-map','[vo]','-map','[ao]','-c:v','libx264','-preset','veryfast','-crf','21','-c:a','aac','-b:a','160k','-movflags','+faststart',o],check=True)
subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-ss',str(min(4, t/3)),'-i',o,'-frames:v','1','-q:v','3',os.path.join(S, out + '.jpg')],check=True)
print(out, round(t, 1), 's')
