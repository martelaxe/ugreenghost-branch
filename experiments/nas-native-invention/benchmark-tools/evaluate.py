#!/usr/bin/env python3
"""Post-run evaluator of frozen answer key, results and per-operation event records."""
import json, collections, pathlib
R=pathlib.Path(__file__).resolve().parents[1]
key=json.loads((R/'answer-key/answer-key.json').read_text())['classification']
manifest=json.loads((R/'fixture/input-manifest.json').read_text())
res={}
for cond in ('G','S'):
 p=R/'runs'/cond
 out=json.loads((p/'response.json').read_text())
 events=[json.loads(x) for x in (p/'adapter-events.jsonl').read_text().splitlines()]
 checks=collections.Counter((e['operation'],e['side'],e.get('relative')) for e in events if e['ok'])
 cnt=collections.Counter(e['operation'] for e in events)
 expected=collections.Counter(key.values())
 exceptions={x['path']:x['status'] for x in out['exceptions']}
 exp_ex={p:s for p,s in key.items() if s!='identical'}
 errors=[{'path':p,'expected':s,'returned':exceptions.get(p)} for p,s in exp_ex.items() if exceptions.get(p)!=s]
 errors += [{'path':p,'expected':key.get(p,'not_in_scope'),'returned':s} for p,s in exceptions.items() if key.get(p)!=s and p not in exp_ex]
 missing_digest=[]; missing_diff_evidence=[]
 for path,status in key.items():
  if status=='identical':
   if not all(checks['sha256',side,path] for side in ('source','destination')) or manifest['source/'+path]['sha256']!=manifest['destination/'+path]['sha256']: missing_digest.append(path)
  if status=='different':
   a,b=(manifest[x+'/'+path] for x in ('source','destination'))
   size=all(checks['stat',side,path] for side in ('source','destination')) and a['size']!=b['size']
   hashes=all(checks['sha256',side,path] for side in ('source','destination')) and a['sha256']!=b['sha256']
   if not (size or hashes): missing_diff_evidence.append(path)
 execution=json.loads((p/'execution.json').read_text())
 d={'actual_counts':out['counts'],'expected_counts':dict(expected),'counts_match':all(out['counts'].get(x,0)==expected[x] for x in ('identical','different','source_only','destination_only','unverified')),'exception_errors':errors,'exception_entries':len(out['exceptions']),'duplicate_exception_entries':len(out['exceptions'])-len(exceptions),'identical_missing_paired_hashes':missing_digest,'different_missing_evidence':missing_diff_evidence,'complete_list_evidence':all(checks['list',side,None] for side in ('source','destination')),'adapter_counts':dict(cnt),'adapter_errors':sum(not x['ok'] for x in events),'out_of_scope_attempts':sum(x.get('side') not in ('source','destination') for x in events),'hash_bytes':sum(e['bytes_read'] for e in events if e['operation']=='sha256'),'distinct_hash_paths':len({(e['side'],e['relative']) for e in events if e['operation']=='sha256' and e['ok']}),'model_usage':execution['usage_reported'],'wall_seconds':execution['elapsed_seconds'],'shell_tool_calls':execution['command_tool_count'],'reported_limitations':out['limitations']}
 d['correctness_gate']=d['counts_match'] and not errors and d['duplicate_exception_entries']==0 and not missing_digest and not missing_diff_evidence and d['complete_list_evidence']
 res[cond]=d
(R/'measurements.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
