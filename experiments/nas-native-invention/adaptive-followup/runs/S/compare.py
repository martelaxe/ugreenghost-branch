import subprocess,json,concurrent.futures
from collections import Counter
cache={('list','small','source',None):{'paths':sorted(f'group_{i%9:02d}/item_{i:04d}.bin' for i in range(120)),'complete':True},('stat','small','source','group_00/item_0000.bin'):{'size':2048},('sha256','small','source','group_00/item_0000.bin'):{'sha256':'a7f1c3ae702b078d8208cd00a4f99441feac2ea601df892236b9a2e29f32fae8'}}
def call(op,w,s,p=None):
 k=(op,w,s,p)
 if k in cache:return cache[k]
 try:
  r=subprocess.run(['python3','/tmp/tools/adapter.py',op,w,s]+([p] if p is not None else []),capture_output=True,text=True)
  d=json.loads(r.stdout)
  if r.returncode or not isinstance(d,dict) or d.get('error'):d={'error':d}
 except Exception as e:d={'error':str(e)}
 cache[k]=d
 return d
def batch(tasks):
 with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:list(pool.map(lambda a:call(*a),tasks))
def good(op,w,s,p):
 d=cache.get((op,w,s,p),{})
 key='size' if op=='stat' else 'sha256'
 return key in d and not d.get('error')
results=[]
for w in ['small','large','matching','different','incomplete']:
 batch([('list',w,s) for s in ['source','destination']])
 ls=[cache['list',w,s,None] for s in ['source','destination']]
 sets=[set(d.get('paths',[])) for d in ls]; complete=[d.get('complete') is True and not d.get('error') for d in ls]
 common=sorted(sets[0]&sets[1]);n=min(8,len(common))
 samples=[common[round(i*(len(common)-1)/(n-1))] for i in range(n)] if n>1 else common[:n]
 batch([(op,w,s,p) for p in samples for op in ['stat','sha256'] for s in ['source','destination']])
 skipped=sum(cache['stat',w,'source',p]['size']+cache['stat',w,'destination',p]['size'] for p in samples if all(good('stat',w,s,p) for s in ['source','destination']) and cache['stat',w,'source',p]['size']!=cache['stat',w,'destination',p]['size'])
 remaining=[p for p in common if p not in samples]; estimate=skipped/n*len(remaining) if n else None; threshold=2*len(remaining)*262144
 branch='metadata-first' if estimate is not None and estimate>threshold else 'direct SHA-256'
 if branch=='metadata-first':
  batch([('stat',w,s,p) for p in remaining for s in ['source','destination']])
  tohash=[p for p in remaining if all(good('stat',w,s,p) for s in ['source','destination']) and cache['stat',w,'source',p]['size']==cache['stat',w,'destination',p]['size']]
 else:tohash=remaining
 batch([('sha256',w,s,p) for p in tohash for s in ['source','destination']])
 paths=[]
 for p in sorted(sets[0]|sets[1]):
  if p not in sets[1]:status='source_only' if complete[1] else 'unverified'
  elif p not in sets[0]:status='destination_only' if complete[0] else 'unverified'
  else:
   failure=any(cache.get((op,w,s,p),{}).get('error') for op in ['stat','sha256'] for s in ['source','destination'])
   meta=all(good('stat',w,s,p) for s in ['source','destination']);hashed=all(good('sha256',w,s,p) for s in ['source','destination'])
   if failure:status='unverified'
   elif meta and cache['stat',w,'source',p]['size']!=cache['stat',w,'destination',p]['size']:status='different'
   elif hashed:status='identical' if cache['sha256',w,'source',p]['sha256']==cache['sha256',w,'destination',p]['sha256'] else 'different'
   else:status='unverified'
  paths.append({'path':p,'status':status})
 counts=dict.fromkeys(['identical','different','source_only','destination_only','unverified'],0);counts.update(Counter(p['status'] for p in paths))
 failures=[f'{op} {s} {p}' for (op,ww,s,p),d in cache.items() if ww==w and d.get('error')]
 explanation='All returned paths are reported. '+('Both listings complete. ' if all(complete) else 'Incomplete listings prevent complete archive coverage; paths absent from an incomplete listing remain unverified, and undisclosed paths cannot be enumerated. ')+('Operation failures: '+', '.join(failures)+'. ' if failures else 'No operation failures. ')
 explanation+='Identity requires matching actual SHA-256 values; unequal actual sizes or hashes establish differences.'
 uncertainty='Sample-based extrapolation is uncertain and is not measured time or guaranteed NAS cost.'
 if any(not all(good('stat',w,s,p) for s in ['source','destination']) for p in samples):uncertainty+=' Failed sample metadata contributes no invented size; estimate uses only observed unequal-size sums divided by all selected samples.'
 results.append(dict(name=w,paths=paths,counts=counts,source_complete=complete[0],destination_complete=complete[1],both_metadata_count=sum(all(good('stat',w,s,p) for s in ['source','destination']) for p in common),both_hash_count=sum(all(good('sha256',w,s,p) for s in ['source','destination']) for p in common),explanation=explanation,next_action='Retry incomplete listings and failed operations through the read-only adapter, then compare newly disclosed paths.' if not all(complete) or failures else ('Review the reported differences and one-sided paths before planning any synchronization.' if counts['different'] or counts['source_only'] or counts['destination_only'] else 'Retain this comparison as a baseline for a future read-only verification.'),strategy=f'{branch}; {n} evenly spaced sorted common-path samples, each requested with stat and SHA-256 on both sides; {len(remaining)} remaining common paths. Observed sampled unequal-size byte sum={skipped}; estimated skipped bytes={estimate}; hypothetical stat threshold={threshold} bytes (2 × remaining × 262144). {uncertainty}'))
 print(json.dumps({k:v for k,v in results[-1].items() if k!='paths'}),flush=True)
with open('/tmp/out/response.json','w') as f:json.dump({'workloads':results},f,indent=2)
