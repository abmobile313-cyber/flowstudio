import json
from data13_specs import B
D = []
ctr = dict(seo=26, mkt=23, chatbot=27, deck=26, dash=24, course=25, pc=19, shop=21, aiauto=30, combo=31, voice=24, music=25, pb=27, app=31, web=21)
def add(kind, **k):
    ctr[kind] += 1; D.append(dict(id=f'{kind}-u{ctr[kind]:02d}', kind=kind, **k))
for n, b in enumerate(B):
    P = f'aiphoto-c{18+n}'; U = f'ugc-c{24+n}'; a = b['acc']
    add('shop', acc=a, brand=b['up'], dom=b['dom'], soft=b['soft'], menu=b['menu'], badge="Best sellers", h=b['h1'], sub=b['sub'], hero=P, prods=[[P if i % 2 == 0 else U] + p for i, p in enumerate(b['prods'])])
    add('web', acc=a, brand=b['up'], dom=b['dom'], menu=b['menu'][:3], hero=P, badge=b['tag'].split(',')[0][:28], h1=b['h1'], p=b['sub'], cta=b['cta'], feats=b['feats'], gal=[P, U, P])
    add('seo', acc=a, q=b['q'], site=f"{b['dom']} › guides", title=b['st'], desc=b['sd'], brand=b['n'], img=P, traffic=["14.6k", "22.8k", "17.3k", "26.4k", "19.9k", "13.7k", "21.2k", "11.8k"][n], leads=["720", "1,060", "640", "910", "480", "700", "1,340", "820"][n], serp=b['serp'])
    add('dash', acc=a, brand=b['n'], slug=b['dom'].split('.')[0], nav=["Overview"] + b['menu'][:4], kpi=b['kpi'], line=[38 + i * 4 + (i % 3) for i in range(14)], dt="By channel", split=[48, 34, 15], tt="Top performers", rows=b['rows'], lt="This month")
    add('deck', acc=a, brand=b['n'], tag=b['tag'], img=P, prob=b['prob'], probp=b['probp'], facts=b['facts'], trac=b['trac'], growth=[["Q1", 58], ["Q2", 112], ["Q3", 172], ["Q4", 236]], ask=b['ask'], use=b['use'])
    add('chatbot', acc="#25d366", brand=b['n'], chat=b['chat'], flow=b['flow'], stats=b['stats'])
    c = b['course']; add('course', acc=a, brand=c[0], slug=c[1], img=P, cap=c[8], title=c[2], by=c[3], n=c[4], stu=c[5], rate=c[6], lessons=c[7], done=2)
    m = b['music']; add('music', acc=m[2], title=m[0], artist=m[1], img=U, desc=f"Lyric reel for {b['n']} with brand visuals and captions cut to the beat.", chips=["Lyric reel", "Brand visuals", "Beat sync", "Reels"], lines=m[3], stats=[["1.1M", "views"], ["+28k", "followers"]])
    pc = b['pc']; add('pc', acc=a, brand=pc['brand'], shop=pc['shop'], tabs=pc['tabs'], cols=pc['cols'], items=pc['items'], side=pc['side'], tot=pc['tot'] + [["Total", ""]][:0], grand=pc['grand'], btn=pc['btn'], toast=pc['toast'])
    add('combo', acc=a, brand=pc['brand'], shop=pc['shop'], app=f"{b['n']} · Owner", tabs=pc['tabs'], cols=pc['cols'], items=pc['items'], side=pc['side'], tot=pc['tot'], grand=pc['grand'], btn=pc['btn'], toast=pc['toast'], feed=pc['feed'])
    k = b['mkt']; add('mkt', acc=a, brand=b['n'], aud=k[0], camp=k[1], kpi=[["48.6%", "Open rate"], ["13.2%", "Click rate"], [k[0].split()[0], "Sent"], ["₹3.1L", "Sales"]], bars=[24, 31, 40, 48, 57, 63, 71, 80, 88, 95], img=P, head=k[2], line=k[3], btn=k[4], wa=k[5], reply=k[6])
    add('voice', acc=a, brand=f"{b['n']} ad", img=P, subs=b['voice'], langs=[["English", "Ready"], ["Urdu", "Ready"], ["French", "Ready"], ["Arabic", "Ready"]], tracks=[["Voice-over", a], ["Urdu dub", "#26c6da"], ["French dub", "#ab47bc"], ["Music", "#66bb6a"]])
    ap = b['app']; add('app', acc=a, bg2=b['soft'], brand=b['n'], tagline=ap['tagline'], desc=ap['desc'], hello=ap['hello'], h1=ap['h1'], chips=ap['chips'], items=[[P, b['prods'][0][0], b['prods'][0][1], b['tag'][:30]], [U, b['prods'][1][0], b['prods'][1][1], "Customer favourite"]], detail=ap['detail'], opts=ap['opts'], cta=f"Continue · {b['prods'][0][1]}", t3=ap['t3'], t3s=ap['t3s'], track=ap['track'], foot=ap['foot'])
    add('pb', acc=a, name=b['n'], role=b['tag'], handle=b['handle'], av=P, before=["1,200", "4,100", "2,600", "3,300", "900", "1,700", "5,200", "2,000"][n], after=["48.6k", "86.2k", "61.4k", "72.8k", "24.9k", "57.1k", "112k", "39.6k"][n], months="7", posts="186", fol="96", bio=f"✨ {b['tag'][:40]} 👇", grid=[P, U, P, U, P, U], did=["Creator reels every week", "Offer posts with WhatsApp links", "Reviews and stories daily"])
    add('aiauto', acc=a, brand=b['n'], prompt=f"{b['n']} posts + creator reviews", month="Monthly plan", posts=[[P, "Hero product post", "Scheduled 9 AM"], [U, "Creator review", "Scheduled 6 PM"], [P, "Offer of the week", "Scheduled 11 AM"], [U, "Customer story", "Scheduled 7 PM"]])
json.dump(D, open('data13.json', 'w'), ensure_ascii=False); print(len(D))
