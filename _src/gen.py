#!/usr/bin/env python3
"""Flow Studio multi-page builder. Edit _src/base.html (the full single page), then run: python3 _src/gen.py
Every page is the same base with only its own sections shown, its own hero, title and meta."""
import re, os, json, html
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = open(os.path.join(R, '_src/base.html')).read()
E = html.escape
SITE = "https://pixelflowstudio.agency/"
WA = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Z"/></svg>'
# --- services (same order as SERVICES in base.html) ---
SV = [
 ("shoot-and-edit","Shoot + Edit","shoot","We come with camera, lights and sound, shoot your content and edit it end to end.",
  ["Planning call, shot list and location / props checklist","Camera crew with cinema camera, gimbal, LED lights and wireless mics","Reels, ads, interviews, events and product films","Full edit: cuts, colour grading, captions, music and sound design","Delivery in 9:16, 1:1 and 16:9, ready for every platform"],"Restaurants, boutiques, clinics, gyms, real estate, events and brands that need fresh content every month.","2–7 days after the shoot"),
 ("video-editing","Video Editing","edit","Reels, shorts and long-form YouTube with captions, colour grading and sound design.",
  ["Hook-first reel and shorts editing","YouTube long-form and podcast multicam edits","Animated captions and subtitles in any language","Colour grading, sound clean-up, music and SFX","Thumbnails on request"],"Creators, coaches, podcasters and brands who already shoot and want a pro edit.","1–3 days per reel"),
 ("commercial-video-editing","Commercial Video Editing","comm","Brand promos, product films and ad cuts built for Instagram, YouTube and TV screens.",
  ["Script, storyboard and ad structure built to sell","15s, 30s and 60s ad cuts plus story / reel versions","Premium colour grade, motion graphics and logo animation","Licensed music, voiceover and sound design","Mall-screen, billboard and TV-ready exports"],"Product launches, retail brands, real estate and any business running paid ads.","5–12 days"),
 ("graphic-designing","Graphic Designing","design","Thumbnails, posters, carousels, logos and brand kits.",
  ["Logos and complete brand identity kits","Posters, flyers and festive campaign creatives","Instagram posts, carousels and story designs","YouTube thumbnails that get clicks","Visiting cards and stationery, print-ready"],"Every business that wants to look premium online and in print.","1–4 days"),
 ("commercial-graphic-designing","Commercial Graphic Designing","cdesign","Packaging, labels, product posters, menus and ad creatives for businesses.",
  ["Product packaging and label design, print-ready","Restaurant and café menus","Product posters, catalogues and brochures","Ad creatives for Meta and Google ads","Hoardings, standees and shop signage"],"Food brands, cosmetics, perfumes, FMCG, restaurants and retail stores.","3–10 days"),
 ("social-media-handling","Social Media Handling","social","Posting calendar, captions, hashtags and replying to your community.",
  ["Monthly content calendar planned with you","Post and reel design in your brand style","Captions, hashtags and best-time scheduling","Replying to comments and DMs","Monthly summary of what worked"],"Shops and brands who want a professional page without doing it themselves.","Monthly plan"),
 ("social-media-management","Social Media Management","smm","Growth strategy, analytics reports, ad campaigns and content planning.",
  ["Growth strategy and competitor research","Meta and Instagram ad campaigns","Monthly analytics report with next steps","Influencer and UGC planning","Funnel from awareness to sales"],"Businesses ready to grow followers, leads and sales with a clear plan.","Monthly plan"),
 ("landing-page-design","Landing Page Design","landing","One-page sites with WhatsApp, payments and your branding.",
  ["High-converting one-page design for your offer","WhatsApp, call and Book Now buttons","Online payments and lead forms","Fast on mobile, SEO basics included","Your domain connected, hosting guidance"],"Coaches, events, launches, clinics and anyone running ads.","3–7 days"),
 ("website-development","Website Development","website","Business websites, portfolios and online stores that you can edit yourself.",
  ["Multi-page business websites and portfolios","Online stores with cart, payments and order tracking","Admin panel to edit products and prices yourself","Mobile-first, fast and SEO-ready","Domain, email and Google setup"],"Brands, shops, schools, clinics, agencies and personal brands.","1–4 weeks"),
 ("pc-mobile-combo-app","PC + Mobile Combo App","combo","One connected system on computer and phone together, with live data on PC, Android and iPhone.",
  ["Desktop software for the counter or office","Matching Android and iPhone app","Live sync of billing, stock, attendance or appointments","Owner dashboard and staff logins","Training and support after launch"],"Schools, shops, clinics, warehouses, cafés and offices.","3–8 weeks"),
 ("mobile-app-development","Mobile App Development","app","Android and iOS apps built for your business, published on Play Store and App Store.",
  ["Shopping, booking, delivery, education and custom apps","Clean UI/UX design before development","Payments, notifications and login","Admin panel for your team","Play Store and App Store publishing"],"Startups and businesses that want their own app.","3–10 weeks"),
 ("pc-software","PC Software","pc","Windows and Mac software made to your requirement: billing, stock, CRM, school or clinic management.",
  ["Billing, GST invoices and stock software","CRM, school, clinic and shop management","Works offline, with backups","Reports and Excel / PDF exports","Installer, training and updates"],"Shops, distributors, schools, clinics and offices.","2–8 weeks"),
 ("custom-software-web-apps","Custom Software & Web Apps","custom","Dashboards, admin panels, customer portals and automation that connect your website, app, payments and WhatsApp.",
  ["Admin dashboards and customer portals","Automation: orders → payments → WhatsApp","Integrations with Razorpay, Google and Meta","Secure hosting and logins","Built around your exact workflow"],"Growing businesses that have outgrown spreadsheets.","2–10 weeks"),
 ("ai-video-ads","AI Video Ads & Reels","aiads","Cinematic product ads, launch films and reels made with the latest AI video tools, finished by our editors.",
  ["Concept and script for your product","AI product scenes: splashes, levitation, worlds","Edited with music, SFX and captions","Every format: reel, story, YouTube, TV","Ready in days, no shoot needed"],"Product brands, launches, e-commerce and festive campaigns.","3–7 days"),
 ("ai-product-photoshoot","AI Product Photoshoot","aiphoto","Studio-quality product photos and lifestyle scenes for your catalogue, website and ads.",
  ["Catalogue-ready product photos on any set","Lifestyle scenes for ads and social media","Consistent look across your whole range","High-resolution files for print and web","No studio, models or travel needed"],"E-commerce stores, D2C brands, perfumes, cosmetics and food brands.","2–5 days"),
 ("ai-films-storytelling","AI Films & Storytelling","aifilm","Cinematic short films, brand stories, historical, mythological and devotional stories, explainers and series.",
  ["Script and storyboard","Consistent AI characters and worlds","Voiceover in any language","Music, sound design and colour grade","Shorts, episodes and full series"],"Brands, channels, educators, faith content and storytellers.","1–3 weeks"),
 ("ai-content-automation","AI Content Automation","aiauto","A system that plans, creates and posts your content every week, approved by you.",
  ["Weekly content plan created automatically","AI visuals, captions and voiceovers","You approve, it posts on schedule","Results report every week","Cheaper than a full-time content team"],"Busy owners who want consistent posting without the work.","Monthly plan"),
]
PAGES = {
 "index": dict(show="hero next services samples clients ai why", title="Flow Studio · Video, Design, Social Media & Websites"),
 "services": dict(show="services ai process why", title="Services · Flow Studio", h=("What we make","17 services. <span class=\"rbt\">One creative studio.</span>","Video, design, social media, websites, apps, software and AI. Pick one service or hand us everything.")),
 "work": dict(show="samples work reels", title="Our Work & Samples · Flow Studio", h=("Portfolio","See the work <span class=\"rbt\">before you book</span>","Hundreds of samples across every service, plus concept reels for every industry. Tap any folder to open it.")),
 "reels": dict(show="reels", title="Sample Reels · Flow Studio", h=("Reels","A reel for <span class=\"rbt\">every industry</span>","Concept reels made by our team to show the style we bring to each kind of business. Tap to watch with sound.")),
 "packages": dict(show="pricing faq", title="Packages & Pricing · Flow Studio", h=("Packages","Ready packages. <span class=\"rbt\">Pay online.</span>","Fixed-price packages you can order today, or a custom quote with 40% advance and 60% on delivery.")),
 "about": dict(show="about clients process why", title="About Flow Studio · Founder Arsalan Ahmed Shaikh", h=None),
 "contact": dict(show="contact faq", title="Contact & Free Quote · Flow Studio", h=("Start a project","Tell us your idea. <span class=\"rbt\">Get a free quote.</span>","WhatsApp us, call, email or fill the short brief. We reply fast.")),
}
NAV = [("index","Home"),("services","Services"),("work","Work"),("reels","Reels"),("packages","Packages"),("about","About"),("contact","Contact")]
def href(k): return "./" if k == "index" else f"{k}"
def nav(cur):
    return "".join(f'<a href="{href(k)}"{" aria-current=\"page\"" if k==cur else ""}>{n}</a>' for k,n in NAV) + '<a href="#" data-shop-orders>My orders</a>'
