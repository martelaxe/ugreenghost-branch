"""Synthetic fixture-only analogue, not UGREEN or actual approval."""
from pathlib import Path
import hashlib, json, shutil, os
R=Path(__file__).resolve().parent; base=R/'prototypes/A'; out=base/'local-organization'; target=out/'disposable'
def snapshot(p): return {str(f.relative_to(p)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(p.rglob('*')) if f.is_file()}
def main():
 out.mkdir(exist_ok=True)
 if target.exists():shutil.rmtree(target)
 shutil.copytree(base/'archive',target); before=snapshot(target)
 # Explicitly invented fixture event, not human or gateway approval.
 approval_fixture=True
 if not approval_fixture:raise RuntimeError('No simulated consent')
 folder=target/'prepared/equipment-rental';folder.mkdir(parents=True,exist_ok=False)
 src=target/'inbox/receipt-k.txt';dst=folder/'receipt-k.txt'
 fd=os.open(dst,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
 with os.fdopen(fd,'wb') as w,src.open('rb') as r:shutil.copyfileobj(r,w)
 after=snapshot(target);added=sorted(after.keys()-before.keys());modified=[p for p in before if before[p]!=after.get(p)];removed=sorted(before.keys()-after.keys())
 assert added==['prepared/equipment-rental/receipt-k.txt'] and not modified and not removed and after[added[0]]==before['inbox/receipt-k.txt']
 event={'kind':'local Python fixture copy, NOT NAS','synthetic_approval_fixture':True,'source':'inbox/receipt-k.txt','destination':added[0],'source_sha256':before['inbox/receipt-k.txt'],'destination_sha256':after[added[0]],'added':added,'modified_existing':modified,'removed':removed,'note':'created a local folder and copied one item; originals preserved; no actual UGREEN execution, user or gateway approval, or atomicity guarantee on NAS'}
 for name,data in [('before.json',before),('after.json',after),('event.json',event)]:(out/name).write_text(json.dumps(data,indent=2)+'\n')
 (out/'before-after.md').write_text('# Local-only grouping analogue\n\nIn a disposable copy of the A fixture, local Python created `prepared/equipment-rental/` and copied the receipt into it. The approval is a simulated test input, not a human or UGREEN platform approval.\n\n- Source: `inbox/receipt-k.txt`\n- New copy: `prepared/equipment-rental/receipt-k.txt`\n- Source and new copy SHA-256: `'+event['source_sha256']+'`\n- Added paths: '+str(added)+'\n- Changed existing paths: '+str(modified)+'\n- Removed paths: '+str(removed)+'\n\nThe original duplicate remains in `inbox/`. This local operation does not prove UGREEN mkdir/copy approval, collision handling or verification behavior.\n')
 print(json.dumps(event,indent=2))
if __name__=='__main__':main()
