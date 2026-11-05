"""Research-only policy simulation. No UGREEN agent, model or SKILL.md execution."""
from dataclasses import dataclass, field
@dataclass
class Evidence:
    path: str
    kind: str
    excerpt: str
@dataclass
class Review:
    state: str
    conclusions: list = field(default_factory=list)
    unknown: list = field(default_factory=list)
    evidence: list = field(default_factory=list)
    write: bool = False

def assess(*,target,authorized,inventory_status='completed',inventory_complete=False,doc_status='completed',evidence=(),hashes=None,scope_changed=False):
    if not target: return Review('WAITING FOR USER',unknown=['target not specified'])
    if not authorized: return Review('WAITING FOR USER',unknown=['target is outside authorized scope'])
    if inventory_status in ('waiting_user','waiting_approval'):
        return Review('WAITING FOR USER' if inventory_status=='waiting_user' else 'WAITING FOR APPROVAL',unknown=['discovery pending'])
    if inventory_status in ('failed','cancelled'):
        return Review(inventory_status.upper(),unknown=['discovery incomplete'])
    e=[x for x in evidence if x.path and x.excerpt]
    unknown=[] if inventory_complete else ['inventory coverage unknown']
    if scope_changed: unknown.append('new review required; earlier results may be stale')
    if doc_status!='completed':
        unknown.append('document analysis '+doc_status)
        state={'failed':'PARTIALLY COMPLETED','cancelled':'CANCELLED','waiting_user':'WAITING FOR USER','waiting_approval':'WAITING FOR APPROVAL'}.get(doc_status,'PARTIALLY COMPLETED')
        return Review(state,unknown=unknown,evidence=e)
    conclusions=[]
    for x in e:
        if x.kind=='direct': conclusions.append('source references target: '+x.path)
        elif x.kind in ('ambiguous','historical','contrary'): unknown.append(x.kind+': '+x.path)
    if not any(x.kind=='direct' for x in e): conclusions.append('no direct reference found in reviewed evidence')
    if hashes is not None:
        if len(hashes)>=2 and all(hashes):
            conclusions.append('same bytes at check time' if len(set(hashes))==1 else 'bytes differ')
            unknown.append('copy roles and safety of deletion are not proven by hashes')
        else: unknown.append('hash comparison incomplete')
    return Review('PARTIALLY COMPLETED' if unknown else 'COMPLETED',conclusions,unknown,e)
