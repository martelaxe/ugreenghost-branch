"""Find exact literal quote candidates in report text; nonmatches are NOT automatic errors."""
import json,re,unicodedata
from pathlib import Path
base=Path(__file__).resolve().parent
out=[]
for p in sorted((base/'execution').glob('[ABC]-[GS]-[12].md')):
 case=p.name[0]; sources={str(q.relative_to(base/'fixtures'/case)):q.read_text() for q in (base/'fixtures'/case).rglob('*.txt')}
 text=p.read_text();spans=re.findall(r'“([^”\n]{15,300})”|"([^"\n]{15,300})"',text)
 checks=[]
 for a,b in spans:
  v=a or b
  if v.startswith(('http','/tmp/')):continue
  matches=[name for name,body in sources.items() if v in body]
  checks.append({'quote':v,'exact_matches':matches})
 out.append({'run':p.stem,'quotes':checks,'note':'An unmatched span may be an original creative title or a paraphrase, not necessarily an inaccurate source quote. Check context and semantics manually.'})
(base/'review/automated-quote-candidates.json').write_text(json.dumps(out,indent=2)+'\n')
print('Quote candidates recorded; context and semantic support require manual judgment.')
