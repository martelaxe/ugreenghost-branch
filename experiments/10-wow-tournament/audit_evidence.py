"""Mechanical citation and quote candidate audit; no semantic entailment guarantee."""
import json,re
from pathlib import Path
base=Path(__file__).resolve().parent
status=json.loads((base/'outputs/status.json').read_text());out=[]
for r in status['runs']:
 name=r['name'];report=(base/'outputs'/name/'raw-response.md').read_text();root=base/'fixtures'/name
 paths=sorted(set(re.findall(r'`([^`\n]+\.txt)`',report)))
 invalid=[p for p in paths if not (root/p).is_file()]
 source={str(f.relative_to(root)):f.read_text() for f in root.rglob('*.txt')}
 quotes=[]
 for q in re.findall(r'“([^”\n]{12,300})”',report):
  matches=[p for p,s in source.items() if q in s]
  quotes.append({'quote':q,'exact_source_matches':matches})
 out.append({'name':name,'source_paths':paths,'nonexistent_paths':invalid,'quoted_spans':quotes,'warning':'Quoted spans without matches can be creative text or minimally edited excerpts; assess context. Exact matches do not establish entailment. Inline citations outside backticks and claims without citations require manual review.'})
(base/'evidence-audit.json').write_text(json.dumps(out,indent=2)+'\n')
for r in out:
 print(r['name'],'cited',len(r['source_paths']),'bad',len(r['nonexistent_paths']),'quote_candidates',len(r['quoted_spans']),'unmatched',sum(not x['exact_source_matches'] for x in r['quoted_spans']))
