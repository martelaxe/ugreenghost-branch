import json,re,posixpath,collections
with open('/tmp/out/evidence.json') as f: evidence=json.load(f)
paths=evidence['listing']['paths']; occupied=set(paths); items=[]; groups=collections.defaultdict(list)
for path in paths:
    r=evidence['reads'][path]; row={'path':path,'action':'defer','destination':None,'reason':''}; items.append(row)
    if 'text' not in r:
        row['reason']='Adapter UTF-8 read failed; category/year unknown. Please provide readable evidence.'; continue
    t=r['text']
    cats=set(re.findall(r'Category:\s*([A-Za-z]+)',t))
    dates=re.findall(r'Date:\s*([^;\n"\\]+)',t)
    years=set(y for d in dates for y in re.findall(r'(?<!\d)\d{4}(?!\d)',d))
    if len(cats)!=1 or not cats<= {'finance','projects','personal'} or len(years)!=1 or not dates:
        row['reason']=f'Insufficient or conflicting fields: categories={sorted(cats)}, Date years={sorted(years)}. Please clarify authoritative category/year.'; continue
    cat=next(iter(cats)); year=next(iter(years)); parents=[f'sorted/{cat}/{year}',f'historic/{cat}/{year}']
    if posixpath.dirname(path) in parents:
        row.update(action='keep',reason=f'Content confirms {cat}/{year}; direct parent is acceptable.'); continue
    alternatives=[p+'/'+posixpath.basename(path) for p in parents]
    free=[p for p in alternatives if p not in occupied]
    if path.startswith('historic/'):
        row['reason']=f'Content confirms {cat}/{year}; current parent violates policy. Clarify historic move restriction before correction: does it permit relocation within historic/? Acceptable targets: '+', '.join(alternatives)+'. No move proposed pending resolution.'; continue
    groups[(cat,year,posixpath.basename(path))].append((row,free,alternatives))
for group in groups.values():
    free=group[0][1]; alternatives=group[0][2]
    if len(group)>len(free):
        for row,_,_ in group:
            if not free: row['reason']='Collision: both acceptable targets occupied at inventory time: '+', '.join(alternatives)+'. Please decide a policy-compliant resolution; no overwrite or rename.'
            else: row['reason']=f'Contested destinations: {len(group)} records compete for {len(free)} currently free paths: '+', '.join(free)+'. Defer entire group; please decide. No duplicate merge or rename.'
    else:
        for (row,_,_),dest in zip(group,free):
            row.update(action='move',destination=dest,reason='Content confirms category/year; current parent is noncompliant. Preserve basename; destination free at inventory time. Acceptable alternatives: '+', '.join(alternatives)+'.')
counts=collections.Counter(r['action'] for r in items)
plan={'items':items,'coverage':f"Adapter complete=true inventory: {len(paths)} regular files, exactly one row each. Every file read once through adapter (four UTF-8 errors); no classification from names/extensions. Two list calls returned inventory; first read reused. Counts: {dict(counts)}. No unlisted archive contents inferred; no archive files changed. All inventoried files covered; unreadable/conflicting metadata remain unknown.",'policy_conflicts':'Historic correction requirement and historic move restriction need clarification for 12 noncompliant historic/old records: does the restriction forbid their relocation, or allow moving within historic/ to the correct category/year? These files are deferred pending an explicit resolution; neither interpretation is imposed. Separately, clarify authoritative metadata for conflicting records, supply readable evidence for unreadable records, and resolve occupied/contested targets as identified in deferred rows.','approval':'proposed only, no action executed'}
assert len(items)==len(set(paths))
dests=[r['destination'] for r in items if r['action']=='move']
assert len(dests)==len(set(dests)) and not occupied.intersection(dests)
with open('/tmp/out/plan.json','w') as f: json.dump(plan,f,indent=2); f.write('\n')
print(json.dumps({'files':len(paths),'counts':dict(counts),'unique_free_move_destinations':len(dests)}))
