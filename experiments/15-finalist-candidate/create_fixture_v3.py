from pathlib import Path
import shutil,json,hashlib
R=Path(__file__).resolve().parent;src=R/'fixtures-v2';dst=R/'fixtures-v3'
if dst.exists():raise SystemExit('Refuse to overwrite v3')
for case in ['base','critical','irrelevant','restricted','business']:
 old=src/case/'archive';new=dst/case/'archive';shutil.copytree(old,new)
 if case=='business':
  f=new/'finance/payment.txt';s=f.read_text();assert 'Payment confirmation:' in s;f.write_text('Current payment confirmation for this management review, dated 24 April 2027: 800 units received against final invoice INV-22.\n')
 data={str(p.relative_to(new)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(new.rglob('*')) if p.is_file()};(new.parent/'manifest.json').write_text(json.dumps(data,indent=2)+'\n')
base=json.loads((dst/'base/manifest.json').read_text())
for case in ['critical','irrelevant']:
 x=json.loads((dst/case/'manifest.json').read_text());diff=[k for k in base if base[k]!=x.get(k)];print(case,'changed files:',diff);assert diff==(['rights/art17.txt'] if case=='critical' else ['other/decor.txt'])
(dst/'answer-key.md').write_text('# Post-observation v3 fixture key\n\nFictional assessment date is 25 April 2027. The workshop occurred on 18 April and the payment record is dated 24 April. The volunteer roster explicitly covers the full public hours. Event public-use permission is dated 3 March, preceding the as-of date. Other ground truth and controlled mutations remain as in prior fixture keys. This key was written after v1 and partial v2 outputs and before v3 runs.\n')
