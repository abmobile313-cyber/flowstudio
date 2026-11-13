import json
D = []
def add(kind, i, **k): D.append(dict(id=f'{kind}-u{i:02d}', kind=kind, **k))

# Mobile apps
A = [
 dict(acc="#e11d48", bg2="#fff5f5", brand="Saffron Table", tagline="Food delivery app", desc="Order, pay and track — Android & iOS", hello="Good evening, Sana 👋", h1="What are you craving?",
      chips=["Biryani", "Kebabs", "Desserts"], items=[["ai-m4", "Smash Burger", "₹249", "Grill House · 25 min"], ["aiads-m6", "Belgian Choco Cone", "₹129", "Scoops · 15 min"]],
      detail="Double patty, cheddar, caramelised onion, house sauce.", opts=["Regular", "Large", "+ Fries"], cta="Add to cart · ₹249", t3="Order on the way", t3s="Arriving in 18 min",
      track=[["Order placed", "7:42 PM"], ["Being prepared", "7:44 PM"], ["Picked up by Imran", "7:58 PM"], ["Delivered", "Expected 8:16 PM"]], foot=["Paid by UPI", "₹249"]),
 dict(acc="#0f766e", bg2="#f2fbf9", brand="GlowCare", tagline="Skin-clinic booking app", desc="Book, consult and reorder in one place", hello="Hi Ayesha 🌿", h1="Your skin plan",
      chips=["Facials", "Laser", "Products"], items=[["comm-v03", "HydraGlow Facial", "₹2,499", "60 min · Dr. Nair"], ["aiphoto-m1", "Curry Leaf Serum", "₹899", "Free delivery"]],
      detail="Deep cleanse, hydration and LED therapy for dull skin.", opts=["Sat 11 AM", "Sat 4 PM", "Sun 12 PM"], cta="Book slot · ₹2,499", t3="Your appointments", t3s="Next visit in 2 days",
      track=[["Consultation", "Done · 2 Nov"], ["Facial session 1", "Done · 9 Nov"], ["Facial session 2", "Sat 16 Nov, 11 AM"], ["Review & products", "After session 3"]], foot=["Reminder on", "ON"]),
 dict(acc="#2563eb", bg2="#f3f6ff", brand="FitForge", tagline="Gym & coaching app", desc="Plans, check-ins and progress for members", hello="Morning, Vikram 💪", h1="Today's workout",
      chips=["Strength", "HIIT", "Yoga"], items=[["comm-v07", "Upper Body Power", "45 min", "Coach Meera · 6 exercises"], ["comm-v02", "Protein Shake", "₹180", "Order at counter"]],
      detail="Bench press, rows, shoulder press and core finisher.", opts=["Beginner", "Intermediate", "Pro"], cta="Start workout", t3="Your progress", t3s="Week 6 of 12",
      track=[["Weight", "82 → 76 kg"], ["Bench press", "60 → 80 kg"], ["Attendance", "22 of 24 days"], ["Next check-in", "Monday"]], foot=["Streak", "18 days"]),
 dict(acc="#b8860b", bg2="#fbf8f2", brand="Maison Ilyaa", tagline="Luxury perfume store app", desc="Shop, gift and reorder in two taps", hello="Welcome back ✨", h1="Find your signature",
      chips=["Oud", "Floral", "Fresh"], items=[["aiads-m1", "Navrasa EDP", "₹2,490", "Saffron · rose · oud"], ["ai-product-noir-dune", "Noir Dune EDP", "₹3,190", "Amber · vetiver"]],
      detail="A warm saffron and rose blend that lasts past midnight.", opts=["50 ml", "100 ml", "Gift box"], cta="Add to bag · ₹2,490", t3="Your order", t3s="Arriving Thursday",
      track=[["Order confirmed", "Mon 10:12 AM"], ["Packed in gift box", "Mon 4:30 PM"], ["Shipped · Blue Dart", "Tue 9:05 AM"], ["Out for delivery", "Thursday"]], foot=["Gift note added", "✓"]),
 dict(acc="#7c3aed", bg2="#f7f3ff", brand="StayEase", tagline="Hotel booking app", desc="Rooms, add-ons and check-in on the phone", hello="Plan your weekend 🌄", h1="Stays near you",
      chips=["Resorts", "Villas", "City"], items=[["camera-4", "Hilltop Resort", "₹6,800", "Lonavala · pool view"], ["comm-v06", "The Grand Saffron", "₹9,400", "Jaipur · heritage suite"]],
      detail="Infinity pool, valley-view rooms and breakfast included.", opts=["1 night", "2 nights", "+ Spa"], cta="Book · ₹6,800 / night", t3="Your trip", t3s="Check-in in 3 days",
      track=[["Booking confirmed", "#HT-88213"], ["Payment received", "₹13,600"], ["Online check-in", "Opens 24 hrs before"], ["Room ready", "Sat, 2 PM"]], foot=["Free cancellation", "till Thu"]),
]
for i, a in enumerate(A): add('app', i + 7, **a)

