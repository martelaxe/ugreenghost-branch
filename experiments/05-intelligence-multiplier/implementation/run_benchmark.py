#!/usr/bin/env python3
"""Research-only benchmark launcher. Temporarily restricts project access."""
from concurrent.futures import ThreadPoolExecutor,as_completed
from pathlib import Path
import datetime,hashlib,json,os,shutil,stat,subprocess,tempfile,time
import harness
R=Path(__file__).resolve().parents[1];PROJECT=R.parents[1]
pre=json.loads((R/'execution/preregistration.json').read_text());manifest=json.loads((R/'execution/source-manifest.json').read_text())
for name,h in pre['hashes'].items():
 if hashlib.sha256((R/name).read_bytes()).hexdigest()!=h:raise RuntimeError('Frozen file mismatch: '+name)
B=Path(tempfile.mkdtemp(prefix='ugreen05-benchmark-',dir='/tmp'));tools=B/'sandbox-tools';tools.mkdir()
bwrap=tools/'bwrap';shutil.copyfile('/tmp/ugreen-blind-01-r0oqy1ev/sandbox-tools/usr/bin/bwrap',bwrap);bwrap.chmod(0o755)
env=os.environ.copy();env['PATH']=str(tools)+':'+env['PATH']
prompts={'g':(R/'generic-prompt.md').read_bytes(),'p':(R/'specialized-prompt.md').read_bytes()}
cells=[(a,m) for m in ('g','p','h') for a in ('a','b','c')]
runs=[(a,m,n) for n in (1,2) for a,m in (cells if n==1 else list(reversed(cells)))]
for a,m,n in runs:
 tag=f'{a}-{m}{n}';ws=B/tag/'workspace';ws.mkdir(parents=True)
 for rel,hashes in manifest.items():
  src=R/'datasets'/a/rel;dest=ws/rel
  if src.is_symlink() or hashlib.sha256(src.read_bytes()).hexdigest()!=hashes[a]:raise ValueError('source mismatch')
  dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
  if hashlib.sha256(dest.read_bytes()).hexdigest()!=hashes[a]:raise ValueError('copy mismatch')
 items=list(ws.rglob('*'))
 if any(p.is_symlink() for p in items) or {str(p.relative_to(ws)) for p in items if p.is_file()}!=set(manifest):raise ValueError('workspace mismatch')
protected=[p for p in (PROJECT,Path('/tmp/ugreen-blind-01-r0oqy1ev'),Path('/tmp/ugreen-opportunity-02-fttklbkb'),Path('/tmp/ugreen03-v8tnvnea'),Path('/tmp/ugreen03-retry-kgbzpo7f')) if p.is_dir()]
modes={str(p):stat.S_IMODE(p.stat().st_mode) for p in protected};changed=[]
def run(t):
 a,m,n=t;tag=f'{a}-{m}{n}';run_dir=B/tag;ws=run_dir/'workspace';work=run_dir/'raw';work.mkdir()
 started=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.monotonic()
 if m=='h':
  res=harness.run(ws,work,env); outcome={'technical_ok':res['technical_ok'],'candidate_json_valid':res['candidate_json_valid'],'verifier_json_valid':res['verifier_json_valid'],'calls':[res['candidate_call']]+([res['verifier_call']] if res['verifier_call'] else []),'coverage':res['coverage'],'accepted_count':len(res['accepted']),'rejected_count':len(res['rejected'])}
 else:
  report=work/'report.md';events=work/'events.jsonl';err=work/'stderr.log';(work/'prompt.txt').write_bytes(prompts[m]);args=['codex','exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','--sandbox','read-only','-m','gpt-6-luna','-c','model_reasoning_effort="low"','-c','web_search="disabled"','--cd',str(ws),'--output-last-message',str(report),'--json','-']
  with events.open('wb') as out,err.open('wb') as se:
   try: proc=subprocess.run(args,input=prompts[m],stdout=out,stderr=se,cwd=ws,env=env,timeout=360);exit_code=proc.returncode;error=None
   except subprocess.TimeoutExpired:exit_code=None;error='timeout 360s'
  logs=[]
  for line in events.read_text(errors='replace').splitlines():
   try:logs.append(json.loads(line))
   except json.JSONDecodeError:pass
  cmds=[e['item'] for e in logs if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='command_execution']
  outcome={'technical_ok':exit_code==0 and any(x.get('type')=='turn.completed' for x in logs) and report.exists() and bool(report.read_text()) and any(c.get('exit_code')==0 for c in cmds),'calls':[{'exit_code':exit_code,'error':error,'thread_id':next((x.get('thread_id') for x in logs if x.get('type')=='thread.started'),None),'usage':next((x.get('usage') for x in logs if x.get('type')=='turn.completed'),None),'turn_completed':any(x.get('type')=='turn.completed' for x in logs),'successful_commands':sum(c.get('exit_code')==0 for c in cmds),'command':args}],'coverage':'model-selected; audit event logs for actual files'}
 items=list(ws.rglob('*'));integrity=not any(p.is_symlink() for p in items) and {str(p.relative_to(ws)) for p in items if p.is_file()}==set(manifest) and all(hashlib.sha256((ws/rel).read_bytes()).hexdigest()==h[a] for rel,h in manifest.items())
 outcome.update({'tag':tag,'archive':a,'method':m,'replicate':n,'started_utc':started,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'duration_seconds':round(time.monotonic()-tick,3),'workspace_integrity':integrity,'report_present':(work/'report.md').is_file(),'requested_model':'gpt-6-luna','requested_reasoning':'low','backend_identity_echoed':False})
 (run_dir/'status.json').write_text(json.dumps(outcome,indent=2)+'\n');print(tag,'technical',outcome['technical_ok'],'time',outcome['duration_seconds'],'calls',len(outcome['calls']),flush=True);return outcome
print('Prepared',len(runs),'workspaces at',B,flush=True);results=[]
try:
 for p in protected:p.chmod(0);changed.append(p)
 with ThreadPoolExecutor(max_workers=4) as ex:
  futures={ex.submit(run,t):t for t in runs}
  for f in as_completed(futures):
   try:results.append(f.result())
   except Exception as e:results.append({'tag':'-'.join(map(str,futures[f])),'technical_ok':False,'launcher_error':repr(e)});print('Launcher failure',futures[f],repr(e),flush=True)
finally:
 for p in reversed(changed):p.chmod(modes[str(p)])
print('Restored original directory permissions',flush=True)
for a,m,n in runs:
 tag=f'{a}-{m}{n}';run_dir=B/tag
 if (run_dir/'raw').exists():shutil.copytree(run_dir/'raw',R/'execution'/tag,dirs_exist_ok=False)
 if (run_dir/'status.json').exists():shutil.copyfile(run_dir/'status.json',R/'execution'/f'{tag}-status.json')
 if (run_dir/'raw/report.md').exists():shutil.copyfile(run_dir/'raw/report.md',R/'results'/f'{tag}.md')
(R/'execution/process-status.json').write_text(json.dumps({'temporary_root':str(B),'protected_original_modes':modes,'permissions_restored':True,'results':sorted(results,key=lambda x:x['tag'])},indent=2)+'\n')
print('Saved',len(results),'attempts',flush=True)
