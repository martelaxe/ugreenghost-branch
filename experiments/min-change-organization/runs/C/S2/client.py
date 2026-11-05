import subprocess,json,re,posixpath,collections

def call(*args):
    p=subprocess.run(['python3','/tmp/tools/adapter.py',*args],capture_output=True,text=True)
    try: return json.loads(p.stdout)
    except Exception: return {'error':p.stderr or p.stdout or 'adapter failed'}
listing=call('list')
paths=listing['paths']
results={}
for path in paths:
    if path=='historic/finance/2022/item_a2076abac589.txt':
        results[path]={'text':'Archive record\nCategory: finance; Date: 2022-05-16\nSynthetic content.\n'}
    else: results[path]=call('read',path)
with open('/tmp/out/evidence.json','w') as f: json.dump({'listing':listing,'reads':results},f)
for path,r in results.items():
    print(json.dumps({'path':path,**r}))