# Websites
W = [
 dict(acc="#c2410c", brand="SAFFRON TABLE", dom="saffrontable.in", menu=["Menu", "Catering", "Locations"], hero="ai-m4", badge="Now delivering", h1="Fire-grilled, made fresh.", p="Order online in 60 seconds. Fresh food at your door in 30 minutes.", cta="Order now",
      feats=[["🔥", "Charcoal grill", "Every order made fresh"], ["🛵", "30-min delivery", "Live tracking"], ["💳", "Pay your way", "UPI, cards, cash"]], gal=["ai-m4", "aiads-m6", "aiads-m3"]),
 dict(acc="#b8860b", brand="MAISON ILYAA", dom="maisonilyaa.com", menu=["Perfumes", "Gifts", "Story"], hero="ai-product-noir-dune", badge="New · Noir Dune", h1="Scents that stay till midnight.", p="Small-batch perfumes made with saffron, oud and Taif rose.", cta="Shop now",
      feats=[["✨", "12-hour wear", "Lab-tested longevity"], ["🎁", "Gift ready", "Free luxury box"], ["🌍", "Ships worldwide", "Insured delivery"]], gal=["aiads-m1", "pack-m2", "ai-m6"]),
 dict(acc="#0f766e", brand="GLOWCARE CLINIC", dom="glowcare.clinic", menu=["Treatments", "Doctors", "Results"], hero="comm-v03", badge="Dermatologist-led", h1="Healthy skin, real results.", p="Facials, laser and skin plans by certified doctors. Book online in a minute.", cta="Book a visit",
      feats=[["🩺", "Certified doctors", "10+ years experience"], ["📅", "Book online", "Pick your slot"], ["⭐", "4.9 rating", "2,300+ reviews"]], gal=["comm-v03", "edit-v04", "aiphoto-m1"]),
 dict(acc="#dc2626", brand="IRON FORGE", dom="ironforge.fit", menu=["Programs", "Coaches", "Pricing"], hero="comm-v07", badge="Free trial week", h1="Train hard. See results.", p="Strength, HIIT and coaching with a plan built for you.", cta="Join now",
      feats=[["🏋️", "Pro equipment", "Open 5 AM – 11 PM"], ["👥", "Expert coaches", "Personal plans"], ["📈", "Track progress", "In the app"]], gal=["comm-v07", "comm-v02", "edit-v03"]),
 dict(acc="#a16207", brand="THE GRAND SAFFRON", dom="grandsaffron.com", menu=["Rooms", "Dining", "Weddings"], hero="comm-v06", badge="Heritage luxury", h1="A palace stay in Jaipur.", p="Royal suites, rooftop dining and weddings planned to the last detail.", cta="Check availability",
      feats=[["👑", "Royal suites", "Private butler"], ["🍽", "Rooftop dining", "Rajasthani & global"], ["💍", "Weddings", "Up to 800 guests"]], gal=["comm-v06", "design-v05", "comm-v04"]),
]
for i, w in enumerate(W): add('web', i + 3, **w)

# Social media handling (business Instagram, zero to hero)
P = [
 dict(acc="#dc2626", name="Iron Forge Gym", role="Gym · Pune. We plan, shoot and post 20 reels a month.", handle="ironforge.fit", av="comm-v07", before="1,800", after="64.2k", months="6", posts="312", fol="210",
      bio="🏋️ Gym · Pune · Free trial week 👇", grid=["comm-v07", "comm-v02", "edit-v03", "edit-v02", "comm-v07", "comm-v02"], did=["20 reels a month", "Trend audio + captions", "Ads that bring walk-ins"]),
 dict(acc="#b8860b", name="Maison Ilyaa", role="Luxury perfume brand. Content plan, shoots and ads.", handle="maisonilyaa", av="aiads-m1", before="3,200", after="88.9k", months="8", posts="246", fol="150",
      bio="✨ Perfumes that stay till midnight · Shop 👇", grid=["aiads-m1", "ai-product-noir-dune", "pack-m2", "ai-m6", "comm-v08", "aiads-m1"], did=["Product films every week", "Influencer collabs", "Shop links on every post"]),
 dict(acc="#0f766e", name="GlowCare Clinic", role="Skin clinic. Doctor-led reels and patient stories.", handle="glowcare.clinic", av="comm-v03", before="950", after="41.7k", months="5", posts="188", fol="120",
      bio="🩺 Dermatologist-led skin care · Book 👇", grid=["comm-v03", "edit-v04", "aiphoto-m1", "comm-v03", "edit-v04", "aiphoto-m1"], did=["Doctor tips twice a week", "Before/after with consent", "Booking link + DM replies"]),
 dict(acc="#a16207", name="The Grand Saffron", role="Heritage hotel. Wedding and stay content that sells.", handle="thegrandsaffron", av="comm-v06", before="4,100", after="126k", months="9", posts="402", fol="98",
      bio="👑 Heritage luxury · Jaipur · Weddings & stays", grid=["comm-v06", "design-v05", "comm-v04", "comm-v06", "design-v05", "comm-v04"], did=["Cinematic room tours", "Wedding highlight reels", "Direct-booking campaigns"]),
]
for i, x in enumerate(P): add('pb', i + 8, **x)

json.dump(D, open('data2.json', 'w'), ensure_ascii=False)
print(len(D))
