import json
D = []
def add(kind, i, **k): D.append(dict(id=f'{kind}-u{i:02d}', kind=kind, **k))

for i, (acc, brand, dom, soft, menu, badge, h, sub, hero, prods) in enumerate([
 ("#a16207", "AUREN", "aurenwatches.com", "#f3efe6", ["Automatic", "Classic", "Straps", "Service"], "New · Emerald", "Time, made beautiful", "Swiss-movement automatics with Indian craftsmanship.", "aiphoto-c03", [["aiphoto-c03", "Auren Emerald", "₹84,500", "₹92,000"], ["comm-v08", "Auren Classic", "₹62,000", "₹68,000"], ["aiphoto-c03", "Emerald Steel", "₹71,000", "₹78,000"], ["comm-v08", "Gold Dress", "₹58,000", "₹64,000"]]),
 ("#ea580c", "STRYDE", "stryde.in", "#f6eee6", ["Running", "Trail", "Training", "Sale"], "New drop", "Run lighter. Go further.", "The Run 3 — our lightest runner yet.", "aiphoto-c04", [["aiphoto-c04", "Stryde Run 3", "₹4,299", "₹4,999"], ["design-2", "Stryde Trail", "₹4,799", "₹5,499"], ["design-m2", "Summit 001", "₹5,199", "₹5,999"], ["aiphoto-m2", "Desert Pro", "₹4,999", "₹5,699"]]),
 ("#0f766e", "LUMEA", "lumea.in", "#eef4f0", ["Face", "Body", "Kits", "Skin quiz"], "Best seller", "Glow, the natural way", "Clean skincare made with Indian botanicals.", "aiphoto-c01", [["aiphoto-c01", "Curry Leaf Serum", "₹899", "₹1,099"], ["pack-m5", "Daily Gel Cream", "₹749", "₹899"], ["aiphoto-m1", "Night Balm", "₹999", "₹1,199"], ["pack-m8", "Calm Candle", "₹649", "₹799"]]),
 ("#7c2d12", "MAISON ILYAA", "maisonilyaa.com", "#f5efe7", ["Perfumes", "Attars", "Gift sets", "Story"], "Noir is here", "Leave a trail they remember", "Saffron, oud and Taif rose — made in small batches.", "aiphoto-c02", [["aiphoto-c02", "Ilyaa Noir", "₹3,490", "₹3,990"], ["aiads-m1", "Navrasa EDP", "₹2,490", "₹2,990"], ["ai-product-noir-dune", "Noir Dune", "₹3,190", "₹3,690"], ["pack-m2", "Gift Box", "₹4,500", "₹5,200"]]),
]): add('shop', i + 7, acc=acc, brand=brand, dom=dom, soft=soft, menu=menu, badge=badge, h=h, sub=sub, hero=hero, prods=prods)

for i, (acc, q, site, title, desc, brand, im, tr, ld, serp) in enumerate([
 ("#a16207", "best automatic watch under 1 lakh", "aurenwatches.com › journal", "Best Automatic Watches Under ₹1 Lakh: A Buyer's Guide", "Movements, case sizes and straps explained, with the 7 watches worth your money.", "Auren Watches", "aiphoto-c03", "22.6k", "418", [["chrono24.in › automatic", "Automatic watches — shop", "New and pre-owned."], ["reddit.com › r/Watches", "First automatic under 1L?", "Thread · 312 answers"]]),
 ("#ea580c", "best running shoes for beginners india", "stryde.in › run-guide", "Best Running Shoes for Beginners (2026): How to Choose", "Cushioning, fit and surface — a simple guide to your first pair.", "Stryde", "aiphoto-c04", "31.9k", "1,280", [["amazon.in › running-shoes", "Running shoes — buy online", "Free delivery."], ["runnersworld.com › guides", "Beginner shoe guide", "Expert picks."]]),
 ("#7c2d12", "oud perfume long lasting", "maisonilyaa.com › journal", "Oud Perfumes That Last 12 Hours: How to Pick and Wear", "What makes oud last, how to layer it, and 5 blends for Indian weather.", "Maison Ilyaa", "aiphoto-c02", "18.7k", "960", [["nykaa.com › oud", "Oud perfumes", "Shop top picks."], ["fragrantica.com › notes", "Oud — note guide", "Community reviews."]]),
 ("#0891b2", "teeth whitening cost pune", "smilecare.in › blog", "Teeth Whitening in Pune: Cost, Safety & Results", "Clinic vs home kits, how long it lasts and what dentists recommend.", "SmileCare Dental", "brand-c02", "12.3k", "540", [["practo.com › pune", "Dentists in Pune", "Book online."], ["healthline.com › teeth", "Is whitening safe?", "Medically reviewed."]]),
]): add('seo', i + 12, acc=acc, q=q, site=site, title=title, desc=desc, brand=brand, img=im, traffic=tr, leads=ld, serp=serp)

