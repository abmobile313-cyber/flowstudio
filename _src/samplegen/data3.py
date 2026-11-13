import json
D = []
def add(kind, i, **k): D.append(dict(id=f'{kind}-u{i:02d}', kind=kind, **k))

# ---------- Mobile apps ----------
for i, a in enumerate([
 dict(acc="#ea580c", bg2="#fff7ed", brand="Hill Bean Café", tagline="Café order-ahead app", desc="Skip the queue — order, pay, pick up", hello="Morning, Kabir ☕", h1="Your usual?",
      chips=["Coffee", "Cold brew", "Bakes"], items=[["aiphoto-m4", "Sahyadri Roast", "₹540", "Fresh beans · 250 g"], ["pack-m1", "Monsoon Malabar", "₹590", "Roasted this week"]],
      detail="Smooth, chocolatey single-estate beans roasted every Monday.", opts=["Whole bean", "Filter grind", "Espresso"], cta="Add to order · ₹540", t3="Ready for pickup", t3s="Counter 2 · Bandra",
      track=[["Order received", "8:02 AM"], ["Barista making it", "8:04 AM"], ["Ready at counter", "8:07 AM"], ["Picked up", "—"]], foot=["Points earned", "+54"]),
 dict(acc="#16a34a", bg2="#f0fdf4", brand="Nectar Valley", tagline="Juice subscription app", desc="Fresh cold-pressed juice every morning", hello="Hi Riya 🍊", h1="Tomorrow's box",
      chips=["Citrus", "Greens", "Kids"], items=[["aiads-m3", "Citrus Burst", "₹149", "300 ml · no sugar"], ["pack-m3", "Mango Guava Jamun", "₹169", "300 ml · cold-pressed"]],
      detail="Orange, sweet lime and ginger, pressed at 4 AM and delivered chilled.", opts=["Daily", "Weekdays", "Weekends"], cta="Subscribe · ₹149/day", t3="Delivery tracker", t3s="Arriving by 7:30 AM",
      track=[["Pressed", "4:10 AM"], ["Packed chilled", "5:00 AM"], ["Out for delivery", "6:45 AM"], ["At your door", "~7:25 AM"]], foot=["Skip tomorrow", "Tap"]),
 dict(acc="#9333ea", bg2="#faf5ff", brand="Swarnika Jewellers", tagline="Jewellery showroom app", desc="Browse, try-on and book a showroom visit", hello="Namaste, Meher ✨", h1="Bridal collection",
      chips=["Necklaces", "Bangles", "Rings"], items=[["design-jewellery-ad", "Emerald Choker", "₹2,48,000", "22 kt · 46 g"], ["design-3", "Temple Gold Set", "₹1,86,500", "22 kt · 38 g"]],
      detail="Hand-set emeralds on 22 kt gold, with matching earrings.", opts=["Try at home", "Showroom", "Video call"], cta="Book a visit", t3="Your visit", t3s="Saturday, 12:30 PM",
      track=[["Visit booked", "Sat 12:30 PM"], ["Designer assigned", "Ms. Kapoor"], ["Pieces kept ready", "6 designs"], ["Reminder", "Fri evening"]], foot=["Gold rate today", "₹7,240/g"]),
 dict(acc="#0891b2", bg2="#ecfeff", brand="ShipFast", tagline="Courier & tracking app", desc="Book pickups and track every parcel live", hello="Hello, Patel Stores 📦", h1="Today's shipments",
      chips=["Pickups", "In transit", "Delivered"], items=[["camera-1", "48 parcels", "₹3,120", "Pickup 4 PM · Andheri"], ["camera-m5", "Express · 6", "₹1,140", "Same-day Mumbai"]],
      detail="Your 48 parcels are packed and labelled. Rider arrives at 4 PM.", opts=["Standard", "Express", "COD"], cta="Confirm pickup", t3="Parcel #SF-20418", t3s="Pune → Mumbai",
      track=[["Picked up", "Mon 4:12 PM"], ["Hub · Pune", "Mon 9:40 PM"], ["Hub · Mumbai", "Tue 6:05 AM"], ["Out for delivery", "Tue 10 AM"]], foot=["COD collected", "₹42,600"]),
 dict(acc="#dc2626", bg2="#fef2f2", brand="AutoPro", tagline="Car service app", desc="Book a service, see photos, pay online", hello="Hi Farhan 🚗", h1="Your SUV",
      chips=["Service", "Wash", "Tyres"], items=[["aiads-m4", "Full service", "₹4,499", "Oil + filters + check-up"], ["camera-m5", "Ceramic coat", "₹12,900", "3-year shine"]],
      detail="Free pick-up and drop. Photo updates at every step.", opts=["Today", "Tomorrow", "Pick date"], cta="Book · ₹4,499", t3="Service live", t3s="Bay 3 · Technician Ravi",
      track=[["Car picked up", "9:05 AM"], ["Inspection done", "10:20 AM · 8 photos"], ["Oil + filters", "11:40 AM"], ["Wash & ready", "~2:30 PM"]], foot=["Pay online", "₹4,499"]),
]): add('app', i + 12, **a)

