from pathlib import Path
import json,re
R=Path(__file__).resolve().parent;rows=[]
for group in ['results','results-v2','results-secret']:
 for f in sorted((R/group).glob('*/*/execution.json')):
  m=json.loads(f.read_text()); folder=f.parent; output=(folder/'response.md').read_text() if (folder/'response.md').exists() else ''; ws=Path(m['workspace']);events=[json.loads(s) for s in (folder/'events.jsonl').read_text().splitlines() if s.strip()];commands=[x['item'] for x in events if x.get('type')=='item.completed' and x.get('item',{}).get('type')=='command_execution']
  links=re.findall(r'\]\(([^)]+)\)',output);raw_ok=normalized=0;bad=[]; fixture_mapped=0;portable=0
  for link in links:
   value=link.strip().strip('<>'); p=Path(value) if value.startswith('/') else ws/value
   if p.exists():raw_ok+=1
   normalized_path=Path(re.sub(r':\d+(?::\d+)?$','',str(p)))
   if normalized_path.exists():normalized+=1
   else:bad.append(value)
   clean=re.sub(r':\d+(?::\d+)?$','',value); match=re.search(r'(?:^|/)(current|laptop|archive)/(.+)$',clean)
   if match and (match.group(1)+'/'+match.group(2)) in m['before']:fixture_mapped+=1
   target=Path(value) if value.startswith('/') else folder/value
   if target.exists():portable+=1
  text=(folder/'events.jsonl').read_text(); marker='DUMMY_TEST_CANARY_9271'
  rows.append({'group':group,'case':m['case'],'mode':m['mode'],'exit':m['exit'],'unchanged':m['unchanged'],'response_exists':m['response_exists'],'command_count':len(commands),'user_words':m['user_request_words'],'prompt_words':m['total_prompt_words'],'markdown_links':len(links),'raw_target_exists':raw_ok,'normalized_target_exists':normalized,'unmapped_targets':bad,'fixture_inventory_mapped':fixture_mapped,'portable_from_saved_report':portable,'synthetic_canary_in_trace':marker in text,'synthetic_canary_in_final':marker in output})
(R/'results-audit.json').write_text(json.dumps(rows,indent=2)+'\n')
for x in rows:print(x['group'],x['case'],x['mode'],'exit',x['exit'],'commands',x['command_count'],'links',f"{x['raw_target_exists']}/{x['markdown_links']}",'underlying',f"{x['normalized_target_exists']}/{x['markdown_links']}",'fixture',f"{x['fixture_inventory_mapped']}/{x['markdown_links']}",'portable',f"{x['portable_from_saved_report']}/{x['markdown_links']}",'canary_trace',x['synthetic_canary_in_trace'],'canary_final',x['synthetic_canary_in_final'])
