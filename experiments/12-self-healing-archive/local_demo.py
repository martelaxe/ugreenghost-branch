"""Research-only fixture adapter; no UGREEN agents or real user approval."""
from pathlib import Path
import hashlib, json, os, shutil, tempfile
R=Path(__file__).resolve().parent
SRC='shared/review_17.txt'; DST='projects/harbor/assets/launch-cover.txt'
EXPECTED=json.loads((R/'initial-manifest.json').read_text())[SRC]['sha256']
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def snapshot(root):
 return {str(p.relative_to(root)):digest(p) for p in sorted(root.rglob('*')) if p.is_file()}
def run_copy(root, *, user_approval=False, gateway_approval=False, fail_write=False, fail_verify=False, expected=EXPECTED):
 root=root.resolve(); source=root/SRC; target=root/DST
 event={'simulation':True,'user_approval_fixture':user_approval,'gateway_approval_fixture':gateway_approval,'action_requested':True,'action_reported_completed':False,'verification':'not_attempted','status':'stopped'}
 if not user_approval or not gateway_approval: event['reason']='approval missing or denied'; return event
 # Only known fixed fixture paths, reject symlink escape or untrusted existing targets.
 if source.is_symlink() or any(p.is_symlink() for p in target.parents if p!=root and p!=root.parent): event['reason']='symlink';return event
 if not source.is_file() or not target.parent.is_dir(): event['reason']='source or destination directory unavailable';return event
 before=digest(source)
 if before!=expected: event['reason']='source hash differs from approved plan';return event
 if target.exists() or target.is_symlink(): event['reason']='destination occupied';return event
 if fail_write: event['reason']='injected write failure before copy';return event
 try:
  fd=os.open(target,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
  with os.fdopen(fd,'wb') as out,source.open('rb') as inp: shutil.copyfileobj(inp,out)
 except OSError as e: event['reason']='local write error: '+str(e);return event
 event['action_reported_completed']=True
 if fail_verify: event.update(status='unverified',verification='failed',reason='injected verification failure');return event
 try:
  source_after=digest(source); target_after=digest(target)
 except OSError as e: event.update(status='unverified',verification='failed',reason=str(e));return event
 event.update(source_sha256_before=before,source_sha256_after=source_after,destination_sha256=target_after)
 if before==source_after==target_after: event.update(status='verified',verification='matched',reason='copy exists; original remains and bytes match')
 else: event.update(status='unverified',verification='mismatch',reason='post-copy check did not match')
 return event

def demo():
 out=R/'local-demo';out.mkdir(exist_ok=True);fixture=out/'disposable-after'
 if fixture.exists(): shutil.rmtree(fixture)
 shutil.copytree(R/'archive',fixture)
 before=snapshot(fixture); result=run_copy(fixture,user_approval=True,gateway_approval=True); after=snapshot(fixture)
 (out/'before.json').write_text(json.dumps(before,indent=2)+'\n');(out/'after.json').write_text(json.dumps(after,indent=2)+'\n')
 (out/'event.json').write_text(json.dumps(result,indent=2)+'\n')
 added=sorted(set(after)-set(before)); changed=[x for x in before if x in after and before[x]!=after[x]]; removed=sorted(set(before)-set(after))
 (out/'before-after.md').write_text('# Local fixture result — not a UGREEN operation\n\nThe two approvals below are test inputs, not real user or platform approvals. No NAS was accessed.\n\n- Source: `'+SRC+'`\n- Destination: `'+DST+'`\n- Simulated user approval: true; simulated gateway approval: true\n- Local Python filesystem copy status: '+result['status']+'\n- Source SHA-256 before and after: `'+result.get('source_sha256_before','unknown')+'` / `'+result.get('source_sha256_after','unknown')+'`\n- Destination SHA-256: `'+result.get('destination_sha256','unknown')+'`\n- Added paths: '+str(added)+'\n- Changed existing paths: '+str(changed)+'\n- Removed paths: '+str(removed)+'\n\nThe expected fixture path exists with matching bytes; this does not establish that an external application opens the project or that UGREEN executes or enforces the same operation.\n')
 print(json.dumps(result,indent=2)); assert result['status']=='verified' and added==[DST] and not changed and not removed
if __name__=='__main__':demo()
