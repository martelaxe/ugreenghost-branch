import json,re
from pathlib import Path,PurePosixPath
from collections import defaultdict,Counter
x=json.loads(Path('/tmp/out/evidence.json').read_text())
paths=x['inventory']['paths']; occupied=set(paths)
items={}; groups=defaultdict(list)
for p in paths:
 r=json.loads(x['reads'][p]['stdout'])
 row={'path':p,'action':'defer','destination':None,'reason':''};items[p]=row
 if 'text' not in r:
  row['reason']='Unreadable as UTF-8; category and year unknown. Please provide readable Category and Date fields.'
  continue
 t=r['text']
 cats=set(re.findall(r'Category:\s*([A-Za-z]+)',t))
 dates=re.findall(r'Date:\s*([0-9/-]+)',t)
 years=set(y for d in dates for y in re.findall(r'(?<!\d)\d{4}(?!\d)',d))
 if len(cats)!=1 or not cats <= {'finance','projects','personal'} or len(years)!=1 or not dates or any(not re.search(r'(?<!\d)\d{4}(?!\d)',d) for d in dates):
  row['reason']='Missing, unsupported, or conflicting Category/Date evidence; please clarify fields.'
  continue
 c=next(iter(cats));y=next(iter(years))
 dirs=[f'sorted/{c}/{y}',f'historic/{c}/{y}']
 if str(PurePosixPath(p).parent) in dirs:
  row.update(action='keep',reason=f'Contents establish {c}/{y}; direct parent is already acceptable.')
 else:
  targets=[f'{d}/{PurePosixPath(p).name}' for d in dirs]
  groups[tuple(targets)].append((p,c,y))
for targets,records in groups.items():
 free=[t for t in targets if t not in occupied]
 if len(records)>len(free):
  for p,c,y in records:
   items[p]['reason']=(f'Collision: both acceptable destinations occupied at inventory: {", ".join(targets)}. Please decide how to resolve without overwrite or rename.' if not free else f'Competing group: {len(records)} records share basename for {c}/{y}, but only {len(free)} acceptable paths are free. Defer entire group; please decide placement. No merge or rename.')
 else:
  for (p,c,y),target in zip(records,free):
   items[p].update(action='move',destination=target,reason=f'Contents establish {c}/{y}; current parent is noncompliant; target was free at inventory; preserve basename.')
plan={'items':[items[p] for p in paths], 'coverage':'Adapter returned complete=true: all 186 inventoried regular files have exactly one row and were read once via adapter; 182 readable, 4 UTF-8 errors. All extensions treated as records. No classification from names. No unlisted contents inferred; no files omitted. Unreadable metadata and collision decisions remain unresolved.','policy_conflicts':'none; occupied destinations and competing records are handled by the explicit deferral rules. Clarification requested in deferred rows.','approval':'proposed only, no action executed'}
assert len(items)==len(paths)==186
moves=[r['destination'] for r in items.values() if r['action']=='move']
assert len(set(moves))==len(moves) and not set(moves)&occupied
Path('/tmp/out/plan.json').write_text(json.dumps(plan,indent=2)+'\n')
print(dict(Counter(r['action'] for r in items.values())))