# ---------- PC + phone combo ----------
for i, c in enumerate([
 dict(acc="#7c3aed", brand="SalonDesk", shop="Front desk · Glow Salon", app="Glow Salon · Owner", tabs=["Bookings", "Clients", "Billing", "Stock"], cols=["Client", "Service", "Stylist", "Time"],
      items=[["Ayesha K.", "Hair spa", "Neha", "11:00"], ["Ritika S.", "Bridal trial", "Pooja", "12:30"], ["Sana M.", "Keratin", "Neha", "2:00"], ["Zoya F.", "Facial", "Imran", "3:30"]],
      side="Today", tot=[["Bookings", "26"], ["Walk-ins", "7"]], grand="₹38,400", btn="Bill & send receipt", toast="Receipt sent to Ayesha on SMS",
      feed=[["New booking 4:30 PM", "Hair colour · Pooja"], ["Today ₹38,400", "33 clients"], ["Low stock: serum", "4 left"]]),
 dict(acc="#0f766e", brand="PharmaFlow", shop="Counter · City Pharmacy", app="City Pharmacy · Owner", tabs=["Billing", "Stock", "Expiry", "Suppliers"], cols=["Medicine", "Qty", "Batch", "Amount"],
      items=[["Paracetamol 650", "2 strips", "PC2411", "₹64"], ["Vitamin D3 60k", "4 caps", "VD0926", "₹132"], ["Cough syrup 100 ml", "1", "CS1102", "₹118"], ["BP monitor", "1", "OM2205", "₹1,890"]],
      side="Bill #4471", tot=[["Items", "4"], ["Discount", "₹110"]], grand="₹2,094", btn="Print + WhatsApp bill", toast="Bill synced to owner's phone",
      feed=[["Sale ₹2,094", "Counter 1 · just now"], ["Expiring in 30 days", "14 items"], ["Today ₹61,380", "212 bills"]]),
 dict(acc="#b45309", brand="HotelOS", shop="Reception · Hilltop Resort", app="Hilltop · Manager", tabs=["Rooms", "Check-in", "Housekeeping", "Billing"], cols=["Room", "Guest", "Status", "Nights"],
      items=[["Valley 204", "Mr. Desai", "Checked in", "2"], ["Pool 108", "Ms. Fernandes", "Arriving", "3"], ["Suite 301", "Mr. Khan", "Cleaning", "—"], ["Valley 210", "Mrs. Rao", "Checked in", "1"]],
      side="Tonight", tot=[["Occupied", "38 / 42"], ["Arrivals", "9"]], grand="90% full", btn="Send check-in link", toast="Room 301 ready · housekeeping updated",
      feed=[["Room 301 is ready", "Housekeeping · Sunil"], ["Arrival: Ms. Fernandes", "ETA 3:30 PM"], ["Tonight 90% full", "₹4.2L revenue"]]),
 dict(acc="#2563eb", brand="FitDesk", shop="Front desk · Iron Forge", app="Iron Forge · Member", tabs=["Members", "Check-ins", "Plans", "Payments"], cols=["Member", "Plan", "Valid till", "Status"],
      items=[["Vikram R.", "Annual", "Mar 2027", "Active"], ["Meera I.", "Quarterly", "Jan 2027", "Active"], ["Kabir S.", "Monthly", "18 Nov", "Renew"], ["Aisha N.", "Annual", "Aug 2027", "Active"]],
      side="Today", tot=[["Check-ins", "624"], ["Renewals due", "31"]], grand="92% renew", btn="Send renewal reminders", toast="Reminders sent to 31 members",
      feed=[["Checked in ✓", "6:42 AM · Iron Forge"], ["Workout: Upper Body", "45 min · Coach Meera"], ["Plan renews", "18 Nov · ₹2,499"]]),
]): add('combo', i + 12, **c)