for i, (acc, brand, chat, flow, stats) in enumerate([
 ("#25d366", "Lumea Skincare", [["u", "Which serum for oily skin?"], ["b", "Hi 🌿 Quick skin check — how does your skin feel by noon?", ["Oily all over", "Oily T-zone", "Dry"]], ["u", "Oily T-zone"], ["b", "Try our Curry Leaf Serum (₹899) — light, non-greasy. Add a gel cream?", ["Serum only", "Serum + cream"]], ["u", "Serum + cream"], ["b", "✅ Added both — ₹1,648 with free delivery. Pay here to confirm."]],
  [["💬", "Customer asks on WhatsApp"], ["🧪", "Bot runs a skin quiz"], ["🛍", "Recommends products"], ["💳", "Sends payment link"], ["🔁", "Reminds to reorder"]], [["2.4x", "WhatsApp sales"], ["38%", "reorder rate"], ["2 sec", "first reply"]]),
 ("#25d366", "Stryde", [["u", "Is Run 3 good for flat feet?"], ["b", "Hi 🏃 Yes — Run 3 has a stable heel. Your usual size?", ["UK 8", "UK 9", "UK 10"]], ["u", "UK 9"], ["b", "UK 9 is in stock ✅ ₹4,299, free exchange in 30 days. Order?", ["Order now", "Talk to expert"]], ["u", "Order now"], ["b", "🎉 Ordered! Delivery by Thursday. Track it right here."]],
  [["💬", "Shopper asks a question"], ["👟", "Bot checks size & stock"], ["💳", "Takes the order"], ["🚚", "Sends tracking"], ["⭐", "Asks for a review"]], [["1,500", "chats / month"], ["31%", "convert to orders"], ["0", "missed questions"]]),
 ("#25d366", "Kapoor & Associates", [["u", "I need help with a property agreement"], ["b", "Hello 👋 Is this for buying, selling or renting?", ["Buying", "Selling", "Renting"]], ["u", "Buying"], ["b", "A consult with Adv. Kapoor is ₹1,500 (30 min). Pick a time:", ["Mon 11 AM", "Tue 4 PM"]], ["u", "Mon 11 AM"], ["b", "📅 Booked for Monday 11 AM. Please share the draft here before the call."]],
  [["💬", "Client enquiry"], ["📋", "Bot asks the matter type"], ["📅", "Books a consult"], ["📄", "Collects documents"], ["🔔", "Reminds before the call"]], [["320", "consults / month"], ["0", "calls missed"], ["24/7", "enquiries handled"]]),
]): add('chatbot', i + 12, acc=acc, brand=brand, chat=chat, flow=flow, stats=stats)

