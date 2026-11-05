#!/usr/bin/env python3
"""Retry only first-round technical read failures, using normal Codex sandbox."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import tempfile,hashlib,json,shutil,subprocess,os,time,datetime,stat
root=Path(__file__).resolve().parents[1];project=root.parents[1]
manifest=json.loads((root/'execution/source-manifest.json').read_text());pre=json.loads((root/'execution/preregistration.json').read_text())
for name,digest in pre['hashes'].items():
 if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest: raise RuntimeError('Changed pre-registration: '+name)
cells=[('archive-a','g'),('archive-b','g'),('archive-c','g'),('archive-a','s'),('archive-b','s'),('archive-c','s')]
ids=[(a,w,n) for n in (1,2) for a,w in (cells if n==1 else list(reversed(cells)))]
# Confirm all prior sessions failed to execute any evidence-reading command.
for a,w,n in ids:
 tag=f'{a}-{w}{n}'; events=[json.loads(s) for s in (root/'execution'/f'{tag}-events.jsonl').read_text().splitlines()]
 commands=[e['item'] for e in events if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='command_execution']
 if not commands or any(c.get('exit_code')==0 for c in commands):raise RuntimeError('Not a confirmed technical failure: '+tag)
base=Path(tempfile.mkdtemp(prefix='ugreen03-retry-',dir='/tmp')); tools=base/'sandbox-tools';tools.mkdir()
bwrap=tools/'bwrap';shutil.copyfile('/tmp/ugreen03-v8tnvnea/sandbox-tools/bwrap',bwrap);bwrap.chmod(0o755)
for archive,workflow,n in ids:
 tag=f'{archive}-{workflow}{n}';workspace=base/tag/'workspace';workspace.mkdir(parents=True)
 for name,hashes in manifest.items():
  orig=root/'datasets'/archive/name;dest=workspace/name
  if orig.is_symlink() or hashlib.sha256(orig.read_bytes()).hexdigest()!=hashes[archive]:raise RuntimeError('Invalid source '+str(orig))
  dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(orig,dest)
  if hashlib.sha256(dest.read_bytes()).hexdigest()!=hashes[archive]:raise RuntimeError('Invalid copied file '+str(dest))
 items=list(workspace.rglob('*'))
 if any(p.is_symlink() for p in items) or {str(p.relative_to(workspace)) for p in items if p.is_file()}!=set(manifest):raise RuntimeError('Invalid workspace')
prompts={'g':(root/'prompts/generic.txt').read_bytes(),'s':(root/'prompts/specialized.txt').read_bytes()}
env=os.environ.copy();env['PATH']=str(tools)+':'+env['PATH'];codex=shutil.which('codex');assert codex
# Protect the project and prior experiment temporary roots from investigator reads.
protected=[p for p in (project,Path('/tmp/ugreen03-v8tnvnea'),Path('/tmp/ugreen-blind-01-r0oqy1ev'),Path('/tmp/ugreen-opportunity-02-fttklbkb')) if p.is_dir()]
old_modes={str(p):stat.S_IMODE(p.stat().st_mode) for p in protected};changed=[]
def work(t):
 archive,workflow,n=t;tag=f'{archive}-{workflow}{n}';run=base/tag;workspace=run/'workspace';report=run/'last-message.md'
 args=[codex,'exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','--sandbox','read-only','-c','web_search="disabled"','--cd',str(workspace),'--output-last-message',str(report),'--json','-']
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.monotonic();out=run/'events.jsonl';err=run/'stderr.log'
 with out.open('wb') as stdout,err.open('wb') as stderr:
  try:
   proc=subprocess.run(args,input=prompts[workflow],stdout=stdout,stderr=stderr,env=env,cwd=workspace,timeout=600);code=proc.returncode;failure=None
  except subprocess.TimeoutExpired:code=None;failure='timeout after 600 seconds'
 end=datetime.datetime.now(datetime.timezone.utc).isoformat();duration=time.monotonic()-tick
 events=[]
 for line in out.read_text(errors='replace').splitlines():
  try:events.append(json.loads(line))
  except json.JSONDecodeError:pass
 cmds=[e['item'] for e in events if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='command_execution']
 items=list(workspace.rglob('*'))
 integrity=not any(p.is_symlink() for p in items) and {str(p.relative_to(workspace)) for p in items if p.is_file()}==set(manifest) and all(hashlib.sha256((workspace/name).read_bytes()).hexdigest()==h[archive] for name,h in manifest.items())
 info={'tag':tag,'archive':archive,'workflow':workflow,'replicate':n,'attempt':2,'started_utc':start,'ended_utc':end,'duration_seconds':round(duration,3),'exit_code':code,'technical_error':failure,'thread_id':next((e.get('thread_id') for e in events if e.get('type')=='thread.started'),None),'turn_completed':any(e.get('type')=='turn.completed' for e in events),'turn_failed':any(e.get('type') in ('turn.failed','error') for e in events),'successful_commands':sum(c.get('exit_code')==0 for c in cmds),'failed_commands':sum(c.get('exit_code')!=0 for c in cmds),'usage':next((e.get('usage') for e in events if e.get('type')=='turn.completed'),None),'output_present':report.exists() and report.stat().st_size>0,'workspace_integrity':'pass' if integrity else 'FAIL','model':'CLI default; identifier not in CLI JSON events','reasoning':'CLI default; not exposed in CLI JSON events','prompt_sha256':hashlib.sha256(prompts[workflow]).hexdigest(),'command':args}
 (run/'status.json').write_text(json.dumps(info,indent=2)+'\n')
 print(tag,'exit',code,'turn',info['turn_completed'],'successful commands',info['successful_commands'],'seconds',info['duration_seconds'],flush=True)
 return info
print('Prepared retry workspace:',base,'protecting paths:',len(protected),flush=True)
results=[]
try:
 for p in protected: p.chmod(0);changed.append(p)
 with ThreadPoolExecutor(max_workers=4) as ex:
  futures={ex.submit(work,t):t for t in ids}
  for f in as_completed(futures):
   try: results.append(f.result())
   except Exception as e:results.append({'tag':'-'.join(map(str,futures[f])),'technical_error':repr(e)});print('Launcher failure:',repr(e),flush=True)
finally:
 for p in reversed(changed):p.chmod(old_modes[str(p)])
print('Restored protected path permissions',flush=True)
for a,w,n in ids:
 tag=f'{a}-{w}{n}';run=base/tag
 for name,dest in [('events.jsonl',root/'execution'/f'{tag}-retry-events.jsonl'),('stderr.log',root/'execution'/f'{tag}-retry-stderr.log'),('status.json',root/'execution'/f'{tag}-retry-status.json'),('last-message.md',root/'results'/f'{tag}-retry.md')]:
  if (run/name).exists():shutil.copyfile(run/name,dest)
(root/'execution/retry-status.json').write_text(json.dumps({'temporary_root':str(base),'protected_modes':old_modes,'restored':True,'results':sorted(results,key=lambda x:x['tag'])},indent=2)+'\n')
print('Retry attempts captured:',len(results),flush=True)
