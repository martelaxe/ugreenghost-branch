"""Check model Markdown source links against fixtures; stripping nonportable line notation."""
import json,re
from pathlib import Path
root=Path(__file__).resolve().parent
out=[]
for case in ('normal','incomplete','permission'):
 for method in ('G','S'):
  p=root/'outputs'/f'{case}-{method}'/'raw-response.md';text=p.read_text();audit=[]
  for target in re.findall(r'\]\(([^)]+)\)',text):
   raw=target.strip('<>');path=re.sub(r':\d+(?:[–-]\d+)?$','',raw.removeprefix('/tmp/work/'))
   exists=(root/'fixtures'/case/path).is_file()
   audit.append({'target':target,'normalized_fixture_path':path,'source_exists_after_normalization':exists,'host_portable':False,'reason':'Path points into temporary workspace or uses workspace-relative path with line suffix.'})
  out.append({'case':case,'method':method,'links':audit,'missing_after_normalization':sum(not x['source_exists_after_normalization'] for x in audit),'note':'Only Markdown links checked. Valid line-number resolution and semantic entailment are not established.'})
(root/'link-audit.json').write_text(json.dumps(out,indent=2)+'\n')
for x in out:print(x['case'],x['method'],'markdown links',len(x['links']),'missing source after normalization',x['missing_after_normalization'])
