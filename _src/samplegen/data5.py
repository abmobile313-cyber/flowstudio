import json
D = []
def add(kind, i, **k): D.append(dict(id=f'{kind}-u{i:02d}', kind=kind, **k))

for i, a in enumerate([
 dict(acc="#0f766e", bg2="#f0fdfa", brand="Lumea", tagline="Skincare shop app", desc="Skin quiz, routines and one-tap reorder", hello="Hi Sana 🌿", h1="Your routine",
      chips=["Serums", "Creams", "Kits"], items=[["aiphoto-c01", "Curry Leaf Serum", "₹899", "30 ml · for dull skin"], ["pack-m5", "Daily Gel Cream", "₹749", "50 ml · oil-free"]],
      detail="Brightening serum with curry leaf and niacinamide. Use morning and night.", opts=["30 ml", "50 ml", "Kit"], cta="Add to bag · ₹899", t3="Reorder reminder", t3s="Serum runs out in 5 days",
      track=[["Skin quiz", "Done · Combination"], ["Routine set", "3 steps"], ["Order #LM-3302", "Delivered"], ["Next refill", "21 Nov"]], foot=["Auto-refill", "ON"]),
 dict(acc="#a16207", bg2="#fefce8", brand="Auren", tagline="Luxury watch store app", desc="Explore, book a viewing and track service", hello="Good evening ✦", h1="New arrivals",
      chips=["Automatic", "Chronograph", "Dress"], items=[["aiphoto-c03", "Auren Emerald", "₹84,500", "Rose gold · 41 mm"], ["comm-v08", "Auren Classic", "₹62,000", "Gold · 38 mm"]],
      detail="Open-heart automatic, sunburst green dial, Italian leather strap.", opts=["Book viewing", "Video call", "Buy now"], cta="Book a private viewing", t3="Your viewing", t3s="Saturday · 4 PM",
      track=[["Viewing booked", "Sat 4 PM"], ["Watch reserved", "Auren Emerald"], ["Advisor", "Mr. Mehta"], ["Reminder", "Fri evening"]], foot=["Free strap engraving", "✓"]),
 dict(acc="#ea580c", bg2="#fff7ed", brand="Stryde", tagline="Sportswear shop app", desc="Shop drops, size help and run tracking", hello="Ready to run, Kabir? 🏃", h1="New drop",
      chips=["Running", "Trail", "Training"], items=[["aiphoto-c04", "Stryde Run 3", "₹4,299", "Light · breathable"], ["design-2", "Stryde Trail", "₹4,799", "Grip · all-terrain"]],
      detail="Our lightest runner yet. Cushioned sole, sand-proof knit upper.", opts=["UK 8", "UK 9", "UK 10"], cta="Add to cart · ₹4,299", t3="This week's runs", t3s="12.4 km · 3 runs",
      track=[["Mon · 5 km", "28:40"], ["Wed · 4.2 km", "23:10"], ["Fri · 3.2 km", "17:55"], ["Sun · long run", "Planned"]], foot=["Order status", "Shipped"]),
 dict(acc="#1d4ed8", bg2="#eff6ff", brand="Kapoor Legal", tagline="Law-firm client app", desc="Case updates, documents and meetings", hello="Hello, Mr. Shah", h1="Your matters",
      chips=["Active", "Documents", "Invoices"], items=[["print-c01", "Property agreement", "Review", "Adv. Kapoor · due Fri"], ["design-v05", "Trademark filing", "Filed", "Hearing in Jan"]],
      detail="Draft sale agreement ready for your review. 3 comments from counsel.", opts=["Approve", "Comment", "Call"], cta="Book a meeting", t3="Matter timeline", t3s="Property · Bandra",
      track=[["Documents received", "4 Nov"], ["Title search done", "8 Nov"], ["Draft shared", "12 Nov"], ["Signing", "Planned 20 Nov"]], foot=["Next meeting", "Mon 11 AM"]),
]): add('app', i + 16, **a)

