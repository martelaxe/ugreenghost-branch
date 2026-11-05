#!/usr/bin/env python3
"""Launch preregistered blind Codex runs; saves raw evidence outside workspaces."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import tempfile, hashlib, json, shutil, subprocess, os, time, datetime
root=Path(__file__).resolve().parents[1]
project=root.parents[1]
manifest=json.loads((root/'execution/source-manifest.json').read_text())
pre=json.loads((root/'execution/preregistration.json').read_text())
for name,digest in pre['hashes'].items():
 if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest: raise RuntimeError('Preregistration changed: '+name)
base=Path(tempfile.mkdtemp(prefix='ugreen03-',dir='/tmp'))
bwrap=base/'sandbox-tools'/'bwrap';bwrap.parent.mkdir()
shutil.copyfile('/tmp/ugreen-blind-01-r0oqy1ev/sandbox-tools/usr/bin/bwrap',bwrap);bwrap.chmod(0o755)
cells=[('archive-a','g'),('archive-b','g'),('archive-c','g'),('archive-a','s'),('archive-b','s'),('archive-c','s')]
ids=[(a,w,n) for n in (1,2) for a,w in (cells if n==1 else list(reversed(cells)))]
for archive,workflow,n in ids:
 tag=f'{archive}-{workflow}{n}';run=base/tag;workspace=run/'workspace';workspace.mkdir(parents=True)
 src=root/'datasets'/archive
 for name, hashes in manifest.items():
  orig=src/name;dest=workspace/name
  if orig.is_symlink() or hashlib.sha256(orig.read_bytes()).hexdigest()!=hashes[archive]:raise ValueError('Invalid source '+str(orig))
  dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(orig,dest)
  if hashlib.sha256(dest.read_bytes()).hexdigest()!=hashes[archive]:raise ValueError('Invalid copy '+str(dest))
 items=list(workspace.rglob('*'))
 if any(p.is_symlink() for p in items) or {str(p.relative_to(workspace)) for p in items if p.is_file()}!=set(manifest):raise ValueError('Invalid workspace '+str(workspace))
(root/'execution/workspaces.json').write_text(json.dumps({'temporary_root':str(base),'count':len(ids),'workspace_files':len(manifest),'tags':[f'{a}-{w}{n}' for a,w,n in ids]},indent=2)+'\n')
prompts={'g':(root/'prompts/generic.txt').read_bytes(),'s':(root/'prompts/specialized.txt').read_bytes()}
env=os.environ.copy();env['PATH']=str(bwrap.parent)+':'+env['PATH']
codex=shutil.which('codex');assert codex
other_temp=[Path('/tmp/ugreen-blind-01-r0oqy1ev'),Path('/tmp/ugreen-opportunity-02-fttklbkb')]
def work(t):
 archive,workflow,n=t;tag=f'{archive}-{workflow}{n}'; run=base/tag; workspace=run/'workspace'
 others=[base/f'{a}-{w}{num}' for a,w,num in ids if (a,w,num)!=t]
 masks=[project]+[p for p in other_temp+others if p.is_dir()]
 outer=[str(bwrap),'--bind','/','/']
 for p in masks:outer+=['--tmpfs',str(p)]
 report=run/'last-message.md'
 args=outer+['--',codex,'exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','--sandbox','read-only','-c','web_search="disabled"','--cd',str(workspace),'--output-last-message',str(report),'--json','-']
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.monotonic()
 out=run/'events.jsonl';err=run/'stderr.log'
 with out.open('wb') as stdout,err.open('wb') as stderr:
  try:
   proc=subprocess.run(args,input=prompts[workflow],stdout=stdout,stderr=stderr,env=env,cwd=workspace,timeout=600)
   code=proc.returncode;failure=None
  except subprocess.TimeoutExpired:
   code=None;failure='timeout after 600 seconds'
 duration=time.monotonic()-tick
 end=datetime.datetime.now(datetime.timezone.utc).isoformat()
 for name in manifest:
  if hashlib.sha256((workspace/name).read_bytes()).hexdigest()!=manifest[name][archive]:raise RuntimeError('Workspace changed '+tag+'/'+name)
 ws=list(workspace.rglob('*'))
 if any(p.is_symlink() for p in ws) or {str(p.relative_to(workspace)) for p in ws if p.is_file()}!=set(manifest):raise RuntimeError('Workspace membership changed '+tag)
 eventdata=[]
 for line in out.read_text(errors='replace').splitlines():
  try:eventdata.append(json.loads(line))
  except json.JSONDecodeError:pass
 info={'tag':tag,'archive':archive,'workflow':workflow,'replicate':n,'started_utc':start,'ended_utc':end,'duration_seconds':round(duration,3),'exit_code':code,'technical_error':failure,'thread_id':next((e.get('thread_id') for e in eventdata if e.get('type')=='thread.started'),None),'turn_completed':any(e.get('type')=='turn.completed' for e in eventdata),'turn_failed':any(e.get('type') in ('turn.failed','error') for e in eventdata),'usage':next((e.get('usage') for e in eventdata if e.get('type')=='turn.completed'),None),'output_present':report.exists() and report.stat().st_size>0,'workspace_integrity':'pass','model':'CLI default, identifier not exposed in JSONL','reasoning':'CLI default, not separately exposed','prompt_sha256':hashlib.sha256(prompts[workflow]).hexdigest(),'mask_count':len(masks),'command':args}
 for f in (out,err):shutil.copyfile(f,root/'execution'/f'{tag}-{f.name}')
 if report.exists():shutil.copyfile(report,root/'results'/f'{tag}.md')
 (root/'execution'/f'{tag}-status.json').write_text(json.dumps(info,indent=2)+'\n')
 print(tag,'exit',code,'completed',info['turn_completed'],'report',info['output_present'],'seconds',info['duration_seconds'],flush=True)
 return info
print('Temporary root:',base,'prepared:',len(ids),'runs',flush=True)
with ThreadPoolExecutor(max_workers=4) as ex:
 future={ex.submit(work,t):t for t in ids}; results=[]
 for f in as_completed(future):
  try:results.append(f.result())
  except Exception as e:
   print('Launcher error',future[f],repr(e),flush=True)
   results.append({'tag':'-'.join(map(str,future[f])),'technical_error':repr(e)})
(root/'execution/process-status.json').write_text(json.dumps(sorted(results,key=lambda x:x['tag']),indent=2)+'\n')
print('All launch attempts completed:',len(results),flush=True)
