"""Mechanically check Markdown source links only, relative to assigned fixture."""
import json,re
from pathlib import Path
BASE=Path(__file__).resolve().parent
status=json.loads((BASE/'execution/status.json').read_text()); out=[]
for run in status['runs']:
 tag=f"{run['case']}-{run['method']}-{run['trial']}";report=BASE/'execution'/(tag+'.md')
 if not report.exists(): out.append({'run':tag,'missing_report':True});continue
 links=re.findall(r'\]\(([^)]+)\)',report.read_text()); checked=[]
 for target in links:
  path=target.split('#')[0].strip('<>')
  if path.startswith(('http://','https://','mailto:','#')):checked.append({'target':target,'status':'external-or-anchor-not-audited'});continue
  if path.startswith('/tmp/work/'):
   rel=path[len('/tmp/work/'):]
  elif path.startswith('/'): checked.append({'target':target,'status':'invalid-absolute'});continue
  else:rel=path
  dest=(Path(run['workspace'])/rel).resolve();src=Path(run['workspace']).resolve()
  if not dest.is_relative_to(src):stat='outside-workspace'
  elif dest.is_file():stat='exists'
  else:stat='not-found'
  checked.append({'target':target,'status':stat})
 out.append({'run':tag,'markdown_links':checked,'bad_count':sum(x['status'] not in ('exists','external-or-anchor-not-audited') for x in checked),'audited_count':sum(x['status'] not in ('external-or-anchor-not-audited',) for x in checked),'note':'Bare filenames and logical support require separate review.'})
(BASE/'review/automated-link-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print('Markdown citation path audit recorded; bare filenames and semantics excluded.')
