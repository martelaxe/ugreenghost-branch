import subprocess,json

def call(*args):
 p=subprocess.run(['python3','/tmp/tools/adapter.py',*args],capture_output=True,text=True)
 return {'code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
r=call('list')
inv=json.loads(r['stdout'])
results={p:call('read',p) for p in inv['paths']}
with open('/tmp/out/evidence.json','w') as f: json.dump({'inventory':inv,'reads':results},f)
for p,r in list(results.items())[:4]: print(p,repr(r))
print('files',len(results))
