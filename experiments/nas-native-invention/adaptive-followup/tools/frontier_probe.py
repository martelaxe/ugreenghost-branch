"""Exploratory post-hoc demonstration; does not alter the preregistered test."""
import json
from pathlib import Path
from adapter_core import Adapter
R=Path(__file__).resolve().parents[1];log=R/'runs/frontier-probe/events.jsonl';a=Adapter(R/'fixture/work',json.loads((R/'fixture/faults.json').read_text()),log);name='incomplete'
l={s:a.call('list',name,s) for s in ('source','destination')}; sets={s:set(l[s]['paths']) for s in l};common=sorted(sets['source']&sets['destination']);known=sets['source']|sets['destination'];result={p:'unknown' for p in known}
def check(p):
 h=[a.call('sha256',name,s,p) for s in ('source','destination')]
 if any('error' in x for x in h):result[p]='unknown: read denied';return
 result[p]='content-verified identical' if h[0]['sha256']==h[1]['sha256'] else 'content-verified different'
def snap(step):
 counts={v:sum(x==v for x in result.values()) for v in sorted(set(result.values()))}
 return {'step':step,'source_listing_complete':l['source']['complete'],'destination_listing_complete':l['destination']['complete'],'known_paths':len(known),'status_counts':counts,'archive_coverage':'unknown: destination listing incomplete','per_path':dict(sorted(result.items()))}
for p in common[:5]:check(p)
stages=[snap('User asks to examine at most five common paths')]
p=common[5];check(p);stages.append(snap('User chooses one additional path: '+p))
(R/'runs/frontier-probe/output.json').write_text(json.dumps(stages,indent=2)+'\n');print(json.dumps([{k:v for k,v in s.items() if k!='per_path'} for s in stages],indent=2))
