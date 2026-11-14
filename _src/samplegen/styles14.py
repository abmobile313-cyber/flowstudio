# UI-style showcase films (batch 14): skeuomorphism, neumorphism, claymorphism, glassmorphism, bento grid.
# usage: python3 styles14.py OUTDIR   -> writes ui-sNN.html (1080x720, pure CSS animation, 6 s)
import sys, os, json
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
FONT = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
BASE = """
@property --p{syntax:'<number>';inherits:true;initial-value:0}
@property --n{syntax:'<integer>';inherits:true;initial-value:0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:720px;overflow:hidden;font-family:Poppins,system-ui,sans-serif}
.chip{position:absolute;left:28px;top:24px;z-index:50;font:600 13px Poppins;letter-spacing:.14em;text-transform:uppercase;padding:8px 14px;border-radius:30px;animation:fi .6s .1s both}
@keyframes fi{from{opacity:0;transform:translateY(-8px)}}
@keyframes up{from{opacity:0;transform:translateY(60px) scale(.96)}}
@keyframes pop{0%{opacity:0;transform:scale(.6)}70%{transform:scale(1.06)}100%{opacity:1;transform:scale(1)}}
@keyframes ring{from{--p:0}}
@keyframes cnt{from{--n:0}}
@keyframes grow{from{transform:scaleY(0)}}
@keyframes growx{from{transform:scaleX(0)}}
@keyframes float{50%{transform:translateY(-14px)}}
.num{counter-reset:n var(--n)}.num::after{content:counter(n)}
.cur{position:absolute;z-index:60;width:26px;height:26px;pointer-events:none}
.cur::before{content:'';position:absolute;inset:0;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M3 2l7 19 2.6-7.4L20 11z' fill='%23111' stroke='white' stroke-width='1.6'/></svg>") no-repeat;background-size:contain}
.tap{position:absolute;z-index:59;width:44px;height:44px;border-radius:50%;border:3px solid rgba(255,255,255,.9);opacity:0}
@keyframes tapk{0%{opacity:.9;transform:scale(.3)}100%{opacity:0;transform:scale(1.4)}}
"""
def cursor(path, taps):
    # path: list of (t_seconds, x, y)
    tot = 6.0; ks = []
    for t, x, y in path: ks.append(f"{t/tot*100:.1f}%{{left:{x}px;top:{y}px}}")
    s = f"<style>@keyframes cmv{{{''.join(ks)}}}</style><div class='cur' style='animation:cmv 6s linear both'></div>"
    for t, x, y in taps:
        s += f"<div class='tap' style='left:{x-18}px;top:{y-18}px;animation:tapk .6s {t}s both'></div>"
    return s
def page(css, body, title):
    return f"<!doctype html><html><head><meta charset='utf-8'>{FONT}<style>{BASE}{css}</style></head><body>{body}</body></html>"

ITEMS = []
def add(id_, html, fold, title, sub):
    open(f"{OUT}/{id_}.html", 'w').write(html); ITEMS.append([fold, "video", id_, title, sub])

