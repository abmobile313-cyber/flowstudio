import json
D = []
def add(kind, i, **k): D.append(dict(id=f'{kind}-u{i:02d}', kind=kind, **k))

for i, a in enumerate([
 dict(acc="#0891b2", bg2="#ecfeff", brand="Pulse", tagline="Audio gadget store app", desc="Shop, pair and update your earbuds", hello="Hey Riya 🎧", h1="Your devices",
      chips=["Earbuds", "Speakers", "Cases"], items=[["aiphoto-c05", "Pulse Air Pro", "₹6,499", "ANC · 36 hr battery"], ["aiphoto-c05", "Pulse Lite", "₹2,999", "24 hr battery"]],
      detail="Active noise cancelling, spatial audio and a 10-minute fast charge.", opts=["White", "Black", "Mint"], cta="Buy now · ₹6,499", t3="Pulse Air Pro", t3s="Connected · Battery 82%",
      track=[["Noise cancelling", "On"], ["Firmware 3.2", "Updated"], ["Find my earbuds", "Ready"], ["Warranty", "Till Nov 2027"]], foot=["Battery", "82%"]),
 dict(acc="#16a34a", bg2="#f0fdf4", brand="ScentKart", tagline="Perfume shop app", desc="Find your scent, try samples, reorder", hello="Hi Arjun ✨", h1="Picked for you",
      chips=["Oud", "Fresh", "Car scents"], items=[["ugc-c08", "Car Diffuser", "₹499", "Lasts 45 days"], ["aiphoto-c02", "Noir Attar", "₹899", "12 ml · roll-on"]],
      detail="A clean woody scent for your car. Clips on the vent, lasts 45 days.", opts=["Woody", "Fresh", "Floral"], cta="Add to cart · ₹499", t3="Your order", t3s="Arriving tomorrow",
      track=[["Order placed", "Mon 6:10 PM"], ["Packed", "Tue 9 AM"], ["Shipped", "Tue 2 PM"], ["Delivery", "Wed by 7 PM"]], foot=["Free samples", "2 added"]),
]): add('app', i + 20, **a)

for i, c in enumerate([
 dict(acc="#7c3aed", brand="StayDesk", shop="Reception · StayEase", app="StayEase · Guest", tabs=["Rooms", "Check-in", "Service", "Billing"], cols=["Room", "Guest", "Status", "Request"],
      items=[["101", "Ms. Rao", "Checked in", "Towels"], ["204", "Mr. Shah", "Arriving", "Early check-in"], ["305", "Mr. Khan", "Checked in", "Room service"], ["402", "Mrs. Iyer", "Cleaning", "—"]],
      side="Tonight", tot=[["Occupied", "28 / 32"], ["Requests", "6"]], grand="88% full", btn="Assign to staff", toast="Room 305 order sent to kitchen", feed=[["Room service on the way", "Room 305 · 15 min"], ["Digital key ready", "Tap to unlock"], ["Late checkout", "Approved till 1 PM"]]),
 dict(acc="#ea580c", brand="StoreSync", shop="Billing · Stryde Store", app="Stryde · Owner", tabs=["Billing", "Stock", "Online orders", "Reports"], cols=["Item", "Size", "Qty", "Amount"],
      items=[["Run 3", "UK 9", "1", "₹4,299"], ["Trail", "UK 8", "1", "₹4,799"], ["Running socks (3)", "M", "2", "₹798"], ["Water bottle", "—", "1", "₹599"]],
      side="Bill #ST-4120", tot=[["Discount", "₹500"], ["GST", "included"]], grand="₹9,995", btn="Bill + WhatsApp receipt", toast="Sale synced to owner's phone", feed=[["Sale ₹9,995", "Pune store · now"], ["Online order #8812", "Ship today"], ["Low stock: Run 3 UK 9", "4 left"]]),
]): add('combo', i + 20, **c)

for i, (acc, brand, chat, flow, stats) in enumerate([
 ("#25d366", "StayEase Hotel", [["u", "Can I check in early tomorrow?"], ["b", "Hi 👋 What time do you arrive?", ["9 AM", "11 AM", "1 PM"]], ["u", "11 AM"], ["b", "Early check-in at 11 AM is ₹800. Shall I add it?", ["Yes, add", "No thanks"]], ["u", "Yes, add"], ["b", "✅ Done! Your room will be ready at 11 AM. Digital key comes here 30 min before."]],
  [["💬", "Guest messages"], ["🏨", "Bot checks the room"], ["💳", "Adds paid extras"], ["🔑", "Sends digital key"], ["⭐", "Asks for a review"]], [["0", "calls to reception"], ["₹1.8L", "extras sold / month"], ["24/7", "replies"]]),
 ("#25d366", "Pulse Audio", [["u", "My left earbud isn't connecting"], ["b", "Sorry about that 🎧 Let's fix it. Which model?", ["Air Pro", "Lite"]], ["u", "Air Pro"], ["b", "Put both in the case, hold the button 10 sec till the light blinks white. Done?", ["Fixed ✅", "Still not working"]], ["u", "Fixed ✅"], ["b", "Great! 🎉 Your warranty is active till Nov 2027 if you ever need us."]],
  [["💬", "Customer reports issue"], ["🛠", "Bot runs a fix guide"], ["📦", "Books a replacement"], ["🧾", "Checks warranty"], ["😊", "Closes the ticket"]], [["72%", "solved by bot"], ["3 min", "average fix"], ["4.7★", "support rating"]]),
]): add('chatbot', i + 16, acc=acc, brand=brand, chat=chat, flow=flow, stats=stats)

json.dump(D, open('data8.json', 'w'), ensure_ascii=False)
print(len(D))