for i, (acc, title, artist, im, desc, chips, lines, stats) in enumerate([
 ("#22c55e", "Morning Light", "Meher · acoustic", "ugc-c04", "Soft acoustic lyric reel with café visuals and handwritten captions.", ["Acoustic", "Handwritten type", "Café visuals", "Reels"], ["Coffee and <span>sunlight</span>", "Slow start, <span>soft</span> heart", "Stay a while <span>longer</span>", "Morning <span>light</span>, you and I"], [["780k", "views"], ["+26k", "listeners"]]),
 ("#f97316", "Run It Up", "Kabir & The Line", "aiphoto-c04", "Sports anthem visualiser with bold captions synced to every kick.", ["Sports", "Bold captions", "Beat sync", "Ads ready"], ["Lace them <span>tight</span>", "Hit the <span>road</span>", "Every mile a <span>story</span>", "Run it, run it <span>up</span>"], [["1.9M", "views"], ["+48k", "followers"]]),
 ("#eab308", "Golden Hour", "Noor · single", "aiphoto-c02", "Luxury slow-motion lyric reel with gold smoke and soft serif type.", ["Luxury", "Slow motion", "Serif type", "YouTube Shorts"], ["Smoke and <span>amber</span>", "A scent of <span>you</span>", "Stay till the <span>night</span>", "Golden hour, <span>golden</span> you"], [["1.1M", "views"], ["41%", "watched twice"]]),
 ("#ec4899", "Tum Ho", "Rehaan · romantic", "comm-v04", "Wedding-season romantic reel with soft-focus visuals and Urdu-English lyrics.", ["Romantic", "Wedding season", "Soft focus", "Reels"], ["Tum ho to <span>roshni</span>", "Har pal <span>khaas</span>", "Saath chalo <span>hamesha</span>", "Tum ho, <span>bas</span> tum"], [["2.3M", "views"], ["+57k", "followers"]]),
]): add('music', i + 11, acc=acc, title=title, artist=artist, img=im, desc=desc, chips=chips, lines=lines, stats=stats)

for i, w in enumerate([
 dict(acc="#a16207", brand="AUREN", dom="aurenwatches.com", menu=["Collection", "Service", "Stores"], hero="aiphoto-c03", badge="The Emerald collection", h1="Time, made beautiful.", p="Swiss-movement automatics, finished by hand. Book a private viewing.", cta="Book a viewing",
      feats=[["⌚", "Swiss movement", "5-year warranty"], ["🛠", "Lifetime service", "At every store"], ["🚚", "Insured delivery", "Pan-India"]], gal=["aiphoto-c03", "comm-v08", "aiphoto-c02"]),
 dict(acc="#ea580c", brand="STRYDE", dom="stryde.in", menu=["Shop", "Run club", "Stores"], hero="aiphoto-c04", badge="Run 3 · new", h1="Run lighter. Go further.", p="Our lightest runner yet, tested on Indian roads. Free size exchange.", cta="Shop Run 3",
      feats=[["👟", "180 g", "Lightest we've made"], ["🔁", "Free exchange", "30 days"], ["🏃", "Run club", "Every Sunday"]], gal=["aiphoto-c04", "edit-v02", "design-2"]),
 dict(acc="#0891b2", brand="SMILECARE", dom="smilecare.in", menu=["Treatments", "Doctors", "Book"], hero="brand-c02", badge="Painless dentistry", h1="Smile with confidence.", p="Whitening, aligners and implants by certified dentists. Book online in a minute.", cta="Book a check-up",
      feats=[["🦷", "Certified dentists", "15+ years"], ["📅", "Online booking", "Same-day slots"], ["💳", "Easy EMI", "0% interest"]], gal=["brand-c02", "comm-v03", "edit-v04"]),
 dict(acc="#1d4ed8", brand="KAPOOR & ASSOCIATES", dom="kapoorlaw.in", menu=["Practice", "Team", "Contact"], hero="print-c01", badge="Since 1998", h1="Clear advice. Strong results.", p="Property, corporate and family law. Book a 30-minute consultation online.", cta="Book a consult",
      feats=[["⚖️", "25+ years", "2,000+ matters"], ["📄", "Document review", "48-hour turnaround"], ["🔒", "Confidential", "Always"]], gal=["print-c01", "design-v05", "comm-v06"]),
]): add('web', i + 8, **w)

json.dump(D, open('data6.json', 'w'), ensure_ascii=False)
print(len(D))