# ---------------- 1. SKEUOMORPHISM ----------------
def skeuo(id_, brand, sub, accent, a2, kind):
    css = f"""
body{{background:radial-gradient(1200px 700px at 30% 10%,#f4f6fa,#dfe4ec);}}
.chip{{background:linear-gradient(#fff,#e9edf3);color:#3b4252;box-shadow:0 2px 0 #fff inset,0 6px 14px rgba(40,50,80,.18),0 0 0 1px #cfd6e2}}
.ph{{position:absolute;top:96px;width:300px;height:580px;border-radius:38px;background:linear-gradient(160deg,#fdfdfd,#e6eaf0);box-shadow:0 1px 0 #fff inset,0 -2px 0 rgba(0,0,0,.05) inset,0 30px 60px rgba(40,55,90,.25),0 0 0 1px #d4dae4;padding:26px 22px;animation:up .9s cubic-bezier(.2,.8,.2,1) both}}
.p1{{left:60px;animation-delay:.15s}}.p2{{left:390px;animation-delay:.35s}}.p3{{left:720px;animation-delay:.55s}}
.h{{font:500 12px Poppins;color:#8a93a6}}.hb{{font:700 19px Poppins;color:#2b3142}}
.av{{position:absolute;right:22px;top:26px;width:42px;height:42px;border-radius:12px;background:linear-gradient(135deg,{accent},{a2});box-shadow:0 6px 12px rgba(0,0,0,.2),0 1px 0 rgba(255,255,255,.6) inset}}
.knob{{margin:34px auto 0;width:190px;height:190px;border-radius:50%;background:conic-gradient({accent} 0 calc(var(--p)*1%),#e3e7ee 0);display:grid;place-items:center;animation:ring 2.2s .9s cubic-bezier(.3,.7,.2,1) both;--p:72;box-shadow:0 14px 28px rgba(40,55,90,.22)}}
.knob i{{width:142px;height:142px;border-radius:50%;background:linear-gradient(150deg,#ffffff,#dde2ea);box-shadow:0 2px 0 #fff inset,0 10px 20px rgba(0,0,0,.18);display:grid;place-items:center;font-style:normal}}
.big{{font:700 30px Poppins;color:#2b3142}}.sm{{font:500 11px Poppins;color:#99a1b2;text-align:center}}
.bar{{height:12px;border-radius:8px;background:#e1e5ec;box-shadow:inset 0 2px 4px rgba(0,0,0,.15);margin-top:10px;overflow:hidden}}
.bar b{{display:block;height:100%;width:72%;border-radius:8px;background:linear-gradient(90deg,{accent},{a2});transform-origin:left;animation:growx 1.6s 1.2s both;box-shadow:0 1px 0 rgba(255,255,255,.5) inset}}
.row{{display:flex;justify-content:space-between;margin-top:26px;font:600 12px Poppins;color:#5b6375}}
.btns{{display:flex;justify-content:space-between;margin-top:30px}}
.bt{{width:52px;height:52px;border-radius:16px;background:linear-gradient(160deg,#fff,#e2e6ed);box-shadow:0 1px 0 #fff inset,0 8px 14px rgba(40,55,90,.2),0 0 0 1px #d3d9e3;display:grid;place-items:center;font-size:20px;color:#6b7386}}
.bt.on{{background:linear-gradient(160deg,{accent},{a2});color:#fff;animation:press .5s 3.6s both}}
@keyframes press{{50%{{transform:translateY(3px);box-shadow:0 2px 4px rgba(0,0,0,.25)}}}}
.tile{{height:108px;border-radius:20px;background:linear-gradient(160deg,#fff,#e6eaf0);box-shadow:0 1px 0 #fff inset,0 10px 18px rgba(40,55,90,.16),0 0 0 1px #d6dce6;display:grid;place-items:center;text-align:center;animation:pop .6s both}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:22px}}
.tile b{{font:700 20px Poppins;color:#2b3142;display:block}}.tile span{{font:500 11px Poppins;color:#8a93a6}}
.area{{margin-top:20px;height:150px;border-radius:22px;background:linear-gradient(160deg,#fff,#e6eaf0);box-shadow:0 10px 18px rgba(40,55,90,.16),0 0 0 1px #d6dce6;overflow:hidden;position:relative}}
.area svg{{position:absolute;bottom:0;left:0;width:100%;height:100%}}
.area path{{transform-origin:bottom;animation:grow 1.6s 1.6s cubic-bezier(.3,.7,.2,1) both}}
.dial{{margin:40px auto 0;width:200px;height:200px;border-radius:50%;background:radial-gradient(circle at 50% 50%,transparent 58%,#e2e6ed 59%);position:relative}}
.dial::before{{content:'';position:absolute;inset:0;border-radius:50%;background:conic-gradient(from 200deg,{a2},{accent} calc(var(--p)*0.9deg),transparent 0);-webkit-mask:radial-gradient(circle,transparent 62%,#000 63%);animation:ring 2.4s 1.1s both;--p:260}}
.dial i{{position:absolute;inset:34px;border-radius:50%;background:linear-gradient(150deg,#fff,#dde2ea);box-shadow:0 2px 0 #fff inset,0 14px 24px rgba(0,0,0,.2);display:grid;place-items:center;font-style:normal}}
"""
    if kind == 'fin':
        p1 = f"<div class='h'>Good morning,</div><div class='hb'>Hello, Arjun</div><div class='av'></div><div class='knob'><i><div><div class='big'>₹<span class='num' style='animation:cnt 2.2s .9s both;--n:64250'></span></div><div class='sm'>Balance</div></div></i></div><div class='row'><span>Saved this week</span><span>₹8,600</span></div><div class='bar'><b></b></div><div class='btns'><div class='bt on'>◔</div><div class='bt'>★</div><div class='bt'>▤</div><div class='bt'>⚙</div></div>"
        p2 = f"<div class='hb' style='text-align:center'>Overview</div><div class='sm' style='margin-top:6px'>Last 30 days ▾</div><div class='grid'><div class='tile' style='animation-delay:1s'><div><b class='num' style='animation:cnt 1.6s 1s both;--n:238'></b><span>Payments</span></div></div><div class='tile' style='animation-delay:1.15s'><div><b class='num' style='animation:cnt 1.6s 1.1s both;--n:46'></b><span>Bills paid</span></div></div><div class='tile' style='animation-delay:1.3s'><div><b>₹3.3L</b><span>Spending</span></div></div><div class='tile' style='animation-delay:1.45s'><div><b>12</b><span>Goals</span></div></div></div><div class='area'><svg viewBox='0 0 260 150' preserveAspectRatio='none'><path d='M0 150 L0 90 L40 70 L80 95 L120 50 L160 75 L200 35 L260 60 L260 150Z' fill='url(#g)'/><defs><linearGradient id='g' x1='0' x2='1'><stop offset='0' stop-color='{a2}'/><stop offset='1' stop-color='{accent}'/></linearGradient></defs></svg></div>"
        p3 = f"<div class='hb'>‹ &nbsp;Budget</div><div class='h' style='margin-top:14px'>This month</div><div class='big'>₹52,000</div><div class='dial'><i><div><div class='big' style='font-size:24px'><span class='num' style='animation:cnt 2.4s 1.1s both;--n:72'></span>%</div><div class='sm'>used</div></div></i></div><div class='btns' style='justify-content:center;gap:22px'><div class='bt'>＋</div><div class='bt on'>⇄</div><div class='bt'>▣</div></div>"
    elif kind == 'home':
        p1 = f"<div class='h'>Living room</div><div class='hb'>Climate</div><div class='av'></div><div class='dial'><i><div><div class='big'><span class='num' style='animation:cnt 2.4s 1.1s both;--n:24'></span>°C</div><div class='sm'>Cooling</div></div></i></div><div class='row'><span>Humidity</span><span>48%</span></div><div class='bar'><b></b></div><div class='btns'><div class='bt on'>❄</div><div class='bt'>☀</div><div class='bt'>☁</div><div class='bt'>⏻</div></div>"
        p2 = f"<div class='hb' style='text-align:center'>Devices</div><div class='sm' style='margin-top:6px'>6 rooms · all online</div><div class='grid'><div class='tile' style='animation-delay:1s'><div><b>💡</b><span>Lights · On</span></div></div><div class='tile' style='animation-delay:1.15s'><div><b>🔒</b><span>Door · Locked</span></div></div><div class='tile' style='animation-delay:1.3s'><div><b>📺</b><span>TV · Off</span></div></div><div class='tile' style='animation-delay:1.45s'><div><b>🌀</b><span>Fan · 3</span></div></div></div><div class='area'><svg viewBox='0 0 260 150' preserveAspectRatio='none'><path d='M0 150 L0 100 L40 80 L80 90 L120 60 L160 70 L200 45 L260 55 L260 150Z' fill='url(#g)'/><defs><linearGradient id='g' x1='0' x2='1'><stop offset='0' stop-color='{a2}'/><stop offset='1' stop-color='{accent}'/></linearGradient></defs></svg></div>"
        p3 = f"<div class='hb'>‹ &nbsp;Energy</div><div class='h' style='margin-top:14px'>Today</div><div class='big'><span class='num' style='animation:cnt 2s 1s both;--n:18'></span> kWh</div><div class='knob'><i><div><div class='big' style='font-size:24px'>−22%</div><div class='sm'>vs last week</div></div></i></div><div class='btns' style='justify-content:center;gap:22px'><div class='bt'>◐</div><div class='bt on'>⚡</div><div class='bt'>▣</div></div>"
    else:  # music
        p1 = f"<div class='h'>Now playing</div><div class='hb'>Raat Ki Rani</div><div class='av'></div><div class='knob' style='animation-duration:5s'><i style='background:repeating-radial-gradient(circle,#2a2d36 0 2px,#1d1f26 2px 4px);animation:spin 6s linear both'><div style='width:54px;height:54px;border-radius:50%;background:linear-gradient(135deg,{accent},{a2})'></div></i></div><div class='row'><span>1:42</span><span>3:58</span></div><div class='bar'><b style='width:44%'></b></div><div class='btns'><div class='bt'>⏮</div><div class='bt on'>⏸</div><div class='bt'>⏭</div><div class='bt'>♡</div></div><style>@keyframes spin{{to{{transform:rotate(540deg)}}}}</style>"
        p2 = f"<div class='hb' style='text-align:center'>Library</div><div class='sm' style='margin-top:6px'>Recently played ▾</div><div class='grid'><div class='tile' style='animation-delay:1s'><div><b class='num' style='animation:cnt 1.6s 1s both;--n:128'></b><span>Songs</span></div></div><div class='tile' style='animation-delay:1.15s'><div><b>14</b><span>Playlists</span></div></div><div class='tile' style='animation-delay:1.3s'><div><b>32h</b><span>This month</span></div></div><div class='tile' style='animation-delay:1.45s'><div><b>9</b><span>Artists</span></div></div></div><div class='area'><svg viewBox='0 0 260 150' preserveAspectRatio='none'><path d='M0 150 L0 110 L20 80 L40 100 L60 60 L80 90 L100 40 L120 85 L140 55 L160 95 L180 50 L200 80 L220 60 L240 90 L260 70 L260 150Z' fill='url(#g)'/><defs><linearGradient id='g' x1='0' x2='1'><stop offset='0' stop-color='{a2}'/><stop offset='1' stop-color='{accent}'/></linearGradient></defs></svg></div>"
        p3 = f"<div class='hb'>‹ &nbsp;Equalizer</div><div class='h' style='margin-top:14px'>Preset</div><div class='big' style='font-size:22px'>Warm Studio</div><div class='dial'><i><div><div class='big' style='font-size:24px'>+<span class='num' style='animation:cnt 2.4s 1.1s both;--n:6'></span> dB</div><div class='sm'>Bass</div></div></i></div><div class='btns' style='justify-content:center;gap:22px'><div class='bt'>🔈</div><div class='bt on'>🎚</div><div class='bt'>🔊</div></div>"
    body = f"<div class='chip'>Skeuomorphism UI</div><div class='ph p1'>{p1}</div><div class='ph p2'>{p2}</div><div class='ph p3'>{p3}</div>" + cursor([(0,1000,700),(2.8,520,600),(3.55,250,620),(4.6,250,620),(5.4,880,610),(6,880,610)],[(3.6,250,620),(5.4,880,610)])
    add(id_, page(css, body, brand), 'app', 'Skeuomorphism app UI', f"{brand} · {sub}")

