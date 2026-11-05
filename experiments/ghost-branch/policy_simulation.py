"""Research-only state simulation, not UGREEN execution or SKILL.md interpreter."""
from dataclasses import dataclass
@dataclass(frozen=True)
class Evidence:
    source: str
    statement: str
    kind: str
    retrieved: bool = True

def assess(evidence, current_coverage='unknown'):
    valid=[x for x in evidence if x.retrieved and x.source and x.statement]
    kinds={x.kind for x in valid}
    unknown=[x.kind for x in evidence if not x.retrieved or not x.source or not x.statement]
    if any(k in ('retirement','security-decision') for k in kinds): category='RETIRED FOR A REASON'
    elif 'current-equivalent' in kinds: category='NOT ESTABLISHED'
    elif any(x.kind in ('security-decision','retirement','blocker') for x in evidence if x not in valid):category='UNCERTAIN'
    elif 'historical-source' in kinds and not unknown: category='RECLAIM CANDIDATE'
    elif 'historical-source' in kinds or 'screenshot' in kinds: category='UNCERTAIN'
    else: category='NOT ESTABLISHED'
    return {'category':category,'evidence':valid,'unknown':unknown,'coverage':current_coverage,'absence_claim':False,'action':'investigate' if category=='RECLAIM CANDIDATE' else 'review or clarify'}

def status(current, child, has_required):
    if child=='waiting_approval':return {'state':'WAITING FOR APPROVAL','saved':False,'evidence':current}
    if child=='waiting_user':return {'state':'WAITING FOR USER','saved':False,'evidence':current}
    if child in ('failed','cancelled'):return {'state':child.upper(),'saved':False,'evidence':current}
    if child=='completed' and has_required:return {'state':'COMPLETED','saved':True,'evidence':current}
    return {'state':'UNKNOWN','saved':False,'evidence':current}

def safe_excerpt(path, value):
    blocked=['.env','private_key','credentials','secret']
    if any(x in path.lower() for x in blocked):return None
    if any(x in value.lower() for x in ['fake_secret_value','private key','access token=']):return None
    return value
