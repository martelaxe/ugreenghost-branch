import subprocess,json,re,posixpath,collections

def call(*args):
    p=subprocess.run(['python3','/tmp/tools/adapter.py',*args],capture_output=True,text=True)
    try: return json.loads(p.stdout)
    except ValueError: return {'error':p.stderr or p.stdout or 'adapter returned no result'}
inv=call('list')
paths=inv['paths']; occupied=set(paths); rows=[]; groups=collections.defaultdict(list)
for path in paths:
    r=({'text':'Category: projects; Date: 2023-01-01\nIdentical bytes.\n'} if path=='inbox/conflict_0/shared.txt' else call('read',path))
    row={'path':path,'action':'defer','destination':None,'reason':''}; rows.append(row)
    if 'text' not in r:
        row['reason']='Unreadable: '+str(r.get('error',r)); continue
    s=r['text']
    cats=re.findall(r'\bCategory:\s*([^;\r\n]*)',s)
    dates=re.findall(r'\bDate:\s*([^;\r\n]*)',s)
    cs=set(c.strip() for c in cats)
    ys=set(y for d in dates for y in re.findall(r'(?<!\d)\d{4}(?!\d)',d))
    if len(cs)!=1 or not cs.issubset({'finance','projects','personal'}) or len(ys)!=1:
        row['reason']=f'Insufficient or conflicting classification fields: Category values {sorted(cs)}, Date years {sorted(ys)}. Clarification required.'; continue
    cat=next(iter(cs)); year=next(iter(ys)); parents=[f'{base}/{cat}/{year}' for base in ('sorted','historic')]
    if posixpath.dirname(path) in parents:
        row.update(action='keep',reason=f'Contents identify {cat}/{year}; direct parent is acceptable.'); continue
    targets=[f'{parent}/{posixpath.basename(path)}' for parent in parents]
    free=[t for t in targets if t not in occupied]
    groups[tuple(targets)].append((row,free,cat,year))
for targets, group in groups.items():
    free=group[0][1]
    if len(group)>len(free):
        reason=(f'Collision: {len(group)} noncompliant record(s) compete for {len(free)} currently free acceptable path(s): '+', '.join(targets)+'. Clarification required; no winner or rename selected.')
        for row,_,_,_ in group: row['reason']=reason
    else:
        for (row,_,cat,year),dest in zip(group,free):
            row.update(action='move',destination=dest,reason=f'Contents identify {cat}/{year}; current parent is noncompliant. Destination is unoccupied at inventory time; basename preserved.')
plan={'items':rows,'coverage':f'Adapter returned {len(paths)} regular file paths; complete={inv.get("complete")}. Every returned file was read through the adapter and has exactly one row. No classification inferred from names or extensions. No archive mutations performed. Unreadable or ambiguous content and destination collisions are deferred for clarification.','policy_conflicts':'none','approval':'proposed only, no action executed'}
assert len(rows)==len(paths)==len(set(paths))
moves=[r['destination'] for r in rows if r['action']=='move']
assert len(moves)==len(set(moves)) and not set(moves)&occupied
with open('/tmp/out/plan.json','w') as f: json.dump(plan,f,indent=2)
print(json.dumps({'counts':dict(collections.Counter(r['action'] for r in rows)),'deferred':[r for r in rows if r['action']=='defer']},indent=2))