# ---------------- 2. NEUMORPHISM ----------------
def neu(id_, brand, sub, bg, accent, a2, kind):
    css = f"""
body{{background:{bg}}}
.chip{{background:{bg};color:#55657a;box-shadow:6px 6px 14px rgba(0,0,0,.12),-6px -6px 14px rgba(255,255,255,.8)}}
.card{{position:absolute;top:96px;border-radius:34px;background:{bg};box-shadow:18px 18px 40px rgba(60,90,120,.22),-18px -18px 40px rgba(255,255,255,.85);padding:28px;animation:up .9s cubic-bezier(.2,.8,.2,1) both}}
.c1{{left:110px;width:380px;height:560px;animation-delay:.15s}}.c2{{left:560px;width:410px;height:580px;top:80px;animation-delay:.4s}}
.top{{display:flex;justify-content:space-between;align-items:center;color:#5b6b80;font:600 14px Poppins;letter-spacing:.3em}}
.ic{{width:40px;height:40px;border-radius:12px;background:{bg};box-shadow:5px 5px 10px rgba(60,90,120,.2),-5px -5px 10px rgba(255,255,255,.9);display:grid;place-items:center;color:#5b6b80;font-size:16px}}
.t1{{font:500 30px Poppins;color:#3c4a5c;margin-top:30px}}.t2{{font:400 13px Poppins;color:#8a98aa}}
.inset{{margin-top:20px;border-radius:20px;background:{bg};box-shadow:inset 6px 6px 12px rgba(60,90,120,.2),inset -6px -6px 12px rgba(255,255,255,.85);padding:18px 20px;font:500 13px Poppins;color:#6a7a8e}}
.inset div{{display:flex;justify-content:space-between;margin:4px 0}}
.lt{{height:8px;border-radius:6px;box-shadow:inset 2px 2px 4px rgba(60,90,120,.25),inset -2px -2px 4px #fff;margin-top:10px;overflow:hidden}}
.lt b{{display:block;height:100%;width:38%;border-radius:6px;background:linear-gradient(90deg,{accent},{a2});transform-origin:left;animation:growx 1.4s 1.3s both}}
.li{{display:flex;align-items:center;gap:16px;margin-top:22px;animation:fi .5s both}}
.th{{width:78px;height:58px;border-radius:16px;box-shadow:5px 5px 10px rgba(60,90,120,.2),-5px -5px 10px rgba(255,255,255,.9)}}
.li .nm{{font:600 14px Poppins;color:#3c4a5c;flex:1}}.li .nm small{{display:block;font:400 11px Poppins;color:#8a98aa}}
.pl{{width:34px;height:34px;border-radius:50%;background:{bg};box-shadow:4px 4px 8px rgba(60,90,120,.22),-4px -4px 8px #fff;display:grid;place-items:center;font-size:11px;color:{accent}}}
.tog{{width:70px;height:36px;border-radius:20px;background:{bg};box-shadow:inset 4px 4px 8px rgba(60,90,120,.25),inset -4px -4px 8px #fff;position:relative}}
.tog i{{position:absolute;top:4px;left:4px;width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,{accent},{a2});box-shadow:3px 3px 6px rgba(0,0,0,.2);animation:tg .4s 3.7s both}}
@keyframes tg{{to{{left:38px}}}}
.donut{{margin:26px auto 0;width:210px;height:210px;border-radius:50%;background:{bg};box-shadow:12px 12px 24px rgba(60,90,120,.22),-12px -12px 24px #fff;display:grid;place-items:center}}
.donut .rg{{width:170px;height:170px;border-radius:50%;background:conic-gradient({accent},{a2} calc(var(--p)*1%),transparent 0);-webkit-mask:radial-gradient(circle,transparent 58%,#000 59%);animation:ring 2.4s 1s cubic-bezier(.3,.7,.2,1) both;--p:73;filter:drop-shadow(0 0 10px {accent}88)}}
.donut .in{{position:absolute;width:104px;height:104px;border-radius:50%;background:{bg};box-shadow:inset 6px 6px 12px rgba(60,90,120,.2),inset -6px -6px 12px #fff;display:grid;place-items:center;font:600 20px Poppins;color:#3c4a5c}}
.bars{{display:flex;justify-content:space-around;margin-top:26px}}
.bw{{text-align:center;font:500 11px Poppins;color:#8a98aa}}
.bs{{width:28px;height:120px;border-radius:16px;box-shadow:inset 4px 4px 8px rgba(60,90,120,.22),inset -4px -4px 8px #fff;display:flex;align-items:flex-end;margin:0 auto 8px;overflow:hidden}}
.bs b{{display:block;width:100%;border-radius:16px;transform-origin:bottom;animation:grow 1.4s both}}
.nav{{display:flex;justify-content:space-around;margin-top:22px}}
"""
    if kind == 'fit':
        thumbs = [('#f6b07a','Warm-up','0:40'),('#5cd4d0','Core twist','0:40'),('#f08ac0','Deadlift','0:40')]
        c1 = f"<div class='top'><span>←</span><span>{brand.upper()}</span><span>◯</span></div><div class='t1'>Day 1</div><div class='t2'>Strength</div><div class='inset'><div><span>Rounds</span><span>4</span></div><div><span>Time</span><span>30 min</span></div><div><span>Intensity</span><span></span></div><div class='lt'><b></b></div></div>"
        c1 += ''.join(f"<div class='li' style='animation-delay:{1.4+i*.25}s'><div class='th' style='background:linear-gradient(135deg,{c},#fff6)'></div><div class='nm'>{n}<small>{t}</small></div><div class='pl'>▶</div></div>" for i,(c,n,t) in enumerate(thumbs))
        c2 = f"<div class='top'><span>⁘</span><span>{brand.upper()}</span><span>◯</span></div><div style='display:flex;justify-content:space-between;align-items:center;margin-top:22px'><div class='t1' style='margin:0;font-size:26px'>Statistics</div><div class='tog'><i></i></div></div><div class='donut'><div class='rg'></div><div class='in'><span><span class='num' style='animation:cnt 2.4s 1s both;--n:73'></span>%</span></div></div><div class='bars'>"
        c2 += ''.join(f"<div class='bw'><div class='bs'><b style='height:{h}%;background:linear-gradient({a},{b});animation-delay:{1.6+i*.2}s'></b></div>{n}<br><b style='color:#3c4a5c'>{h}%</b></div>" for i,(n,h,a,b) in enumerate([('Relax',82,'#3fd0e8','#2a7bff'),('Cardio',24,'#c9d4e0','#b7c4d4'),('Strength',54,'#ffc078','#ff8a3d'),('Stretch',91,'#ff8bd0','#ff3d9a')]))
        c2 += "</div>"
    elif kind == 'home':
        rooms = [('#ffd479','Living room','4 devices'),('#9fd7ff','Bedroom','3 devices'),('#b9f0c8','Kitchen','5 devices')]
        c1 = f"<div class='top'><span>☰</span><span>{brand.upper()}</span><span>◯</span></div><div class='t1'>Good evening</div><div class='t2'>Inside 24°C · Outside 31°C</div><div class='inset'><div><span>Power today</span><span>12.4 kWh</span></div><div><span>Saved</span><span>18%</span></div><div class='lt'><b></b></div></div>"
        c1 += ''.join(f"<div class='li' style='animation-delay:{1.4+i*.25}s'><div class='th' style='background:linear-gradient(135deg,{c},#fff8)'></div><div class='nm'>{n}<small>{t}</small></div><div class='pl'>›</div></div>" for i,(c,n,t) in enumerate(rooms))
        c2 = f"<div class='top'><span>←</span><span>AIR CONDITIONER</span><span>⋯</span></div><div style='display:flex;justify-content:space-between;align-items:center;margin-top:22px'><div class='t1' style='margin:0;font-size:26px'>Cooling</div><div class='tog'><i></i></div></div><div class='donut'><div class='rg'></div><div class='in'><span><span class='num' style='animation:cnt 2.4s 1s both;--n:22'></span>°C</span></div></div><div class='bars'>"
        c2 += ''.join(f"<div class='bw'><div class='bs'><b style='height:{h}%;background:linear-gradient({a},{b});animation-delay:{1.6+i*.2}s'></b></div>{n}<br><b style='color:#3c4a5c'>{h}%</b></div>" for i,(n,h,a,b) in enumerate([('Fan',60,'#3fd0e8','#2a7bff'),('Swing',30,'#c9d4e0','#b7c4d4'),('Eco',78,'#9be7a8','#2fbf71'),('Timer',45,'#ffc078','#ff8a3d')]))
        c2 += "</div>"
    else:  # meditation
        ses = [('#c7b8ff','Morning calm','10 min'),('#ffc6d9','Deep sleep','20 min'),('#b6ecf0','Focus breath','5 min')]
        c1 = f"<div class='top'><span>☰</span><span>{brand.upper()}</span><span>◯</span></div><div class='t1'>Breathe</div><div class='t2'>Your daily practice</div><div class='inset'><div><span>Streak</span><span>12 days</span></div><div><span>Mindful minutes</span><span>214</span></div><div class='lt'><b></b></div></div>"
        c1 += ''.join(f"<div class='li' style='animation-delay:{1.4+i*.25}s'><div class='th' style='background:linear-gradient(135deg,{c},#fff8)'></div><div class='nm'>{n}<small>{t}</small></div><div class='pl'>▶</div></div>" for i,(c,n,t) in enumerate(ses))
        c2 = f"<div class='top'><span>←</span><span>SESSION</span><span>⋯</span></div><div style='display:flex;justify-content:space-between;align-items:center;margin-top:22px'><div class='t1' style='margin:0;font-size:26px'>Focus</div><div class='tog'><i></i></div></div><div class='donut'><div class='rg'></div><div class='in'><span><span class='num' style='animation:cnt 2.4s 1s both;--n:4'></span>:00</span></div></div><div class='bars'>"
        c2 += ''.join(f"<div class='bw'><div class='bs'><b style='height:{h}%;background:linear-gradient({a},{b});animation-delay:{1.6+i*.2}s'></b></div>{n}<br><b style='color:#3c4a5c'>{h}%</b></div>" for i,(n,h,a,b) in enumerate([('Calm',88,'#c7b8ff','#7a5cff'),('Sleep',64,'#ffc6d9','#ff6fa3'),('Focus',72,'#b6ecf0','#26b7c9'),('Mood',80,'#ffe1a8','#ffb23d')]))
        c2 += "</div>"
    body = f"<div class='chip'>Neumorphism UI</div><div class='card c1'>{c1}</div><div class='card c2'>{c2}</div>" + cursor([(0,1050,700),(2.6,960,300),(3.65,935,265),(4.4,935,265),(5.3,450,560),(6,450,560)],[(3.7,935,265),(5.3,450,560)])
    add(id_, page(css, body, brand), 'app', 'Neumorphism app UI', f"{brand} · {sub}")

