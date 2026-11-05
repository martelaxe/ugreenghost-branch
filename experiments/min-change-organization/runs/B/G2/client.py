import subprocess,json,re
from pathlib import PurePosixPath,Path
from collections import defaultdict,Counter

def call(*args):
 p=subprocess.run(['python3','/tmp/tools/adapter.py',*args],capture_output=True,text=True)
 return p
p=call('list')
inv=json.loads(p.stdout)
paths=inv['paths']
reads={}
for path in paths:
 p=call('read',path)
 reads[path]={'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
Path('/tmp/out/evidence.json').write_text(json.dumps({'inventory':inv,'reads':reads},indent=2))
print('Inventory:',len(paths),'files; reads complete')
for path,r in list(reads.items())[:4]:print(path,repr(r))
print('Read failures:',[(p,r) for p,r in reads.items() if r['returncode']])
