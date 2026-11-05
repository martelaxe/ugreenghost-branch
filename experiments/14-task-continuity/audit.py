from pathlib import Path
from urllib.parse import unquote
import json,re,hashlib
R=Path(__file__).resolve().parent
r=[]
for f in sorted((R/'runs').glob('*/response.md')):
 name=f.parent.name;w=R/'workspaces'/name;links=re.findall(r'\]\(([^)]+)\)',f.read_text());rows=[]
 for x in links:
  if x.startswith(('http://','https://','mailto:','#')):continue
  raw=unquote(x.split('#')[0]);rawpath=Path(raw);rawresolved=rawpath.is_file() if rawpath.is_absolute() else (f.parent/rawpath).is_file()
  cleaned=re.sub(r':\d+(?:[-–]\d+)?$','',raw)
  if cleaned.startswith('/tmp/work/'):relative=cleaned[len('/tmp/work/'):]
  elif cleaned.startswith('/tmp/'):relative=None
  else:relative=cleaned.removeprefix('./')
  mapped=(w/relative).resolve() if relative is not None else None
  allowed=bool(mapped and (mapped==w.resolve() or w.resolve() in mapped.parents));mappedexists=bool(allowed and mapped.is_file())
  rows.append({'link':x,'raw_resolves_from_report':rawresolved,'mapped_workspace_source_exists':mappedexists,'outside_workspace_or_unmapped':not allowed})
 rec=json.loads((f.parent/'execution.json').read_text());r.append({'run':name,'links':rows,'input_unchanged':rec['inputs_unchanged'],'tool_commands':rec['tool_commands_count'],'elapsed_seconds':rec['elapsed_seconds'],'exit':rec['exit']})
summary={'run_count':len(r),'links':sum(len(x['links']) for x in r),'raw_resolve':sum(y['raw_resolves_from_report'] for x in r for y in x['links']),'mapped_exists':sum(y['mapped_workspace_source_exists'] for x in r for y in x['links']),'all_inputs_unchanged':all(x['input_unchanged'] for x in r),'runs':r}
(R/'audit.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({k:v for k,v in summary.items() if k!='runs'},indent=2))
for x in r:
 bad=[y['link'] for y in x['links'] if not y['mapped_workspace_source_exists']]
 print(x['run'],'links',len(x['links']),'mapped missing',len(bad),'tools',x['tool_commands'],'sec',x['elapsed_seconds']);
 if bad:print('  ',bad[:8])
