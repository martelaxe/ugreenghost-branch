import subprocess,json

def call(*args):
 p=subprocess.run(['python3','/tmp/tools/adapter.py',*args],capture_output=True,text=True)
 return {'code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
inv=call('list')
data=json.loads(inv['stdout'])
records={p:call('read',p) for p in data['paths']}
with open('/tmp/out/evidence.json','w') as f: json.dump({'inventory':data,'reads':records},f)
for p,r in records.items():
 print(json.dumps({'path':p,**r}))
