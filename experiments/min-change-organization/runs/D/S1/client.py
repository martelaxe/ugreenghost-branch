import subprocess,json
from pathlib import PurePosixPath

def call(*args):
 p=subprocess.run(['python3','/tmp/tools/adapter.py',*args],capture_output=True,text=True)
 return p
p=call('list')
inv=json.loads(p.stdout)
results=[]
for path in inv['paths']:
 p=call('read',path)
 results.append({'path':path,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
with open('/tmp/out/returned.json','w') as f: json.dump({'inventory':inv,'reads':results},f)
for r in results: print(json.dumps(r))
