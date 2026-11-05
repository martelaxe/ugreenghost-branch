import json,re,posixpath,collections
x=json.load(open('/tmp/out/evidence.json'))
paths=x['inventory']['paths']; occupied=set(paths); rows={}; groups=collections.defaultdict(list)
for p in paths:
 r=x['reads'][p]; data=json.loads(r['stdout'])
 row={'path':p,'action':'defer','destination':None,'reason':''};rows[p]=row
 if r['code'] or 'text' not in data:
  row['reason']='Unreadable through UTF-8 adapter; category and year unverified. Please provide readable record evidence.'
  continue
 t=data['text']
 cats=set(re.findall(r'Category:\s*([^;\s"\,}]+)',t))
 dates=re.findall(r'Date:\s*([^;\n"}]+)',t)
 years=set(y for d in dates for y in re.findall(r'(?<!\d)\d{4}(?!\d)',d))
 if len(cats)!=1 or not cats <= {'finance','projects','personal'} or len(years)!=1 or not dates or any(not re.search(r'(?<!\d)\d{4}(?!\d)',d) for d in dates):
  row['reason']=f'Missing, unsupported, or conflicting fields: categories={sorted(cats)}, Date years={sorted(years)}. Please clarify record evidence.'
  continue
 c=next(iter(cats)); y=next(iter(years)); parents=[f'sorted/{c}/{y}',f'historic/{c}/{y}']
 if posixpath.dirname(p) in parents:
  row.update(action='keep',reason=f'Content confirms {c}/{y}; direct parent already acceptable.')
 else:
  groups[(c,y,posixpath.basename(p))].append(p)
for (c,y,name),members in groups.items():
 targets=[f'{root}/{c}/{y}/{name}' for root in ('sorted','historic')]
 free=[p for p in targets if p not in occupied]
 if len(members)>len(free):
  reason=(f'Collision: {len(members)} records compete for {len(free)} currently free acceptable paths ({", ".join(targets)}). Defer entire group; please decide how to resolve without overwrite, rename, deletion, or merge.' if len(members)>1 else f'Collision: both acceptable paths occupied at inventory time ({", ".join(targets)}). Please decide resolution; no overwrite or rename allowed.')
  for p in members:rows[p]['reason']=reason
 else:
  for p,d in zip(members,free):rows[p].update(action='move',destination=d,reason=f'Content confirms {c}/{y}; current direct parent is noncompliant; target free at inventory; basename preserved.')
plan={'items':[rows[p] for p in paths], 'coverage':f'Adapter reported complete=true: all {len(paths)} inventoried regular files included exactly once; each read once through adapter, regardless of extension. Unreadable contents remain unknown as identified in deferred rows. No unlisted contents inferred; no uncovered inventoried files.', 'policy_conflicts':'none; destination collisions and unreadable evidence require clarification as recorded in deferred rows.', 'approval':'proposed only, no action executed'}
assert len(rows)==len(paths)
move=[r['destination'] for r in rows.values() if r['action']=='move']
assert len(move)==len(set(move)) and not set(move)&occupied
with open('/tmp/out/plan.json','w') as f:json.dump(plan,f,indent=2);f.write('\n')
print(collections.Counter(r['action'] for r in rows.values()))
for r in rows.values():
 if r['action']=='defer':print(r['path'],r['reason'])
