import sys,json,os,time
from pathlib import Path
root=Path('/tmp/work/archive');log=Path('/tmp/out/adapter-events.jsonl');start=time.monotonic();op=sys.argv[1] if len(sys.argv)>1 else '';rel=sys.argv[2] if len(sys.argv)>2 else None
e={'operation':op,'path':rel,'bytes_read':0,'ok':False}
try:
 if op=='list' and rel is None:
  paths=[]
  for p in root.rglob('*'):
   if p.is_symlink():raise PermissionError('symlink')
   if p.is_file():paths.append(p.relative_to(root).as_posix())
  out={'paths':sorted(paths),'complete':True};e['count']=len(paths)
 elif op=='read' and rel is not None:
  p=(root/rel).resolve(strict=True)
  if not p.is_relative_to(root.resolve()) or not p.is_file() or (root/rel).is_symlink():raise PermissionError('outside permitted archive')
  data=p.read_bytes();e['bytes_read']=len(data)
  out={'text':data.decode('utf8')}
 else:raise ValueError('unsupported operation')
 e['ok']=True;print(json.dumps(out))
except Exception as ex:
 e['error']=type(ex).__name__+': '+str(ex);print(json.dumps({'error':e['error']}))
finally:
 e['elapsed_ms']=round((time.monotonic()-start)*1000,3)
 with log.open('a') as f:f.write(json.dumps(e)+'\n')
