/* Flow Studio app: installable, opens fast, works offline for pages already visited */
const C="fs-v30";
self.addEventListener("install",e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(["/","/logo.webp"])).catch(()=>{}));self.skipWaiting()});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))});
self.addEventListener("fetch",e=>{const r=e.request,u=new URL(r.url);if(r.method!=="GET"||u.origin!==location.origin)return;
  if(r.mode==="navigate"){const key=u.pathname;e.respondWith(fetch(r).then(res=>{const cp=res.clone();caches.open(C).then(c=>c.put(key,cp));return res}).catch(()=>caches.match(key).then(m=>m||caches.match("/"))));return}
  e.respondWith(caches.match(r).then(m=>m||fetch(r)))});
