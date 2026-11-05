from pathlib import Path
import json,hashlib,xml.sax.saxutils as X
P=Path(__file__).parent; A=P/'fictional-assets';O=P/'outputs';A.mkdir(exist_ok=True);O.mkdir(exist_ok=True)
# Real SVG drawings; all descriptions and roles are fictional, manually supplied fixture metadata.
data=[('arrival-red','arrival','red','#c3423f','people arrive'),('arrival-blue','arrival','blue','#347bb2','people arrive'),('workshop-red','workshop','red','#b42b3d','hands build together'),('workshop-blue','workshop','blue','#246eae','hands build together'),('ending-green','ending','green','#4b935d','display opens')]
manifest=[]
for name,role,color,fill,meaning in data:
 shapes={'arrival':'<rect x="30" y="18" width="46" height="60" fill="#eee"/><circle cx="62" cy="48" r="3" fill="#222"/><path d="M110 48 H155 M145 38 L155 48 L145 58" fill="none" stroke="white" stroke-width="5"/>','workshop':'<path d="M35 22 L90 77 M90 22 L35 77" stroke="white" stroke-width="10"/><circle cx="130" cy="50" r="23" fill="none" stroke="white" stroke-width="8"/>','ending':'<path d="M45 75 V20 L100 33 L45 48" stroke="white" stroke-width="5" fill="#eee"/><path d="M120 75 L150 23 L180 75 Z" fill="white"/>'}
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="200" height="100"><rect width="200" height="100" rx="8" fill="{fill}"/>{shapes[role]}<text x="10" y="92" fill="#fff">{X.escape(name)}</text></svg>'
 (A/(name+'.svg')).write_text(svg);manifest.append({'path':'fictional-assets/'+name+'.svg','role':role,'declared_color':color,'declared_subject':meaning})
(P/'fixture-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in A.glob('*')}
def render(label,excluded):
 chosen=[]
 for role in ['arrival','workshop','ending']:
  item=next((x for x in manifest if x['role']==role and x['declared_color'] not in excluded),None);chosen.append((role,item))
 panels=[]
 for n,(role,item) in enumerate(chosen):
  x=20+n*220
  if item:
   raw=(P/item['path']).read_text();inside=raw[raw.index('>')+1:raw.rindex('</svg>')];panels.append(f'<g transform="translate({x},50)">{inside}</g><text x="{x}" y="40">{role}: {item["declared_color"]}</text>')
  else:panels.append(f'<rect x="{x}" y="50" width="200" height="100" fill="#ddd"/><text x="{x}" y="40">{role}: NO SUPPORTED ASSET</text>')
 out='<svg xmlns="http://www.w3.org/2000/svg" width="680" height="180"><rect width="680" height="180" fill="white"/><g font-family="sans-serif" font-size="14">'+''.join(panels)+'</g></svg>'
 (O/(label+'.svg')).write_text(out)
 result={'excluded_declared_colors':sorted(excluded),'selected':{r:(i['path'] if i else None) for r,i in chosen},'missing_roles':[r for r,i in chosen if i is None]}
 (O/(label+'.json')).write_text(json.dumps(result,indent=2)+'\n');return result
results={'baseline':render('baseline',set()),'no-red':render('no-red',{'red'}),'no-red-or-blue':render('no-red-or-blue',{'red','blue'})}
after={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in A.glob('*')};assert before==after
(P/'observations.json').write_text(json.dumps({'results':results,'source_hashes_before':before,'source_hashes_after':after,'sources_unchanged':before==after,'runtime':'local deterministic Python using hand-authored fixture labels; no AI or NAS'},indent=2)+'\n');print(json.dumps(results,indent=2))
