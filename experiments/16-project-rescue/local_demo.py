from pathlib import Path
import os,shutil,json,hashlib
R=Path(__file__).parent; D=R/'demo'; D.mkdir(exist_ok=True); W=D/'workspace'
if W.exists(): shutil.rmtree(W)
shutil.copytree(R/'fixtures/creative',W)
raw=(R/'runs/creative-S/response.md').read_text()
src='shared/q7.svg';dst='projects/cedar/assets/lantern-banner.svg'
assert '/tmp/work/'+src in raw and '/tmp/work/'+dst in raw, 'Demo action was not proposed by frozen-S model.'
def manifest():return {str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(W.rglob('*')) if p.is_file()}
before=manifest();source=W/src;target=W/dst;sourcehash=before[src]
assert target.parent.is_dir() and not target.exists()
# Research-only test input, not human or NAS approval.
approvals={'user_approved':True,'gateway_approved':True,'synthetic_test_flags':True}
assert approvals['user_approved'] and approvals['gateway_approved']
assert hashlib.sha256(source.read_bytes()).hexdigest()==sourcehash
fd=os.open(target,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
with os.fdopen(fd,'wb') as out:out.write(source.read_bytes())
after=manifest();unchanged=all(after.get(p)==v for p,v in before.items());equal=after[dst]==after[src]==sourcehash
assert unchanged and equal and set(after)-set(before)=={dst}
(D/'before.json').write_text(json.dumps(before,indent=2)+'\n');(D/'after.json').write_text(json.dumps(after,indent=2)+'\n')
(D/'approval-simulation.json').write_text(json.dumps(approvals,indent=2)+'\n')
record={'operation':'local Python copy with os.O_CREAT|os.O_EXCL','source':src,'destination':dst,'original_source_sha256':sourcehash,'post_source_sha256':after[src],'destination_sha256':after[dst],'original_files_unchanged':unchanged,'added_paths':sorted(set(after)-set(before)),'verification':'verified locally','ugreen_action':False,'real_user_or_gateway_approval':False}
(D/'copy-record.json').write_text(json.dumps(record,indent=2)+'\n')
shutil.copyfile(R/'runs/creative-S/response.md',D/'raw-model-response.md');shutil.copyfile(R/'runs/creative-S/prompt.md',D/'user-prompt-and-skill.md')
print(json.dumps(record,indent=2))
