"""Create clearly labeled derived local copies with validated links; originals unchanged."""
from pathlib import Path
from urllib.parse import unquote
import json,re
R=Path(__file__).resolve().parent;count=0
for f in sorted((R/'runs').glob('*/response.md')):
 w=(R/'workspaces'/f.parent.name).resolve();s=f.read_text();replaced=[0]
 def repl(match):
  label,url=match.group(1),match.group(2)
  if url.startswith(('http://','https://','mailto:','#')):return match.group(0)
  path=unquote(url.split('#')[0]);path=re.sub(r':\d+(?:[-–]\d+)?$','',path)
  rel=path[len('/tmp/work/'):] if path.startswith('/tmp/work/') else path.removeprefix('./')
  p=(w/rel).resolve()
  if w not in p.parents or not p.is_file():return match.group(0)
  replaced[0]+=1;return '['+label+'](../../workspaces/'+f.parent.name+'/'+p.relative_to(w).as_posix()+')'
 new=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',repl,s)
 out=f.parent/'response-portable.md';out.write_text('> Locally adapted copy: only source-link targets were rewritten to the archived fixture; the raw model response is in `response.md`. This is not a UGREEN capability.\n\n'+new)
 count+=replaced[0]
print('Rewritten validated local links:',count)
