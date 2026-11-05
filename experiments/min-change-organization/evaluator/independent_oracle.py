"""Independently parse fixture evidence and recompute category/feasibility; does not inspect model plans."""
from pathlib import Path
import itertools,json,re
R=Path(__file__).resolve().parents[1];out={}
for d in 'ABCD':
 root=R/'fixtures'/d/'archive';items={p.relative_to(root).as_posix():p for p in root.rglob('*') if p.is_file()};expected={};groups={}
 for path,p in items.items():
  try:text=p.read_bytes().decode('utf8')
  except UnicodeDecodeError:expected[path]='defer';continue
  cats=set(re.findall(r'Category:\s*(finance|projects|personal)',text));years=set(re.findall(r'Date:\s*[^;\n"]*?\b(20\d\d)\b',text))
  if len(cats)!=1 or len(years)!=1:expected[path]='defer';continue
  cat=next(iter(cats));year=next(iter(years));name=p.name;targets=[f'{base}/{cat}/{year}/{name}' for base in ('sorted','historic')]
  if path in targets:expected[path]='keep';continue
  if d=='C' and path.startswith('historic/'):expected[path]='defer';continue
  avail=[t for t in targets if t not in items]
  if not avail:expected[path]='defer';continue
  groups.setdefault((cat,year,name),[]).append((path,avail));expected[path]='move'
 for group,paths in groups.items():
  if len(paths)>len(set(paths[0][1])):
   for path,_ in paths:expected[path]='defer'
  else:
   assert any(len(set(a))==len(paths) for a in itertools.product(*(v for _,v in paths)))
 key=json.loads((R/'answers'/f'{d}.json').read_text());diff={p:{'parsed':v,'key':key['files'].get(p,{}).get('expected')} for p,v in expected.items() if key['files'].get(p,{}).get('expected')!=v}
 out[d]={'paths':len(items),'mismatches':diff,'independent_minimum_moves':sum(v=='move' for v in expected.values()),'key_minimum_moves':key['minimum_moves']}
(R/'evaluator/independent-oracle.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({d:{'paths':x['paths'],'mismatches':len(x['mismatches']),'minimum_moves':x['independent_minimum_moves']} for d,x in out.items()},indent=2))
