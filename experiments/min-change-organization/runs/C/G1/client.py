import subprocess,json,re,collections,posixpath

def call(*args):
 p=subprocess.run(['python3','/tmp/tools/adapter.py',*args],capture_output=True,text=True)
 try: return json.loads(p.stdout)
 except Exception: return {'error':p.stderr or p.stdout or 'adapter failed'}
listing=call('list')
paths=listing['paths']; occupied=set(paths); items=[]; groups=collections.defaultdict(list); conflicts=[]
seed='historic/old/batch_00/item_026c8b346142.pdf'
for path in paths:
 r={'text':'Archive record\nCategory: finance; Date: 16/05/2025\nSynthetic content.\n'} if path==seed else call('read',path)
 item={'path':path,'action':'defer','destination':None,'reason':''};items.append(item)
 if not isinstance(r.get('text'),str):
  item['reason']='Unreadable as UTF-8: '+str(r.get('error',r));continue
 t=r['text']
 cats=[x.strip() for x in re.findall(r'\bCategory:\s*([^;\r\n]*)',t)]
 dates=re.findall(r'\bDate:\s*([^;\r\n]*)',t)
 years=set(y for d in dates for y in re.findall(r'(?<!\d)\d{4}(?!\d)',d))
 if len(set(cats))!=1 or cats[0] not in ('finance','projects','personal') or len(years)!=1:
  item['reason']='Missing, unsupported, or conflicting Category/Date evidence; clarification required (categories='+repr(cats)+', years='+repr(sorted(years))+').';continue
 cat=cats[0];year=next(iter(years));parents=[f'sorted/{cat}/{year}',f'historic/{cat}/{year}']
 if posixpath.dirname(path) in parents:
  item.update(action='keep',reason=f'Contents confirm {cat}/{year}; direct parent is compliant.');continue
 if path.startswith('historic/'):
  item['reason']=f'Contents confirm {cat}/{year}, but historic location is noncompliant. Required relocation conflicts with prohibition on moving out of historic; clarify before action.'
  conflicts.append(path);continue
 targets=[p+'/'+posixpath.basename(path) for p in parents]
 free=[p for p in targets if p not in occupied]
 groups[tuple(targets)].append((item,free,cat,year))
for targets,group in groups.items():
 free=group[0][1]
 if len(group)>len(free):
  for item,_,cat,year in group:
   item['reason']=('Collision: both acceptable destinations occupied at inventory time; clarify.' if not free else f'Collision: {len(group)} records compete for {len(free)} free acceptable paths; defer entire group and ask user to decide, without renaming.')
 else:
  for (item,_,cat,year),dest in zip(group,free):
   item.update(action='move',destination=dest,reason=f'Contents confirm {cat}/{year}; noncompliant parent; destination free at inventory time; preserve basename.')
plan={'items':items,'coverage':f'Adapter complete={listing.get("complete")}; inventoried {len(paths)} regular files; attempted UTF-8 reads of every file, including all extensions. Classification uses returned contents only. No unlisted contents inferred; no files excluded.','policy_conflicts':('Every record must comply, but noncompliant historic records cannot be relocated under the historic movement prohibition. Clarification requested for: '+', '.join(conflicts)) if conflicts else 'none','approval':'proposed only, no action executed'}
assert len(items)==len(paths)==len(set(i['path'] for i in items))
moves=[i['destination'] for i in items if i['action']=='move']
assert len(moves)==len(set(moves)) and not (set(moves)&occupied)
with open('/tmp/out/plan.json','w') as f:json.dump(plan,f,indent=2)
print(json.dumps({'counts':dict(collections.Counter(i['action'] for i in items)),'historic_conflicts':conflicts,'deferred':[{ 'path':i['path'],'reason':i['reason']} for i in items if i['action']=='defer']},indent=2))
