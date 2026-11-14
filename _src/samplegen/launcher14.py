# Launcher theme scene A (lock screen, home screen + widgets, notification shade + quick settings, app drawer)
# for 5 UI styles x light/dark. Scene B is the phone kit (phonekit14.py). The two 6 s scenes are joined into one 12 s film.
# usage: python3 launcher14.py OUTDIR  -> ui-kNNa.html
import sys, os
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D, 'phonekit14.py')).read().split('rows = []')[0].replace("OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)", "")
ns = {'__file__': os.path.join(D, 'phonekit14.py')}; exec(src, ns)
tokens, BASE, FONT, cursor = ns['tokens'], ns['BASE'], ns['FONT'], ns['cursor']

APPS = [('Phone','✆','#34c759'),('Messages','✉','#2f8cff'),('Contacts','☺','#ff9f0a'),('Camera','◉','#5e5ce6'),('Gallery','❀','#ff375f'),('Clock','◷','#64d2ff'),('Calendar','14','#ff453a'),('Music','♫','#bf5af2'),
        ('Notes','✎','#ffd60a'),('Weather','☀','#0a84ff'),('Files','▤','#30d158'),('Settings','⚙','#8e8e93'),('Mail','@','#0a84ff'),('Maps','⌖','#32d74b'),('Calculator','±','#ff9f0a'),('Store','◆','#5e5ce6')]

