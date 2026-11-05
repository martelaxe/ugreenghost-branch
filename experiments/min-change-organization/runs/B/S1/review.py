import subprocess,json
from pathlib import Path

def adapter(*args):
 p=subprocess.run(['python3','/tmp/tools/adapter.py',*args],capture_output=True,text=True)
 return {'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
r=adapter('list')
listing=json.loads(r['stdout'])
results={p:adapter('read',p) for p in listing['paths']}
Path('/tmp/out/evidence.json').write_text(json.dumps({'listing':listing,'reads':results}))
for p,r in results.items():
 print(json.dumps({'path':p,**r}))
