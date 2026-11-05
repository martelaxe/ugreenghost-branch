"""Local research-only per-path adapter, not a UGREEN tool."""
import sys,os,json,hashlib,time
from pathlib import Path
root=Path('/tmp/work'); log=Path('/tmp/out/adapter-events.jsonl'); begin=time.monotonic()
event={'operation':sys.argv[1] if len(sys.argv)>1 else None,'side':sys.argv[2] if len(sys.argv)>2 else None,'relative':sys.argv[3] if len(sys.argv)>3 else None,'bytes_read':0,'ok':False}
try:
 if len(sys.argv)<3:raise ValueError('usage: operation side [relative path]')
 op,side=sys.argv[1:3]
 if side not in ('source','destination'):raise PermissionError('side is not authorized')
 base=root/side
 if op=='list' and len(sys.argv)==3:
  found=[]
  for p in base.rglob('*'):
   if p.is_symlink():raise PermissionError('symlink')
   if p.is_file():found.append(p.relative_to(base).as_posix())
  event['enumerated']=len(found);out={'paths':sorted(found),'complete':True}
 elif op in ('stat','sha256') and len(sys.argv)==4:
  rel=Path(sys.argv[3]); p=(base/rel).resolve(strict=True)
  if rel.is_absolute() or not p.is_relative_to(base.resolve()) or not p.is_file():raise PermissionError('invalid or outside path')
  if any(x.is_symlink() for x in [base/rel,*list((base/rel).parents)[:len(rel.parts)]]):raise PermissionError('symlink')
  if op=='stat':
   st=p.stat();out={'size':st.st_size,'mtime_ns':st.st_mtime_ns}
  else:
   h=hashlib.sha256()
   with p.open('rb') as f:
    while True:
     chunk=f.read(65536)
     if not chunk:break
     h.update(chunk);event['bytes_read']+=len(chunk)
   out={'sha256':h.hexdigest()}
 else:raise ValueError('unsupported operation/arguments')
 event['ok']=True;print(json.dumps(out))
except Exception as e:
 event['error']=type(e).__name__+': '+str(e);print(json.dumps({'error':event['error']}),file=sys.stderr);sys.exit(1)
finally:
 event['duration_ms']=round((time.monotonic()-begin)*1000,3)
 with log.open('a',encoding='utf8') as f:f.write(json.dumps(event,sort_keys=True)+'\n')
