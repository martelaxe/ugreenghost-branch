import os,json,hashlib,time
from pathlib import Path
VALID=('small','large','matching','different','incomplete')
class Adapter:
 def __init__(self,root,faults,log):self.root=Path(root);self.faults=faults;self.log=Path(log)
 def call(self,op,w,side,rel=None):
  start=time.monotonic();e={'operation':op,'workload':w,'side':side,'path':rel,'bytes_read':0,'ok':False}
  try:
   if w not in VALID or side not in ('source','destination'):raise PermissionError('unauthorized scope')
   base=self.root/w/side
   if op=='list' and rel is None:
    paths=[]
    for p in base.rglob('*'):
     if p.is_symlink():raise PermissionError('symlink encountered')
     if p.is_file():paths.append(p.relative_to(base).as_posix())
    complete=True
    if w=='incomplete' and side=='destination':paths.remove(self.faults['hidden']);complete=False
    out={'paths':sorted(paths),'complete':complete}
   else:
    if op not in ('stat','sha256') or rel is None:raise ValueError('bad operation')
    if w=='incomplete' and rel==self.faults['denied']:raise PermissionError('simulated denied entry')
    p=(base/rel).resolve(strict=True)
    if not p.is_relative_to(base.resolve()) or not p.is_file():raise PermissionError('out of scope')
    if op=='stat':out={'size':p.stat().st_size}
    else:
     h=hashlib.sha256()
     with p.open('rb') as f:
      while True:
       chunk=f.read(65536)
       if not chunk:break
       h.update(chunk);e['bytes_read']+=len(chunk)
     out={'sha256':h.hexdigest()}
   e['ok']=True;e['result']=out;return out
  except Exception as ex:
   e['error']=str(ex);return {'error':str(ex)}
  finally:
   e['elapsed_ms']=round((time.monotonic()-start)*1000,4);self.log.parent.mkdir(parents=True,exist_ok=True)
   with self.log.open('a') as f:f.write(json.dumps(e,separators=(',',':'))+'\n')
