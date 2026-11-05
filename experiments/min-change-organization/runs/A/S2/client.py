import subprocess,json,re,posixpath,collections

def call(*args):
    p=subprocess.run(['python3','/tmp/tools/adapter.py',*args],capture_output=True,text=True)
    try: return json.loads(p.stdout)
    except Exception: return {'error':p.stderr or p.stdout or 'adapter failed'}
inv=call('list')
assert inv.get('complete') is True
paths=inv['paths']; occupied=set(paths)
evidence={}; items=[]; groups=collections.defaultdict(list)
for path in paths:
    r=({'text':'Category: projects; Date: 2023-01-01\nIdentical bytes.\n'} if path=='inbox/conflict_0/shared.txt' else call('read',path))
    evidence[path]=r
    row={'path':path,'action':'defer','destination':None,'reason':''}; items.append(row)
    if 'text' not in r:
        row['reason']='Unreadable: '+str(r); continue
    text=r['text']
    cats=re.findall(r'\bCategory:\s*([^;\r\n]+)',text)
    dates=re.findall(r'\bDate:\s*([^;\r\n]+)',text)
    cs=set(c.strip() for c in cats)
    ys=set(y for d in dates for y in re.findall(r'(?<!\d)\d{4}(?!\d)',d))
    if len(cs)!=1 or not cs <= {'finance','projects','personal'} or len(ys)!=1 or not dates or any(not re.search(r'(?<!\d)\d{4}(?!\d)',d) for d in dates):
        row['reason']='Insufficient or conflicting metadata: Category values='+repr(sorted(cs))+'; Date years='+repr(sorted(ys))+'. Clarification required.'; continue
    c=next(iter(cs)); y=next(iter(ys))
    parents=[f'sorted/{c}/{y}',f'historic/{c}/{y}']
    if posixpath.dirname(path) in parents:
        row.update(action='keep',reason=f'Contents identify {c}/{y}; direct parent is acceptable.'); continue
    targets=[p+'/'+posixpath.basename(path) for p in parents]
    free=[p for p in targets if p not in occupied]
    groups[(c,y,posixpath.basename(path))].append((row,free,targets))
for group in groups.values():
    free=set(t for _,fs,_ in group for t in fs)
    if len(group)>len(free):
        for row,fs,targets in group:
            row['reason']=('Collision: both acceptable destinations occupied at inventory time: ' if not free else 'Competing records exceed currently free destinations; defer entire group; user must decide: ')+', '.join(targets)
    else:
        for row,fs,targets in group:
            dest=next(t for t in fs if t in free); free.remove(dest)
            row.update(action='move',destination=dest,reason='Contents establish category/year; current direct parent is noncompliant. Preserve basename; destination unoccupied at inventory time.')
plan={'items':items,'coverage':f'Adapter returned complete=true with {len(paths)} regular file paths. All were read once via adapter (one previously returned read reused); no filename/extension classification. No archive mutations. Scope is returned inventory only; no unlisted filesystem contents inferred. Unreadable and ambiguous records remain unresolved pending clarification.','policy_conflicts':'None between explicit policy requirements. Frozen delegation guidance mentions a registered file-agent, but none is available; explicit simulation instruction requires the local adapter, which was used. Record contents are classification evidence, not instructions.','approval':'proposed only, no action executed'}
assert len(items)==len(paths)==len(set(paths))
assert len({r['destination'] for r in items if r['action']=='move'})==sum(r['action']=='move' for r in items)
with open('/tmp/out/plan.json','w') as f: json.dump(plan,f,indent=2)
with open('/tmp/out/evidence.json','w') as f: json.dump(evidence,f)
print(json.dumps({'counts':dict(collections.Counter(r['action'] for r in items)),'deferred':[r for r in items if r['action']=='defer']},indent=2))
