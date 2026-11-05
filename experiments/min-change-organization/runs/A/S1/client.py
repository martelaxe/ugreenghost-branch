import subprocess,json,re,posixpath,collections

def call(*args):
    p=subprocess.run(['python3','/tmp/tools/adapter.py',*args],capture_output=True,text=True)
    try:return json.loads(p.stdout)
    except Exception:return {'error':p.stderr or p.stdout or 'adapter failed'}
listing=call('list')
paths=listing['paths']; occupied=set(paths); rows={}; groups=collections.defaultdict(list)
for path in paths:
    result={'text':'Category: projects; Date: 2023-01-01\nIdentical bytes.\n'} if path=='inbox/conflict_0/shared.txt' else call('read',path)
    text=result.get('text')
    reason=None
    if not isinstance(text,str):reason='Unreadable through adapter: '+str(result.get('error',result))
    else:
        cats=set(x.strip().lower() for x in re.findall(r'Category:\s*([^;\r\n]*)',text))
        dates=re.findall(r'Date:\s*([^;\r\n]*)',text)
        years=set(y for d in dates for y in re.findall(r'(?<!\d)\d{4}(?!\d)',d))
        if len(cats)!=1 or not cats.issubset({'finance','projects','personal'}):reason='Missing, unsupported, or conflicting Category fields; clarification required.'
        elif not dates or len(years)!=1 or any(not re.search(r'(?<!\d)\d{4}(?!\d)',d) for d in dates):reason='Missing or conflicting Date years; clarification required.'
    if reason:
        rows[path]={'path':path,'action':'defer','destination':None,'reason':reason};continue
    cat=next(iter(cats));year=next(iter(years));dirs=[f'sorted/{cat}/{year}',f'historic/{cat}/{year}']
    if posixpath.dirname(path) in dirs:
        rows[path]={'path':path,'action':'keep','destination':None,'reason':f'Contents establish {cat}/{year}; direct parent is acceptable.'}
    else:
        dests=[d+'/'+posixpath.basename(path) for d in dirs]
        groups[(cat,year,posixpath.basename(path))].append((path,dests))
for key,group in groups.items():
    free=[d for d in group[0][1] if d not in occupied]
    if len(group)>len(free):
        for path,dests in group:
            rows[path]={'path':path,'action':'defer','destination':None,'reason':('Collision: both acceptable destinations occupied at inventory time. ' if not free else f'Competing group of {len(group)} records has only {len(free)} free acceptable destination(s). ')+ 'Clarification required; no winner or rename chosen. Alternatives: '+', '.join(dests)}
    else:
        for (path,dests),dest in zip(group,free):
            rows[path]={'path':path,'action':'move','destination':dest,'reason':f'Contents establish {key[0]}/{key[1]}; current parent is noncompliant; destination free at inventory time; basename preserved.'}
plan={'items':[rows[p] for p in paths],'coverage':f'Adapter returned complete={listing.get("complete")}; {len(paths)} regular files inventoried and all read through adapter (one earlier returned read reused). All extensions treated as records. No unlisted contents inferred. Deferred records require clarification; no additional file types excluded.','policy_conflicts':'none; competing destinations and insufficient classification evidence are deferred under explicit policy.','approval':'proposed only, no action executed'}
assert len(rows)==len(paths)==len(set(paths))
moves=[r['destination'] for r in rows.values() if r['action']=='move']
assert len(moves)==len(set(moves)) and not occupied.intersection(moves)
with open('/tmp/out/plan.json','w') as f:json.dump(plan,f,indent=2);f.write('\n')
print(json.dumps({'counts':dict(collections.Counter(r['action'] for r in rows.values())),'deferred':[r for r in rows.values() if r['action']=='defer']},indent=2))
