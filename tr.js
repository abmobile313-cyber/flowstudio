/* Flow Studio auto-translate: English · हिन्दी · العربية
   Everything on screen (menus, buttons, messages, chats) is shown in the viewer's language.
   Uses Google's free translate endpoint from the browser; results are cached on the device. */
(function () {
  const LG = { en: "English", hi: "हिन्दी", ar: "العربية" }, SH = { en: "EN", hi: "हिं", ar: "عر" };
  let LANG = "en";
  try { LANG = localStorage.getItem("fs-lang") || ""; } catch (e) {}
  if (!LG[LANG]) { const n = (navigator.language || "en").toLowerCase(); LANG = n.startsWith("ar") ? "ar" : n.startsWith("hi") ? "hi" : "en"; }
  const ORIG = new WeakMap(), SKIP = "script,style,textarea,input,select,option,code,pre,svg,.mono,[data-notr],.idc,.oc,.paper,.pvw,#clock,.trp,.brand,.fdr,.cav,.cmh,.bc,.tid,.bct,[contenteditable]";
  const MSGSEL = ".msg,.cm,.chat,.tk,.np .it,.tcp,.toast";
  let cache = {};
  const ck = () => "fs-tr-" + LANG;
  const loadC = () => { try { cache = JSON.parse(localStorage.getItem(ck()) || "{}"); } catch (e) { cache = {}; } };
  let saveT = 0; const saveC = () => { clearTimeout(saveT); saveT = setTimeout(() => { try { const k = Object.keys(cache); if (k.length > 6000) k.slice(0, k.length - 5000).forEach(x => delete cache[x]); localStorage.setItem(ck(), JSON.stringify(cache)); } catch (e) {} }, 800); };
  loadC();
  const worth = s => { const t = s.trim(); if (t.length < 2 || !/\p{L}{2}/u.test(t)) return false; if (/^(FS-|P\d{6}-|T\d{6}-|G\d{6}-)[\w-]*$/i.test(t)) return false; if (/^[\w.+-]+@[\w-]+\.[\w.]+$/.test(t) || /^https?:\/\//.test(t) || /^[\w-]+\.(com|in|agency|app)$/i.test(t)) return false; return true; };
  const asciiOnly = s => !/[\u0600-\u06FF\u0750-\u077F\u0900-\u0DFF\u0E00-\u0FFF\u3040-\u30FF\u4E00-\u9FFF\uAC00-\uD7AF\u0400-\u04FF]/.test(s);
  function need(node) {
    const p = node.parentElement; if (!p || p.closest(SKIP)) return false;
    const o = ORIG.has(node) ? ORIG.get(node) : node.nodeValue; if (!worth(o)) return false;
    if (LANG === "en") return !asciiOnly(o) || !!p.closest(MSGSEL);
    return true;
  }
  let queue = new Set(), busy = false, timer = 0;
  function walk(root) {
    if (!root) return;
    if (root.nodeType === 3) { visit(root); return; }
    if (root.nodeType !== 1 || root.closest && root.closest(SKIP)) return;
    const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT); let n; while ((n = w.nextNode())) visit(n);
    if (LANG !== "en") root.querySelectorAll && [root, ...root.querySelectorAll("[placeholder],[title],[aria-label]")].forEach(el => { if (!el.getAttribute || el.closest(SKIP + ",.trp") && el.tagName !== "INPUT" && el.tagName !== "TEXTAREA") return; ["placeholder", "title"].forEach(a => { const v = el.getAttribute(a); if (!v) return; const ok = el.getAttribute("data-o-" + a) || v; if (!el.hasAttribute("data-o-" + a)) el.setAttribute("data-o-" + a, v); if (!worth(ok)) return; if (cache[ok] != null) { if (el.getAttribute(a) !== cache[ok]) el.setAttribute(a, cache[ok]); } else queue.add(ok); }); });
  }
  function visit(n) {
    if (!need(n)) return; const o = ORIG.has(n) ? ORIG.get(n) : n.nodeValue; const key = o.trim();
    if (cache[key] != null) apply(n, o, cache[key]); else { if (!ORIG.has(n)) ORIG.set(n, o); queue.add(key); pend.push(n); }
  }
  let pend = [];
  function apply(n, o, tr) {
    if (!ORIG.has(n)) ORIG.set(n, o);
    const lead = o.match(/^\s*/)[0], trail = o.match(/\s*$/)[0], v = lead + tr + trail;
    if (n.nodeValue !== v) { n.nodeValue = v; const p = n.parentElement; if (p && p.closest(MSGSEL) && tr !== o.trim()) p.title = "Original: " + o.trim(); }
  }
  async function flush() {
    if (busy || !queue.size) return; busy = true;
    const all = [...queue]; queue = new Set();
    try {
      for (let i = 0; i < all.length;) {
        const chunk = []; let len = 0;
        while (i < all.length && chunk.length < 40 && len + all[i].length < 4500) { chunk.push(all[i]); len += all[i].length; i++; }
        if (!chunk.length) { chunk.push(all[i].slice(0, 4500)); i++; }
        const b = new URLSearchParams(); chunk.forEach(q => b.append("q", q));
        const r = await fetch("https://translate.googleapis.com/translate_a/t?client=gtx&sl=auto&tl=" + LANG + "&dt=t", { method: "POST", body: b });
        if (!r.ok) throw new Error("tr " + r.status);
        const j = await r.json(); const arr = chunk.length === 1 && !Array.isArray(j[0]) && typeof j[0] === "string" ? [j[0]] : j;
        chunk.forEach((q, k) => { let t = arr[k]; if (Array.isArray(t)) t = t[0]; if (typeof t !== "string") t = q; cache[q] = t; });
      }
      saveC();
    } catch (e) { /* offline or limited: keep the original text */ }
    busy = false;
    const p = pend; pend = []; p.forEach(n => { if (!n.isConnected) return; const o = ORIG.get(n); if (o != null && cache[o.trim()] != null) apply(n, o, cache[o.trim()]); });
    document.querySelectorAll("[data-o-placeholder],[data-o-title]").forEach(el => ["placeholder", "title"].forEach(a => { const o = el.getAttribute("data-o-" + a); if (o && cache[o] != null) el.setAttribute(a, cache[o]); }));
    if (queue.size) schedule();
  }
  function schedule() { clearTimeout(timer); timer = setTimeout(flush, 120); }
  function restore() {
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n; while ((n = w.nextNode())) if (ORIG.has(n)) { n.nodeValue = ORIG.get(n); ORIG.delete(n); }
    document.querySelectorAll("[data-o-placeholder],[data-o-title]").forEach(el => ["placeholder", "title"].forEach(a => { const o = el.getAttribute("data-o-" + a); if (o) el.setAttribute(a, o); el.removeAttribute("data-o-" + a); }));
  }
  function setDir() { document.documentElement.lang = LANG; document.documentElement.classList.toggle("lang-ar", LANG === "ar"); }
  function run() { walk(document.body); schedule(); }
  function set(l) { if (!LG[l] || l === LANG) return; restore(); LANG = l; try { localStorage.setItem("fs-lang", l); } catch (e) {} loadC(); setDir(); paint(); run(); }
  /* language picker */
  const pickers = [];
  function picker(cls) {
    const w = document.createElement("div"); w.className = "trp " + (cls || ""); w.setAttribute("data-notr", "");
    w.innerHTML = `<button type="button" class="trb" aria-label="Language"><svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></svg><b></b></button><div class="trm" hidden>${Object.keys(LG).map(k => `<button type="button" data-lg="${k}">${LG[k]}</button>`).join("")}<small>Auto-translated · messages too</small></div>`;
    const m = w.querySelector(".trm");
    w.querySelector(".trb").onclick = e => { e.stopPropagation(); m.hidden = !m.hidden; };
    m.onclick = e => { const b = e.target.closest("[data-lg]"); if (!b) return; m.hidden = true; set(b.dataset.lg); };
    document.addEventListener("click", e => { if (!w.contains(e.target)) m.hidden = true; });
    pickers.push(w); paint(); return w;
  }
  function paint() { pickers.forEach(w => { w.querySelector(".trb b").textContent = SH[LANG]; w.querySelectorAll("[data-lg]").forEach(b => b.classList.toggle("on", b.dataset.lg === LANG)); }); }
  const css = document.createElement("style");
  css.textContent = `.trp{position:relative;flex:none;font-family:Inter,system-ui,sans-serif}.trb{display:inline-flex;align-items:center;gap:6px;height:38px;padding:0 12px;border-radius:99px;border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.07);color:#fff;cursor:pointer;font:700 13px Inter,system-ui,sans-serif}.trb:hover{background:rgba(255,255,255,.14)}
.trm{position:absolute;right:0;top:calc(100% + 8px);z-index:200;min-width:190px;padding:8px;border-radius:16px;background:rgba(14,12,28,.97);border:1px solid rgba(255,255,255,.16);box-shadow:0 20px 50px rgba(0,0,0,.55);display:grid;gap:4px}.trm[hidden]{display:none}.trm button{text-align:left;padding:10px 12px;border-radius:10px;border:0;background:none;color:#e9e7f5;cursor:pointer;font:600 15px Inter,system-ui,sans-serif}.trm button:hover{background:rgba(255,255,255,.08)}.trm button.on{background:linear-gradient(135deg,#4f7cff,#a64dff);color:#fff}.trm small{color:#9a97b0;font-size:11px;padding:4px 8px 2px}
.trp.fixed{position:fixed;top:calc(14px + env(safe-area-inset-top,0px));right:max(16px,env(safe-area-inset-right,0px));z-index:120}
html.lang-ar #view,html.lang-ar .lg .l,html.lang-ar main section p,html.lang-ar .chat,html.lang-ar .tcm{direction:rtl;text-align:right}`;
  document.head.appendChild(css);
  setDir();
  const mo = new MutationObserver(ms => { let any = false; for (const m of ms) for (const n of m.addedNodes) { if (n.nodeType === 1 || n.nodeType === 3) { walk(n); any = true; } } if (any) schedule(); });
  const start = () => { mo.observe(document.body, { childList: true, subtree: true }); run(); };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
  window.FSTR = { picker, set, get lang() { return LANG; } };
})();
