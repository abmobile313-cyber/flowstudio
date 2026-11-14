# Phone UI kit films: dial pad + contacts + messages in 5 UI styles x light/dark.
# usage: python3 phonekit14.py OUTDIR   -> ui-kNN.html (+ rows in kit_rows.json)
import sys, os, json
sys.argv += [] ; OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
sys.path.insert(0, os.path.dirname(__file__))
import importlib.util
spec = importlib.util.spec_from_file_location('s14', os.path.join(os.path.dirname(__file__), 'styles14.py'))
# reuse BASE/FONT/cursor without running the style generator
src = open(spec.origin).read().split('ITEMS = []')[0].replace('OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)', '')
ns = {}; exec(src, ns)
BASE, FONT, cursor = ns['BASE'], ns['FONT'], ns['cursor']

# per style + mode tokens: page bg, phone surface, raised shadow, pressed (inset) shadow, text, sub, accent, bubble-in, bubble-out, extra
def tokens(style, dark):
    if style == 'skeuo':
        return dict(bg='radial-gradient(1100px 700px at 30% 10%,#3a3f4b,#16181d)' if dark else 'radial-gradient(1100px 700px at 30% 10%,#f6f7fa,#dde2ea)',
            ph='linear-gradient(160deg,#343844,#1e2129)' if dark else 'linear-gradient(160deg,#fdfdfd,#e4e8ef)',
            phs='0 1px 0 rgba(255,255,255,.08) inset,0 30px 60px rgba(0,0,0,.6),0 0 0 1px #0b0c10' if dark else '0 1px 0 #fff inset,0 30px 60px rgba(40,55,90,.25),0 0 0 1px #d2d8e2',
            key='linear-gradient(160deg,#3d4250,#262a33)' if dark else 'linear-gradient(160deg,#ffffff,#e1e5ec)',
            ks='0 1px 0 rgba(255,255,255,.12) inset,0 6px 12px rgba(0,0,0,.5),0 0 0 1px #0d0f13' if dark else '0 1px 0 #fff inset,0 6px 12px rgba(40,55,90,.2),0 0 0 1px #d0d6e0',
            kp='0 2px 4px rgba(0,0,0,.5) inset' if dark else '0 2px 5px rgba(0,0,0,.2) inset',
            tx='#eef1f6' if dark else '#2b3142', sub='#8b93a5', acc='#34c759', acc2='#1f9d48',
            bin='linear-gradient(#454a57,#2e323c)' if dark else 'linear-gradient(#ffffff,#e9edf3)', bout='linear-gradient(#4aa8ff,#1c6fe0)', name='Skeuomorphism')
    if style == 'neu':
        b = '#272b33' if dark else '#e3eaf3'
        return dict(bg=b, ph=b, phs=('14px 14px 30px #15181d,-14px -14px 30px #353b46' if dark else '14px 14px 30px rgba(60,90,120,.22),-14px -14px 30px #ffffff'),
            key=b, ks=('6px 6px 12px #16191e,-6px -6px 12px #363c47' if dark else '6px 6px 12px rgba(60,90,120,.22),-6px -6px 12px #ffffff'),
            kp=('inset 5px 5px 10px #16191e,inset -5px -5px 10px #363c47' if dark else 'inset 5px 5px 10px rgba(60,90,120,.25),inset -5px -5px 10px #fff'),
            tx='#d9e1ec' if dark else '#3c4a5c', sub='#7d8a9c', acc='#7a5cff', acc2='#2fd6ff', bin=b, bout='linear-gradient(135deg,#7a5cff,#2fd6ff)', name='Neumorphism')
    if style == 'clay':
        return dict(bg='radial-gradient(900px 600px at 70% 20%,#3b2d7a,#17112f)' if dark else 'radial-gradient(900px 600px at 70% 20%,#ece6ff,#c3b6ff)',
            ph='#241d45' if dark else '#fbfaff', phs='0 40px 70px rgba(0,0,0,.55),inset 0 -8px 0 rgba(0,0,0,.25)' if dark else '0 40px 70px rgba(50,30,130,.35),inset 0 -8px 0 rgba(80,60,160,.08)',
            key='#352c66' if dark else '#ffffff', ks='inset 0 5px 6px rgba(255,255,255,.12),inset 0 -6px 8px rgba(0,0,0,.35),0 8px 14px rgba(0,0,0,.35)' if dark else 'inset 0 5px 6px rgba(255,255,255,.9),inset 0 -6px 8px rgba(80,60,160,.15),0 8px 14px rgba(60,40,140,.18)',
            kp='inset 0 -3px 4px rgba(255,255,255,.2),inset 0 6px 10px rgba(0,0,0,.35)', tx='#f1eeff' if dark else '#2e2a52', sub='#9b96c4', acc='#3ccf7a', acc2='#22a95c',
            bin='#352c66' if dark else '#ffffff', bout='#6c4cf1', name='Claymorphism')
    if style == 'glass':
        return dict(bg='linear-gradient(135deg,#0e1530,#2a1450 55%,#4a0f4f)' if dark else 'linear-gradient(135deg,#38c6ff,#7b4dff 55%,#c21fd6)',
            ph='linear-gradient(135deg,rgba(255,255,255,.14),rgba(255,255,255,.04))' if dark else 'linear-gradient(135deg,rgba(255,255,255,.35),rgba(255,255,255,.1))',
            phs='0 30px 60px rgba(0,0,0,.45),inset 0 0 0 1.5px rgba(255,255,255,.25)' if dark else '0 30px 60px rgba(30,0,80,.3),inset 0 0 0 1.5px rgba(255,255,255,.6)',
            key='rgba(255,255,255,.12)' if dark else 'rgba(255,255,255,.25)', ks='inset 0 0 0 1px rgba(255,255,255,.3)', kp='inset 0 0 0 30px rgba(255,255,255,.35)',
            tx='#ffffff', sub='rgba(255,255,255,.7)', acc='#34e0a1', acc2='#18a874', bin='rgba(255,255,255,.18)' if dark else 'rgba(255,255,255,.3)', bout='linear-gradient(135deg,#ff6fd8,#7b4dff)', name='Glassmorphism', glass=1)
    # bento
    return dict(bg='#121018' if dark else '#ecebf3', ph='#1c1a26' if dark else '#ffffff', phs='0 30px 60px rgba(0,0,0,.5)' if dark else '0 30px 60px rgba(40,30,90,.18)',
        key='#34304a' if dark else '#e4dff8', ks='inset 0 0 0 1px rgba(91,61,245,.18)', kp='inset 0 0 0 40px #5b3df5', tx='#f4f2ff' if dark else '#1d1640', sub='#8d88a8', acc='#5b3df5', acc2='#3b22c9',
        bin='#292637' if dark else '#f1effa', bout='#5b3df5', name='Bento grid', bento=1)