def phero(kicker, h1, lead, crumbs, extra=""):
    bc = " / ".join(f'<a href="{href(k)}">{E(n)}</a>' if k else E(n) for k,n in crumbs)
    return f'''<section class="phero" data-p="ALL"><div class="wrap"><nav class="crumb mono" aria-label="Breadcrumb">{bc}</nav>
<span class="mono rbt">{kicker}</span><h1>{h1}</h1><p class="lead">{lead}</p>
<div class="ctas"><a class="btn wa" data-wa="Hello Flow Studio, I want a quote." href="#"><span class="shine"></span>{WA}WhatsApp for a quote</a><a class="btn gls" href="contact">Send a brief</a></div>{extra}</div></section>'''
ABOUT = '''<section class="sec about" data-p="about"><div class="wrap"><div class="abgrid">
<div class="abph rv"><div class="zr"><img src="founder.webp" alt="Arsalan Ahmed Shaikh, Founder &amp; MD of Flow Studio" loading="lazy"></div></div>
<div class="rv"><span class="mono rbt">The founder</span><h2>Arsalan Ahmed Shaikh</h2><p class="lead" style="margin-top:6px"><b class="rbt">Founder &amp; Managing Director</b></p>
<p>Flow Studio was started by Arsalan Ahmed Shaikh, a video editor, content creator and AI filmmaker who also runs the Quranic Science channel on YouTube, Instagram and Facebook. Years of making his own videos every week taught him what actually makes people stop scrolling, and that is the craft Flow Studio brings to every client.</p>
<p>Today Flow Studio is one creative team for shoots, editing, design, social media, websites, apps, software and AI films, so a business can hand everything to one studio with one contact.</p>
<img src="sig-white.png" alt="Signature of Arsalan Ahmed Shaikh" style="height:74px;width:auto;margin:16px 0 0;opacity:.95"><div class="fch" style="margin-top:14px"><i>Creative Director</i><i>Lead Video Editor</i><i>AI Film Director</i></div></div></div></div></section>'''
CSS = '''
.phero{position:relative;z-index:2;padding:150px 0 30px}.phero h1{font:800 clamp(38px,6.4vw,84px)/1.02 var(--D);letter-spacing:-.04em;margin:14px 0 16px;text-wrap:balance;max-width:16ch}
.phero .lead{max-width:62ch}.phero .ctas{margin-top:24px}.crumb{display:block;font-size:12px;letter-spacing:.12em;color:var(--mut);margin-bottom:18px}.crumb a{color:#fff;text-decoration:none}.crumb a:hover{text-decoration:underline}
.svx{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:22px;margin-top:34px}.svx .gl{padding:26px;border-radius:24px}.svx h2{font:800 22px/1.2 var(--D);margin:0 0 14px}
.svx ul{list-style:none;padding:0;margin:0;display:grid;gap:12px}.svx li{display:flex;gap:12px;align-items:flex-start;line-height:1.5}.svx li:before{content:"";flex:none;width:10px;height:10px;margin-top:7px;border-radius:50%;background:var(--rb)}
.svx dl{margin:0;display:grid;gap:14px}.svx dt{font:600 11px/1 "JetBrains Mono",monospace;letter-spacing:.16em;color:var(--mut);text-transform:uppercase}.svx dd{margin:6px 0 0;font-weight:600}
.svnav{display:flex;flex-wrap:wrap;gap:8px;margin-top:26px}.svnav a{font-size:13px;font-weight:600;color:#fff;text-decoration:none;padding:8px 13px;border-radius:999px;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.05)}.svnav a[aria-current]{background:var(--rb);background-size:200%;color:#120a20;border:0}
.links a[aria-current]{color:#fff;position:relative}.links a[aria-current]:after{content:"";position:absolute;left:12%;right:12%;bottom:-4px;height:2px;border-radius:2px;background:var(--rb)}
.card .more{display:inline-flex;align-items:center;gap:6px;margin:0 0 12px;font-size:13px;font-weight:700;color:#fff;text-decoration:none;opacity:.85}.card .more:hover{opacity:1;text-decoration:underline}
.abgrid{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:46px;align-items:center}.abph .zr{aspect-ratio:1;border-radius:36px;padding:4px;background:var(--rb);background-size:200% 100%;animation:flow 7s linear infinite;box-shadow:0 30px 120px rgba(155,92,255,.45)}
.abph img{width:100%;height:100%;object-fit:cover;border-radius:32px;display:block;background:radial-gradient(circle at 25% 20%,#ff3d9a 0,transparent 55%),radial-gradient(circle at 85% 30%,#3b82ff 0,transparent 55%),radial-gradient(circle at 60% 100%,#ff8a1f 0,transparent 60%),linear-gradient(160deg,#9b5cff,#1a0f3d)}
.about h2{font:800 clamp(30px,4.4vw,52px)/1.05 var(--D);letter-spacing:-.03em;margin:10px 0 0}.about p{color:var(--mut);line-height:1.7;max-width:62ch}
.nextpg{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}.nextpg a{display:block;padding:22px;border-radius:22px;color:#fff;text-decoration:none}.nextpg b{display:block;font:800 20px/1.2 var(--D);margin-top:6px}.nextpg small{color:var(--mut)}
@media(max-width:820px){.svx,.abgrid{grid-template-columns:1fr}.phero{padding-top:120px}}
'''
NEXT = '''<section class="sec" data-p="next" style="padding-top:10px"><div class="wrap"><div class="nextpg">
<a class="gl glare rv" href="services"><small class="mono rbt">17 SERVICES</small><b>Explore every service →</b><small>Video, design, social, web, apps, AI</small></a>
<a class="gl glare rv" href="work"><small class="mono rbt">PORTFOLIO</small><b>See all our work →</b><small>Samples in every category</small></a>
<a class="gl glare rv" href="packages"><small class="mono rbt">PACKAGES</small><b>Ready packages →</b><small>Order and pay online</small></a>
<a class="gl glare rv" href="contact"><small class="mono rbt">FREE QUOTE</small><b>Start a project →</b><small>We reply on WhatsApp fast</small></a>
</div></div></section>'''
def build(key, show, title, desc, hero, body_attr="", extra_sections=""):
    h = B
    keep = set(show.split()) | {"ALL"}
    # hide every tagged section not in this page
    hide = f'<style>[data-p]{{display:none!important}}' + "".join(f'[data-p~="{k}"]' for k in []) + "</style>"
    sel = ",".join(f'[data-p~="{k}"]' for k in sorted(keep))
    style = f"<style>{CSS}[data-p]:not({sel}){{display:none!important}}</style>"
    h = h.replace("</head>", style + "\n</head>", 1)
    h = re.sub(r"<title>.*?</title>", f"<title>{E(title)}</title>", h, count=1)
    h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{E(desc)}">', h, count=1)
    url = SITE + ("" if key == "index" else key)
    h = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', h, count=1)
    h = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', h, count=1)
    h = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{E(title)}">', h, count=1)
    h = h.replace('<nav class="links" id="links">' + re.search(r'<nav class="links" id="links">(.*?)</nav>', h).group(1) + '</nav>', f'<nav class="links" id="links">{nav(key if key in PAGES else "services")}</nav>', 1)
    h = h.replace("<body>", f"<body data-pg=\"{key}\"{body_attr}>", 1)
    h = h.replace("<!--PHERO-->", (hero or "") + extra_sections + (NEXT if key == "index" else ""), 1)
    open(os.path.join(R, ("index" if key == "index" else key) + ".html"), "w").write(h)
