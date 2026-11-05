from pathlib import Path
import re,json
R=Path(__file__).resolve().parent; root=R/'archive'; rows=[]
for report in sorted((R/'model-runs-fixed').glob('*/response.md')):
 s=report.read_text(); paths=[]
 for x in re.findall(r'`([^`]+)`',s):
  m=re.match(r'((?:projects|shared|admin)/[^\s`:]+)(?::[0-9].*)?$',x)
  if m:
   p=m.group(1); exists=(root/p).exists();paths.append({'path':p,'exists_in_initial_fixture':exists,'expected_missing_target':p=='projects/harbor/assets/launch-cover.txt'})
 rows.append({'report':str(report.relative_to(R)),'references':paths,'unexplained_missing':[x['path'] for x in paths if not x['exists_in_initial_fixture'] and not x['expected_missing_target']]})
(R/'citation-audit.json').write_text(json.dumps(rows,indent=2)+'\n')
print('reports:',len(rows),'unexpected nonexistent cited paths:',sum(len(x['unexplained_missing']) for x in rows))
