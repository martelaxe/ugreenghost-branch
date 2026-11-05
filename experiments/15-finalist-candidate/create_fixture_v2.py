from pathlib import Path
import shutil,json,hashlib
R=Path(__file__).resolve().parent;src=R/'fixtures';dst=R/'fixtures-v2'
if dst.exists():raise SystemExit('Refuse to overwrite v2')
for case in ['base','critical','irrelevant','restricted','business']:
 old=src/case/'archive';new=dst/case/'archive';shutil.copytree(old,new)
 if case!='business':
  f=new/'ops/volunteers.txt';assert f.read_text()=='Two volunteer shifts planned.\n';f.write_text('Confirmed shift roster: Alex works 09:30–11:30; Sam works 11:30–13:00. These shifts cover the whole 10:00–13:00 public schedule, including cleanup. Actual attendance is not yet known.\n')
 data={str(p.relative_to(new)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(new.rglob('*')) if p.is_file()};(new.parent/'manifest.json').write_text(json.dumps(data,indent=2)+'\n')
base=json.loads((dst/'base/manifest.json').read_text())
for case in ['critical','irrelevant']:
 x=json.loads((dst/case/'manifest.json').read_text());diff=[k for k in base if base[k]!=x.get(k)];print(case,'changed files:',diff);assert diff==(['rights/art17.txt'] if case=='critical' else ['other/decor.txt'])
(dst/'answer-key.md').write_text('# Post-observation fixture key\n\nThe added named shift roster establishes continuous coverage of the full 10:00–13:00 schedule, not actual attendance. Other expected conditions and controlled mutations are as in fixtures/answer-key.md; rights are unavailable in restricted. This key was written before v2 runs but after v1 outputs.\n')
