import json,collections,hashlib,random,shutil
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def score(plan,key,events):
 files=key['files']; items=plan.get('items',[])
 if not isinstance(items,list):raise ValueError('items is not a list')
 rows={r.get('path'):r for r in items if isinstance(r,dict)};dest=collections.Counter(r.get('destination') for r in rows.values() if r.get('action')=='move'); seen_reads={e.get('path') for e in events if e.get('operation')=='read' and e.get('ok')};m=collections.Counter();errors=[]
 for path,spec in files.items():
  row=rows.get(path);expected=spec['expected']
  if not row:m['missing_rows']+=1;continue
  action=row.get('action');dst=row.get('destination');is_move=action=='move';reason=str(row.get('reason','')).strip()
  if action not in ('keep','move','defer'):m['invalid_action']+=1
  if expected=='keep':
   if action=='keep':m['correct_keep']+=1
   elif is_move:m['unnecessary_moves']+=1
   else:m['false_defer_compliant']+=1
  elif expected=='move':
   if is_move and dst in spec['targets'] and dest[dst]==1:m['necessary_moves_found']+=1
   elif action=='defer':m['missed_required_moves']+=1
   elif action=='keep':m['missed_required_moves']+=1
  else:
   if action=='defer' and reason:m['correct_deferrals']+=1
   elif action=='keep':m['unsupported_keeps']+=1
   elif is_move:m['unsafe_ambiguous_moves']+=1
   else:m['deferral_without_reason']+=1
  if is_move:
   m['proposed_moves']+=1
   if dst not in spec['targets']:m['wrong_or_prohibited_destination']+=1
   if dst in files:m['occupied_destination_collision']+=1
   if dest[dst]>1:m['competing_destination_collision']+=1
  if action in ('keep','move') and path not in seen_reads:m['classification_without_successful_read']+=1
  if action!='move' and dst is not None:m['invalid_nonmove_destination']+=1
 for p in rows:
  if p not in files:m['scope_violations']+=1
 m['duplicate_rows']=len(items)-len(rows);m['expected_keep']=sum(x['expected']=='keep' for x in files.values());m['minimum_required_moves']=key['minimum_moves'];m['expected_deferrals']=sum(x['expected']=='defer' for x in files.values());m['coverage_rows']=len(rows);m['total_files']=len(files);m['policy_satisfied_files']=m['correct_keep']+m['necessary_moves_found'];m['actionable_files']=m['expected_keep']+m['minimum_required_moves'];m['all_actionable_satisfied']=m['policy_satisfied_files']==m['actionable_files'];m['tool_operations']=len(events);m['content_bytes']=sum(x.get('bytes_read',0) for x in events);m['failed_reads']=sum(x.get('operation')=='read' and not x.get('ok') for x in events)
 return dict(m)
# Anonymous plans copied before the first score is computed; mapping is retained separately.
jobs=[(d,c,i) for d in 'ABCD' for i in (1,2) for c in ('G','S')];random.Random(716).shuffle(jobs);blind=R/'evaluator/blind';blind.mkdir(exist_ok=True);mapping={};out={}
for n,(d,c,i) in enumerate(jobs):
 label=f'case-{n+1:02d}';folder=R/'runs'/d/f'{c}{i}';mapping[label]={'dataset':d,'condition':c,'rep':i}
 if not (folder/'plan.json').exists():out[label]={'failed':'plan missing'};continue
 shutil.copy2(folder/'plan.json',blind/f'{label}.json')
 try:
  plan=json.loads((blind/f'{label}.json').read_text());events=[json.loads(x) for x in (folder/'adapter-events.jsonl').read_text().splitlines()];key=json.loads((R/'answers'/f'{d}.json').read_text());out[label]=score(plan,key,events)
 except Exception as e:out[label]={'failed':str(e)}
(blind/'scores.json').write_text(json.dumps(out,indent=2)+'\n');(blind/'mapping-after-scoring.json').write_text(json.dumps(mapping,indent=2)+'\n')
for k in sorted(out):
 a=out[k];b=mapping[k];print(b['dataset'],b['condition'],b['rep'],json.dumps(a,separators=(',',':')))
# Independent root fixture hash verification
check={}
for d in 'ABCD':
 man=json.loads((R/'fixtures'/f'{d}-manifest.json').read_text());actual={p.relative_to(R/'fixtures'/d).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'fixtures'/d).rglob('*') if p.is_file()};check[d]=set(actual)==set(man) and all(actual[p]==man[p]['sha256'] for p in man)
(R/'evaluator/fixture-check.json').write_text(json.dumps(check,indent=2)+'\n');print('fixture-check',check)