def scene(id_, style, dark):
    T = tokens(style, dark); glass = T.get('glass'); bento = T.get('bento')
    blur = 'backdrop-filter:blur(18px) saturate(140%);' if glass else ''
    rad = {'skeuo': '16px', 'neu': '18px', 'clay': '20px', 'glass': '18px', 'bento': '14px'}[style]
    # app icon look per style
    if style == 'skeuo':
        icon = lambda c: f"background:linear-gradient(160deg,{c},{c}cc 55%,{c}88);box-shadow:0 1px 0 rgba(255,255,255,.55) inset,0 -3px 6px rgba(0,0,0,.25) inset,0 6px 10px rgba(0,0,0,.3);color:#fff"
    elif style == 'neu':
        icon = lambda c: f"background:{T['key']};box-shadow:{T['ks']};color:{c}"
    elif style == 'clay':
        icon = lambda c: f"background:{c};box-shadow:inset 0 5px 6px rgba(255,255,255,.5),inset 0 -6px 8px rgba(0,0,0,.22),0 8px 12px rgba(0,0,0,.22);color:#fff"
    elif style == 'glass':
        icon = lambda c: f"background:linear-gradient(135deg,{c}cc,{c}55);box-shadow:inset 0 0 0 1px rgba(255,255,255,.45);{blur}color:#fff"
    else:
        icon = lambda c: f"background:{c};color:#fff"
    wall = {
        'skeuo': ('linear-gradient(170deg,#2b3a55,#141b2a)' if dark else 'linear-gradient(170deg,#cfe0f5,#f3e7d8)'),
        'neu': T['bg'], 'clay': ('linear-gradient(170deg,#3b2d7a,#1d1640)' if dark else 'linear-gradient(170deg,#d9cfff,#ffd9ec)'),
        'glass': ('radial-gradient(circle at 30% 20%,#ff6fd855,transparent 40%),radial-gradient(circle at 80% 70%,#38c6ff55,transparent 45%),linear-gradient(160deg,#120a2a,#2a1450)' if dark else 'radial-gradient(circle at 30% 20%,#ff9ad9,transparent 40%),radial-gradient(circle at 80% 70%,#7ad7ff,transparent 45%),linear-gradient(160deg,#7b4dff,#c21fd6)'),
        'bento': ('#121018' if dark else '#ecebf3')}[style]
    wtx = '#fff' if (dark or glass or style in ('skeuo',) and dark) else T['tx']
    if style == 'skeuo' and not dark: wtx = '#1f2a3d'
    card = f"background:{T['key'] if not glass else 'rgba(255,255,255,.18)'};box-shadow:{T['ks'] if not bento else 'none'};border-radius:{rad};{blur}color:{T['tx'] if not glass else '#fff'}"
    if style == 'clay': card = f"background:{T['key']};box-shadow:{T['ks']};border-radius:22px;color:{T['tx']}"
    css = f"""
body{{background:{T['bg']}}}
.chip{{background:{'rgba(255,255,255,.14)' if (dark or glass) else '#ffffffcc'};color:{'#fff' if (dark or glass) else '#3b4252'};border:1px solid {'rgba(255,255,255,.3)' if (dark or glass) else '#0001'}}}
.mode{{left:auto;right:28px}}
.ph{{position:absolute;top:84px;width:300px;height:600px;border-radius:{'30px' if bento else '42px'};background:{wall};box-shadow:{T['phs']};overflow:hidden;animation:up .9s cubic-bezier(.2,.8,.2,1) both;color:{wtx}}}
.p1{{left:60px;animation-delay:.1s}}.p2{{left:390px;animation-delay:.3s}}.p3{{left:720px;animation-delay:.5s}}
.sb{{display:flex;justify-content:space-between;padding:14px 22px 0;font:600 12px Poppins}}
.big{{text-align:center;font:300 76px/1 Poppins;margin-top:46px;letter-spacing:-.02em}}
.dt{{text-align:center;font:500 14px Poppins;opacity:.85;margin-top:6px}}
.nt{{margin:12px 16px 0;padding:12px 14px;{card};display:flex;gap:10px;align-items:center;font:600 12px Poppins;animation:bp .5s both}}
@keyframes bp{{from{{opacity:0;transform:translateY(18px) scale(.95)}}}}
.nt i{{width:30px;height:30px;border-radius:10px;display:grid;place-items:center;font-style:normal;font-size:14px;flex:none}}
.nt small{{display:block;font:400 10.5px Poppins;opacity:.7}}
.lb{{position:absolute;bottom:26px;width:52px;height:52px;border-radius:50%;{card};border-radius:50%;display:grid;place-items:center;font-size:20px}}
.hint{{position:absolute;bottom:34px;left:0;right:0;text-align:center;font:500 11px Poppins;opacity:.7;animation:hn 1.6s 1s ease-in-out infinite}}
@keyframes hn{{50%{{transform:translateY(-6px);opacity:1}}}}
.wg{{margin:12px 16px 0;padding:14px 16px;{card};animation:pop .55s both}}
.wrow{{display:flex;gap:12px;margin:12px 16px 0}}
.wrow .wg{{margin:0;flex:1}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px 6px;padding:16px 14px 0}}
.ap{{text-align:center;font:500 9.5px Poppins;animation:pop .45s both}}
.ap i{{width:48px;height:48px;border-radius:{rad};margin:0 auto 5px;display:grid;place-items:center;font:700 19px Poppins;font-style:normal}}
.dock{{position:absolute;left:14px;right:14px;bottom:16px;height:74px;{card};border-radius:26px;display:flex;justify-content:space-around;align-items:center;animation:up .6s 1.6s both}}
.dock .ap i{{margin:0}}
.srch{{margin:14px 16px 0;height:38px;{card};border-radius:20px;display:flex;align-items:center;padding:0 14px;font:500 11.5px Poppins;opacity:.95}}
.shade{{position:absolute;inset:0;background:{'rgba(10,12,20,.55)' if dark else 'rgba(255,255,255,.35)'};backdrop-filter:blur(16px);transform:translateY(-100%);animation:sd .7s 1.3s cubic-bezier(.2,.8,.2,1) both;padding:0 0 0}}
@keyframes sd{{to{{transform:none}}}}
.qs{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:14px 16px 0}}
.qt{{height:58px;{card};display:grid;place-items:center;font:600 18px Poppins;position:relative}}
.qt.on{{background:linear-gradient(135deg,{T['acc']},{T['acc2']}) !important;color:#fff !important}}
.qt.fl{{animation:fl .3s 3.6s both}}
@keyframes fl{{to{{background:linear-gradient(135deg,#ffd60a,#ff9f0a);color:#fff}}}}
.ql{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:4px 16px 0;font:500 8.5px Poppins;text-align:center;opacity:.8}}
.br{{margin:14px 16px 0;height:34px;{card};border-radius:18px;position:relative;overflow:hidden}}
.br b{{position:absolute;left:0;top:0;bottom:0;width:64%;background:linear-gradient(90deg,{T['acc']},{T['acc2']});border-radius:18px;transform-origin:left;animation:bw 1.4s 2.4s ease-in-out both}}
@keyframes bw{{0%{{transform:scaleX(.55)}}100%{{transform:scaleX(1)}}}}
.br span{{position:absolute;left:12px;top:7px;color:#fff;font-size:15px}}
.mp{{margin:12px 16px 0;padding:12px;{card};display:flex;gap:10px;align-items:center;font:600 11.5px Poppins}}
.mp i{{width:44px;height:44px;border-radius:12px;background:linear-gradient(135deg,#ff6fa3,#7b4dff);flex:none}}
.mp .pb{{height:4px;border-radius:3px;background:#8884;margin-top:6px;overflow:hidden}}
.mp .pb b{{display:block;height:100%;width:40%;background:{T['acc']};animation:growx 4s 1.6s linear both;transform-origin:left}}
"""
    # phone 1: lock screen
    p1 = (f"<div class='sb'><span>Jio 5G</span><span>▮▮▮ 🔋 86%</span></div><div class='big'>9:41</div><div class='dt'>Saturday, 14 November</div>"
          f"<div class='nt' style='animation-delay:1.4s'><i style='{icon('#2f8cff')}'>✉</i><div>Ammi<small>Order ready hai? 🙏</small></div></div>"
          f"<div class='nt' style='animation-delay:1.8s'><i style='{icon('#34c759')}'>₹</i><div>Payment received<small>₹2,580 from Bilal Shaikh</small></div></div>"
          f"<div class='nt' style='animation-delay:2.2s'><i style='{icon('#ff9f0a')}'>◷</i><div>Fajr alarm<small>Tomorrow 5:12 AM</small></div></div>"
          f"<div class='lb' style='left:26px'>🔦</div><div class='lb' style='right:26px'>📷</div><div class='hint'>⌃ Swipe up to open</div>")
    # phone 2: home screen with widgets + icons + dock
    apps = ''.join(f"<div class='ap' style='animation-delay:{1.0+i*.06:.2f}s'><i style='{icon(c)}'>{g}</i>{n}</div>" for i, (n, g, c) in enumerate(APPS[4:16]))
    dock = ''.join(f"<div class='ap' style='animation-delay:{1.7+i*.08:.2f}s'><i style='{icon(c)}'>{g}</i></div>" for i, (n, g, c) in enumerate(APPS[:4]))
    p2 = (f"<div class='sb'><span>9:41</span><span>▮▮▮ 5G 🔋</span></div>"
          f"<div class='wg' style='animation-delay:.8s;display:flex;justify-content:space-between;align-items:center'><div><div style='font:300 34px Poppins;line-height:1'>9:41</div><div style='font:500 10.5px Poppins;opacity:.7'>Sat, 14 Nov · Nashik</div></div><div style='text-align:right'><div style='font:600 22px Poppins'>☀ 28°</div><div style='font:500 10px Poppins;opacity:.7'>Sunny · H31 L19</div></div></div>"
          f"<div class='wrow'><div class='wg' style='animation-delay:.95s'><div style='font:600 10px Poppins;opacity:.7'>BATTERY</div><div style='font:700 20px Poppins'><span class='num' style='animation:cnt 1.8s 1s both;--n:86'></span>%</div></div><div class='wg' style='animation-delay:1.05s'><div style='font:600 10px Poppins;opacity:.7'>STEPS</div><div style='font:700 20px Poppins'><span class='num' style='animation:cnt 1.8s 1.1s both;--n:6420'></span></div></div></div>"
          f"<div class='grid'>{apps}</div><div class='srch' style='position:absolute;left:0;right:0;bottom:96px'>⌕ &nbsp;Search apps, contacts, web</div><div class='dock'>{dock}</div>")
    # phone 3: home behind + notification shade with quick settings sliding down
    qs = [('ᯤ', 'Wi-Fi', 1), ('ᛒ', 'Bluetooth', 1), ('⇅', 'Data', 0), ('🔦', 'Torch', 2), ('☾', 'DND', 0), ('✈', 'Airplane', 0), ('⟳', 'Rotate', 1), ('⌖', 'Location', 0)]
    qh = ''.join(f"<div class='qt{' on' if o==1 else ''}{' fl' if o==2 else ''}'>{g}</div>" for g, n, o in qs[:4]) + ''.join(f"<div class='qt{' on' if o==1 else ''}'>{g}</div>" for g, n, o in qs[4:])
    ql1 = ''.join(f"<span>{n}</span>" for g, n, o in qs[:4]); ql2 = ''.join(f"<span>{n}</span>" for g, n, o in qs[4:])
    allapps = ''.join(f"<div class='ap'><i style='{icon(c)}'>{g}</i>{n}</div>" for (n, g, c) in APPS[:12])
    p3 = (f"<div class='sb'><span>9:41</span><span>▮▮▮ 5G 🔋</span></div><div class='grid' style='padding-top:30px'>{allapps}</div>"
          f"<div class='shade'><div class='sb' style='color:{T['tx'] if not (dark or glass) else '#fff'}'><span style='font:600 20px Poppins'>9:41</span><span>Sat, 14 Nov &nbsp;⚙</span></div>"
          f"<div class='qs'>{qh[:0]}" + ''.join(f"<div class='qt{' on' if o==1 else ''}{' fl' if o==2 else ''}'>{g}</div>" for g, n, o in qs[:4]) + f"</div><div class='ql'>{ql1}</div>"
          f"<div class='qs'>" + ''.join(f"<div class='qt{' on' if o==1 else ''}'>{g}</div>" for g, n, o in qs[4:]) + f"</div><div class='ql'>{ql2}</div>"
          f"<div class='br'><b></b><span>☀</span></div>"
          f"<div class='mp'><i></i><div style='flex:1'>Raat Ki Rani · TuneLoft<div class='pb'><b></b></div></div><span style='font-size:18px'>⏸</span></div>"
          f"<div class='nt' style='animation-delay:2.6s'><i style='{icon('#2f8cff')}'>✉</i><div>Ammi<small>Order ready hai? 🙏</small></div></div>"
          f"<div class='nt' style='animation-delay:2.9s'><i style='{icon('#34c759')}'>₹</i><div>Payment received<small>₹2,580 from Bilal</small></div></div></div>")
    mode = 'Dark' if dark else 'Light'
    body = (f"<div class='chip'>{T['name']} launcher theme</div><div class='chip mode'>{'☾' if dark else '☀'} {mode} mode</div>"
            f"<div class='ph p1'>{p1}</div><div class='ph p2'>{p2}</div><div class='ph p3'>{p3}</div>"
            + cursor([(0, 1050, 700), (1.0, 870, 96), (1.9, 870, 380), (3.0, 925, 165), (3.6, 925, 165), (6, 900, 600)], [(1.0, 870, 96), (3.6, 925, 165)]))
    html = f"<!doctype html><html><head><meta charset='utf-8'>{FONT}<style>{BASE}{css}</style></head><body>{body}</body></html>"
    open(f"{OUT}/{id_}a.html", 'w').write(html)

n = 1
for st in ['skeuo', 'neu', 'clay', 'glass', 'bento']:
    for dark in (False, True):
        scene(f'ui-k{n:02d}', st, dark); n += 1
print('ok')
