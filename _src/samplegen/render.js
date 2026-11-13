const {chromium}=require('playwright');const fs=require('fs');const {spawn}=require('child_process');
(async()=>{const [dir,out,fps,dur,only]=[process.argv[2],process.argv[3],+(process.argv[4]||25),+(process.argv[5]||5),process.argv[6]];
fs.mkdirSync(out,{recursive:true});const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:720}});
for(const f of fs.readdirSync(dir).filter(x=>x.endsWith('.html')&&(!only||x.startsWith(only)))){
 const id=f.replace('.html','');await p.goto('file://'+dir+'/'+f);await p.evaluate(()=>document.fonts.ready);
 await p.evaluate(()=>Promise.all([...document.images].map(i=>i.complete?1:new Promise(r=>{i.onload=i.onerror=r}))));
 const ff=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-framerate',String(fps),'-i','-','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart',out+'/'+id+'.raw.mp4']);
 const n=Math.round(fps*dur);
 for(let i=0;i<n;i++){const t=i/fps*1000;await p.evaluate(t=>{document.getAnimations().forEach(a=>{a.pause();a.currentTime=t})},t);
  const buf=await p.screenshot({type:'jpeg',quality:92});ff.stdin.write(buf);}
 ff.stdin.end();await new Promise(r=>ff.on('close',r));console.log('done',id);}
await b.close();})();
