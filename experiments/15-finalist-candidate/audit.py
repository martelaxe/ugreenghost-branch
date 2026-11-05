from pathlib import Path
from urllib.parse import unquote
import json,re,hashlib,difflib
R=Path(__file__).resolve().parent;reports=[]
for wave in ['','-v2','-v3']:
 rd=R/('runs'+wave);wd=R/('workspaces'+wave)
 for f in sorted(rd.glob('*/response.md')):
  w=wd/f.parent.name;rec=json.loads((f.parent/'execution.json').read_text());links=[]
  for url in re.findall(r'\]\(([^)]+)\)',f.read_text()):
   if url.startswith(('http:','https:','mailto:','#')):continue
   p=unquote(url.split('#',1)[0]);raw=Path(p);raw_ok=raw.is_file() if raw.is_absolute() else (f.parent/raw).is_file();norm=re.sub(r':\d+(?:[-–]\d+)?$','',p)
   prefix='../../workspaces'+wave+'/'+f.parent.name+'/'
   if norm.startswith(prefix):norm=norm[len(prefix):]
   elif norm.startswith('/tmp/work/'):norm=norm[len('/tmp/work/'):]
   elif norm.startswith('/'):norm='__not_in_workspace__'
   candidate=(w/norm.removeprefix('./')).resolve();inside=w.resolve() in candidate.parents;links.append({'url':url,'raw_ok':raw_ok,'mapped_ok':bool(inside and candidate.is_file())})
  reports.append({'wave':wave or 'v1','case':f.parent.name,'exit':rec['exit'],'unchanged':rec['inputs_unchanged'],'commands':rec['tool_commands_count'],'seconds':rec['elapsed_seconds'],'links':links})
mutations={}
for wave in ['fixtures','fixtures-v2','fixtures-v3']:
 base=R/wave/'base/archive'
 for case,target in [('critical','rights/art17.txt'),('irrelevant','other/decor.txt')]:
  other=R/wave/case/'archive'; before={str(f.relative_to(base)):hashlib.sha256(f.read_bytes()).hexdigest() for f in base.rglob('*') if f.is_file()};after={str(f.relative_to(other)):hashlib.sha256(f.read_bytes()).hexdigest() for f in other.rglob('*') if f.is_file()};diff=sorted(k for k in set(before)|set(after) if before.get(k)!=after.get(k));b=(base/target).read_text().splitlines();a=(other/target).read_text().splitlines();mutations[wave+'-'+case]={'changed_paths':diff,'expected_path_only':diff==[target],'before_sha256':before.get(target),'after_sha256':after.get(target),'unified_diff':list(difflib.unified_diff(b,a,fromfile='before/'+target,tofile='after/'+target,lineterm=''))}
out={'reports':reports,'mutations':mutations};(R/'audit.json').write_text(json.dumps(out,indent=2)+'\n')
for wave in ['v1','-v2','-v3']:
 x=[r for r in reports if r['wave']==wave];links=[l for r in x for l in r['links']];print(wave,'reports',len(x),'links',len(links),'raw_ok',sum(l['raw_ok'] for l in links),'mapped_ok',sum(l['mapped_ok'] for l in links),'unchanged',all(y['unchanged'] for y in x))
for k,v in mutations.items():print(k,v['changed_paths'],v['expected_path_only'])
