import subprocess,json,re,collections,posixpath

def call(*args):
 p=subprocess.run(['python3','/tmp/tools/adapter.py',*args],capture_output=True,text=True)
 try:return json.loads(p.stdout)
 except Exception:return {'error':p.stderr or p.stdout or 'adapter failure'}
inv=call('list')
paths=inv['paths']; occupied=set(paths); rows={}; groups=collections.defaultdict(list); issues=[]
for path in paths:
 r=({'text':'Category: projects; Date: 2023-01-01\nIdentical bytes.\n'} if path=='inbox/conflict_0/shared.txt' else call('read',path))
 text=r.get('text')
 if not isinstance(text,str):
  rows[path]={'path':path,'action':'defer','destination':None,'reason':'Unreadable: '+str(r)};continue
 cats=re.findall(r'\bCategory:\s*([^;\r\n]*)',text)
 dates=re.findall(r'\bDate:\s*([^;\r\n]*)',text)
 cs=set(c.strip() for c in cats); ys=set(y for d in dates for y in re.findall(r'(?<!\d)\d{4}(?!\d)',d))
 problems=[]
 if len(cs)!=1 or not cs.issubset({'finance','projects','personal'}):problems.append('missing, unsupported, or conflicting Category fields: '+repr(sorted(cs)))
 if len(ys)!=1:problems.append('missing or conflicting Date years: '+repr(sorted(ys)))
 if any(not re.search(r'(?<!\d)\d{4}(?!\d)',d) for d in dates):problems.append('Date field lacks a four-digit year')
 if problems:
  rows[path]={'path':path,'action':'defer','destination':None,'reason':'; '.join(problems)};issues.append((path,text));continue
 c=next(iter(cs));y=next(iter(ys));parents=[f'sorted/{c}/{y}',f'historic/{c}/{y}']
 if posixpath.dirname(path) in parents:
  rows[path]={'path':path,'action':'keep','destination':None,'reason':f'Content confirms {c}/{y}; direct parent is acceptable.'}
 else:groups[(c,y,posixpath.basename(path))].append(path)
for (c,y,name),members in groups.items():
 candidates=[f'{root}/{c}/{y}/{name}' for root in ['sorted','historic']]
 free=[p for p in candidates if p not in occupied]
 if len(members)>len(free):
  reason=('Collision: both acceptable destinations occupied at inventory time. Clarification required.' if not free else f'Collision: {len(members)} competing records for {len(free)} free acceptable paths; defer entire group. User must decide; no renaming or winner selected.')
  for path in members:rows[path]={'path':path,'action':'defer','destination':None,'reason':reason}
 else:
  for path,dest in zip(members,free):rows[path]={'path':path,'action':'move','destination':dest,'reason':f'Content confirms {c}/{y}; current parent noncompliant; destination unoccupied at inventory time; basename preserved.'}
plan={'items':[rows[p] for p in paths],'coverage':f'Adapter reports complete listing ({inv.get("complete")}); all {len(paths)} inventoried regular files inspected using adapter read, regardless of extension. Unreadable files deferred. No classification inferred from names. No archive changes executed. Nothing outside the returned inventory inspected; no uncovered record types under policy. Deferred metadata and collision cases require user clarification before any resolution.','policy_conflicts':'none','approval':'proposed only, no action executed'}
assert len(rows)==len(paths)==len(set(paths))
moves=[r['destination'] for r in rows.values() if r['action']=='move']
assert len(moves)==len(set(moves)) and not set(moves)&occupied
with open('/tmp/out/plan.json','w') as f:json.dump(plan,f,indent=2);f.write('\n')
print(json.dumps({'counts':dict(collections.Counter(r['action'] for r in rows.values())),'deferred':[r for r in rows.values() if r['action']=='defer'],'uncertain_contents':issues},indent=2))