for k, p in PAGES.items():
    hero = None
    if p.get("h"): hero = phero(p["h"][0], p["h"][1], p["h"][2], [("index","Home"),(None, p["title"].split(" · ")[0])])
    desc = {"index":None}.get(k) or (p["h"][2] if p.get("h") else "Flow Studio is a creative studio founded by Arsalan Ahmed Shaikh: shoots, editing, design, social media, websites, apps and AI films.")
    if k == "index": desc = re.search(r'<meta name="description" content="([^"]*)"', B).group(1); desc = html.unescape(desc)
    if k == "about": hero = phero("About us", "One studio. <span class=\"rbt\">Every visual you need.</span>", "Flow Studio is a creative studio for shoots, editing, design, social media, websites, apps, software and AI films, working with businesses in India and worldwide.", [("index","Home"),(None,"About")])
    build(k, p["show"], p["title"], desc, hero, extra_sections=ABOUT if k == "about" else "")
svnav = lambda cur: '<div class="svnav">' + "".join(f'<a href="{s[0]}"{" aria-current=\"page\"" if s[0]==cur else ""}>{E(s[1])}</a>' for s in SV) + '</div>'
for i, (slug, name, fold, d, bullets, ideal, dl) in enumerate(SV):
    extra = f'''<div class="svx"><div class="gl rv"><h2>What you get</h2><ul>{"".join(f"<li>{E(b)}</li>" for b in bullets)}</ul></div>
<div class="gl rv"><dl><div><dt>Ideal for</dt><dd>{E(ideal)}</dd></div><div><dt>Typical delivery</dt><dd>{E(dl)}</dd></div><div><dt>Payment</dt><dd>40% advance · 60% on final delivery</dd></div></dl>
<p style="margin-top:20px"><a class="btn rb" href="#" data-quote="{i}"><span class="shine"></span>Get quotation</a></p></div></div>{svnav(slug)}'''
    hero = phero("Service " + str(i+1).zfill(2) + " / 17", E(name).replace(" ", " ", 1), E(d), [("index","Home"),("services","Services"),(None,name)], extra)
    build(slug, "samples process contact faq", f"{name} · Flow Studio", f"{name} by Flow Studio: {d}", hero, body_attr=f' data-fold="{fold}" data-svc="{i}"')
# sitemap
urls = [SITE] + [SITE + k for k in PAGES if k != "index"] + [SITE + s[0] for s in SV]
open(os.path.join(R, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
open(os.path.join(R, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
json.dump([s[0] for s in SV], open(os.path.join(R, "_src/slugs.json"), "w"))
print("built", len(PAGES) + len(SV), "pages")
