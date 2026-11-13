import json
D = []
def add(kind, i, **k): D.append(dict(id=f'{kind}-u{i:02d}', kind=kind, **k))

for i, (acc, brand, tag, im, prob, probp, facts, trac, growth, ask, use) in enumerate([
 ("#0f766e", "Lumea", "Clean skincare made with Indian botanicals.", "aiphoto-c01", "Most skincare isn't made for Indian skin.", "Humidity and pollution need lighter, cleaner formulas.", [["₹15,000 Cr", "skincare market"], ["38%", "reorder rate"], ["4.8★", "rating"]], "D2C revenue up 5x in 18 months.", [["H1", 50], ["H2", 105], ["H3", 170], ["H4", 236]], "Raising ₹8 Cr", "Retail in 300 stores and 3 new hero products."),
 ("#a16207", "Auren", "Swiss-movement watches with Indian craft.", "aiphoto-c03", "Luxury watches cost too much for first-time buyers.", "Young professionals want an heirloom watch under ₹1 lakh.", [["₹9,000 Cr", "watch market"], ["42", "viewings / week"], ["5 yr", "warranty"]], "Sales up 3.2x since the Emerald launch.", [["Q1", 60], ["Q2", 110], ["Q3", 175], ["Q4", 236]], "Raising ₹14 Cr", "Four boutiques and an online try-at-home service."),
 ("#ea580c", "Stryde", "Running shoes built for Indian roads.", "aiphoto-c04", "Global running shoes aren't made for our roads.", "Heat, dust and broken roads wear shoes out in months.", [["₹6,500 Cr", "sports shoes"], ["180 g", "lightest runner"], ["31%", "repeat buyers"]], "Units sold up 4.1x in a year.", [["Q1", 55], ["Q2", 100], ["Q3", 165], ["Q4", 236]], "Raising ₹20 Cr", "Own factory line, 50 run clubs and 3 new models."),
 ("#1d4ed8", "Kapoor Legal", "Modern legal services for families and startups.", "print-c01", "Legal help feels slow, costly and confusing.", "People don't know what a matter will cost or how long it takes.", [["2,000+", "matters handled"], ["48 hr", "document review"], ["96", "consults / month"]], "Clients up 2.8x with online booking.", [["2023", 70], ["2024", 125], ["2025", 180], ["2026", 236]], "Raising ₹5 Cr", "Fixed-price legal plans and a client app."),
]): add('deck', i + 13, acc=acc, brand=brand, tag=tag, img=im, prob=prob, probp=probp, facts=facts, trac=trac, growth=growth, ask=ask, use=use)

for i, (acc, brand, im, subs, langs, tracks) in enumerate([
 ("#0f766e", "Lumea ad", "aiphoto-c01", ["Glow, the natural way", "Qudrati chamak", "Brille naturellement", "تألق بطريقة طبيعية"], [["English", "Ready"], ["Urdu", "Ready"], ["French", "Ready"], ["Arabic", "Ready"]], [["Voice-over", "#14b8a6"], ["Urdu dub", "#ff7043"], ["Arabic dub", "#ab47bc"], ["Music", "#66bb6a"]]),
 ("#a16207", "Auren film", "aiphoto-c03", ["Time, made beautiful", "Waqt, khoobsurat", "El tiempo, hecho belleza", "الوقت، بجمال"], [["English", "Ready"], ["Urdu", "Ready"], ["Spanish", "Ready"], ["Arabic", "Ready"]], [["Narration", "#f59e0b"], ["Urdu dub", "#26c6da"], ["Spanish dub", "#ec407a"], ["Ambience", "#66bb6a"]]),
 ("#ea580c", "Stryde launch", "aiphoto-c04", ["Run lighter. Go further.", "Halke qadam, lambi daud", "Leichter laufen, weiter kommen", "اركض أخف، واذهب أبعد"], [["English", "Ready"], ["Urdu", "Ready"], ["German", "Ready"], ["Arabic", "Ready"]], [["Voice-over", "#f97316"], ["Urdu dub", "#26c6da"], ["German dub", "#5c6bc0"], ["Music", "#66bb6a"]]),
 ("#7c2d12", "Maison Ilyaa film", "aiphoto-c02", ["Leave a trail they remember", "Ek khushboo jo yaad rahe", "Laissez un sillage inoubliable", "اترك أثرًا لا يُنسى"], [["English", "Ready"], ["Urdu", "Ready"], ["French", "Ready"], ["Arabic", "Ready"]], [["Narration", "#b45309"], ["Urdu dub", "#26c6da"], ["French dub", "#ab47bc"], ["Music", "#66bb6a"]]),
]): add('voice', i + 11, acc=acc, brand=brand, img=im, subs=subs, langs=langs, tracks=tracks)

