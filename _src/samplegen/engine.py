#!/usr/bin/env python3
"""Flow Studio UI-mockup sample engine: builds one HTML scene per sample (5 s CSS animation)."""
import json, os, sys, html
import os
S = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'samples')) + '/'
def img(n): return 'file://' + S + n + '.jpg'
e = html.escape

BASE_CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:720px;overflow:hidden}
body{font-family:Inter,'DejaVu Sans',sans-serif;color:#10131a;
 background:radial-gradient(120% 90% at 30% 15%,var(--g1),transparent 60%),radial-gradient(90% 80% at 85% 90%,var(--g2),transparent 60%),#07080d;}
body:after{content:"";position:fixed;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.018) 0 1px,transparent 1px 80px),repeating-linear-gradient(0deg,rgba(255,255,255,.018) 0 1px,transparent 1px 80px);pointer-events:none}
.stage{position:absolute;inset:0;perspective:1600px;display:grid;place-items:center}
.cam{transform-style:preserve-3d;animation:cam 5s cubic-bezier(.45,.05,.3,1) both;position:relative}
@keyframes cam{from{transform:rotateY(-9deg) rotateX(5deg) scale(.95) translateY(10px)}to{transform:rotateY(5deg) rotateX(2deg) scale(1.03) translateY(-4px)}}
.lap{width:820px}
.lap .bez{background:#0c0d11;border-radius:22px 22px 6px 6px;padding:14px 14px 18px;box-shadow:0 0 0 1.5px #2a2c33,0 40px 90px -20px rgba(0,0,0,.85),0 0 120px -30px var(--acc)}
.lap .scr{height:500px;border-radius:8px;overflow:hidden;position:relative;background:#fff}
.lap .base{height:16px;margin:0 -46px;background:linear-gradient(#cfd2d8,#8d9097);border-radius:0 0 18px 18px;box-shadow:0 18px 40px -10px rgba(0,0,0,.8)}
.lap .base:before{content:"";display:block;width:120px;height:6px;margin:0 auto;background:#a8abb2;border-radius:0 0 8px 8px}
.ph{position:absolute;width:236px;height:480px;border-radius:38px;background:#0b0c10;padding:10px;box-shadow:0 0 0 2px #34363d,0 40px 80px -20px rgba(0,0,0,.9),0 0 90px -30px var(--acc)}
.ph .scr{width:100%;height:100%;border-radius:29px;overflow:hidden;position:relative;background:#fff}
.ph .scr:before{content:"";position:absolute;top:7px;left:50%;width:70px;height:20px;margin-left:-35px;border-radius:12px;background:#000;z-index:9}
.solo{left:50%;top:50%;transform:translate(-50%,-50%) translateZ(40px)}
.bar{height:30px;background:#f1f2f5;display:flex;align-items:center;gap:6px;padding:0 12px;border-bottom:1px solid #e3e5ea;font-size:11px;color:#6b7180}
.bar i{width:10px;height:10px;border-radius:50%;background:#ff5f57}.bar i+i{background:#febc2e}.bar i+i+i{background:#28c840}
.bar .url{margin-left:14px;flex:1;background:#fff;border-radius:6px;padding:4px 10px;border:1px solid #e3e5ea}
.fu{animation:fu .6s cubic-bezier(.2,.8,.2,1) both}
@keyframes fu{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
.pop{animation:pop .45s cubic-bezier(.2,1.4,.4,1) both}
@keyframes pop{from{opacity:0;transform:scale(.6)}to{opacity:1;transform:none}}
.grow{transform-origin:bottom;animation:grow .9s cubic-bezier(.2,.8,.2,1) both}
@keyframes grow{from{transform:scaleY(0)}to{transform:scaleY(1)}}
.growx{transform-origin:left;animation:growx 1s cubic-bezier(.2,.8,.2,1) both}
@keyframes growx{from{transform:scaleX(0)}to{transform:scaleX(1)}}
.scroll{animation:scroll 3.4s cubic-bezier(.6,0,.25,1) 1.1s both}
@keyframes scroll{from{transform:none}to{transform:translateY(var(--sy))}}
.cursor{position:absolute;width:18px;height:18px;z-index:50;background:none}
.cursor:before{content:"";position:absolute;inset:0;clip-path:polygon(0 0,0 100%,30% 72%,52% 100%,64% 94%,44% 66%,82% 66%);background:#111;filter:drop-shadow(0 0 1.5px #fff) drop-shadow(0 0 1.5px #fff)}
.typing{display:inline-flex;gap:3px}.typing b{width:5px;height:5px;border-radius:50%;background:#9aa0aa;animation:bl 1s infinite}
@keyframes bl{50%{opacity:.25}}
.num{font-variant-numeric:tabular-nums}
.tag{display:inline-block;font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:3px 8px;border-radius:99px;background:var(--acc);color:#fff}
"""

def page(css, body, acc, g1, g2, js=''):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>:root{{--acc:{acc};--g1:{g1};--g2:{g2}}}{BASE_CSS}{css}</style></head>
<body><div class="stage"><div class="cam">{body}</div></div><script>{js}</script></body></html>"""

def d(x): return f'animation-delay:{x:.2f}s'

# ---------------- SEO ----------------
def seo(v):
    rows = ''.join(f'<div class="r fu" style="{d(.5+i*.12)}"><small>{e(u)}</small><b>{e(t)}</b><p>{e(s)}</p></div>' for i,(u,t,s) in enumerate(v['serp']))
    css = """.g{padding:14px 26px;font-size:12px;width:520px}.q{display:flex;gap:10px;align-items:center;margin-bottom:12px}.q b{font:800 22px Inter;letter-spacing:-.02em}
.q b span:nth-child(1){color:#4285f4}.q b span:nth-child(2){color:#ea4335}.q b span:nth-child(3){color:#fbbc05}.q b span:nth-child(4){color:#34a853}
.box{flex:1;border:1px solid #dfe1e5;border-radius:24px;padding:9px 16px;box-shadow:0 1px 6px rgba(32,33,36,.15);font-size:13px}
.box i{font-style:normal;overflow:hidden;white-space:nowrap;display:inline-block;vertical-align:bottom;border-right:2px solid #333;animation:ty 1.2s steps(40) .2s both}
@keyframes ty{from{width:0}to{width:var(--w)}}
.r{margin:10px 0 12px}.r small{color:#4d5156;font-size:11px}.r b{display:block;color:#1a0dab;font-size:15px;font-weight:500;margin:2px 0}.r p{color:#4d5156;font-size:11.5px;line-height:1.45}
.win{position:relative;padding:10px 54px 10px 12px;margin:0 -12px;border-radius:12px;background:linear-gradient(90deg,var(--acc2),transparent);animation:fu .6s both .45s}
.win:after{content:"#1";position:absolute;right:14px;top:12px;font:900 28px Inter Display;color:var(--acc)}
.blog{position:absolute;right:22px;top:112px;width:250px;border-radius:14px;background:#fff;box-shadow:0 20px 50px -10px rgba(0,0,0,.35);overflow:hidden;animation:fu .7s both 2.2s;font-size:11px}
.blog img{width:100%;height:110px;object-fit:cover}.blog div{padding:10px 12px}.blog h4{font:800 14px/1.25 Inter Display;margin:6px 0}
.st{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:8px}.st span{background:#f4f5f8;border-radius:8px;padding:6px;text-align:center;font-weight:800;font-size:13px}.st small{display:block;font-weight:500;font-size:9px;color:#777}"""
    body = f"""<div class="lap"><div class="bez"><div class="scr"><div class="bar"><i></i><i></i><i></i><span class="url">google.com/search?q={e(v['q']).replace(' ','+')}</span></div>
<div class="g"><div class="q"><b><span>G</span><span>o</span><span>o</span><span>g</span>le</b><div class="box"><i style="--w:{len(v['q'])*7.4}px">{e(v['q'])}</i></div></div>
<div class="win"><small style="color:#202124;font-weight:600">{e(v['site'])}</small><b style="display:block;color:#1a0dab;font-size:16px;font-weight:600;margin:3px 0">{e(v['title'])}</b><p style="color:#4d5156;font-size:11.5px">{e(v['desc'])}</p></div>
{rows}</div>
<div class="blog"><img src="{img(v['img'])}"><div><span class="tag">Blog · SEO</span><h4>{e(v['title'])}</h4><p style="color:#666">{e(v['brand'])} · 6 min read</p>
<div class="st"><span class="pop" style="{d(2.8)}">#1<small>Google rank</small></span><span class="pop" style="{d(3.0)}">{e(v['traffic'])}<small>visits/mo</small></span><span class="pop" style="{d(3.2)}">{e(v['leads'])}<small>enquiries</small></span></div></div></div>
</div></div><div class="base"></div></div>"""
    return page(css.replace('var(--acc2)', v['acc'] + '22'), body, v['acc'], v['acc'] + '66', '#1e2b5a88')

# ---------------- Email + WhatsApp marketing ----------------
def mkt(v):
    css = """.mail{display:grid;grid-template-columns:170px 1fr;height:470px;font-size:11px}
.side{background:#f6f7fb;padding:14px;border-right:1px solid #e6e8ee}.side b{display:block;font-size:13px;margin-bottom:10px}.side div{padding:6px 8px;border-radius:7px;color:#555}.side .on{background:var(--acc);color:#fff;font-weight:700}
.main{padding:16px 18px;overflow:hidden}.main h3{font:800 17px Inter Display;margin-bottom:10px}
.k{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.k div{border:1px solid #eceef3;border-radius:10px;padding:9px}.k b{font:800 20px Inter Display;display:block}.k small{color:#888}
.chart{display:flex;align-items:flex-end;gap:7px;height:120px;margin:14px 0 8px;padding:10px;border:1px solid #eceef3;border-radius:10px}.chart i{flex:1;background:linear-gradient(var(--acc),#0000);border-radius:4px 4px 0 0}
.nl{position:absolute;left:182px;top:205px;width:260px;border-radius:10px;overflow:hidden;box-shadow:0 14px 40px -12px rgba(0,0,0,.4);background:#fff;animation:fu .6s both 1.6s}.nl img{width:100%;height:96px;object-fit:cover}.nl div{padding:9px 11px}.nl h4{font:800 13px Inter Display;margin:4px 0}.nl a{display:inline-block;margin-top:6px;background:var(--acc);color:#fff;padding:5px 12px;border-radius:99px;font-weight:700;text-decoration:none}
.wa{background:#efe7dd;height:100%;padding:44px 10px 10px;font-size:10.5px}.wa .top{position:absolute;top:0;left:0;right:0;height:58px;background:#075e54;color:#fff;padding:30px 12px 0;font-weight:700;font-size:12px}
.msg{background:#fff;border-radius:9px;padding:6px;margin-top:20px;box-shadow:0 1px 1px rgba(0,0,0,.12);animation:fu .6s both 2.4s}.msg img{width:100%;height:110px;object-fit:cover;border-radius:6px}.msg p{margin:6px 2px;line-height:1.4}
.msg .cta{border-top:1px solid #eee;text-align:center;color:#128c7e;font-weight:700;padding-top:6px}
.tick{color:#34b7f1;font-size:10px;text-align:right}
.rep{background:#dcf8c6;border-radius:9px;padding:6px 8px;margin:8px 0 0 50px;animation:fu .5s both 3.6s}"""
    bars = ''.join(f'<i class="grow" style="height:{h}%;{d(.6+i*.07)}"></i>' for i,h in enumerate(v['bars']))
    kp = ''.join(f'<div class="fu" style="{d(.3+i*.12)}"><b class="num">{e(a)}</b><small>{e(b)}</small></div>' for i,(a,b) in enumerate(v['kpi']))
    body = f"""<div class="lap"><div class="bez"><div class="scr"><div class="bar"><i></i><i></i><i></i><span class="url">campaigns · {e(v['brand'])}</span></div>
<div class="mail"><div class="side"><b>{e(v['brand'])}</b><div class="on">Campaigns</div><div>Audience · {e(v['aud'])}</div><div>Automations</div><div>WhatsApp broadcast</div><div>Reports</div></div>
<div class="main"><h3>{e(v['camp'])}</h3><div class="k">{kp}</div><div class="chart">{bars}</div></div></div>
<div class="nl"><img src="{img(v['img'])}"><div><span class="tag">Newsletter</span><h4>{e(v['head'])}</h4><p style="color:#666">{e(v['line'])}</p><a>{e(v['btn'])}</a></div></div>
</div></div><div class="base"></div></div>
<div class="ph" style="right:-26px;top:40px;transform:translateZ(90px) scale(.9)"><div class="scr"><div class="wa"><div class="top">{e(v['brand'])} ✓</div>
<div class="msg"><img src="{img(v['img'])}"><p><b>{e(v['head'])}</b><br>{e(v['wa'])}</p><div class="tick">10:30 ✓✓</div><div class="cta">{e(v['btn'])}</div></div>
<div class="rep">{e(v['reply'])} <span class="tick">10:32</span></div></div></div></div>"""
    return page(css, body, v['acc'], v['acc'] + '55', '#0e5e4a77')

# ---------------- Chatbot ----------------
def chatbot(v):
    css = """.wa{background:#efe7dd;height:100%;padding:62px 9px 12px;font-size:10.5px;display:flex;flex-direction:column;justify-content:flex-end;gap:6px}
.top{position:absolute;top:0;left:0;right:0;height:58px;background:#075e54;color:#fff;padding:30px 12px 0;font-weight:700;font-size:12px;z-index:3}.top small{display:block;font-weight:400;font-size:9px;opacity:.8}
.b{max-width:84%;padding:6px 8px;border-radius:9px;line-height:1.38;box-shadow:0 1px 1px rgba(0,0,0,.1)}.u{align-self:flex-end;background:#dcf8c6}.bt{align-self:flex-start;background:#fff}
.qr{display:flex;flex-wrap:wrap;gap:4px;margin-top:2px}.qr span{border:1px solid #128c7e;color:#128c7e;border-radius:99px;padding:3px 7px;font-weight:700;font-size:9.5px;background:#fff}
.flow{position:absolute;left:-330px;top:20px;width:290px;font-size:11px;color:#e9ecf5}
.flow h3{font:800 20px Inter Display;color:#fff;margin-bottom:12px}.node{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-radius:12px;padding:9px 11px;margin-bottom:9px;backdrop-filter:blur(6px);display:flex;gap:8px;align-items:center}
.node i{width:22px;height:22px;border-radius:7px;background:var(--acc);display:grid;place-items:center;font-style:normal;font-size:12px}
.st{position:absolute;right:-300px;top:70px;width:250px;color:#fff}.st div{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);border-radius:14px;padding:12px 14px;margin-bottom:10px}.st b{font:800 26px Inter Display;display:block}.st small{opacity:.75}"""
    msgs = ''
    t = .4
    for who, txt, *q in v['chat']:
        cls = 'u' if who == 'u' else 'bt'
        qr = ''.join(f'<span>{e(x)}</span>' for x in q[0]) if q else ''
        msgs += f'<div class="b {cls} fu" style="{d(t)}">{txt}{"<div class=qr>"+qr+"</div>" if qr else ""}</div>'
        t += .48
    nodes = ''.join(f'<div class="node fu" style="{d(.3+i*.25)}"><i>{ic}</i>{e(n)}</div>' for i,(ic,n) in enumerate(v['flow']))
    stats = ''.join(f'<div class="fu" style="{d(2.6+i*.3)}"><b>{e(a)}</b><small>{e(b)}</small></div>' for i,(a,b) in enumerate(v['stats']))
    body = f"""<div style="width:236px;height:480px;position:relative"><div class="flow"><h3>{e(v['brand'])}<br><span style="color:var(--acc)">AI WhatsApp bot</span></h3>{nodes}</div>
<div class="ph" style="left:0;top:0"><div class="scr"><div class="top">{e(v['brand'])} <small>bot · replies instantly</small></div><div class="wa">{msgs}</div></div></div>
<div class="st">{stats}</div></div>"""
    return page(css, body, v['acc'], v['acc'] + '55', '#0b6b5a66')

# ---------------- Pitch deck ----------------
def deck(v):
    css = """.sl{position:absolute;inset:0;padding:40px 46px;animation:sl 5s both;opacity:0}
@keyframes sl{0%{opacity:0;transform:translateX(40px)}4%{opacity:1;transform:none}26%{opacity:1;transform:none}31%{opacity:0;transform:translateX(-40px)}100%{opacity:0}}
.sl h2{font:800 34px/1.05 Inter Display;letter-spacing:-.02em}.sl p{color:#5d6370;font-size:14px;margin-top:10px;max-width:420px;line-height:1.5}
.cover{background:linear-gradient(135deg,var(--acc),#10131a);color:#fff}.cover p{color:#ffffffcc}.cover img{position:absolute;right:0;top:0;width:44%;height:100%;object-fit:cover;clip-path:polygon(18% 0,100% 0,100% 100%,0 100%)}
.bars{display:flex;gap:22px;align-items:flex-end;height:230px;margin-top:24px}.bars div{width:70px;text-align:center;font-weight:800}.bars i{display:block;background:linear-gradient(var(--acc),var(--acc)88);border-radius:8px 8px 0 0;margin-bottom:6px}
.big{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:30px}.big div{border-radius:16px;background:#f4f5f8;padding:18px}.big b{font:800 36px Inter Display;color:var(--acc);display:block}
.pn{position:absolute;bottom:14px;right:20px;font-size:11px;color:#999}"""
    s1 = f'<div class="sl cover" style="{d(0)}"><span class="tag" style="background:#fff;color:#111">Investor deck · 2026</span><h2 style="margin-top:18px;max-width:420px">{e(v["brand"])}</h2><p>{e(v["tag"])}</p><img src="{img(v["img"])}"></div>'
    s2 = f'<div class="sl" style="animation-delay:1.25s;background:#fff"><span class="tag">The problem</span><h2 style="margin-top:14px">{e(v["prob"])}</h2><p>{e(v["probp"])}</p><div class="big">' + ''.join(f'<div><b>{e(a)}</b>{e(b)}</div>' for a,b in v['facts']) + '</div><span class="pn">02</span></div>'
    bars = ''.join(f'<div><i style="height:{h}px"></i>{e(l)}</div>' for l,h in v['growth'])
    s3 = f'<div class="sl" style="animation-delay:2.5s;background:#fff"><span class="tag">Traction</span><h2 style="margin-top:14px">{e(v["trac"])}</h2><div class="bars">{bars}</div><span class="pn">05</span></div>'
    s4 = f'<div class="sl cover" style="animation-delay:3.75s;animation-name:sl4"><span class="tag" style="background:#fff;color:#111">The ask</span><h2 style="margin-top:18px">{e(v["ask"])}</h2><p>{e(v["use"])}</p><img src="{img(v["img"])}"></div>'
    css += "@keyframes sl4{0%{opacity:0;transform:translateX(40px)}5%{opacity:1;transform:none}100%{opacity:1}}"
    body = f'<div class="lap"><div class="bez"><div class="scr">{s1}{s2}{s3}{s4}</div></div><div class="base"></div></div>'
    return page(css, body, v['acc'], v['acc'] + '55', '#22183a88')

# ---------------- Dashboard ----------------
def dash(v):
    css = """.db{display:grid;grid-template-columns:150px 1fr;height:470px;font-size:11px;background:#0f1218;color:#dfe3ec}
.nav{background:#0a0c11;padding:14px 12px;border-right:1px solid #1d212b}.nav b{display:block;color:#fff;font-size:13px;margin-bottom:12px}.nav div{padding:6px 8px;border-radius:7px;color:#8a92a6;margin-bottom:2px}.nav .on{background:var(--acc)22;color:var(--acc);font-weight:700}
.m{padding:14px 16px;display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:min-content;gap:10px}
.c{background:#161a23;border:1px solid #232836;border-radius:12px;padding:11px}.c small{color:#8a92a6}.c b{display:block;font:800 21px Inter Display;color:#fff;margin-top:3px}.c em{font-style:normal;color:#3ddc97;font-size:10px}
.w2{grid-column:span 3}.w1{grid-column:span 1}
.ln{height:150px;margin-top:8px}.ln path{stroke-dasharray:1400;stroke-dashoffset:1400;animation:dr 2.2s cubic-bezier(.4,0,.2,1) .7s forwards}
@keyframes dr{to{stroke-dashoffset:0}}
.donut{width:120px;height:120px;border-radius:50%;margin:10px auto;background:conic-gradient(var(--acc) 0 var(--p1),#7c5cff 0 var(--p2),#3ddc97 0 var(--p3),#2a3040 0);-webkit-mask:radial-gradient(circle,#0000 45%,#000 46%);animation:pop .8s both 1s}
.tb{grid-column:span 4}.tb div{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;padding:6px 0;border-top:1px solid #232836}.tb b{font-size:11px;display:inline;font-family:Inter;color:#fff}"""
    kp = ''.join(f'<div class="c fu" style="{d(.3+i*.12)}"><small>{e(a)}</small><b class="num">{e(b)}</b><em>▲ {e(c)}</em></div>' for i,(a,b,c) in enumerate(v['kpi']))
    pts = v['line']; n = len(pts); W = 470; H = 140
    mx = max(pts); path = 'M' + ' L'.join(f'{i*W/(n-1):.0f},{H-p/mx*H*0.9:.0f}' for i,p in enumerate(pts))
    area = path + f' L{W},{H} L0,{H} Z'
    rows = ''.join(f'<div class="fu" style="{d(2.4+i*.15)}"><span><b>{e(r[0])}</b></span><span>{e(r[1])}</span><span>{e(r[2])}</span><span style="color:#3ddc97">{e(r[3])}</span></div>' for i,r in enumerate(v['rows']))
    p = v['split']
    body = f"""<div class="lap"><div class="bez"><div class="scr" style="background:#0f1218"><div class="bar" style="background:#0a0c11;border-color:#1d212b;color:#8a92a6"><i></i><i></i><i></i><span class="url" style="background:#161a23;border-color:#232836">app.{e(v['slug'])}.in/dashboard</span></div>
<div class="db"><div class="nav"><b>{e(v['brand'])}</b><div class="on">Overview</div>{''.join(f'<div>{e(x)}</div>' for x in v['nav'])}</div>
<div class="m">{kp}<div class="c w2 fu" style="{d(.6)}"><small>{e(v['lt'])}</small><svg class="ln" viewBox="0 0 {W} {H}" width="100%" preserveAspectRatio="none"><defs><linearGradient id="g" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{v['acc']}" stop-opacity=".35"/><stop offset="1" stop-color="{v['acc']}" stop-opacity="0"/></linearGradient></defs><path d="{area}" fill="url(#g)" class="fu" style="animation-delay:1.6s;stroke-dasharray:none"/><path d="{path}" fill="none" stroke="{v['acc']}" stroke-width="3"/></svg></div>
<div class="c w1 fu" style="{d(.8)}"><small>{e(v['dt'])}</small><div class="donut" style="--p1:{p[0]}%;--p2:{p[0]+p[1]}%;--p3:{p[0]+p[1]+p[2]}%"></div></div>
<div class="c tb fu" style="{d(2.2)}"><small>{e(v['tt'])}</small>{rows}</div></div></div></div></div><div class="base"></div></div>"""
    return page(css, body, v['acc'], v['acc'] + '44', '#16224688')

# ---------------- Online course ----------------
def course(v):
    css = """.cp{display:grid;grid-template-columns:1fr 230px;height:470px;font-size:11px}
.pl{padding:14px;background:#0d0f14}.vid{position:relative;height:280px;border-radius:12px;overflow:hidden}.vid img{width:100%;height:100%;object-fit:cover;animation:kb 5s linear both}
@keyframes kb{from{transform:scale(1.02)}to{transform:scale(1.12)}}
.vid .pb{position:absolute;left:12px;right:12px;bottom:12px;height:5px;border-radius:9px;background:#ffffff44}.vid .pb i{display:block;height:100%;width:62%;background:var(--acc);border-radius:9px}
.vid .play{position:absolute;left:50%;top:50%;width:58px;height:58px;margin:-29px;border-radius:50%;background:#ffffffdd;display:grid;place-items:center;font-size:20px;animation:pop .5s both .5s}
.vid .cap{position:absolute;left:0;right:0;bottom:30px;text-align:center;color:#fff;font-weight:700;font-size:14px;text-shadow:0 2px 6px #000;animation:fu .5s both 1.6s}
.pl h3{color:#fff;font:800 18px Inter Display;margin:12px 0 4px}.pl p{color:#9aa3b5}
.pg{display:flex;gap:8px;margin-top:10px}.pg span{background:#1a1e28;color:#cfd6e4;border-radius:9px;padding:7px 10px}
.ls{background:#fff;padding:12px;overflow:hidden}.ls b{font-size:12px}.li{display:flex;gap:8px;align-items:center;padding:8px;border-radius:9px;margin-top:6px;background:#f5f6f9}.li i{width:20px;height:20px;border-radius:50%;background:#e2e5ec;display:grid;place-items:center;font-style:normal;font-size:10px}
.li.d i{background:#3ddc97;color:#fff}.li.on{background:var(--acc);color:#fff}.li.on i{background:#fff;color:var(--acc)}
.cert{position:absolute;right:-90px;bottom:-30px;width:250px;transform:translateZ(80px) rotate(-4deg);background:#fffdf6;border-radius:12px;padding:16px;box-shadow:0 30px 60px -15px rgba(0,0,0,.7);text-align:center;border:3px double #c9a54a;animation:fu .8s both 3.2s}
.cert h4{font:800 16px Inter Display;margin:6px 0 2px}.cert small{color:#777;font-size:10px}"""
    les = ''.join(f'<div class="li {"d" if i<v["done"] else ("on" if i==v["done"] else "")} fu" style="{d(.3+i*.1)}"><i>{"✓" if i<v["done"] else i+1}</i>{e(x)}</div>' for i,x in enumerate(v['lessons']))
    body = f"""<div class="lap"><div class="bez"><div class="scr"><div class="bar"><i></i><i></i><i></i><span class="url">learn.{e(v['slug'])}.com/course</span></div>
<div class="cp"><div class="pl"><div class="vid"><img src="{img(v['img'])}"><div class="play">▶</div><div class="cap">{e(v['cap'])}</div><div class="pb"><i class="growx" style="{d(.8)}"></i></div></div>
<h3>{e(v['title'])}</h3><p>{e(v['by'])}</p><div class="pg"><span>{e(v['n'])} lessons</span><span>{e(v['stu'])} students</span><span>★ {e(v['rate'])}</span><span>Certificate</span></div></div>
<div class="ls"><b>Course content</b>{les}</div></div></div></div><div class="base"></div></div>
<div class="cert"><span class="tag">Certificate</span><h4>{e(v['title'])}</h4><small>Awarded to Ayesha K. · {e(v['brand'])}</small></div>"""
    return page(css, body, v['acc'], v['acc'] + '44', '#2b1d4a88')

# ---------------- PC software ----------------
def pc(v):
    css = """.win{height:500px;background:#eef1f6;font-size:11px;display:flex;flex-direction:column}
.tb{height:32px;background:var(--acc);color:#fff;display:flex;align-items:center;padding:0 12px;font-weight:700;gap:10px}.tb span{margin-left:auto;opacity:.8;font-weight:500}
.rb{display:flex;gap:4px;padding:7px 10px;background:#fff;border-bottom:1px solid #dde2ea}.rb div{padding:5px 10px;border-radius:6px;color:#4a5263}.rb .on{background:var(--acc)18;color:var(--acc);font-weight:700}
.bd{flex:1;display:grid;grid-template-columns:1fr 260px;gap:10px;padding:10px}
.tbl{background:#fff;border-radius:10px;border:1px solid #dde2ea;overflow:hidden}.tbl .h,.tbl .r{display:grid;grid-template-columns:2.4fr .8fr 1fr 1fr;padding:7px 10px}.tbl .h{background:#f6f8fb;font-weight:700;color:#6a7385}.tbl .r{border-top:1px solid #f0f2f6}
.tbl .r.new{background:#fff8e1}
.sum{background:#fff;border-radius:10px;border:1px solid #dde2ea;padding:12px;display:flex;flex-direction:column;gap:8px}.sum h4{font:800 14px Inter Display}.sum .t{display:flex;justify-content:space-between}.sum .g{font:800 24px Inter Display;color:var(--acc)}
.btn{background:var(--acc);color:#fff;text-align:center;border-radius:8px;padding:9px;font-weight:800}
.toast{position:absolute;right:20px;bottom:20px;background:#10131a;color:#fff;border-radius:10px;padding:10px 14px;font-size:11px;animation:fu .5s both 3.9s;display:flex;gap:8px;align-items:center}.toast i{width:18px;height:18px;border-radius:50%;background:#3ddc97;display:grid;place-items:center;font-style:normal}"""
    rows = ''.join(f'<div class="r fu{" new" if i==len(v["items"])-1 else ""}" style="{d(.4+i*.32)}"><span>{e(a)}</span><span>{e(b)}</span><span>{e(c)}</span><span><b>{e(dd)}</b></span></div>' for i,(a,b,c,dd) in enumerate(v['items']))
    tabs = ''.join(f'<div class="{"on" if i==0 else ""}">{e(x)}</div>' for i,x in enumerate(v['tabs']))
    body = f"""<div class="lap"><div class="bez"><div class="scr"><div class="win"><div class="tb">◆ {e(v['brand'])} <span>{e(v['shop'])} · Desktop</span></div><div class="rb">{tabs}</div>
<div class="bd"><div class="tbl"><div class="h">{''.join(f'<span>{e(x)}</span>' for x in v['cols'])}</div>{rows}</div>
<div class="sum"><h4>{e(v['side'])}</h4>{''.join(f'<div class="t fu" style="{d(2.2+i*.15)}"><span>{e(a)}</span><b>{e(b)}</b></div>' for i,(a,b) in enumerate(v['tot']))}<div class="g pop" style="{d(3.0)}">{e(v['grand'])}</div><div class="btn pop" style="{d(3.3)}">{e(v['btn'])}</div></div></div>
<div class="toast"><i>✓</i>{e(v['toast'])}</div></div></div></div><div class="base"></div></div>"""
    return page(css, body, v['acc'], v['acc'] + '44', '#13304a88')

# ---------------- E-commerce store ----------------
def shop(v):
    css = """.st{font-size:11px}.nv{display:flex;align-items:center;gap:16px;padding:12px 22px;border-bottom:1px solid #eee}.nv b{font:900 17px Inter Display;letter-spacing:.06em;color:var(--acc)}.nv span{color:#555}.nv .cart{margin-left:auto;position:relative;font-size:16px}
.nv .cart em{position:absolute;top:-6px;right:-9px;background:var(--acc);color:#fff;font-style:normal;font-size:9px;border-radius:99px;padding:1px 5px;animation:pop .4s both 3.3s}
.hero{display:grid;grid-template-columns:1fr 1fr;height:220px;background:var(--soft)}.hero div{padding:30px 26px}.hero h2{font:800 28px/1.05 Inter Display;letter-spacing:-.02em}.hero p{color:#555;margin:8px 0 12px}.hero a{background:#111;color:#fff;padding:8px 16px;border-radius:99px;font-weight:700}.hero img{width:100%;height:220px;object-fit:cover}
.gr{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;padding:16px 22px}.p{border-radius:12px;overflow:hidden;background:#fafafa;border:1px solid #f0f0f0}.p img{width:100%;height:120px;object-fit:cover}.p div{padding:8px}.p b{display:block}.p s{color:#aaa;margin-left:5px}.p .add{margin-top:6px;text-align:center;border:1px solid #111;border-radius:99px;padding:4px;font-weight:700}
.p.hit .add{animation:hit .4s both 3.1s}@keyframes hit{to{background:#111;color:#fff}}
.drw{position:absolute;right:0;top:30px;bottom:0;width:250px;background:#fff;box-shadow:-20px 0 40px -10px rgba(0,0,0,.25);padding:16px;animation:drw .5s cubic-bezier(.2,.8,.2,1) both 3.5s}@keyframes drw{from{transform:translateX(100%)}to{transform:none}}
.drw h4{font:800 15px Inter Display;margin-bottom:10px}.ci{display:flex;gap:8px;align-items:center}.ci img{width:54px;height:54px;border-radius:8px;object-fit:cover}.pay{margin-top:14px;background:var(--acc);color:#fff;text-align:center;border-radius:99px;padding:10px;font-weight:800}"""
    ps = ''.join(f'<div class="p fu{" hit" if i==1 else ""}" style="{d(1.2+i*.15)}"><img src="{img(x[0])}"><div><b>{e(x[1])}</b>{e(x[2])}<s>{e(x[3])}</s><div class="add">Add to cart</div></div></div>' for i,x in enumerate(v['prods']))
    hp = v['prods'][1]
    body = f"""<div class="lap"><div class="bez"><div class="scr"><div class="bar"><i></i><i></i><i></i><span class="url">{e(v['dom'])}</span></div><div class="st" style="--soft:{v['soft']}">
<div class="nv"><b>{e(v['brand'])}</b>{''.join(f'<span>{e(x)}</span>' for x in v['menu'])}<span class="cart">🛍<em>1</em></span></div>
<div class="scroll" style="--sy:-112px"><div class="hero"><div class="fu" style="{d(.2)}"><span class="tag">{e(v['badge'])}</span><h2 style="margin-top:8px">{e(v['h'])}</h2><p>{e(v['sub'])}</p><a>Shop now</a></div><img src="{img(v['hero'])}"></div><div class="gr">{ps}</div></div>
<div class="drw"><h4>Your cart</h4><div class="ci"><img src="{img(hp[0])}"><div><b>{e(hp[1])}</b><br>{e(hp[2])}</div></div><div class="t" style="display:flex;justify-content:space-between;margin-top:14px"><span>Total</span><b>{e(hp[2])}</b></div><div class="pay">Pay securely · UPI / Card</div></div>
</div></div></div><div class="base"></div></div>"""
    return page(css, body, v['acc'], v['acc'] + '44', '#3a1d1d88')

# ---------------- AI content automation ----------------
def aiauto(v):
    css = """.au{display:grid;grid-template-columns:240px 1fr;height:470px;font-size:11px;background:#0e1016;color:#dfe3ec}
.pr{padding:14px;border-right:1px solid #1e2230}.pr b{color:#fff;font-size:13px}.pr .in{margin-top:10px;background:#161a23;border:1px solid #2a3040;border-radius:10px;padding:10px;color:#cfd6e4;line-height:1.5;min-height:80px}
.pr .in i{font-style:normal;display:block;animation:fu .6s both .2s}
@keyframes ty{from{max-width:0}to{max-width:200px}}
.stp{margin-top:10px;display:flex;flex-direction:column;gap:6px}.stp div{display:flex;gap:8px;align-items:center;padding:7px 9px;border-radius:8px;background:#161a23}.stp i{width:16px;height:16px;border-radius:50%;background:#3ddc97;font-style:normal;display:grid;place-items:center;font-size:9px;color:#000}
.cal{padding:14px;display:grid;grid-template-columns:repeat(2,1fr);gap:10px;align-content:start}.cal h3{grid-column:span 2;color:#fff;font:800 16px Inter Display;display:flex;justify-content:space-between}
.post{border-radius:10px;overflow:hidden;background:#161a23;border:1px solid #232836}.post img{width:100%;height:122px;object-fit:cover}.post div{padding:6px 7px}.post small{color:#3ddc97;font-weight:700}"""
    st = ''.join(f'<div class="fu" style="{d(1.2+i*.3)}"><i>✓</i>{e(x)}</div>' for i,x in enumerate(['Ideas researched','Captions written','Visuals generated','Scheduled to Instagram & Facebook']))
    posts = ''.join(f'<div class="post pop" style="{d(2.0+i*.17)}"><img src="{img(x[0])}"><div><b>{e(x[1])}</b><br><small>● {e(x[2])}</small></div></div>' for i,x in enumerate(v['posts']))
    body = f"""<div class="lap"><div class="bez"><div class="scr" style="background:#0e1016"><div class="bar" style="background:#0a0c11;border-color:#1d212b;color:#8a92a6"><i></i><i></i><i></i><span class="url" style="background:#161a23;border-color:#232836">autopilot · {e(v['brand'])}</span></div>
<div class="au"><div class="pr"><b>Content autopilot</b><div class="in"><i>{e(v['prompt'])}</i></div><div class="stp">{st}</div></div>
<div class="cal"><h3>{e(v['month'])} <span class="tag">{len(v['posts'])*4} posts ready</span></h3>{posts}</div></div></div></div><div class="base"></div></div>"""
    return page(css, body, v['acc'], v['acc'] + '44', '#1b2f3a88')

# ---------------- PC + mobile combo ----------------
def combo(v):
    c = pc(dict(v, items=v['items'][:4])).replace('<div class="toast">','<div class="toast" style="left:20px;right:auto">')
    ph = f"""<div class="ph" style="right:-14px;bottom:-30px;top:auto;transform:translateZ(110px) rotate(3deg) scale(.86);width:210px;height:430px"><div class="scr" style="background:#f4f6fa;font-size:10px">
<div style="background:var(--acc);color:#fff;padding:34px 12px 12px;font-weight:800;font-size:13px">{e(v['app'])}</div>
<div style="padding:10px;display:flex;flex-direction:column;gap:7px">{''.join(f'<div class="fu" style="{d(1.0+i*.45)};background:#fff;border-radius:10px;padding:8px;box-shadow:0 2px 6px rgba(0,0,0,.06)"><b>{e(a)}</b><br><span style="color:#777">{e(b)}</span></div>' for i,(a,b) in enumerate(v['feed']))}
<div class="pop" style="{d(3.9)};background:#10131a;color:#fff;border-radius:10px;padding:8px">🔔 {e(v['toast'])}</div></div></div></div>"""
    sync = f'<div class="pop" style="{d(2.6)};position:absolute;left:50%;bottom:-36px;transform:translateX(-50%) translateZ(60px);background:#fff;border-radius:99px;padding:7px 14px;font:800 11px Inter;box-shadow:0 10px 30px rgba(0,0,0,.4)">⟳ Synced live · PC ⇄ Phone</div>'
    return c.replace('</div></div><script>', ph + sync + '</div></div><script>')

# ---------------- Voiceover & dubbing ----------------
def voice(v):
    import random
    random.seed(v['brand'])
    css = """.ed{height:470px;background:#0f1117;color:#d9deea;font-size:11px;display:grid;grid-template-rows:230px 1fr}
.pv{display:grid;grid-template-columns:1fr 260px;gap:10px;padding:10px}.pv .v{position:relative;border-radius:10px;overflow:hidden}.pv img{width:100%;height:100%;object-fit:cover}
.pv .sub{position:absolute;left:0;right:0;bottom:12px;text-align:center}.pv .sub span{background:#000a;color:#fff;padding:4px 10px;border-radius:6px;font-weight:700;font-size:13px;position:absolute;left:50%;transform:translateX(-50%);white-space:nowrap;opacity:0}
.langs{background:#161a23;border-radius:10px;padding:10px;display:flex;flex-direction:column;gap:6px}.langs div{display:flex;justify-content:space-between;padding:6px 8px;border-radius:7px;background:#1d2230}.langs .on{background:var(--acc);color:#fff;font-weight:700}
.tl{padding:8px 10px;position:relative}.tr{display:grid;grid-template-columns:90px 1fr;align-items:center;height:40px;border-top:1px solid #1e2230}.tr b{color:#fff;font-size:10.5px}
.wf{display:flex;align-items:center;gap:2px;height:32px}.wf i{flex:1;background:var(--c);border-radius:2px;opacity:.9}
.ph2{position:absolute;top:4px;bottom:0;width:2px;background:#fff;left:100px;animation:ph 5s linear both;box-shadow:0 0 8px #fff}@keyframes ph{from{left:100px}to{left:96%}}"""
    def wf(c):
        return '<div class="wf" style="--c:' + c + '">' + ''.join(f'<i class="grow" style="height:{random.randint(15,100)}%;{d(.3+j*.012)}"></i>' for j in range(90)) + '</div>'
    tracks = ''.join(f'<div class="tr"><b>{e(n)}</b>{wf(c)}</div>' for n,c in v['tracks'])
    subs = ''.join(f'<span style="animation:sb 5s both;animation-delay:{i*1.25}s">{e(x)}</span>' for i,x in enumerate(v['subs']))
    css += "@keyframes sb{0%{opacity:0}3%{opacity:1}24%{opacity:1}26%,100%{opacity:0}}"
    langs = ''.join(f'<div class="fu {"on" if i==0 else ""}" style="{d(.3+i*.12)}"><span>{e(a)}</span><span>{e(b)}</span></div>' for i,(a,b) in enumerate(v['langs']))
    body = f"""<div class="lap"><div class="bez"><div class="scr" style="background:#0f1117"><div class="bar" style="background:#0a0c11;border-color:#1d212b;color:#8a92a6"><i></i><i></i><i></i><span class="url" style="background:#161a23;border-color:#232836">dubbing studio · {e(v['brand'])}</span></div>
<div class="ed"><div class="pv"><div class="v"><img src="{img(v['img'])}"><div class="sub">{subs}</div></div><div class="langs"><b style="color:#fff">AI voice-over &amp; dubbing</b>{langs}</div></div>
<div class="tl">{tracks}<div class="ph2"></div></div></div></div></div><div class="base"></div></div>"""
    return page(css, body, v['acc'], v['acc'] + '44', '#2a1640aa')

# ---------------- Music / lyric reel ----------------
def music(v):
    import random
    random.seed(v['title'])
    css = """.ph .scr{background:#000}.bg{position:absolute;inset:-20px;background-size:cover;background-position:center;filter:saturate(1.2) brightness(.55);animation:kb 5s linear both}
@keyframes kb{from{transform:scale(1.05)}to{transform:scale(1.2) rotate(1deg)}}
.ly{position:absolute;left:14px;right:14px;top:150px;color:#fff;text-align:center}.ly div{font:900 25px/1.05 Inter Display;letter-spacing:-.01em;text-transform:uppercase;opacity:0;position:absolute;left:0;right:0;text-shadow:0 4px 18px rgba(0,0,0,.6)}
.ly span{color:var(--acc)}
.eq{position:absolute;left:18px;right:18px;bottom:70px;height:60px;display:flex;align-items:flex-end;gap:3px}.eq i{flex:1;background:linear-gradient(var(--acc),#fff);border-radius:3px;transform-origin:bottom}
.ttl{position:absolute;left:14px;right:14px;bottom:26px;color:#fff;font-size:11px;display:flex;gap:8px;align-items:center}.ttl img{width:30px;height:30px;border-radius:6px;object-fit:cover}
.side{position:absolute;left:-330px;top:40px;width:290px;color:#fff}.side h3{font:800 24px/1.1 Inter Display}.side p{opacity:.75;font-size:12px;margin:8px 0 14px;line-height:1.5}
.side .k{display:flex;gap:8px;flex-wrap:wrap}.side .k span{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:99px;padding:6px 10px;font-size:11px}
.st{position:absolute;right:-290px;top:120px;width:240px;color:#fff}.st div{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);border-radius:14px;padding:12px 14px;margin-bottom:10px}.st b{font:800 26px Inter Display;display:block}"""
    n = len(v['lines'])
    seg = 5 / n
    for i in range(n):
        a = i*seg/5*100; b = (i+1)*seg/5*100
        css += f"@keyframes l{i}{{0%,{a:.1f}%{{opacity:0;transform:translateY(20px) scale(.9)}}{a+3:.1f}%{{opacity:1;transform:none}}{max(a+3.1,b-2):.1f}%{{opacity:1;transform:none}}{b:.1f}%,100%{{opacity:0;transform:translateY(-14px)}}}}"
    lines = ''.join(f'<div style="animation:l{i} 5s both">{x}</div>' for i,x in enumerate(v['lines']))
    eq = ''.join(f'<i style="height:{random.randint(20,100)}%;animation:eq{j%4} {0.35+0.1*(j%3):.2f}s ease-in-out infinite alternate"></i>' for j in range(28))
    css += ''.join(f"@keyframes eq{k}{{from{{transform:scaleY({0.2+0.15*k:.2f})}}to{{transform:scaleY(1)}}}}" for k in range(4))
    body = f"""<div style="width:236px;height:480px;position:relative"><div class="side"><span class="tag">Music &amp; song reel</span><h3 style="margin-top:10px">{e(v['title'])}</h3><p>{e(v['desc'])}</p><div class="k">{''.join(f'<span>{e(x)}</span>' for x in v['chips'])}</div></div>
<div class="ph" style="left:0;top:0"><div class="scr"><div class="bg" style="background-image:url('{img(v['img'])}')"></div><div class="ly">{lines}</div><div class="eq">{eq}</div>
<div class="ttl"><img src="{img(v['img'])}"><div><b>{e(v['title'])}</b><br>{e(v['artist'])}</div></div></div></div>
<div class="st">{''.join(f'<div class="fu" style="{d(1.5+i*.4)}"><b>{e(a)}</b>{e(b)}</div>' for i,(a,b) in enumerate(v['stats']))}</div></div>"""
    return page(css, body, v['acc'], v['acc'] + '55', '#3a103a99')

# ---------------- Personal branding ----------------
def pb(v):
    css = """.ig{font-size:10.5px;padding-top:38px}.hd{display:flex;gap:12px;align-items:center;padding:6px 12px}.av{width:62px;height:62px;border-radius:50%;padding:2px;background:linear-gradient(45deg,#f9a825,#e91e63,#7b1fa2)}.av img{width:100%;height:100%;border-radius:50%;object-fit:cover;border:2px solid #fff}
.hd .n{display:flex;gap:12px;text-align:center}.hd .n b{display:block;font-size:13px}
.bio{padding:4px 12px 8px;line-height:1.4}.bio b{font-size:11.5px}
.btns{display:flex;gap:5px;padding:0 12px 8px}.btns span{flex:1;text-align:center;background:#efefef;border-radius:7px;padding:5px;font-weight:700}.btns .f{background:#0095f6;color:#fff}
.g{display:grid;grid-template-columns:repeat(3,1fr);gap:2px}.g img{width:100%;height:76px;object-fit:cover}
.side{position:absolute;left:-340px;top:20px;width:300px;color:#fff}.side h3{font:800 24px/1.1 Inter Display}.side p{opacity:.75;margin:8px 0 14px;font-size:12px;line-height:1.5}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:10px}.cmp div{border-radius:14px;padding:12px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14)}.cmp b{font:800 24px Inter Display;display:block}.cmp .a b{color:var(--acc)}
.chk{margin-top:12px;display:flex;flex-direction:column;gap:7px;font-size:12px}.chk div{display:flex;gap:8px}.chk i{font-style:normal;color:var(--acc)}"""
    grid = ''.join(f'<img class="pop" src="{img(x)}" style="{d(.6+i*.12)}">' for i,x in enumerate(v['grid']))
    chk = ''.join(f'<div class="fu" style="{d(2.4+i*.3)}"><i>✓</i>{e(x)}</div>' for i,x in enumerate(v['did']))
    body = f"""<div style="width:236px;height:480px;position:relative"><div class="side"><span class="tag">Zero → hero</span><h3 style="margin-top:10px">{e(v['name'])}</h3><p>{e(v['role'])}</p>
<div class="cmp"><div class="fu" style="{d(.4)}"><small>Before</small><b>{e(v['before'])}</b>followers</div><div class="a fu" style="{d(1.2)}"><small>After {e(v['months'])} months</small><b>{e(v['after'])}</b>followers</div></div><div class="chk">{chk}</div></div>
<div class="ph" style="left:0;top:0"><div class="scr"><div class="ig"><div style="text-align:center;font-weight:800;font-size:12px;padding-bottom:4px">{e(v['handle'])} ✓</div>
<div class="hd"><div class="av"><img src="{img(v['av'])}"></div><div class="n"><div><b>{e(v['posts'])}</b>posts</div><div><b class="pop" style="{d(1.4)}">{e(v['after'])}</b>followers</div><div><b>{e(v['fol'])}</b>following</div></div></div>
<div class="bio"><b>{e(v['name'])}</b><br>{e(v['bio'])}</div><div class="btns"><span class="f">Follow</span><span>Message</span><span>Book a call</span></div><div class="g">{grid}</div></div></div></div></div>"""
    return page(css, body, v['acc'], v['acc'] + '55', '#4a2a1499')

# ---------------- Mobile app (3 screens) ----------------
def app(v):
    css = """.ph .scr{font-size:10px;color:#141821}.ap{position:absolute;inset:0;padding:38px 12px 12px;display:flex;flex-direction:column;gap:8px;background:var(--bg2)}
.ap h4{font:800 15px Inter Display}.ap .sub{color:#6b7280;font-size:9.5px}
.chip{display:flex;gap:5px}.chip span{padding:4px 8px;border-radius:99px;background:#fff;border:1px solid #e5e7eb;font-weight:700;font-size:9px}.chip span:first-child{background:var(--acc);color:#fff;border-color:var(--acc)}
.card{background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,.07)}.card img{width:100%;height:92px;object-fit:cover}.card div{padding:7px 9px}.card b{display:block;font-size:11px}
.row{display:flex;justify-content:space-between;align-items:center}.pill{background:var(--acc);color:#fff;border-radius:99px;padding:6px 10px;font-weight:800;text-align:center}
.hero{height:190px;border-radius:16px;overflow:hidden;position:relative}.hero img{width:100%;height:100%;object-fit:cover}
.tl div{display:flex;gap:8px;align-items:flex-start;margin-bottom:9px}.tl i{width:12px;height:12px;border-radius:50%;background:#d1d5db;flex:none;margin-top:1px}.tl .ok i{background:var(--acc)}
.nav{position:absolute;left:0;right:0;bottom:0;height:40px;background:#fff;border-top:1px solid #eee;display:flex;justify-content:space-around;align-items:center;font-size:14px;color:#9ca3af}.nav b{color:var(--acc)}
.title{position:absolute;left:50%;top:-92px;transform:translateX(-50%);white-space:nowrap;text-align:center;color:#fff}.title h3{font:800 24px Inter Display}.title p{opacity:.7;font-size:12px}"""
    cards = ''.join(f'<div class="card fu" style="{d(.5+i*.15)}"><img src="{img(c[0])}"><div><div class="row"><b>{e(c[1])}</b><span style="color:var(--acc);font-weight:800">{e(c[2])}</span></div><span class="sub">{e(c[3])}</span></div></div>' for i,c in enumerate(v['items'][:2]))
    s1 = f'<div class="ap"><span class="sub">{e(v["hello"])}</span><h4>{e(v["h1"])}</h4><div class="chip">{"".join(f"<span>{e(x)}</span>" for x in v["chips"])}</div>{cards}</div><div class="nav"><b>⌂</b><span>⌕</span><span>♡</span><span>☺</span></div>'
    it = v['items'][0]
    s2 = f'<div class="ap"><div class="hero"><img src="{img(it[0])}"></div><div class="row"><h4>{e(it[1])}</h4><b style="color:var(--acc);font-size:14px">{e(it[2])}</b></div><span class="sub">{e(v["detail"])}</span><div class="chip">{"".join(f"<span>{e(x)}</span>" for x in v["opts"])}</div><div class="pill pop" style="{d(2.0)};margin-top:auto">{e(v["cta"])}</div></div>'
    tl = ''.join(f'<div class="fu {"ok" if i < 3 else ""}" style="{d(2.6+i*.25)}"><i></i><div><b>{e(a)}</b><br><span class="sub">{e(b)}</span></div></div>' for i,(a,b) in enumerate(v['track']))
    s3 = f'<div class="ap"><h4>{e(v["t3"])}</h4><span class="sub">{e(v["t3s"])}</span><div class="card" style="padding:12px;margin-top:6px"><div class="tl">{tl}</div></div><div class="card fu" style="{d(3.6)};padding:10px"><div class="row"><b>{e(v["foot"][0])}</b><span class="pill" style="padding:4px 9px">{e(v["foot"][1])}</span></div></div></div>'
    body = f"""<div style="width:820px;height:480px;position:relative"><div class="title fu"><span class="tag">{e(v['tagline'])}</span><h3 style="margin-top:6px">{e(v['brand'])}</h3><p>{e(v['desc'])}</p></div>
<div class="ph" style="left:20px;top:40px;transform:rotate(-6deg) translateZ(-40px) scale(.92)"><div class="scr" style="--bg2:{v['bg2']}">{s1}</div></div>
<div class="ph" style="left:292px;top:18px;transform:translateZ(60px) scale(.94)"><div class="scr" style="--bg2:{v['bg2']}">{s2}</div></div>
<div class="ph" style="left:564px;top:40px;transform:rotate(6deg) translateZ(-40px) scale(.92)"><div class="scr" style="--bg2:{v['bg2']}">{s3}</div></div></div>"""
    return page(css, body.replace('<div style="width:820px;height:480px;position:relative">','<div style="width:820px;height:480px;position:relative;margin-top:96px">'), v['acc'], v['acc'] + '55', '#1b1f3a99')

# ---------------- Website (laptop + phone) ----------------
def web(v):
    css = """.st{font-size:11px;color:#14161c}.nv{display:flex;align-items:center;gap:18px;padding:13px 26px;position:absolute;top:0;left:0;right:0;z-index:3;color:var(--nfg)}.nv b{font:900 16px Inter Display;letter-spacing:.04em}.nv span{opacity:.85}.nv a{margin-left:auto;background:var(--acc);color:#fff;padding:7px 14px;border-radius:99px;font-weight:800}
.hero{position:relative;height:330px;overflow:hidden}.hero img{width:100%;height:100%;object-fit:cover;animation:kb 5s linear both}@keyframes kb{from{transform:scale(1.04)}to{transform:scale(1.12)}}
.hero:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.72),rgba(0,0,0,.05))}
.hero .tx{position:absolute;left:30px;top:90px;z-index:2;color:#fff;max-width:380px}.hero h1{font:800 34px/1.02 Inter Display;letter-spacing:-.02em}.hero p{opacity:.85;margin:10px 0 14px;font-size:12.5px;line-height:1.5}.hero .b{display:inline-block;background:var(--acc);color:#fff;padding:9px 16px;border-radius:99px;font-weight:800}
.feat{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;padding:20px 26px;background:#fff}.feat div{border:1px solid #eee;border-radius:12px;padding:12px}.feat b{display:block;font:800 14px Inter Display;margin-bottom:4px}.feat i{font-style:normal;font-size:18px}
.gal{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;padding:0 26px 20px;background:#fff}.gal img{width:100%;height:120px;object-fit:cover;border-radius:10px}
.mob .scr{font-size:9px}.mob .hero{height:230px}.mob .hero .tx{left:14px;top:70px;max-width:180px}.mob h1{font-size:20px}.mob .nv{padding:30px 12px 8px;gap:8px}.mob .nv span,.mob .nv a{display:none}"""
    feats = ''.join(f'<div class="fu" style="{d(1.6+i*.15)}"><i>{ic}</i><b>{e(a)}</b>{e(b)}</div>' for i,(ic,a,b) in enumerate(v['feats']))
    gal = ''.join(f'<img src="{img(x)}">' for x in v['gal'])
    hero = lambda: f'<div class="hero"><img src="{img(v["hero"])}"><div class="tx"><span class="tag">{e(v["badge"])}</span><h1 style="margin-top:8px">{e(v["h1"])}</h1><p>{e(v["p"])}</p><span class="b">{e(v["cta"])}</span></div></div>'
    nav = f'<div class="nv"><b>{e(v["brand"])}</b>{"".join(f"<span>{e(x)}</span>" for x in v["menu"])}<a>{e(v["cta"])}</a></div>'
    body = f"""<div class="lap" style="margin-left:-150px"><div class="bez"><div class="scr"><div class="bar"><i></i><i></i><i></i><span class="url">{e(v['dom'])}</span></div>
<div class="st" style="--nfg:#fff;position:relative;height:470px;overflow:hidden"><div class="scroll" style="--sy:-140px">{nav}{hero()}<div class="feat">{feats}</div><div class="gal">{gal}</div></div></div></div></div><div class="base"></div></div>
<div class="ph mob" style="right:-96px;top:40px;transform:translateZ(110px) scale(.86)"><div class="scr"><div class="st" style="--nfg:#fff;position:relative">{nav}{hero()}<div class="feat" style="grid-template-columns:1fr;padding:12px">{feats}</div></div></div></div>"""
    return page(css, body, v['acc'], v['acc'] + '44', '#1a1f33aa')

T = dict(app=app, web=web, seo=seo, mkt=mkt, chatbot=chatbot, deck=deck, dash=dash, course=course, pc=pc, shop=shop, aiauto=aiauto, combo=combo, voice=voice, music=music, pb=pb)

if __name__ == '__main__':
    data = json.load(open(sys.argv[1]))
    out = sys.argv[2]; os.makedirs(out, exist_ok=True)
    only = sys.argv[3] if len(sys.argv) > 3 else None
    for s in data:
        if only and not s['id'].startswith(only): continue
        open(os.path.join(out, s['id'] + '.html'), 'w').write(T[s['kind']](s))
    print('ok')