# ---------------- 3. CLAYMORPHISM ----------------
def clay(id_, brand, sub, bg1, bg2, main, kind):
    css = f"""
body{{background:radial-gradient(900px 600px at 70% 20%,{bg1},{bg2})}}
.chip{{background:#fff;color:{main};box-shadow:0 10px 20px rgba(60,40,140,.2),inset 0 -4px 0 rgba(0,0,0,.06)}}
.ph{{position:absolute;width:300px;height:600px;border-radius:44px;background:#fbfaff;box-shadow:0 40px 70px rgba(50,30,130,.35),inset 0 -8px 0 rgba(80,60,160,.08);overflow:hidden;animation:up 1s cubic-bezier(.2,.8,.2,1) both}}
.a{{left:200px;top:80px;transform:rotate(-8deg);animation-delay:.15s}}.b{{left:560px;top:70px;transform:rotate(6deg);animation-delay:.4s}}
.ph .in{{animation:float 4s 1.4s ease-in-out infinite}}
.hd{{height:250px;background:{main};border-radius:0 0 40px 40px;padding:24px 22px;color:#fff;position:relative}}
.cc{{margin-top:28px;border-radius:24px;padding:18px;background:linear-gradient(145deg,{main},#0002);box-shadow:inset 0 6px 10px rgba(255,255,255,.35),inset 0 -8px 12px rgba(0,0,0,.25),0 16px 26px rgba(0,0,0,.3);font:500 12px Poppins;animation:pop .7s 1s both}}
.cc b{{display:block;font:700 22px Poppins;margin:4px 0 12px}}
.qs{{display:flex;justify-content:space-between;padding:18px 18px 0}}
.q{{text-align:center;font:500 10px Poppins;color:#6a6890}}
.q i{{display:block;width:52px;height:52px;border-radius:18px;margin:0 auto 6px;box-shadow:inset 0 6px 8px rgba(255,255,255,.55),inset 0 -6px 10px rgba(0,0,0,.18),0 10px 16px rgba(0,0,0,.18);animation:pop .55s both;display:grid;place-items:center;font-style:normal;color:#fff;font-size:20px}}
.rc{{padding:14px 18px 0;font:700 15px Poppins;color:#2e2a52}}
.tx{{margin:10px 16px 0;border-radius:18px;background:#fff;box-shadow:0 10px 18px rgba(60,40,140,.14),inset 0 -4px 0 rgba(60,40,140,.06);display:flex;align-items:center;gap:12px;padding:10px 12px;font:600 12px Poppins;color:#2e2a52;animation:up .6s both}}
.tx i{{width:34px;height:34px;border-radius:12px;box-shadow:inset 0 4px 6px rgba(255,255,255,.5),inset 0 -4px 6px rgba(0,0,0,.2)}}
.tx span{{flex:1}}.tx small{{display:block;font:400 10px Poppins;color:#9a98b8}}
.chart{{margin:20px 16px 0;height:220px;border-radius:28px;background:{main};box-shadow:inset 0 8px 12px rgba(255,255,255,.3),inset 0 -10px 14px rgba(0,0,0,.25),0 16px 26px rgba(0,0,0,.25);display:flex;align-items:flex-end;justify-content:space-around;padding:20px 16px}}
.chart b{{width:20px;border-radius:12px;background:linear-gradient(#ffb3c1,#ff6f8f);box-shadow:inset 0 4px 4px rgba(255,255,255,.6),0 6px 10px rgba(0,0,0,.25);transform-origin:bottom;animation:grow 1.2s both}}
.navb{{position:absolute;bottom:0;left:0;right:0;height:70px;background:{main};border-radius:30px 30px 0 0;display:flex;justify-content:space-around;align-items:center;color:#fffc;font-size:18px}}
.fab{{width:60px;height:60px;border-radius:50%;background:{main};box-shadow:inset 0 6px 8px rgba(255,255,255,.4),inset 0 -6px 10px rgba(0,0,0,.3),0 8px 16px rgba(0,0,0,.3);margin-top:-36px;display:grid;place-items:center;color:#fff;animation:press2 .5s 3.7s both}}
@keyframes press2{{50%{{transform:scale(.88)}}}}
"""
    if kind == 'bank':
        hd = f"<div style='display:flex;justify-content:space-between;font-size:18px'><span>⁘</span><span style='width:30px;height:30px;border-radius:50%;background:#ffd6a8;display:inline-block'></span></div><div class='cc'>Balance<b>₹<span class='num' style='animation:cnt 2s 1.2s both;--n:328000'></span></b>•••• •••• •••• 3432 &nbsp;&nbsp; 10/30</div>"
        qs = [('#3ccf7a','⇄','Transfer'),('#ff8fb1','₹','Pay bill'),('#8b7bff','🛍','Shop'),('#4cc9e0','◎','Saving')]
        tx = [('#ff6b6b','Cloud subscription','21 Dec','₹649'),('#3ccf7a','Bank transfer','21 Dec','₹2,580'),('#ff6b6b','Coffee house','20 Dec','₹180')]
        t2 = 'Spending'
    elif kind == 'kids':
        hd = f"<div style='display:flex;justify-content:space-between;font-size:18px'><span>⁘</span><span style='width:30px;height:30px;border-radius:50%;background:#ffe08a;display:inline-block'></span></div><div class='cc'>Hi Aanya! Today's stars<b>⭐ <span class='num' style='animation:cnt 2s 1.2s both;--n:48'></span> stars</b>Level 6 · Super reader</div>"
        qs = [('#3ccf7a','A','ABC'),('#ff8fb1','1','Maths'),('#8b7bff','♪','Rhymes'),('#4cc9e0','✎','Draw')]
        tx = [('#ffb547','Phonics: B words','Done','+5 ⭐'),('#3ccf7a','Count to 20','Done','+4 ⭐'),('#8b7bff','Colour the fish','New','+3 ⭐')]
        t2 = 'Learning week'
    else:
        hd = f"<div style='display:flex;justify-content:space-between;font-size:18px'><span>⁘</span><span style='width:30px;height:30px;border-radius:50%;background:#ffd6a8;display:inline-block'></span></div><div class='cc'>Your order arrives in<b><span class='num' style='animation:cnt 2s 1.2s both;--n:18'></span> min</b>Rider Imran is on the way</div>"
        qs = [('#ff9f43','🍛','Thali'),('#ff8fb1','🥗','Healthy'),('#8b7bff','🍰','Dessert'),('#3ccf7a','🥤','Drinks')]
        tx = [('#ff9f43','Rajma chawal thali','Today','₹149'),('#3ccf7a','Paneer wrap','Yesterday','₹119'),('#ff8fb1','Gulab jamun (2)','Yesterday','₹60')]
        t2 = 'Orders this week'
    a = f"<div class='in'><div class='hd'>{hd}</div><div class='qs'>" + ''.join(f"<div class='q'><i style='background:{c};animation-delay:{1.3+i*.15}s'>{s}</i>{n}</div>" for i,(c,s,n) in enumerate(qs)) + "</div><div class='rc'>Recent</div>" + ''.join(f"<div class='tx' style='animation-delay:{1.9+i*.2}s'><i style='background:{c}'></i><span>{n}<small>{d}</small></span><b style='color:{c}'>{v}</b></div>" for i,(c,n,d,v) in enumerate(tx)) + "</div><div class='navb'><span>⌂</span><span>✉</span><div class='fab'>▣</div><span>◷</span><span>☺</span></div>"
    b = f"<div class='in'><div style='padding:24px 22px 0;display:flex;justify-content:space-between;font:700 18px Poppins;color:#2e2a52'><span>‹</span><span>{t2}</span><span>⋮</span></div><div class='chart'>" + ''.join(f"<b style='height:{h}%;animation-delay:{1.4+i*.15}s'></b>" for i,h in enumerate([40,72,58,90,64,80])) + "</div><div class='rc' style='padding-top:20px'>History</div>" + ''.join(f"<div class='tx' style='animation-delay:{2.2+i*.2}s'><i style='background:{c}'></i><span>{n}<small>{d}</small></span><b style='color:{c}'>{v}</b></div>" for i,(c,n,d,v) in enumerate(tx[::-1])) + "</div>"
    body = f"<div class='chip'>Claymorphism UI</div><div class='ph a'>{a}</div><div class='ph b'>{b}</div>" + cursor([(0,1050,700),(2.8,380,640),(3.7,355,610),(4.5,355,610),(5.4,700,330),(6,700,330)],[(3.75,355,610)])
    add(id_, page(css, body, brand), 'app', 'Claymorphism app UI', f"{brand} · {sub}")

