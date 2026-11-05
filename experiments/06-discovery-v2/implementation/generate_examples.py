"""Create three fictional local reports; no model or NAS calls."""
from pathlib import Path
from tempfile import TemporaryDirectory
from copy import deepcopy
from discovery_v2 import inventory, investigate, render_report

OUT = Path(__file__).resolve().parents[1] / 'examples'

with TemporaryDirectory(prefix='discovery-v2-examples-') as directory:
    root = Path(directory)
    (root/'need.txt').write_text('The neighborhood group asked about an accessible tabletop activity.')
    (root/'asset.txt').write_text('The studio owns a reusable illustration for internal mockups.')
    sources, coverage = inventory(root)
    candidate = {'id': 'example', 'discovery': 'Explore a tabletop activity using the reusable illustration.',
        'why_matters': 'It might help the neighborhood group consider an accessible activity.',
        'claims': [{'id':'need','text':'The group asked about an activity.','material':True},
                   {'id':'asset','text':'A reusable illustration exists.','material':True}],
        'evidence':[{'id':'e1','claim_id':'need','path':'need.txt','excerpt':sources['need.txt'],'relation':'supports'},
                    {'id':'e2','claim_id':'asset','path':'asset.txt','excerpt':sources['asset.txt'],'relation':'supports'}],
        'reported_blocker':'', 'original_next_action':'Ask the user to review the evidence.'}
    review = {'candidate_id':'example','disposition':'SUPPORTED','explanation':'The two stated facts have matching sources; effectiveness remains untested.',
              'assessments':{'e1':'supports','e2':'supports'},'blockers':[],'blocker_search_complete':True}
    supported = investigate([candidate], sources, coverage, [review])
    assert supported['candidates'][0]['state']=='SUPPORTED'
    (OUT/'01-supported.md').write_text(render_report(supported))
    (root/'rights.txt').write_text('Sharing outside the studio requires separate written permission.')
    sources, coverage = inventory(root)
    blocked_candidate=deepcopy(candidate)
    blocked_candidate['original_next_action']='Share the illustration externally.'
    blocked_candidate['evidence'].append({'id':'e3','claim_id':'restriction','path':'rights.txt','excerpt':sources['rights.txt'],'relation':'supports'})
    blocked_review=deepcopy(review);blocked_review['assessments']['e3']='supports'
    blocked_review['blockers']=[{'claim_id':'restriction','evidence_id':'e3','text':'External sharing requires written permission.'}]
    blocked=investigate([blocked_candidate],sources,coverage,[blocked_review])
    assert blocked['candidates'][0]['state']=='BLOCKED'
    (OUT/'02-blocked.md').write_text(render_report(blocked))
    no_finding=investigate([],sources,coverage,[])
    (OUT/'03-insufficient.md').write_text(render_report(no_finding))
print('Generated three illustrative reports from fictional local fixtures.')
