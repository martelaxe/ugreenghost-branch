"""Deterministic fixture/link/frozen-prompt checks, not NAS runtime tests."""
from pathlib import Path
import json,hashlib,re,unittest
R=Path(__file__).resolve().parent; P=R.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
class Integrity(unittest.TestCase):
 def test_skill_unchanged(self):self.assertEqual(sha(P/'prototype/readiness-delta/SKILL.md'),'f1551c265082f62358019a42512c6937a7135054c40c1a1f52fc1691f2c7e152')
 def test_exact_skill_in_all_s_prompts(self):
  skill=(P/'prototype/readiness-delta/SKILL.md').read_text()
  for wave in ['runs','runs-v2','runs-v3']:
   for c in ['base','critical','irrelevant','restricted','business']:
    self.assertIn(skill,(R/wave/(c+'-S')/'prompt.md').read_text())
  self.assertIn(skill,(R/'runs-delta/S/prompt.md').read_text())
 def test_all_30_runs_exited_cleanly_and_unchanged(self):
  for wave in ['runs','runs-v2','runs-v3']:
   for c in ['base','critical','irrelevant','restricted','business']:
    for m in 'GS':
     x=json.loads((R/wave/(c+'-'+m)/'execution.json').read_text());self.assertEqual(x['exit'],0);self.assertTrue(x['inputs_unchanged']);self.assertTrue(x['no_symlinks'])
 def test_mutations_exactly_one_path(self):
  j=json.loads((R/'audit.json').read_text())['mutations'];self.assertEqual(len(j),6);self.assertTrue(all(v['expected_path_only'] for v in j.values()))
 def test_restricted_rights_absent(self):
  for wave in ['workspaces','workspaces-v2','workspaces-v3']:
   for m in 'GS':self.assertFalse((R/wave/('restricted-'+m)/'rights').exists())
 def test_baseline_prior_is_literal_response(self):
  p=R/'runs-v3/base-S/response.md'
  for m in 'GS':self.assertEqual(sha(p),sha(R/'delta-workspaces'/m/'prior/review.md'))
 def test_audit_v3_mechanics(self):
  j=json.loads((R/'audit.json').read_text())['reports'];v=[x for x in j if x['wave']=='-v3'];self.assertEqual(len(v),10);links=[l for x in v for l in x['links']];self.assertEqual((len(links),sum(x['raw_ok'] for x in links),sum(x['mapped_ok'] for x in links)),(82,43,82))
 def test_static_checker_pass(self):
  j=json.loads((R/'static-check.json').read_text());self.assertEqual(j['status'],'static-pass');self.assertEqual(j['summary']['errors'],0);self.assertEqual(j['summary']['warnings'],0)
if __name__=='__main__':unittest.main(verbosity=2)