# ---------------- 4. GLASSMORPHISM ----------------
def glass(id_, brand, sub, g1, g2, g3, head, line, cta, kind):
    css = f"""
body{{background:linear-gradient(135deg,{g1},{g2} 55%,{g3});overflow:hidden}}
.chip{{background:rgba(255,255,255,.22);color:#fff;border:1px solid rgba(255,255,255,.45);backdrop-filter:blur(10px)}}
.orb{{position:absolute;border-radius:50%;animation:float 5s ease-in-out infinite}}
.panel{{position:absolute;left:90px;top:90px;width:900px;height:560px;border-radius:30px;background:linear-gradient(135deg,rgba(255,255,255,.32),rgba(255,255,255,.08));border:1.5px solid rgba(255,255,255,.55);backdrop-filter:blur(22px) saturate(140%);box-shadow:0 30px 60px rgba(30,0,80,.3);animation:up 1s .2s cubic-bezier(.2,.8,.2,1) both;color:#fff;padding:30px 44px}}
.nv{{display:flex;align-items:center;gap:30px;font:500 13px Poppins;opacity:.92}}
.nv .lg{{font:700 17px Poppins;margin-right:auto;display:flex;align-items:center;gap:8px}}
.nv .lg i{{width:22px;height:22px;border-radius:7px;background:linear-gradient(135deg,#fff,#fff6)}}
.nv .su{{padding:8px 16px;border-radius:12px;background:rgba(255,255,255,.25);border:1px solid rgba(255,255,255,.5)}}
.hh{{margin-top:70px;font:700 58px/1.04 Poppins;max-width:470px;text-shadow:0 4px 20px rgba(0,0,0,.15)}}
.hh span{{display:block;animation:up .8s both}}
.ln{{width:330px;height:2px;background:#fffa;margin:22px 0;transform-origin:left;animation:growx 1s 1.6s both}}
.pp{{font:400 14px/1.6 Poppins;max-width:400px;opacity:.9;animation:fi .8s 1.8s both}}
.cta{{display:inline-block;margin-top:30px;padding:14px 26px;border-radius:16px;background:rgba(255,255,255,.9);color:{g2};font:600 14px Poppins;box-shadow:0 10px 24px rgba(0,0,0,.2);animation:pop .6s 2.2s both}}
.cta.pr{{animation:pop .6s 2.2s both,pr .4s 4.1s}}
@keyframes pr{{50%{{transform:scale(.93)}}}}
.gc{{position:absolute;border-radius:22px;background:rgba(255,255,255,.2);border:1px solid rgba(255,255,255,.5);backdrop-filter:blur(14px);padding:16px 18px;font:500 12px Poppins;animation:pop .7s both}}
.gc b{{display:block;font:700 22px Poppins}}
.toast{{position:absolute;left:50%;top:40px;transform:translateX(-50%);padding:12px 20px;border-radius:16px;background:rgba(255,255,255,.28);border:1px solid rgba(255,255,255,.6);backdrop-filter:blur(14px);color:#fff;font:600 13px Poppins;opacity:0;animation:ts 1.6s 4.3s both}}
@keyframes ts{{0%{{opacity:0;transform:translate(-50%,-20px)}}20%,80%{{opacity:1;transform:translate(-50%,0)}}100%{{opacity:1}}}}
"""
    orbs = [(40,60,120,'#5ee7df,#3ab0ff'),(870,40,170,'#7ad7ff,#2f7bff'),(-60,520,240,'#c79bff,#7a3cff'),(640,330,220,'#ff8ac2,#b31f7a'),(560,170,70,'#9ad0ff,#4a7bff'),(820,250,110,'#c69bff,#8a3cff'),(500,420,60,'#7af0d8,#1fa38f')]
    orbh = ''.join(f"<div class='orb' style='left:{x}px;top:{y}px;width:{s}px;height:{s}px;background:radial-gradient(circle at 30% 30%,{c.split(',')[0]},{c.split(',')[1]});animation-delay:{i*.5}s'></div>" for i,(x,y,s,c) in enumerate(orbs))
    hl = ''.join(f"<span style='animation-delay:{.9+i*.25}s'>{w}</span>" for i,w in enumerate(head))
    if kind == 'ai': cards = [(600,140,'Tasks automated','<span class="num" style="animation:cnt 2s 2s both;--n:1240"></span>'),(690,330,'Hours saved / week','<span class="num" style="animation:cnt 2s 2.2s both;--n:36"></span>')]
    elif kind == 'travel': cards = [(600,140,'Trips planned','<span class="num" style="animation:cnt 2s 2s both;--n:8400"></span>+'),(690,330,'Avg. rating','4.9 ★')]
    else: cards = [(600,140,'Projects delivered','<span class="num" style="animation:cnt 2s 2s both;--n:320"></span>+'),(690,330,'Happy clients','<span class="num" style="animation:cnt 2s 2.2s both;--n:98"></span>%')]
    ch = ''.join(f"<div class='gc' style='left:{x}px;top:{y}px;animation-delay:{2+i*.3}s'>{t}<b>{v}</b></div>" for i,(x,y,t,v) in enumerate(cards))
    body = f"{orbh}<div class='chip'>Glassmorphism UI</div><div class='panel'><div class='nv'><div class='lg'><i></i>{brand}</div><span>Home</span><span>Features</span><span>Pricing</span><span>Contact</span><span class='su'>Sign up</span></div><div class='hh'>{hl}</div><div class='ln'></div><div class='pp'>{line}</div><div class='cta pr'>{cta} →</div>{ch}</div><div class='toast'>✓ Welcome to {brand}!</div>" + cursor([(0,1050,700),(3.2,300,600),(4.1,260,585),(6,260,585)],[(4.15,260,585)])
    add(id_, page(css, body, brand), 'landing', 'Glassmorphism landing page', f"{brand} · {sub}")