# ---------- AI content automation ----------
for i, (acc, brand, prompt, month, posts) in enumerate([
 ("#dc2626", "Iron Forge Gym", "Daily gym reels + offers for November", "November plan", [["comm-v07", "Leg day energy", "Scheduled 6 AM"], ["comm-v02", "Protein after workout", "Scheduled 1 PM"], ["edit-v03", "Member of the month", "Scheduled 7 PM"], ["edit-v02", "Run club Sunday", "Scheduled 6 AM"]]),
 ("#0f766e", "GlowCare Clinic", "Skin tips + treatment posts, calm tone", "Winter plan", [["comm-v03", "Hydra facial 101", "Scheduled 11 AM"], ["edit-v04", "LED therapy explained", "Scheduled 6 PM"], ["aiphoto-m1", "Serum routine", "Scheduled 11 AM"], ["comm-v03", "Book before Diwali", "Scheduled 6 PM"]]),
 ("#b45309", "Saffron Table", "Food reels + weekend offers, hungry mood", "Weekend plan", [["ai-m4", "Smash burger drop", "Scheduled 12 PM"], ["aiads-m6", "Dessert hour", "Scheduled 4 PM"], ["aiads-m3", "Fresh juices", "Scheduled 9 AM"], ["design-cafe-poster", "Iced caramel", "Scheduled 7 PM"]]),
 ("#7c3aed", "Swarnika Jewellers", "Wedding-season jewellery posts", "Wedding season", [["design-jewellery-ad", "Emerald edit", "Scheduled 7 PM"], ["design-3", "Gold rate today", "Scheduled 10 AM"], ["comm-v04", "Bridal story", "Scheduled 8 PM"], ["comm-v08", "Watch & jewels", "Scheduled 6 PM"]]),
]): add('aiauto', i + 10, acc=acc, brand=brand, prompt=prompt, month=month, posts=posts)

