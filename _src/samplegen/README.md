# Flow Studio sample generator

Samples on the site come from `const SAMPLES` in `_src/base.html` (rows: `[fold, "video"|"img", file-id, title, sub]`).
After editing SAMPLES run `python3 _src/gen.py` (rebuilds every page and samples.json). Never edit samples.json by hand.

## Quality rules (owner's standing rules)
- Must look like a premium professional studio: no cluttered desks, sticky notes, chai cups, crumbling walls, old-house rooms, village/"desi" looking sets. Rural subjects are fine only if the frame looks professional.
- Never use real famous brand names or logos. Use believable invented brands (Maison Ilyaa, Iron Forge, The Grand Saffron, Saffron Table, GlowCare, Hill Bean...).
- Every sample (poster jpg + mp4) carries the Flow Studio badge watermark (badge.png, bottom-right, 30% of width; 42% on portrait).
- Do not fill folders just for count. Each new sample must be visually checked before adding.
- Photoreal images only from ChatGPT (Meta AI if ChatGPT is at its limit); videos only from Meta AI. Coded UI films (engine.py) are fine for apps, websites, dashboards, software, chatbots, SEO, email, courses, automation.

## Tools
- `engine.py` + `render.js`: UI walkthrough films. Kinds: seo, mkt, chatbot, deck, dash, course, pc, shop, aiauto, combo, voice, music, pb, app, web. Examples of data: data.py, data2.py (ids `<kind>-uNN`, never reuse an id).
- `make.sh data.json`: build + watermark + copy into samples/.
- `shot.js dir id…`: quick PNG preview at 4.5 s for checking.
- `ba.py name=source …`: before/after colour-grade films from existing Meta AI clips (`grade-pNN`).
- `wm_all.py`: watermark pass (paths inside need adjusting).