# ---------------- 5. BENTO GRID ----------------
def bento(id_, brand, sub, dark, c1, c2, kind):
    css = f"""
body{{background:{dark}}}
.chip{{background:#ffffff14;color:#fff;border:1px solid #ffffff30}}
.g{{position:absolute;left:30px;top:84px;right:30px;bottom:30px;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(3,1fr);gap:16px}}
.t{{border-radius:24px;padding:20px 22px;position:relative;overflow:hidden;animation:pop .7s cubic-bezier(.2,.8,.2,1) both;font-family:Poppins}}
.p{{background:{c1};color:#fff}}.l{{background:{c2};color:#1d1640}}
.k{{font:500 13px Poppins;opacity:.8}}.v{{font:700 44px Poppins;line-height:1.1}}
.up{{font:600 13px Poppins;color:#2fbf71}}
.wv{{position:absolute;left:0;right:0;bottom:0;height:70%}}
.wv path{{transform-origin:bottom;animation:grow 1.6s both}}
.ast{{position:absolute;right:30px;bottom:24px;width:90px;height:90px;animation:spin2 6s linear both}}
@keyframes spin2{{to{{transform:rotate(240deg)}}}}
.av{{width:34px;height:34px;border-radius:50%;border:3px solid {c2};display:inline-block;margin-right:-10px}}
.ring{{position:absolute;right:-30px;top:-30px;width:180px;height:180px;border-radius:50%;background:conic-gradient(#ffffff55 calc(var(--p)*1%),#ffffff18 0);-webkit-mask:radial-gradient(circle,transparent 54%,#000 55%);animation:ring 2s 1.4s both;--p:68}}
.ph{{position:absolute;right:-20px;top:20px;width:150px;height:240px;border-radius:26px;background:#111;border:5px solid #222;transform:rotate(-14deg);padding:16px 10px;display:grid;grid-template-columns:1fr 1fr;gap:8px;align-content:start}}
.ph i{{height:40px;border-radius:12px;animation:pop .5s both}}
.bub{{position:absolute;right:24px;bottom:18px;width:120px;height:130px;border-radius:50% 50% 46% 54%;background:linear-gradient(160deg,{c1},#b9a6ff);display:grid;place-items:center;font-size:54px}}
"""
    if kind == 'saas':
        k = [("New users","<span class='num' style='animation:cnt 2s 1.2s both;--n:78'></span>K","+10%"),("Rating","4.9",""),("MRR","₹<span class='num' style='animation:cnt 2.2s 1.4s both;--n:24414'></span>",""),("Revenue","₹<span class='num' style='animation:cnt 2.2s 1.6s both;--n:230545'></span>","+23%"),("Manage your revenue lifecycle","",""),("App icon","","")]
    elif kind == 'notes':
        k = [("Notes written","<span class='num' style='animation:cnt 2s 1.2s both;--n:12'></span>K","+18%"),("App store","4.8",""),("Teams","<span class='num' style='animation:cnt 2.2s 1.4s both;--n:3100'></span>",""),("Pages synced","<span class='num' style='animation:cnt 2.2s 1.6s both;--n:96400'></span>","+31%"),("Think, write and share in one place","",""),("Widgets","","")]
    else:
        k = [("Orders today","<span class='num' style='animation:cnt 2s 1.2s both;--n:4'></span>.2K","+12%"),("Store rating","4.7",""),("Avg. order","₹<span class='num' style='animation:cnt 2.2s 1.4s both;--n:1840'></span>",""),("Sales this month","₹<span class='num' style='animation:cnt 2.2s 1.6s both;--n:982400'></span>","+27%"),("Run your whole store from one screen","",""),("Mobile app","","")]
    wave = f"<svg class='wv' viewBox='0 0 400 140' preserveAspectRatio='none'><path d='M0 140 L0 60 C60 30 100 90 160 60 S260 20 320 50 S380 40 400 30 L400 140Z' fill='#ffffff30' style='animation-delay:1.3s'/><path d='M0 140 L0 90 C60 60 110 110 170 85 S270 60 330 80 S390 70 400 60 L400 140Z' fill='#ffffff55' style='animation-delay:1.5s'/></svg>"
    tiles = [
      f"<div class='t p' style='animation-delay:.2s'><div style='font:800 46px Poppins;margin-top:30px'>{brand.lower()}<span style='color:#b9a6ff'>●</span></div></div>",
      f"<div class='t l' style='grid-column:span 2;animation-delay:.35s'><div class='k'>{k[5][0]}</div><div class='ph'>" + ''.join(f"<i style='background:{c};animation-delay:{1.2+j*.12}s'></i>" for j,c in enumerate([c1,'#ff8a65','#4cc9e0','#ffd166','#2fbf71','#ff6fa3'])) + "</div></div>",
      f"<div class='t l' style='grid-row:span 2;animation-delay:.5s'><div class='k'>Customers</div><div class='bub'>😊</div></div>",
      f"<div class='t l' style='animation-delay:.6s'><div class='k'>{k[0][0]}</div><div class='v'>{k[0][1]}</div><div class='up'>{k[0][2]}</div></div>",
      f"<div class='t l' style='animation-delay:.7s'><div class='v'>{k[1][1]} ↗</div><div style='margin-top:14px'><span class='av' style='background:#ffd166'></span><span class='av' style='background:#ff8a65'></span><span class='av' style='background:#4cc9e0'></span></div></div>",
      f"<div class='t l' style='grid-row:span 2;animation-delay:.8s'><div style='font:500 22px/1.3 Poppins'>{k[4][0]}</div><svg class='ast' viewBox='0 0 100 100'><g fill='{c1}'>" + ''.join(f"<rect x='42' y='4' width='16' height='46' rx='8' transform='rotate({a} 50 50)'/>" for a in range(0,360,60)) + "</g></svg></div>",
      f"<div class='t p' style='grid-column:span 2;animation-delay:.9s'><div class='k'>{k[2][0]}</div><div class='v' style='font-size:36px'>{k[2][1]}</div>{wave}</div>",
      f"<div class='t p' style='animation-delay:1s'><div class='ring'></div><div class='up' style='color:#fff;background:#ffffff26;display:inline-block;padding:4px 10px;border-radius:10px;margin-top:40px'>{k[3][2]}</div><div class='k' style='margin-top:10px'>{k[3][0]}</div><div class='v' style='font-size:28px'>{k[3][1]}</div></div>",
    ]
    body = f"<div class='chip'>Bento grid UI</div><div class='g'>{''.join(tiles)}</div>" + cursor([(0,1050,700),(3,520,250),(3.8,500,240),(6,780,520)],[(3.85,500,240)])
    add(id_, page(css, body, brand), 'dash', 'Bento grid dashboard', f"{brand} · {sub}")

