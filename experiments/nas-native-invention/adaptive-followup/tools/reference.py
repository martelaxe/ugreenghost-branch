import json,random,time,statistics
from pathlib import Path
from adapter_core import Adapter
R=Path(__file__).resolve().parents[1];root=R/'fixture/work';faults=json.loads((R/'fixture/faults.json').read_text());names=('small','large','matching','different','incomplete')
def execute(w,strategy,rep):
 log=R/'runs/reference'/f'{w}-{strategy}-{rep}.jsonl'; a=Adapter(root,faults,log);start=time.monotonic()
 l={s:a.call('list',w,s) for s in ('source','destination')};sets={s:set(l[s]['paths']) for s in l};common=sorted(sets['source']&sets['destination']); rec={};meta={};dig={}
 for p in sets['source']^sets['destination']:
  s='source' if p in sets['source'] else 'destination';o='destination' if s=='source' else 'source';rec[p]=s+'_only' if l[o]['complete'] else 'unverified'
 def pair(p,method,sample=False):
  if method=='meta' or sample:
   ms=[a.call('stat',w,s,p) for s in ('source','destination')];meta[p]=ms
   if any('error' in x for x in ms):rec[p]='unverified';return
   if ms[0]['size']!=ms[1]['size'] and not sample:rec[p]='different';return
  ds=[a.call('sha256',w,s,p) for s in ('source','destination')];dig[p]=ds
  if any('error' in x for x in ds):rec[p]='unverified'
  else:rec[p]='identical' if ds[0]['sha256']==ds[1]['sha256'] else 'different'
 branch=strategy;est=None
 if strategy=='adaptive' and common:
  n=min(8,len(common));sample=[common[(i*(len(common)-1))//(n-1)] for i in range(n)] if n>1 else [common[0]]
  for p in sample:pair(p,'meta',True)
  remaining=[p for p in common if p not in sample];saved=sum(sum(m['size'] for m in meta[p]) for p in sample if p in meta and all('size' in m for m in meta[p]) and meta[p][0]['size']!=meta[p][1]['size']);est=saved/n*len(remaining)
  branch='metadata' if est>2*len(remaining)*262144 else 'direct'
 else:remaining=common
 for p in remaining:pair(p,'meta' if branch=='metadata' else 'direct')
 elapsed=time.monotonic()-start;events=[json.loads(x) for x in log.read_text().splitlines()];counts={k:sum(v==k for v in rec.values()) for k in ('identical','different','source_only','destination_only','unverified')};out={'workload':w,'strategy':strategy,'rep':rep,'branch':branch,'estimated_saved_bytes':est,'wall_seconds':elapsed,'counts':counts,'paths':rec,'list_complete':{s:l[s]['complete'] for s in l},'operations':len(events),'stats':sum(e['operation']=='stat' for e in events),'hashes':sum(e['operation']=='sha256' for e in events),'bytes':sum(e['bytes_read'] for e in events),'errors':sum(not e['ok'] for e in events),'log':str(log.relative_to(R))};(log.with_suffix('.result.json')).write_text(json.dumps(out,indent=2)+'\n');return out
out=[]
for rep in range(3):
 for w in names:
  order=['direct','metadata','adaptive'];order=order[rep:]+order[:rep]
  for s in order:out.append(execute(w,s,rep))
(R/'reference-results.json').write_text(json.dumps(out,indent=2)+'\n')
for w in names:
 for s in ('direct','metadata','adaptive'):
  rows=[x for x in out if x['workload']==w and x['strategy']==s];x=rows[0];print(w,s,'branch',x['branch'],'ops',x['operations'],'bytes',x['bytes'],'median_seconds',round(statistics.median(y['wall_seconds'] for y in rows),4),'unknown',x['counts']['unverified'])