# ---------- AI chatbots ----------
for i, (acc, brand, chat, flow, stats) in enumerate([
 ("#25d366", "Hilltop Resort", [["u", "Room for 2 this weekend?"], ["b", "Hi 👋 Which room would you like?", ["Valley view", "Pool view", "Suite"]], ["u", "Pool view"], ["b", "Pool view, Sat–Sun: ₹6,800/night with breakfast. Book?", ["Book now", "See photos"]], ["u", "Book now"], ["b", "✅ Booked! Pay ₹6,800 advance here to confirm. Check-in from 2 PM."]],
  [["💬", "Guest asks on WhatsApp"], ["🛏", "Bot shows live rooms"], ["💳", "Takes advance payment"], ["📩", "Sends confirmation"], ["⭐", "Asks for review after stay"]], [["3x", "direct bookings"], ["0", "OTA commission"], ["24/7", "instant replies"]]),
 ("#25d366", "Swarnika Jewellers", [["u", "Today's gold rate?"], ["b", "Today 22 kt: ₹7,240/g · 24 kt: ₹7,890/g ✨ Looking for something special?", ["Bridal sets", "Rings", "Book visit"]], ["u", "Bridal sets"], ["b", "Here are 6 bridal sets from ₹1.8 L. Want a video call with our designer?", ["Video call", "Visit showroom"]], ["u", "Visit showroom"], ["b", "📍 Booked for Saturday 12:30 PM. Ms. Kapoor will keep the sets ready."]],
  [["💬", "Customer asks rate"], ["💰", "Bot sends live rate"], ["💍", "Shows designs"], ["📅", "Books showroom visit"], ["🔔", "Reminds a day before"]], [["1,800", "chats / month"], ["44%", "book a visit"], ["2 sec", "first reply"]]),
 ("#25d366", "Iron Forge Gym", [["u", "Gym fees?"], ["b", "Hi 💪 Plans: Monthly ₹2,499 · Quarterly ₹6,499 · Annual ₹19,999. Free trial?", ["Free trial", "Annual plan"]], ["u", "Free trial"], ["b", "Pick a time for your free session:", ["6 AM", "7 PM", "8 PM"]], ["u", "7 PM"], ["b", "✅ Free trial booked today 7 PM with Coach Meera. Bring shoes & water!"]],
  [["💬", "Lead from Instagram ad"], ["🤖", "Bot shares plans"], ["🏋️", "Books free trial"], ["📞", "Alerts the coach"], ["💳", "Sends joining link"]], [["620", "trials booked"], ["41%", "join after trial"], ["0", "missed leads"]]),
 ("#25d366", "City Pharmacy", [["u", "Do you have Vitamin D3 60k?"], ["b", "Yes ✅ ₹33 per capsule. Home delivery in 30 min. Upload prescription?", ["Upload", "Order without"]], ["u", "Upload"], ["b", "Got it 📄 Checked by pharmacist. Total ₹132 for 4 capsules. Deliver to saved address?", ["Yes, deliver", "Change address"]], ["u", "Yes, deliver"], ["b", "🛵 On the way! Rider Amit, arriving in ~25 min."]],
  [["💬", "Customer sends medicine name"], ["📄", "Bot takes prescription"], ["🧑‍⚕️", "Pharmacist approves"], ["💳", "UPI payment link"], ["🛵", "Live delivery update"]], [["900+", "orders / month"], ["30 min", "delivery"], ["4.8★", "rating"]]),
]): add('chatbot', i + 8, acc=acc, brand=brand, chat=chat, flow=flow, stats=stats)

# ---------- SEO ----------
for i, (acc, q, site, title, desc, brand, im, tr, ld, serp) in enumerate([
 ("#16a34a", "cold pressed juice delivery pune", "nectarvalley.in › blog", "Cold-Pressed vs Packaged Juice: What's Really in Your Glass?", "We tested 10 juices for sugar and nutrients. Here's what to drink every morning.", "Nectar Valley", "pack-m3", "19.2k", "940", [["swiggy.com › pune", "Juice delivery in Pune", "Order from top juice bars."], ["zomato.com › pune", "Best juice places in Pune", "Ratings, menus and photos."]]),
 ("#b45309", "heritage hotel jaipur wedding", "grandsaffron.com › weddings", "Planning a Palace Wedding in Jaipur: Cost, Venues & Timeline", "A month-by-month plan for a royal wedding, with real budgets and decor ideas.", "The Grand Saffron", "comm-v06", "26.8k", "312", [["weddingwire.in › jaipur", "Wedding venues in Jaipur", "Compare prices and reviews."], ["wedmegood.com › jaipur", "Palace venues Jaipur", "Photos and packages."]]),
 ("#dc2626", "best gym near me pune", "ironforge.fit › guides", "How to Choose a Gym in Pune: 9 Things to Check Before You Pay", "Equipment, coaches, hidden fees and trial tips — a simple checklist.", "Iron Forge Gym", "comm-v07", "14.4k", "680", [["cult.fit › pune", "Gyms in Pune", "Book a session."], ["justdial.com › Pune", "Gyms near you", "Phone numbers and ratings."]]),
 ("#9333ea", "bridal jewellery designs 2026", "swarnika.in › journal", "Bridal Jewellery Trends 2026: Emerald, Temple Gold & Polki", "The looks brides are choosing this season, with prices and styling tips.", "Swarnika Jewellers", "design-jewellery-ad", "41.3k", "1,520", [["pinterest.com › bridal", "Bridal jewellery ideas", "Explore 10k+ pins."], ["vogue.in › weddings", "Wedding jewellery guide", "Editor's picks."]]),
]): add('seo', i + 8, acc=acc, q=q, site=site, title=title, desc=desc, brand=brand, img=im, traffic=tr, leads=ld, serp=serp)