CONTACTS = [('Ammi','Mobile','#ff8a65'),('Arjun Mehta','Work','#4cc9e0'),('Bilal Shaikh','Mobile','#ffd166'),('Dr. Fatima','Clinic','#2fbf71'),('Imran (Rider)','Mobile','#a78bfa'),('Kavya','Home','#ff6fa3'),('Rohan Office','Work','#5b8def')]
MSGS = [(0,'Assalamu alaikum! Order ready hai?'),(1,'Wa alaikum assalam, haan ji ✓'),(1,'Rider 10 min mein pahunch jayega'),(0,'Perfect, shukriya 🙏'),(1,'Aapka din achha guzre!')]
DIGITS = '98765 43210'

def kit(id_, style, dark):
    T = tokens(style, dark); mode = 'Dark' if dark else 'Light'
    glass = T.get('glass'); bento = T.get('bento')
    blur = 'backdrop-filter:blur(20px) saturate(140%);' if glass else ''
    css = f"""
body{{background:{T['bg']}}}
.chip{{background:{'rgba(255,255,255,.14)' if (dark or glass) else '#ffffffcc'};color:{'#fff' if (dark or glass) else '#3b4252'};border:1px solid {'rgba(255,255,255,.3)' if (dark or glass) else '#0001'}}}
.mode{{left:auto;right:28px}}
.ph{{position:absolute;top:84px;width:300px;height:600px;border-radius:{'30px' if bento else '42px'};background:{T['ph']};box-shadow:{T['phs']};{blur}padding:22px 22px;color:{T['tx']};animation:up .9s cubic-bezier(.2,.8,.2,1) both;overflow:hidden}}
.p1{{left:60px;animation-delay:.1s}}.p2{{left:390px;animation-delay:.3s}}.p3{{left:720px;animation-delay:.5s}}
.sb{{display:flex;justify-content:space-between;font:600 12px Poppins;color:{T['sub']};margin-bottom:12px}}
.ti{{font:700 22px Poppins}}.su{{font:500 12px Poppins;color:{T['sub']}}}
.num2{{height:56px;margin:14px 0 6px;text-align:center;font:600 28px Poppins;letter-spacing:.04em;white-space:nowrap;overflow:hidden}}
.num2 span{{display:inline-block;width:0;overflow:hidden;vertical-align:bottom;animation:dg .01s both}}
@keyframes dg{{to{{width:.62em}}}}
.pad{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px 18px;padding:0 6px}}
.k{{height:64px;border-radius:{'18px' if bento else '50%'};width:{'auto' if bento else '64px'};margin:0 auto;background:{T['key']};box-shadow:{T['ks']};display:grid;place-items:center;font:600 22px Poppins;line-height:1;animation:pop .45s both;{blur}}}
.k small{{display:block;font:600 8px Poppins;letter-spacing:.18em;color:{T['sub']};text-align:center;margin-top:2px}}
.k.pr{{animation:pop .45s both,kp .35s both}}
@keyframes kp{{0%,100%{{}}40%{{box-shadow:{T['kp']};transform:scale(.92)}}}}
.call{{margin:16px auto 0;width:66px;height:66px;border-radius:50%;background:linear-gradient(160deg,{T['acc']},{T['acc2']});display:grid;place-items:center;color:#fff;font-size:26px;box-shadow:0 10px 20px {T['acc']}66,inset 0 3px 4px rgba(255,255,255,.4);animation:pop .5s .9s both,ring2 1.2s 4.6s ease-in-out 1}}
@keyframes ring2{{0%,100%{{transform:scale(1)}}30%{{transform:scale(1.12) rotate(-12deg)}}60%{{transform:scale(1.08) rotate(12deg)}}}}
.srch{{margin:14px 0 10px;height:40px;border-radius:14px;background:{T['key']};box-shadow:{T['kp'] if style=='neu' else T['ks']};display:flex;align-items:center;padding:0 14px;font:500 12px Poppins;color:{T['sub']};{blur}}}
.ct{{display:flex;align-items:center;gap:12px;padding:9px 10px;margin-bottom:8px;border-radius:16px;background:{T['key'] if style in ('clay','bento','glass') else 'transparent'};box-shadow:{T['ks'] if style in ('clay',) else 'none'};animation:up .5s both;{blur}}}
.ct i{{width:38px;height:38px;border-radius:{'12px' if bento else '50%'};display:grid;place-items:center;font:700 14px Poppins;color:#fff;font-style:normal;box-shadow:{'inset 0 3px 4px rgba(255,255,255,.45),inset 0 -4px 6px rgba(0,0,0,.2)' if style=='clay' else 'none'}}}
.ct b{{flex:1;font:600 13px Poppins}}.ct b small{{display:block;font:500 10px Poppins;color:{T['sub']}}}
.ct em{{font-style:normal;color:{T['acc']};font-size:16px}}
.lt{{font:700 11px Poppins;color:{T['sub']};margin:6px 4px}}
.hd{{display:flex;align-items:center;gap:10px;padding-bottom:12px;border-bottom:1px solid {'rgba(255,255,255,.12)' if (dark or glass) else 'rgba(0,0,0,.07)'}}}
.hd i{{width:38px;height:38px;border-radius:50%;background:#ff8a65}}
.bb{{max-width:78%;padding:10px 14px;border-radius:18px;font:500 12.5px/1.4 Poppins;margin-top:10px;animation:bpop .45s both;{blur}}}
@keyframes bpop{{from{{opacity:0;transform:translateY(16px) scale(.9)}}}}
.bi{{background:{T['bin']};box-shadow:{T['ks'] if style!='glass' else 'inset 0 0 0 1px rgba(255,255,255,.3)'};border-bottom-left-radius:6px}}
.bo{{background:{T['bout']};color:#fff;margin-left:auto;border-bottom-right-radius:6px;box-shadow:{'inset 0 4px 6px rgba(255,255,255,.35),inset 0 -5px 8px rgba(0,0,0,.25),0 8px 14px rgba(0,0,0,.2)' if style=='clay' else '0 6px 14px rgba(0,0,0,.18)'}}}
.typ{{display:inline-flex;gap:4px;padding:12px 14px;border-radius:18px;background:{T['bin']};margin-top:10px;box-shadow:{T['ks'] if style!='glass' else 'none'};animation:bpop .4s 4.2s both,hide .01s 5.2s both}}
@keyframes hide{{to{{opacity:0}}}}
.typ i{{width:7px;height:7px;border-radius:50%;background:{T['sub']};animation:dot 1s infinite}}
.typ i:nth-child(2){{animation-delay:.2s}}.typ i:nth-child(3){{animation-delay:.4s}}
@keyframes dot{{50%{{transform:translateY(-5px)}}}}
.inp{{position:absolute;left:18px;right:18px;bottom:18px;height:46px;border-radius:24px;background:{T['key']};box-shadow:{T['kp'] if style=='neu' else T['ks']};display:flex;align-items:center;justify-content:space-between;padding:0 6px 0 16px;font:500 12px Poppins;color:{T['sub']};{blur}}}
.inp b{{width:36px;height:36px;border-radius:50%;background:{T['bout']};display:grid;place-items:center;color:#fff}}
"""
    # dial pad: digits appear in time with presses
    keys = [('1',''),('2','ABC'),('3','DEF'),('4','GHI'),('5','JKL'),('6','MNO'),('7','PQRS'),('8','TUV'),('9','WXYZ'),('*',''),('0','+'),('#','')]
    seq = [c for c in DIGITS if c != ' ']; t0 = 1.4; dt = 0.26
    press = {}
    for i, c in enumerate(seq): press.setdefault(c, []).append(t0 + i * dt)
    num = ''.join(f"<span style='animation-delay:{t0+i*dt:.2f}s'>{c}</span>" + ("<span style='animation-delay:%.2fs'>&nbsp;</span>" % (t0+i*dt) if i == 4 else '') for i, c in enumerate(seq))
    padh = ''
    for j, (k, s) in enumerate(keys):
        ts = press.get(k, [])
        anim = f"pop .45s {.5+j*.05:.2f}s both" + ''.join(f",kp .3s {t:.2f}s" for t in ts)
        padh += f"<div class='k' style='animation:{anim}'><div>{k}<small>{s or '&nbsp;'}</small></div></div>"
    p1 = f"<div class='sb'><span>9:41</span><span>▮▮▮ 5G 🔋</span></div><div class='ti'>Phone</div><div class='su'>Keypad</div><div class='num2'>{num}</div><div class='pad'>{padh}</div><div class='call'>✆</div>"
    cts = ''.join(f"<div class='ct' style='animation-delay:{1+i*.15:.2f}s'><i style='background:{c}'>{n[0]}</i><b>{n}<small>{t}</small></b><em>✆</em></div>" + ("<div class='lt'>B</div>" if i == 1 else '') for i, (n, t, c) in enumerate(CONTACTS[:6]))
    p2 = f"<div class='sb'><span>9:41</span><span>▮▮▮ 5G 🔋</span></div><div class='ti'>Contacts</div><div class='srch'>⌕ &nbsp;Search 248 contacts</div><div class='lt'>A</div>{cts}"
    ms = ''.join(f"<div class='bb {'bo' if w else 'bi'}' style='animation-delay:{1.2+i*.55 if i<4 else 5.3:.2f}s'>{m}</div>" for i, (w, m) in enumerate(MSGS))
    p3 = f"<div class='sb'><span>9:41</span><span>▮▮▮ 5G 🔋</span></div><div class='hd'><i></i><div><div style='font:700 15px Poppins'>Ammi</div><div class='su'>online</div></div><span style='margin-left:auto;color:{T['acc']}'>✆</span></div>{ms}<div class='typ'><i></i><i></i><i></i></div><div class='inp'>Type a message… <b>➤</b></div>"
    body = f"<div class='chip'>{T['name']} launcher theme</div><div class='chip mode'>{'☾' if dark else '☀'} {mode} mode</div><div class='ph p1'>{p1}</div><div class='ph p2'>{p2}</div><div class='ph p3'>{p3}</div>" + cursor([(0,1050,700),(1.2,205,340),(4.2,205,580),(4.7,210,610),(6,210,610)],[(4.75,210,612)])
    html = f"<!doctype html><html><head><meta charset='utf-8'>{FONT}<style>{BASE}{css}</style></head><body>{body}</body></html>"
    open(f"{OUT}/{id_}.html", 'w').write(html)
    return ['app', 'video', id_, f"{T['name']} phone UI · {mode} mode", 'Dial pad · Contacts · Messages']

rows = []; n = 1
for st in ['skeuo', 'neu', 'clay', 'glass', 'bento']:
    for dark in (False, True):
        rows.append(kit(f'ui-k{n:02d}', st, dark)); n += 1
json.dump(rows, open(f"{OUT}/kit_rows.json", 'w'), ensure_ascii=False); print(len(rows))