skeuo('ui-s01','PaisaPro','personal finance app','#ff5e9a','#ffb347','fin')
skeuo('ui-s02','AuraHome','smart home app','#2f8cff','#6ee7f9','home')
skeuo('ui-s03','TuneLoft','music player app','#ff7a3d','#ff3d7f','music')
neu('ui-s04','PulseFit','fitness tracker app','#dbe9f6','#7a4dff','#ff4fd8','fit')
neu('ui-s05','Hommly','smart home control app','#e4ebf3','#2a9dff','#46e0c4','home')
neu('ui-s06','CalmNest','meditation app','#ebe7f6','#8a5cff','#ff7ab0','calm')
clay('ui-s07','Coinly','digital banking app','#e9e4ff','#bdb1ff','#6c4cf1','bank')
clay('ui-s08','Doodle Learn','kids learning app','#ffe9f2','#ffc4dc','#ff5d9e','kids')
clay('ui-s09','Tiffin Go','home food delivery app','#fff1e0','#ffd2a6','#ff8a1f','food')
glass('ui-s10','Nebula AI','AI automation SaaS','#38c6ff','#7b4dff','#c21fd6',['Automate','your work','with AI'],'Nebula AI writes, replies and reports for you, so your team saves hours every single week.','Start free trial','ai')
glass('ui-s11','SkyRoute','travel booking site','#2ed8c3','#2a7bff','#7b4dff',['Your next','trip, sorted'],'Flights, stays and day plans in one place. Smart prices, zero stress.','Plan my trip','travel')
glass('ui-s12','Lumen Studio','creative agency portfolio','#ff9a8b','#a14dff','#3b2bd6',['Design that','moves people'],'Brand identity, websites and motion design for brands that want to stand out.','See our work','agency')
bento('ui-s13','Orbit','revenue SaaS dashboard','#1b1636','#5b3df5','#ece8ff','saas')
bento('ui-s14','Kite','notes app launch page','#13221f','#13a37f','#e3f7ef','notes')
bento('ui-s15','Cartly','store owner dashboard','#22140f','#ff6a2b','#fff0e6','store')
json.dump(ITEMS, open(f"{OUT}/rows.json", 'w'), ensure_ascii=False)
print(len(ITEMS))