for i, (acc, brand, slug, nav, kpi, line, dt, split, tt, rows, lt) in enumerate([
 ("#ea580c", "Stryde", "stryde", ["Sales", "Products", "Stores", "Returns", "Reports"], [["Sales today", "₹9.4 L", "12.8%"], ["Orders", "2,180", "9.6%"], ["Return rate", "3.2%", "1.4%"], ["Repeat buyers", "31%", "4.0%"]], [44, 47, 52, 50, 58, 63, 61, 70, 74, 79, 83, 88, 92, 97], "Sales by channel", [54, 30, 12], "Top products", [["Run 3", "₹4.1 L", "960 pairs", "+24%"], ["Trail", "₹2.6 L", "540 pairs", "+11%"], ["Summit 001", "₹1.8 L", "350 pairs", "+9%"]], "Sales this month"),
 ("#0f766e", "Lumea", "lumea", ["Orders", "Products", "Customers", "Reviews", "Reports"], [["Revenue (MTD)", "₹38.2 L", "14.6%"], ["Orders", "6,420", "11.0%"], ["Reorder rate", "38%", "3.5%"], ["Avg. rating", "4.8★", "0.1"]], [38, 42, 45, 49, 55, 58, 63, 67, 71, 76, 80, 84, 89, 95], "Sales by product", [44, 33, 18], "Top cities", [["Mumbai", "₹9.8 L", "1,620 orders", "+16%"], ["Bengaluru", "₹8.1 L", "1,340 orders", "+13%"], ["Delhi", "₹7.4 L", "1,210 orders", "+10%"]], "Revenue"),
 ("#1d4ed8", "Kapoor Legal", "kapoorlegal", ["Matters", "Clients", "Hearings", "Billing", "Reports"], [["Active matters", "142", "6.0%"], ["Hearings this week", "18", "—"], ["Billed (MTD)", "₹26.4 L", "8.9%"], ["Collected", "91%", "2.2%"]], [50, 52, 55, 54, 58, 61, 60, 64, 67, 70, 72, 75, 78, 82], "Matters by type", [42, 31, 20], "Partners", [["Adv. Kapoor", "48 matters", "₹9.6 L", "+7%"], ["Adv. Mehta", "41 matters", "₹8.2 L", "+9%"], ["Adv. Iyer", "53 matters", "₹8.6 L", "+6%"]], "Billing"),
]): add('dash', i + 12, acc=acc, brand=brand, slug=slug, nav=nav, kpi=kpi, line=line, dt=dt, split=split, tt=tt, rows=rows, lt=lt)

