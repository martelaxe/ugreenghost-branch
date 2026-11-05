import json
import unittest
from checks import CATALOG, REQUIRED, build_rehearsal, catalog_presence

class ResearchChecks(unittest.TestCase):
    def test_documented_shortlist_actions_exist_with_named_agents(self):
        catalog=json.loads(CATALOG.read_text())
        for requirements in REQUIRED.values():
            self.assertTrue(all(catalog_presence(catalog, requirements).values()))
    def test_no_invented_montage_operation_in_catalog(self):
        catalog=json.loads(CATALOG.read_text())
        self.assertFalse(next(iter(catalog_presence(catalog,[('ug-video','render-montage','media-agent')]).values())))
    def test_cited_excerpt_is_preserved(self):
        result=build_rehearsal([{'path':'maintenance.txt','excerpt':'The spare filter is in the labeled blue box.','question':'Where is the spare filter?'}],[],False)
        self.assertIn('maintenance.txt',result)
        self.assertIn('The spare filter is in the labeled blue box.',result)
        self.assertIn('unknown; no claim of complete coverage',result)
    def test_missing_source_or_invented_quote_is_rejected(self):
        for path, excerpt in [('missing.txt','nothing'),('maintenance.txt','The spare is red.')]:
            with self.subTest(path=path,excerpt=excerpt), self.assertRaises(ValueError):
                build_rehearsal([{'path':path,'excerpt':excerpt,'question':'What?'}],[],False)
    def test_missing_record_not_claimed_nonexistent(self):
        result=build_rehearsal([],['recovery.txt'],False)
        self.assertIn('not among the records reviewed',result)
        self.assertIn('may exist elsewhere or be inaccessible',result)
        self.assertNotIn('does not exist',result)

if __name__ == '__main__': unittest.main(verbosity=2)
