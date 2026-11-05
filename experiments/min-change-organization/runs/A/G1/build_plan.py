import subprocess,json,re,posixpath,collections

def call(*args):
 p=subprocess.run(['python3','/tmp/tools/adapter.py',*args],capture_output=True,text=True)
 try: return json.loads(p.stdout)
 except Exception: return {'error':p.stderr or p.stdout or 'adapter failed'}
inv=call('list')
paths=inv['paths']; occupied=set(paths); items=[]; groups=collections.defaultdict(list)
for path in paths:
 data=({'text':'Category: projects; Date: 2023-01-01\nIdentical bytes.\n'} if path=='inbox/conflict_0/shared.txt' else call('read',path))
 s=data.get('text')
 row={'path':path,'action':'defer','destination':None,'reason':''};items.append(row)
 if not isinstance(s,str):
  row['reason']='Unreadable through adapter: '+str(data.get('error',data));continue
 cats=set(v.strip() for v in re.findall(r'\bCategory:\s*([^;\r\n]*)',s))
 dates=re.findall(r'\bDate:\s*([^;\r\n]*)',s)
 years=set(y for d in dates for y in re.findall(r'(?<!\d)\d{4}(?!\d)',d))
 issues=[]
 if len(cats)!=1 or not cats.issubset({'finance','projects','personal'}): issues.append('missing, conflicting, or unsupported Category values: '+repr(sorted(cats)))
 if len(years)!=1: issues.append('missing or conflicting Date years: '+repr(sorted(years)))
 if issues: row['reason']='; '.join(issues)+'; clarification required';continue
 cat=next(iter(cats));year=next(iter(years));parents=[f'sorted/{cat}/{year}',f'historic/{cat}/{year}']
 if posixpath.dirname(path) in parents:
  row.update(action='keep',reason=f'Contents establish {cat}/{year}; direct parent is acceptable');continue
 basename=posixpath.basename(path)
 free=[p+'/'+basename for p in parents if p+'/'+basename not in occupied]
 groups[(cat,year,basename)].append((row,free))
for key,group in groups.items():
 free=group[0][1]
 if len(group)>len(free):
  reason=('Collision: both acceptable destinations occupied at inventory time' if not free else f'Collision: {len(group)} records compete for {len(free)} free acceptable destinations; defer entire group')+'; user decision required; no renaming or overwriting'
  for row,_ in group: row['reason']=reason
 else:
  for (row,_),dest in zip(group,free): row.update(action='move',destination=dest,reason=f'Contents establish {key[0]}/{key[1]}; current parent is noncompliant; destination unoccupied at inventory time; basename preserved')
plan={'items':items,'coverage':f'Adapter reports complete inventory: {len(paths)} regular files; all contents requested through adapter (one earlier read reused). No extension or filename used for classification. No unlisted archive contents inspected. Uncertain records and collisions require clarification; all other files covered.','policy_conflicts':'none','approval':'proposed only, no action executed'}
assert len(items)==len(set(paths))
dests=[i['destination'] for i in items if i['action']=='move']
assert len(dests)==len(set(dests)) and not occupied.intersection(dests)
with open('/tmp/out/plan.json','w') as f: json.dump(plan,f,indent=2); f.write('\n')
print(json.dumps(dict(collections.Counter(i['action'] for i in items))))
print(json.dumps([i for i in items if i['action']=='defer'],indent=2))
