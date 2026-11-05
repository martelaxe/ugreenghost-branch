(() => {
  const $=id=>document.getElementById(id);
  let trial=null, audio=null, heard=[false,false];
  const status=$('status'), controls=$('controls'), reveal=$('reveal');
  function stopAudio(){if(audio){audio.pause();audio.currentTime=0;audio=null;}}
  function load(which){
    stopAudio(); heard=[false,false]; reveal.hidden=true; controls.hidden=true;
    $('listen-a').disabled=true; $('listen-b').disabled=true;
    const keys=FIXTURE.pairs[which], pair=keys.map(k=>FIXTURE.samples[k]);
    trial=makeTrial(pair,Math.random()<0.5);
    if (trial.state==='blocked') {
      status.className='status blocked';
      status.textContent='Comparison blocked: '+trial.issues.join('; ')+'. Ask for the missing capture details. This is not proof the recordings differ.';
      return;
    }
    status.className='status ready';
    status.textContent='Required fixture fields match. This alone does not establish a controlled experiment; weather, recording quality and other factors remain unchecked.';
    controls.hidden=false;
    $('listen-a').disabled=false; $('listen-b').disabled=false;
  }
  function play(i){
    stopAudio();
    audio=new Audio(trial.items[i].path);
    audio.play().then(()=>{heard[i]=true;status.textContent=`Playing recording ${i===0?'1':'2'}. Choose only after listening to both.`;}).catch(()=>{status.textContent='Playback failed. No listening result was recorded.';});
  }
  function answer(choice){
    if (!heard[0] || !heard[1]) {status.className='status blocked';status.textContent='Listen to both recordings before revealing the mapping.';return;}
    const result=decide(trial,choice);stopAudio();
    const [a,b]=result.items;
    const label = s=>`Recording ${s.id}: ${s.calls} synthetic tones; ${s.notes}`;
    $('mapping').textContent=`1 → ${label(a)}  |  2 → ${label(b)}`;
    $('choice').textContent=choice==='unsure'?'You chose: unsure.':`You chose recording ${choice+1}.`;
    $('source-info').textContent=`Fixture sources: ${a.path} and ${b.path}. The matching settings are author-supplied. Four tones vs two is fixture ground truth, not a wildlife observation.`;
    controls.hidden=true;reveal.hidden=false;status.className='status ready';status.textContent='Reveal complete. One response is not evidence of a trend, ecological change or causation.';
  }
  $('ready-pair').addEventListener('click',()=>load('ready'));
  $('missing-pair').addEventListener('click',()=>load('incomplete'));
  $('listen-a').addEventListener('click',()=>play(0));
  $('listen-b').addEventListener('click',()=>play(1));
  $('answer-a').addEventListener('click',()=>answer(0));
  $('answer-b').addEventListener('click',()=>answer(1));
  $('answer-unsure').addEventListener('click',()=>answer('unsure'));
  load('ready');
})();
