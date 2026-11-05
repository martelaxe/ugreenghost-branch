import json,collections,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[1];K=json.loads((R/'answer-key/key.json').read_text())['statuses'];manifest=json.loads((R/'fixture/manifest.json').read_text()); out={'reference':{},'agents':{},'fixture':{}}
for p,v in manifest.items():
 f=R/'fixture/work'/p;h=hashlib.sha256(f.read_bytes()).hexdigest()
 if h!=v['sha256'] or f.stat().st_size!=v['size']:out['fixture'][p]='changed'
out['fixture']={'unchanged':not out['fixture'],'changed':out['fixture']}
for x in json.loads((R/'reference-results.json').read_text()):
 errors=[{'path':p,'expected':s,'actual':x['paths'].get(p)} for p,s in K[x['workload']].items() if x['paths'].get(p)!=s]
 out['reference'][f"{x['workload']}/{x['strategy']}/{x['rep']}"]={'correct':not errors,'errors':errors}
for label in ('G','S'):
 p=R/'runs'/label
 if not (p/'response.json').exists() or not (p/'adapter-events.jsonl').exists():out['agents'][label]={'missing_response_or_log':True};continue
 resp=json.loads((p/'response.json').read_text());ev=[json.loads(x) for x in (p/'adapter-events.jsonl').read_text().splitlines()]; byname={x['name']:x for x in resp['workloads']};res={}
 for name,k in K.items():
  x=byname.get(name)
  if not x:res[name]={'missing_workload':True};continue
  pairs=x['paths'];statuses={i['path']:i['status'] for i in pairs};events=[e for e in ev if e['workload']==name];checks={}
  for e in events:
   if e['ok']:checks[e['operation'],e['side'],e['path']]=e['result']
  errors=[{'path':path,'expected':v,'actual':statuses.get(path)} for path,v in k.items() if statuses.get(path)!=v]
  errors += [{'path':path,'expected':'not_enumerated','actual':v} for path,v in statuses.items() if path not in k]
  correctcount=collections.Counter(statuses.values());meta=0;sha=0;unsupported=[]
  for path,status in statuses.items():
   m=[checks.get(('stat',side,path)) for side in ('source','destination')];h=[checks.get(('sha256',side,path)) for side in ('source','destination')];meta+=all(m);sha+=all(h)
   if status=='identical' and not (all(h) and h[0]['sha256']==h[1]['sha256']):unsupported.append(path)
   if status=='different' and not ((all(m) and m[0]['size']!=m[1]['size']) or (all(h) and h[0]['sha256']!=h[1]['sha256'])):unsupported.append(path)
  actual_complete={side:checks.get(('list',side,None),{}).get('complete') for side in ('source','destination')}
  cnt_ok=all(x['counts'].get(c,0)==correctcount[c] for c in ['identical','different','source_only','destination_only','unverified'])
  coverage_ok=x['source_complete']==actual_complete['source'] and x['destination_complete']==actual_complete['destination']
  frontier_ok=x['both_metadata_count']==meta and x['both_hash_count']==sha
  cnt=collections.Counter(e['operation'] for e in events)
  res[name]={'classifications_correct':not errors,'classification_errors':errors,'duplicate_paths':len(pairs)-len(statuses),'reported_counts_correct':cnt_ok,'reported_coverage_correct':coverage_ok,'frontier_counts_correct':frontier_ok,'actual_both_metadata':meta,'reported_both_metadata':x['both_metadata_count'],'actual_both_hash':sha,'reported_both_hash':x['both_hash_count'],'unsupported_claims':unsupported,'operations':dict(cnt),'bytes_read':sum(e['bytes_read'] for e in events),'errors':sum(not e['ok'] for e in events),'strategy':x['strategy'],'explanation':x['explanation'],'next_action':x['next_action']}
 res['_total']={'operations':len(ev),'bytes_read':sum(e['bytes_read'] for e in ev),'out_of_scope':sum(e.get('workload') not in K or e.get('side') not in ('source','destination') for e in ev)};out['agents'][label]=res
(R/'evaluation.json').write_text(json.dumps(out,indent=2)+'\n')
for k,v in out['reference'].items():
 if not v['correct']:print('REFERENCE ERROR',k,v['errors'][:3])
for label,r in out['agents'].items():
 print('\n',label)
 for name,x in r.items():
  if name=='_total':print(name,x);continue
  print(name,{z:x.get(z) for z in ('classifications_correct','reported_counts_correct','reported_coverage_correct','frontier_counts_correct','operations','bytes_read','errors','strategy')},'bad',len(x.get('classification_errors',[])),'unsupported',len(x.get('unsupported_claims',[])))
print('unchanged',out['fixture']['unchanged'])
