const assert=require('node:assert/strict');const fs=require('node:fs');const vm=require('node:vm');const path=require('node:path');
const ids=['status','controls','reveal','listen-a','listen-b','mapping','choice','source-info','ready-pair','missing-pair','answer-a','answer-b','answer-unsure'];
const elements=Object.fromEntries(ids.map(id=>[id,{id,hidden:false,disabled:false,textContent:'',className:'',events:{},addEventListener(n,f){this.events[n]=f}}]));
class FakeAudio { constructor(src){this.src=src} play(){return Promise.resolve()} pause(){} }
const ctx=vm.createContext({document:{getElementById:id=>elements[id]},Audio:FakeAudio,Math,console});
for(const f of ['data.js','engine.js','app.js'])vm.runInContext(fs.readFileSync(path.join(__dirname,f),'utf8'),ctx,{filename:f});
(async()=>{
 assert.equal(elements.controls.hidden,false);
 elements['answer-a'].events.click();assert.match(elements.status.textContent,/Listen to both/);
 elements['missing-pair'].events.click();assert.equal(elements.controls.hidden,true);assert.match(elements.status.textContent,/mic: missing/);
 elements['ready-pair'].events.click();elements['listen-a'].events.click();elements['listen-b'].events.click();
 await Promise.resolve();await Promise.resolve();
 elements['answer-unsure'].events.click();assert.equal(elements.reveal.hidden,false);assert.match(elements.mapping.textContent,/synthetic tones/);assert.match(elements.status.textContent,/not evidence/);
 console.log('PASS: simulated UI state transition, early answer blocked, missing metadata blocked, reveal after both play promises');
})().catch(e=>{console.error(e);process.exitCode=1});
