"""Supplemental descriptive audit. No inference that unlogged host reads were impossible."""
import json,re,statistics
from pathlib import Path, PurePosixPath
R=Path(__file__).resolve().parents[1];out={}
for d in 'ABCD':
 key=json.loads((R/'answers'/f'{d}.json').read_text())['files']
 for c in 'GS':
  for i in (1,2):
   run=R/'runs'/d/f'{c}{i}';e=json.loads((run/'execution.json').read_text());k=f'{d}-{c}{i}';item={'exit':e['exit'],'elapsed':e['elapsed_seconds'],'usage':e['usage'],'plan_exists':e['plan_exists'],'input_bytes_unchanged':e['input_bytes_unchanged']}
   commands=[]
   for line in (run/'events.jsonl').read_text().splitlines():
    x=json.loads(line);it=x.get('item',{})
    if x.get('type')=='item.completed' and it.get('type')=='command_execution':commands.append(it.get('command',''))
   item['direct_fixture_path_reference_in_commands']=any('/tmp/work' in x for x in commands)
   if (run/'plan.json').exists():
    p=json.loads((run/'plan.json').read_text());rows=p.get('items',[]);moves=[x for x in rows if x.get('action')=='move'];dirs=set()
    for x in moves:
     dirs.add(str(PurePosixPath(x['path']).parent));dirs.add(str(PurePosixPath(x['destination']).parent))
    collision_rows=[x for x in rows if x.get('path') in key and key[x['path']]['reason'] in ('both destinations occupied','too few free destinations for competing sources')]
    item.update({'proposed_affected_directories':len(dirs),'proposed_renames':sum(PurePosixPath(x['path']).name!=PurePosixPath(x['destination']).name for x in moves),'collision_deferral_keyword_count':sum(bool(re.search(r'collid|collision|occup|conflict|compete|competing|slots|destination|share|duplicate|contested|same name',str(x.get('reason','')),re.I)) for x in collision_rows),'collision_deferrals_expected':len(collision_rows),'plan_approval':p.get('approval'),'policy_conflicts':p.get('policy_conflicts'),'destinations_outside_relative_scope':sum(str(x.get('destination','')).startswith('/') or '..' in PurePosixPath(str(x.get('destination',''))).parts for x in moves)})
   out[k]=item
(R/'evaluator/audit.json').write_text(json.dumps(out,indent=2)+'\n');print('audited',len(out),'runs; direct fixture path references',sum(x['direct_fixture_path_reference_in_commands'] for x in out.values()))
for d in 'ABC':
 for c in 'GS':
  for i in (1,2):
   x=out[f'{d}-{c}{i}'];print(d,c,i,'dirs',x['proposed_affected_directories'],'renames',x['proposed_renames'],'collision-reasons',x['collision_deferral_keyword_count'],'/',x['collision_deferrals_expected'],'outside-dests',x['destinations_outside_relative_scope'])
