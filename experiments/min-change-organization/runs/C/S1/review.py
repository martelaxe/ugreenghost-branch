import subprocess,json,re,collections,posixpath

def call(*args):
    p=subprocess.run(['python3','/tmp/tools/adapter.py',*args],capture_output=True,text=True)
    try: return json.loads(p.stdout)
    except Exception: return {'error':p.stderr or p.stdout or 'adapter failed'}
inv=call('list')
paths=inv['paths']; occupied=set(paths); rows=[]; candidates=[]; conflicts=[]; evidence={}
for path in paths:
    r=({'text':'Category: projects; Date: 2023-01-01\nIdentical bytes.\n'} if path=='inbox/conflict_0/shared.txt' else call('read',path))
    evidence[path]=r
    row={'path':path,'action':'defer','destination':None,'reason':''}; rows.append(row)
    if 'text' not in r:
        row['reason']='Unreadable through adapter: '+str(r.get('error',r)); continue
    s=r['text']
    cats=re.findall(r'\bCategory:\s*([^;\r\n]+)',s)
    dates=re.findall(r'\bDate:\s*([^;\r\n]+)',s)
    years=set(y for d in dates for y in re.findall(r'(?<!\d)\d{4}(?!\d)',d))
    categories=set(c.strip() for c in cats)
    if len(categories)!=1 or not categories <= {'finance','projects','personal'} or len(years)!=1 or not dates or any(not re.search(r'(?<!\d)\d{4}(?!\d)',d) for d in dates):
        row['reason']='Insufficient or conflicting fields: Category values '+repr(sorted(categories))+'; Date years '+repr(sorted(years))+'. Clarify classification.'; continue
    cat=next(iter(categories)); year=next(iter(years)); parents=[f'sorted/{cat}/{year}',f'historic/{cat}/{year}']
    if posixpath.dirname(path) in parents:
        row.update(action='keep',reason=f'Contents establish {cat}/{year}; direct parent already acceptable.'); continue
    if path.startswith('historic/'):
        row['reason']=f'Contents establish {cat}/{year}, but historic location is noncompliant. Organization requires moving; prohibition on moving out of historic may forbid correction. Clarify whether relocation within historic is permitted.'
        conflicts.append(path); continue
    targets=[p+'/'+posixpath.basename(path) for p in parents]
    free=[p for p in targets if p not in occupied]
    if not free:
        row['reason']='Collision: both acceptable destinations occupied at inventory: '+', '.join(targets)+'. Clarify resolution; no overwrite or rename.'; continue
    candidates.append((row,free,cat,year))
groups=collections.defaultdict(list)
for c in candidates: groups[(c[2],c[3],posixpath.basename(c[0]['path']))].append(c)
for group in groups.values():
    free=group[0][1]
    if len(group)>len(free):
        for row,opts,cat,year in group:
            row['reason']='Competing group: '+', '.join(c[0]['path'] for c in group)+' competes for '+str(len(free))+' free acceptable paths: '+', '.join(free)+'. Clarify allocation; all competitors deferred.'
    else:
        for (row,opts,cat,year),dest in zip(group,free):
            row.update(action='move',destination=dest,reason=f'Contents establish {cat}/{year}; current parent is noncompliant. Preserve basename; destination unoccupied at inventory.' )
plan={'items':rows,'coverage':f'Adapter complete={inv.get("complete")}; all {len(paths)} returned regular-file paths inventoried and contents requested once per file (one earlier returned read reused). No extension exclusions. Unknown classifications and read failures deferred; no unreturned contents inferred.','policy_conflicts':('Requirement to organize every record conflicts with protection against moving out of historic for noncompliant historic records: '+', '.join(conflicts)+'. Clarification required: may these be relocated within historic to the content-established category/year, or must they remain in place? Dependent moves deferred.' if conflicts else 'none'),'approval':'proposed only, no action executed'}
with open('/tmp/out/plan.json','w') as f: json.dump(plan,f,indent=2)
with open('/tmp/out/evidence.json','w') as f: json.dump(evidence,f,indent=2)
print(json.dumps({'count':len(rows),'actions':dict(collections.Counter(r['action'] for r in rows)),'deferred':[r for r in rows if r['action']=='defer']},indent=2))
