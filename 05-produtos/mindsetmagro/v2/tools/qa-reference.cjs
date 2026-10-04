// Deterministic logic checks; deliberately NOT a visual/browser/Safari test.
const fs=require('fs'),vm=require('vm'),assert=require('assert'),path=require('path');
const out=process.argv[2],html=fs.readFileSync(path.join(out,'MINDSETmagro-2.0-Interativo.html'),'utf8');
const js=html.match(/<script>([\s\S]*)<\/script>/)[1];new vm.Script(js);
const nodes=new Map();class Element{constructor(tag){this.tag=tag;this.children=[];this.value='';this.hidden=false;this.checked=false}append(...xs){this.children.push(...xs)}replaceChildren(...xs){this.children=xs}setAttribute(){}addEventListener(name,fn){this[name]=fn}focus(){this.focused=true}click(){this.onclick?.()}get textContent(){return this._text||''}set textContent(t){this._text=t}}
const document={getElementById(id){if(!nodes.has(id))nodes.set(id,new Element('div'));return nodes.get(id)},createElement(tag){return new Element(tag)}};const storage=new Map(),context={document,console,Date,JSON,Object,Number,String,Array,Error,Math,Blob,URL,setTimeout,confirm:()=>true,window:{print(){}},Option:class{constructor(t,v){this.text=t;this.value=v}},localStorage:{getItem:k=>storage.get(k)||null,setItem:(k,v)=>storage.set(k,v),removeItem:k=>storage.delete(k)}};
vm.createContext(context);vm.runInContext(js,context);const ev=x=>vm.runInContext(x,context);const checks=[];function check(name,fn){fn();checks.push({name,result:'pass'})}
check('No persistence before consent',()=>assert.equal(storage.size,0));
check('Day 2 initially locked',()=>assert.equal(ev('unlocked(2)'),false));
check('Consent then first day render',()=>{ev('begin(true)');assert.equal(ev('started'),true)});
check('Time alone does not unlock',()=>{ev('state.opened[DAYS[0].id]=Date.now()-86401000');assert.equal(ev('unlocked(2)'),false)});
check('Completion plus 24h unlocks',()=>{ev('state.completed[DAYS[0].id]=Date.now()');assert.equal(ev('unlocked(2)'),true)});
check('Completion without interval stays locked',()=>{ev('state.opened[DAYS[0].id]=Date.now()');assert.equal(ev('unlocked(2)'),false)});
check('Known answers round trip',()=>assert.equal(ev("validState({...fresh(),answers:{[Object.keys(FIELDS)[0]]:'Minha prática'}}).answers[Object.keys(FIELDS)[0]]"),'Minha prática'));
check('Unknown fields rejected',()=>assert.throws(()=>ev("validState({...fresh(),answers:{unknown:'x'}})")));
check('Non-string answer rejected',()=>assert.throws(()=>ev("validState({...fresh(),answers:{[Object.keys(FIELDS)[0]]:{x:1}}})")));
check('Long answer rejected',()=>assert.throws(()=>ev("validState({...fresh(),answers:{[Object.keys(FIELDS)[0]]:'x'.repeat(20001)}})")));
check('Future timestamps rejected',()=>assert.throws(()=>ev('validState({...fresh(),opened:{[DAYS[0].id]:Date.now()+1000000}})')));
check('Storage survives resume',()=>{ev("state.answers[Object.keys(FIELDS)[0]]='Salvo';save();state=fresh();begin(true)");assert.equal(ev('state.answers[Object.keys(FIELDS)[0]]'),'Salvo')});
check('Notebook reuses fields',()=>{ev("view='notebook';render()");assert.ok(document.getElementById('content').children.length)});
check('Print uses existing answers',()=>{ev("$('printBtn').onclick()");assert.ok(document.getElementById('printOnly').children.length>1)});
check('Erase clears storage',()=>{ev("$('eraseBtn').onclick()");assert.equal(storage.size,0);assert.equal(ev('Object.keys(state.answers).length'),0)});
check('Mobile CSS controls present',()=>{assert.match(html,/font-size:16px/);assert.match(html,/min-height:44px/);assert.match(html,/max-width:360px/)});
const report={executed_at:new Date().toISOString(),method:'Node VM with minimal DOM harness; source code checks, not browser rendering',checks,not_tested:['Real browser layout 320px','iPhone','Safari','screen reader','Native file download/import chooser','Browser printing','Cross-user server isolation: separate app responsibility']};fs.writeFileSync(path.join(out,'reference-logic-qa.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
