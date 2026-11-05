import json,re
from pathlib import PurePosixPath
with open('/tmp/out/returned.json') as f: data=json.load(f)
items=[]
for r in data['reads']:
    content=json.loads(r['stdout'])['text']
    categories=set(re.findall(r'Category:\s*(finance|projects|personal)\b',content))
    dates=re.findall(r'Date:\s*([0-9/-]+)',content)
    years={y for d in dates for y in re.findall(r'(?<!\d)\d{4}(?!\d)',d)}
    assert len(categories)==len(years)==1
    category=next(iter(categories)); year=next(iter(years))
    parent=str(PurePosixPath(r['path']).parent)
    assert parent in [f'sorted/{category}/{year}',f'historic/{category}/{year}']
    items.append({'path':r['path'],'action':'keep','destination':None,'reason':f'Contents uniquely identify {category}, {year}; direct parent is policy-compliant.'})
plan={'items':items,'coverage':'Adapter returned complete=true with 24 regular files; all 24 were read successfully as UTF-8 and assessed using Category and Date fields. All are already compliant. No required moves, uncertain files, destination collisions, or uncovered inventoried files were found. Coverage is limited to the selected simulated archive returned by the adapter.','policy_conflicts':'none','approval':'proposed only, no action executed'}
assert len(items)==len(data['inventory']['paths'])==24
assert len({i['path'] for i in items})==24
with open('/tmp/out/plan.json','w') as f: json.dump(plan,f,indent=2); f.write('\n')
print('Validated plan: 24 keep, 0 move, 0 defer; exactly one row per inventoried file.')
