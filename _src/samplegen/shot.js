const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:720}});
for(const f of process.argv.slice(3)){await p.goto('file://'+process.argv[2]+'/'+f+'.html');await p.waitForTimeout(300);await p.evaluate(()=>document.getAnimations().forEach(a=>{a.pause();a.currentTime=4500}));await p.screenshot({path:'/tmp/claude-0/-home-claude/b87108f0-499a-542f-82a0-30ba3fa58006/scratchpad/ui/'+f+'.png'});}
await b.close()})()