for i, c in enumerate([
 dict(acc="#dc2626", brand="CaféOS", shop="Counter · Hill Bean Café", app="Hill Bean · Owner", tabs=["Orders", "Kitchen", "Menu", "Reports"], cols=["Order", "Table", "Items", "Total"],
      items=[["#2211", "T3", "2 flat white", "₹360"], ["#2212", "App", "Cold brew + bake", "₹420"], ["#2213", "T6", "Pour-over", "₹240"], ["#2214", "T1", "2 cappuccino", "₹380"]],
      side="Live", tot=[["Open", "9"], ["Done today", "184"]], grand="₹42,610", btn="Send to barista", toast="Order #2214 sent to barista", feed=[["App order #2212", "Pickup 8:20 AM"], ["Today ₹42,610", "184 orders"], ["Beans low: Malabar", "2 bags"]]),
 dict(acc="#0891b2", brand="DentaDesk", shop="Reception · SmileCare", app="SmileCare · Patient", tabs=["Queue", "Patients", "X-rays", "Billing"], cols=["Patient", "Time", "Doctor", "Status"],
      items=[["R. Patel", "10:00", "Dr. Shah", "Done"], ["S. Khan", "10:30", "Dr. Shah", "In chair"], ["A. Joshi", "11:00", "Dr. Kulkarni", "Waiting"], ["M. Rao", "11:30", "Dr. Mehta", "Booked"]],
      side="Today", tot=[["Seen", "18"], ["Waiting", "6"]], grand="₹84,200", btn="Call next patient", toast="A. Joshi notified on phone", feed=[["Your turn in 10 min", "Dr. Kulkarni · Chair 2"], ["X-ray uploaded", "Tap to view"], ["Bill ₹2,400", "Pay online"]]),
 dict(acc="#a16207", brand="JewelDesk", shop="Showroom · Swarnika", app="Swarnika · Owner", tabs=["Sales", "Stock", "Orders", "Gold rate"], cols=["Item", "Weight", "Rate", "Amount"],
      items=[["Emerald choker", "46 g", "₹7,240", "₹3,33,040"], ["Gold bangles (2)", "32 g", "₹7,240", "₹2,31,680"], ["Diamond studs", "4 g", "—", "₹68,000"], ["Making", "—", "—", "₹24,500"]],
      side="Bill #SW-881", tot=[["GST 3%", "₹19,718"], ["Old gold", "−₹42,000"]], grand="₹6,34,938", btn="Print + WhatsApp bill", toast="Sale synced to owner's phone", feed=[["Sale ₹6.35 L", "Counter 2 · now"], ["Gold rate ₹7,240", "Updated 10 AM"], ["Today ₹18.6 L", "14 bills"]]),
 dict(acc="#16a34a", brand="FarmRoute", shop="Dispatch · Nectar Valley", app="Nectar Valley · Rider", tabs=["Routes", "Riders", "Stock", "Returns"], cols=["Route", "Rider", "Bottles", "Status"],
      items=[["Baner", "Imran", "240", "On route"], ["Aundh", "Sagar", "196", "On route"], ["Kothrud", "Rahul", "212", "Loading"], ["Viman Nagar", "Ajay", "180", "Done"]],
      side="This morning", tot=[["Bottles", "9,860"], ["On time", "98%"]], grand="42 routes", btn="Send ETA to customers", toast="ETA sent to 3,412 customers", feed=[["Next stop: Baner Rd", "12 bottles"], ["Route 68% done", "4:50 AM start"], ["Return: 3 empties", "Collected"]]),
]): add('combo', i + 16, **c)

for i, (acc, brand, prompt, month, posts) in enumerate([
 ("#0f766e", "Lumea Skincare", "Daily skin tips + product reels, calm tone", "December plan", [["aiphoto-c01", "Serum spotlight", "Scheduled 10 AM"], ["ugc-c01", "Creator review", "Scheduled 7 PM"], ["pack-m5", "Night routine", "Scheduled 9 PM"], ["aiphoto-m1", "Winter care", "Scheduled 10 AM"]]),
 ("#ea580c", "Stryde", "Running reels + drop countdown", "Drop month", [["aiphoto-c04", "Run 3 drop", "Scheduled 7 AM"], ["edit-v02", "City run", "Scheduled 6 PM"], ["design-2", "Trail series", "Scheduled 7 AM"], ["aiphoto-m2", "Sand test", "Scheduled 6 PM"]]),
 ("#a16207", "Maison Ilyaa", "Evening perfume posts + unboxing reels", "Festive plan", [["aiphoto-c02", "Noir in smoke", "Scheduled 8 PM"], ["ugc-c05", "Unboxing reel", "Scheduled 7 PM"], ["aiads-m1", "Navrasa notes", "Scheduled 8 PM"], ["pack-m2", "Gift box", "Scheduled 11 AM"]]),
 ("#7c3aed", "Hill Bean Café", "Coffee reels + weekend offers", "Monthly plan", [["ugc-c04", "Iced coffee review", "Scheduled 9 AM"], ["brand-c01", "Our new look", "Scheduled 1 PM"], ["aiphoto-m4", "Roast day", "Scheduled 9 AM"], ["pack-m1", "Bean of the week", "Scheduled 1 PM"]]),
]): add('aiauto', i + 14, acc=acc, brand=brand, prompt=prompt, month=month, posts=posts)