# ---------- Email + WhatsApp ----------
for i, (acc, brand, aud, camp, kpi, bars, im, head, line, btn, wa, rep) in enumerate([
 ("#b45309", "The Grand Saffron", "4,960 past guests", "Winter stay offer — Dec", [["51.4%", "Open rate"], ["10.8%", "Click rate"], ["4,960", "Sent"], ["₹6.1L", "Bookings"]], [24, 31, 45, 52, 58, 66, 73, 81, 88, 95], "comm-v06", "Winter at the palace", "Stay 3 nights, pay for 2. Rooftop dinner included.", "Book your stay", "Winter at The Grand Saffron 👑 Stay 3 nights, pay for 2 — till 20 Dec.", "Is the rooftop dinner veg friendly?"),
 ("#dc2626", "Iron Forge Gym", "2,340 members", "New Year transformation", [["47.9%", "Open rate"], ["15.2%", "Click rate"], ["2,340", "Sent"], ["186", "Renewals"]], [30, 36, 44, 49, 63, 70, 74, 85, 90, 96], "comm-v07", "12-week transformation", "Coach-led plan + diet chart. Starts 1 Jan.", "Reserve my spot", "💪 12-week transformation starts 1 Jan. Only 40 spots with Coach Meera.", "Count me in!"),
 ("#16a34a", "Nectar Valley", "7,800 subscribers", "Detox week — subscribers", [["53.6%", "Open rate"], ["16.4%", "Click rate"], ["7,800", "Sent"], ["₹2.3L", "Sales"]], [21, 34, 39, 48, 57, 64, 71, 79, 87, 94], "pack-m3", "7-day detox week", "Seven cold-pressed blends, delivered every morning.", "Start detox", "🍊 7-day detox week is here. Fresh juice at your door every morning.", "Can I pause on Sunday?"),
]): add('mkt', i + 8, acc=acc, brand=brand, aud=aud, camp=camp, kpi=kpi, bars=bars, img=im, head=head, line=line, btn=btn, wa=wa, reply=rep)

# ---------- Online courses ----------
for i, (acc, brand, slug, im, cap, title, by, n, stu, rate, les, done) in enumerate([
 ("#dc2626", "Forge Academy", "forgeacademy", "comm-v07", "Keep your back neutral", "Become a Certified Fitness Coach", "by Coach Meera · 8 hrs", "28", "1,940", "4.9", ["Anatomy basics", "Program design", "Nutrition 101", "Coaching clients", "Online coaching", "Exam & certificate"], 3),
 ("#0f766e", "Derma Learn", "dermalearn", "comm-v03", "Always patch-test first", "Skin Care Business for Beauticians", "by Dr. Priya Nair · 6 hrs", "22", "2,760", "4.8", ["Skin types", "Facial protocols", "Products & safety", "Pricing services", "Instagram for salons", "First 50 clients"], 2),
 ("#b45309", "Hospitality School", "hospitalityschool", "comm-v06", "Greet every guest by name", "Hotel Front-Office Training", "by Rahul Desai · 5 hrs", "18", "3,410", "4.7", ["Grooming & etiquette", "Check-in flow", "Handling complaints", "Upselling rooms", "Billing software", "Mock interview"], 4),
]): add('course', i + 7, acc=acc, brand=brand, slug=slug, img=im, cap=cap, title=title, by=by, n=n, stu=stu, rate=rate, lessons=les, done=done)

json.dump(D, open('data3.json', 'w'), ensure_ascii=False)
print(len(D))
