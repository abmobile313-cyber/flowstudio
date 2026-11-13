import json
D = []
def add(kind, i, **k): D.append(dict(id=f'{kind}-u{i:02d}', kind=kind, **k))

for i, (acc, brand, dom, soft, menu, badge, h, sub, hero, prods) in enumerate([
 ("#0891b2", "PULSE", "pulseaudio.in", "#eaf4f6", ["Earbuds", "Speakers", "Cases", "Support"], "New · Air Pro", "Sound that moves with you", "Active noise cancelling, 36-hour battery, 10-minute fast charge.", "aiphoto-c05", [["aiphoto-c05", "Pulse Air Pro", "₹6,499", "₹7,999"], ["aiphoto-c05", "Pulse Lite", "₹2,999", "₹3,499"], ["aiphoto-c05", "Air Pro · Mint", "₹6,499", "₹7,999"], ["aiphoto-c05", "Charging Case", "₹1,199", "₹1,499"]]),
 ("#16a34a", "NECTAR VALLEY", "nectarvalley.in", "#eef6ee", ["Juices", "Subscriptions", "Gift packs", "Farms"], "Cold-pressed daily", "Fresh from the farm, every morning", "No sugar, no water added — delivered by 7 AM.", "aiphoto-c06", [["aiphoto-c06", "Orange Sunrise", "₹129", "₹149"], ["aiphoto-c06", "Green Detox", "₹149", "₹169"], ["ugc-c09", "Family Pack (6)", "₹699", "₹849"], ["aiphoto-c06", "Weekly Plan", "₹899", "₹1,050"]]),
]): add('shop', i + 11, acc=acc, brand=brand, dom=dom, soft=soft, menu=menu, badge=badge, h=h, sub=sub, hero=hero, prods=prods)

for i, (acc, q, site, title, desc, brand, im, tr, ld, serp) in enumerate([
 ("#0891b2", "best noise cancelling earbuds under 7000", "pulseaudio.in › guides", "Best Noise Cancelling Earbuds Under ₹7,000 (2026 Guide)", "ANC, battery and call quality tested — what really matters before you buy.", "Pulse Audio", "aiphoto-c05", "27.4k", "1,060", [["amazon.in › earbuds", "True wireless earbuds", "Free delivery."], ["gadgets360.com › reviews", "Best TWS earbuds", "Expert reviews."]]),
 ("#7c3aed", "boutique hotel near pune airport", "stayease.in › pune", "Boutique Hotels Near Pune Airport: Early Check-in & Free Pickup", "Rooms 10 minutes from the airport, with digital keys and late checkout.", "StayEase Hotels", "brand-c04", "15.8k", "690", [["booking.com › pune", "Hotels in Pune", "Compare prices."], ["tripadvisor.in › pune", "Pune hotels", "Traveller reviews."]]),
]): add('seo', i + 16, acc=acc, q=q, site=site, title=title, desc=desc, brand=brand, img=im, traffic=tr, leads=ld, serp=serp)

for i, (acc, title, artist, im, desc, chips, lines, stats) in enumerate([
 ("#38bdf8", "Volume Up", "Kabir & The Line", "aiphoto-c05", "Tech-ad style lyric reel with sharp captions cut to every bass hit.", ["Electronic", "Bass sync", "Tech visuals", "Ads ready"], ["Turn the <span>world</span> down", "Turn the <span>beat</span> up", "Only us in the <span>sound</span>", "Volume, volume <span>up</span>"], [["1.4M", "views"], ["+39k", "followers"]]),
 ("#f59e0b", "Subah", "Meher · acoustic", "aiphoto-c06", "Warm morning lyric reel with sunlit kitchen visuals and soft Hindi-English captions.", ["Acoustic", "Morning mood", "Soft type", "Reels"], ["Pehli <span>kiran</span>", "Fresh new <span>day</span>", "Ghar ki <span>khushboo</span>", "Subah, <span>meri</span> subah"], [["860k", "views"], ["+22k", "listeners"]]),
]): add('music', i + 15, acc=acc, title=title, artist=artist, img=im, desc=desc, chips=chips, lines=lines, stats=stats)

json.dump(D, open('data9.json', 'w'), ensure_ascii=False)
print(len(D))