for i, (acc, brand, prompt, month, posts) in enumerate([
 ("#a16207", "Auren Watches", "Luxury watch posts + creator reviews", "Launch month", [["aiphoto-c03", "Emerald macro", "Scheduled 8 PM"], ["ugc-c06", "Creator review", "Scheduled 7 PM"], ["comm-v08", "Gift for her", "Scheduled 11 AM"], ["aiphoto-c03", "Book a viewing", "Scheduled 8 PM"]]),
 ("#1d4ed8", "Kapoor Legal", "Weekly legal tips, trustworthy tone", "Quarter plan", [["print-c01", "Know your agreement", "Scheduled 10 AM"], ["design-v05", "Trademark basics", "Scheduled 6 PM"], ["comm-v06", "Property buying tips", "Scheduled 10 AM"], ["print-c01", "Book a consult", "Scheduled 6 PM"]]),
 ("#dc2626", "Iron Forge", "Brand + merch posts for gym launch", "Launch plan", [["brand-c03", "New identity", "Scheduled 9 AM"], ["ugc-c02", "Whey review", "Scheduled 6 PM"], ["comm-v07", "Coach spotlight", "Scheduled 7 AM"], ["comm-v02", "Free trial week", "Scheduled 6 PM"]]),
]): add('aiauto', i + 18, acc=acc, brand=brand, prompt=prompt, month=month, posts=posts)

for i, (acc, brand, slug, im, cap, title, by, n, stu, rate, les, done) in enumerate([
 ("#7c3aed", "Print School", "printschool", "print-c03", "Foil looks best on dark paper", "Luxury Print & Stationery Design", "by Ayaan Khan · 4 hrs", "16", "1,780", "4.8", ["Paper & finishes", "Foil and letterpress", "Invitations", "Business cards", "Print-ready files", "Working with printers"], 2),
 ("#0891b2", "Clinic Growth", "clinicgrowth", "brand-c02", "Reviews bring new patients", "Marketing for Dental Clinics", "by Dr. Priya Nair · 5 hrs", "18", "1,260", "4.8", ["Clinic branding", "Google profile", "Instagram for doctors", "WhatsApp booking", "Patient reviews", "Running ads"], 3),
 ("#ea580c", "Run Academy", "runacademy", "ugc-c07", "Land soft, under your hips", "5K to Half Marathon", "by Coach Meera · 12 weeks", "36", "4,560", "4.9", ["Week 1 · Easy runs", "Breathing & form", "Choosing shoes", "Long runs", "Race-day plan", "Recovery"], 2),
]): add('course', i + 13, acc=acc, brand=brand, slug=slug, img=im, cap=cap, title=title, by=by, n=n, stu=stu, rate=rate, lessons=les, done=done)

for i, x in enumerate([
 dict(acc="#a16207", name="Auren Watches", role="Watch brand. Macro films, creators and launch reels.", handle="auren.watches", av="aiphoto-c03", before="1,100", after="46.8k", months="6", posts="172", fol="90",
      bio="⌚ Time, made beautiful · Book a viewing 👇", grid=["aiphoto-c03", "ugc-c06", "comm-v08", "aiphoto-c02", "aiphoto-c03", "ugc-c06"], did=["Weekly macro films", "Creator reviews", "Viewing bookings from DMs"]),
 dict(acc="#1d4ed8", name="Kapoor & Associates", role="Law firm. Expert tips that build trust.", handle="kapoor.legal", av="print-c01", before="400", after="21.5k", months="6", posts="140", fol="60",
      bio="⚖️ Property · Corporate · Family law · Book 👇", grid=["print-c01", "design-v05", "comm-v06", "print-c01", "design-v05", "comm-v06"], did=["Tip reels by partners", "Carousels on common cases", "Consult bookings online"]),
 dict(acc="#ea580c", name="Stryde", role="Sportswear. Athletes, run clubs and drops.", handle="stryde.official", av="ugc-c07", before="3,800", after="91.3k", months="8", posts="288", fol="140",
      bio="🏃 Run lighter · Run club every Sunday", grid=["ugc-c07", "aiphoto-c04", "edit-v02", "design-2", "ugc-c07", "aiphoto-c04"], did=["Creator runs every week", "Drop countdowns", "Run-club community"]),
]): add('pb', i + 15, **x)

json.dump(D, open('data7.json', 'w'), ensure_ascii=False)
print(len(D))