for i, (acc, brand, aud, camp, kpi, bars, im, head, line, btn, wa, rep) in enumerate([
 ("#0f766e", "Lumea Skincare", "11,200 customers", "Winter skin kit", [["49.2%", "Open rate"], ["13.6%", "Click rate"], ["11,200", "Sent"], ["₹3.4L", "Sales"]], [22, 30, 41, 47, 56, 63, 70, 79, 86, 93], "aiphoto-c01", "Your winter skin kit", "Serum + cream + balm, 20% off this week.", "Shop the kit", "🌿 Winter skin kit is here — 20% off till Sunday.", "Is it okay for oily skin?"),
 ("#a16207", "Auren Watches", "3,100 collectors", "Private viewing invite", [["58.3%", "Open rate"], ["17.9%", "Click rate"], ["3,100", "Sent"], ["42", "Viewings"]], [28, 35, 46, 53, 59, 68, 74, 83, 89, 97], "aiphoto-c03", "The Emerald collection", "Book a private viewing this weekend.", "Book a viewing", "✦ You're invited: a private viewing of the Auren Emerald this Saturday.", "Saturday 4 PM works"),
 ("#ea580c", "Stryde", "9,640 runners", "Run 3 launch", [["45.8%", "Open rate"], ["12.9%", "Click rate"], ["9,640", "Sent"], ["₹5.7L", "Sales"]], [26, 33, 39, 51, 60, 64, 77, 82, 88, 96], "aiphoto-c04", "Stryde Run 3 is live", "Lightest runner yet. Free size exchange.", "Shop now", "🏃 Run 3 is live — free size exchange for 30 days.", "Do you have UK 9?"),
 ("#dc2626", "Saffron Table", "18,500 diners", "Weekend combo offer", [["43.1%", "Open rate"], ["11.4%", "Click rate"], ["18,500", "Sent"], ["2,140", "Orders"]], [31, 38, 44, 50, 61, 69, 72, 80, 91, 98], "ai-m4", "Weekend burger combo", "Burger + fries + shake at ₹299.", "Order now", "🍔 Weekend combo: burger + fries + shake at ₹299.", "Deliver to Baner?"),
 ("#7c3aed", "Kapoor & Associates", "2,800 clients", "Year-end tax checklist", [["61.0%", "Open rate"], ["19.2%", "Click rate"], ["2,800", "Sent"], ["96", "Consults"]], [35, 41, 47, 55, 62, 70, 78, 84, 90, 99], "print-c01", "Your year-end checklist", "8 things to file before 31 March.", "Book a consult", "📄 Your year-end legal & tax checklist is ready. Book a 20-min consult.", "Monday morning please"),
]): add('mkt', i + 11, acc=acc, brand=brand, aud=aud, camp=camp, kpi=kpi, bars=bars, img=im, head=head, line=line, btn=btn, wa=wa, reply=rep)

for i, (acc, brand, slug, im, cap, title, by, n, stu, rate, les, done) in enumerate([
 ("#a16207", "Luxe Lens", "luxelens", "aiphoto-c03", "Light the metal, not the dial", "Luxury Product Photography", "by Rhea Kapoor · 6 hrs", "24", "2,140", "4.9", ["Gear & studio setup", "Lighting metal & glass", "Macro focus", "Smoke & water effects", "Retouching", "Pricing brand shoots"], 3),
 ("#0f766e", "Brand School", "brandschool", "brand-c01", "One logo, many sizes", "Brand Identity Design from Zero", "by Ayaan Khan · 7 hrs", "26", "3,880", "4.8", ["Brand strategy", "Logo sketching", "Colour & type", "Stationery set", "Brand guidelines", "Pitching clients"], 2),
 ("#ea580c", "Creator Lab", "creatorlab", "ugc-c03", "Hook them in 2 seconds", "UGC Creator Masterclass", "by Zoya Siddiqui · 5 hrs", "20", "6,120", "4.9", ["Phone setup & light", "Hooks that work", "Product reviews", "Unboxing videos", "Editing in CapCut", "Getting brand deals"], 4),
]): add('course', i + 10, acc=acc, brand=brand, slug=slug, img=im, cap=cap, title=title, by=by, n=n, stu=stu, rate=rate, lessons=les, done=done)

for i, x in enumerate([
 dict(acc="#0f766e", name="Lumea Skincare", role="Skincare brand. Creators, product films and ads.", handle="lumea.skin", av="aiphoto-c01", before="2,600", after="72.4k", months="7", posts="264", fol="130",
      bio="🌿 Clean skincare · Made in India · Shop 👇", grid=["aiphoto-c01", "ugc-c01", "pack-m5", "aiphoto-m1", "aiphoto-c01", "ugc-c01"], did=["Creator reviews every week", "Product films", "Shop tags on every post"]),
 dict(acc="#ea580c", name="Stryde", role="Sportswear brand. Drops, run clubs and athlete reels.", handle="stryde.run", av="aiphoto-c04", before="1,400", after="58.9k", months="6", posts="218", fol="160",
      bio="🏃 Run. Lift. Repeat. · New drop 👇", grid=["aiphoto-c04", "edit-v02", "design-2", "aiphoto-m2", "aiphoto-c04", "edit-v03"], did=["Drop countdown reels", "Run-club content", "Athlete collabs"]),
 dict(acc="#a16207", name="Hill Bean Café", role="Café chain. Food reels, creators and offers.", handle="hillbean.cafe", av="brand-c01", before="900", after="38.2k", months="5", posts="196", fol="210",
      bio="☕ Fresh coffee, roasted in the hills · 4 cafés", grid=["brand-c01", "ugc-c04", "aiphoto-m4", "pack-m1", "brand-c01", "ugc-c04"], did=["Daily coffee reels", "Creator visits", "Weekend offer posts"]),
]): add('pb', i + 12, **x)

json.dump(D, open('data5.json', 'w'), ensure_ascii=False)
print(len(D))
