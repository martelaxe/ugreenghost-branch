import json,re,posixpath,collections
x=json.load(open('/tmp/out/evidence.json'))
paths=x['inventory']['paths']; occupied=set(paths); items={}; groups=collections.defaultdict(list); conflicts=[]
for p in paths:
 r=json.loads(x['reads'][p]['stdout'])
 reason=None
 if 'text' not in r:
  reason='Unreadable UTF-8: '+r.get('error','adapter read failed')+'; provide readable contents with Category and Date fields.'
 else:
  t=r['text']
  cats=set(re.findall(r'Category:\s*([A-Za-z]+)',t))
  dates=re.findall(r'Date:\s*([0-9/-]+)',t)
  years=set(y for d in dates for y in re.findall(r'(?<!\d)\d{4}(?!\d)',d))
  if len(cats)!=1 or not cats <= {'finance','projects','personal'} or len(years)!=1 or not dates:
   reason=f'Insufficient or conflicting metadata: Category values {sorted(cats)}, Date years {sorted(years)}; clarify authoritative category/year.'
 if reason:
  items[p]={'path':p,'action':'defer','destination':None,'reason':reason}; continue
 c=next(iter(cats)); y=next(iter(years)); dirs=[f'sorted/{c}/{y}',f'historic/{c}/{y}']
 if posixpath.dirname(p) in dirs:
  items[p]={'path':p,'action':'keep','destination':None,'reason':f'Content confirms {c}/{y}; direct parent is already acceptable.'}
 elif p.startswith('historic/'):
  conflicts.append(p)
  items[p]={'path':p,'action':'defer','destination':None,'reason':f'Content confirms {c}/{y}, but current parent is noncompliant. Stop: universal compliance and restriction on moving historic records need clarification; may this record move within historic/ to historic/{c}/{y}/{posixpath.basename(p)}? No rule chosen.'}
 else:
  targets=[d+'/'+posixpath.basename(p) for d in dirs]
  groups[tuple(targets)].append(p)
for targets,ps in groups.items():
 free=[d for d in targets if d not in occupied]
 if len(free)<len(ps):
  reason=('Collision: both acceptable destinations occupied at inventory time: '+', '.join(targets)+'. Clarify how to resolve without overwriting or renaming.' if not free else f'Competing group of {len(ps)} records for {len(free)} free acceptable paths: '+', '.join(free)+'. Defer entire group; user must decide; no winner, rename, deletion, or duplicate merge.')
  for p in ps: items[p]={'path':p,'action':'defer','destination':None,'reason':reason}
 else:
  for p,d in zip(ps,free): items[p]={'path':p,'action':'move','destination':d,'reason':'Unique Category and Date year in contents; current parent is noncompliant. Preserve basename; destination unoccupied at inventory time.'}
plan={'items':[items[p] for p in paths], 'coverage':f'Adapter complete=true listed {len(paths)} regular files; every file read once through adapter, regardless of extension. 182 returned UTF-8 text; 4 returned decoding errors and remain unclassified. Two list operations; no archive inspection outside adapter. All listed files have exactly one row. No unlisted contents inferred; unreadable metadata remains unknown. No missing-field records observed among readable files. Duplicate records retained separately.', 'policy_conflicts':f'{len(conflicts)} content-classified noncompliant records under historic/old/ are deferred. The requirement that every record comply conflicts with the restriction on moving historic records as applied to these files; clarify whether moves within historic/ are permitted or which requirement takes precedence. Affected paths: '+', '.join(conflicts)+'. Also clarify authoritative metadata for six conflicting records, supply readable evidence for four unreadable records, and resolve the occupied.txt collision and three-record shared.txt competing group. No exception inferred.', 'approval':'proposed only, no action executed'}
assert len(items)==len(paths)==len(set(paths))
moves=[r for r in items.values() if r['action']=='move']
assert len({r['destination'] for r in moves})==len(moves)
assert all(r['destination'] not in occupied and posixpath.basename(r['path'])==posixpath.basename(r['destination']) for r in moves)
with open('/tmp/out/plan.json','w') as f: json.dump(plan,f,indent=2); f.write('\n')
print(dict(collections.Counter(r['action'] for r in items.values())))
print('historic conflicts',len(conflicts))
