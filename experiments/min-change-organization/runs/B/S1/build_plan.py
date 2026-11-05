import json,re,collections
from pathlib import Path,PurePosixPath
E=json.loads(Path('/tmp/out/evidence.json').read_text()); paths=E['listing']['paths']; occupied=set(paths)
items={};groups=collections.defaultdict(list)
for p in paths:
 r=E['reads'][p]; data=json.loads(r['stdout']); t=data.get('text')
 reason=None
 if t is None: reason='Unreadable through adapter: '+data.get('error','read failed')+'; clarification required; no classification inferred.'
 else:
  cats=re.findall(r'\bCategory:\s*([^;\n"\r]+)',t)
  dates=re.findall(r'\bDate:\s*([^;\n"\r]+)',t)
  years=set(y for d in dates for y in re.findall(r'(?<!\d)\d{4}(?!\d)',d))
  cs=set(c.strip() for c in cats)
  if len(cs)!=1 or not cs.issubset({'finance','projects','personal'}) or len(years)!=1 or not dates or any(not re.search(r'(?<!\d)\d{4}(?!\d)',d) for d in dates):
   reason=f'Missing, invalid or conflicting Category/Date evidence: categories={sorted(cs)}, years={sorted(years)}; clarification required.'
 if reason:
  items[p]=dict(path=p,action='defer',destination=None,reason=reason);print(p, data)
  continue
 c=next(iter(cs));y=next(iter(years)); pp=PurePosixPath(p)
 dirs=[f'sorted/{c}/{y}',f'historic/{c}/{y}']
 if str(pp.parent) in dirs: items[p]=dict(path=p,action='keep',destination=None,reason=f'Contents confirm {c}/{y}; direct parent is policy-compliant.')
 else: groups[(c,y,pp.name)].append(p)
for (c,y,name),sources in groups.items():
 alternatives=[f'{root}/{c}/{y}/{name}' for root in ('sorted','historic')]
 free=[d for d in alternatives if d not in occupied]
 if len(sources)>len(free):
  reason=('Collision: both acceptable destinations occupied at inventory time: '+', '.join(alternatives) if not free else f'Contested destinations: {len(sources)} records compete for {len(free)} currently free paths: '+', '.join(free))+ '; all affected records deferred; user decision required; no renaming or merging.'
  for p in sources:items[p]=dict(path=p,action='defer',destination=None,reason=reason)
 else:
  for p,d in zip(sources,free):items[p]=dict(path=p,action='move',destination=d,reason=f'Contents confirm {c}/{y}; current parent noncompliant. Acceptable alternatives: '+', '.join(alternatives)+'. Selected destination is free at inventory time; preserve basename.')
plan=dict(items=[items[p] for p in paths],coverage=f'Adapter returned complete=true, {len(paths)} regular-file paths; every listed file read once through adapter, including all extensions. Read failures explicitly deferred. No archive files inspected directly. No unlisted contents assumed; no inventoried file omitted.',policy_conflicts='none',approval='proposed only, no action executed')
assert len(items)==len(paths)==len(set(paths))
moves=[i['destination'] for i in items.values() if i['action']=='move']
assert len(moves)==len(set(moves)) and not occupied.intersection(moves)
Path('/tmp/out/plan.json').write_text(json.dumps(plan,indent=2)+'\n')
print(collections.Counter(i['action'] for i in items.values()))
for i in items.values():
 if i['action']=='defer':print(json.dumps(i))
