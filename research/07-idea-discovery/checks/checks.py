"""Research-only deterministic checks; no AI, NAS, or official expert outputs."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CATALOG = HERE.parents[2] / 'resources/uliya-skill-kit/data/capability-catalog.json'

# Requested capabilities, not assertions that a complete solution follows from them.
REQUIRED = {
    'Succession rehearsal': [('ug-filesystem','find','file-agent'), ('ug-document','extract','document-agent'), ('ug-knowledge','collect-evidence','knowledge-agent')],
    'Creator consent before reuse': [('ug-photo','meta','photo-agent'), ('ug-document','extract','document-agent'), ('ug-knowledge','collect-evidence','knowledge-agent')],
    'Conversation bridge': [('ug-photo','vision-vlm','photo-agent'), ('ug-document','extract','document-agent'), ('ug-knowledge','collect-evidence','knowledge-agent')],
}

def catalog_presence(catalog, requirements):
    clis = {c['name']: c for c in catalog['clis']}
    return {f'{cli}:{action} -> {agent}': cli in clis and clis[cli]['agent'] == agent and any(a['name'] == action for a in clis[cli]['actions']) for cli, action, agent in requirements}

def build_rehearsal(sources, expected, inventory_complete):
    """Make a deterministic exercise from human-selected evidence, not model reasoning.

    sources: entries with a fixture-relative path, excerpt and a prewritten question.
    Matching checks existence of text only, not semantic validity.
    """
    reviewed = []
    lines = ['# Simulated succession rehearsal', '', 'Human-curated fictional records; quote existence checked locally. Not a NAS result.', '']
    for item in sources:
        path = HERE / 'fixtures' / item['path']
        if not path.is_file() or item['excerpt'] not in path.read_text():
            raise ValueError('Source or exact excerpt unavailable: ' + item['path'])
        reviewed.append(item['path'])
        lines += [f"## {item['question']}", f"Evidence: `{item['path']}` — “{item['excerpt']}”", 'Answer and verify with the responsible person; do not infer unstated facts.', '']
    for name in expected:
        if name not in reviewed:
            lines += [f'Unresolved: `{name}` was not among the records reviewed; it may exist elsewhere or be inaccessible.', '']
    lines += ['Coverage: reviewed ' + (', '.join(reviewed) if reviewed else 'no records') + '.',
              'Inventory completeness: ' + ('declared complete by fixture' if inventory_complete else 'unknown; no claim of complete coverage.'),
              'No credentials, sharing, recovery success, safety clearance or legal authority were verified.', '']
    return '\n'.join(lines)

if __name__ == '__main__':
    catalog = json.loads(CATALOG.read_text())
    for name, requirements in REQUIRED.items():
        print(name, catalog_presence(catalog, requirements))
    print('Negative control (not found is not proof of impossibility):', catalog_presence(catalog, [('ug-video','render-montage','media-agent')]))
    card = build_rehearsal([
        {'path':'maintenance.txt','excerpt':'The spare filter is in the labeled blue box.', 'question':'Where is the spare filter, and is it still there?'},
        {'path':'handoff.txt','excerpt':'Before changing the filter, contact Mira.', 'question':'Who should be contacted before a filter change?'}],
        ['maintenance.txt','handoff.txt','recovery.txt'], False)
    (HERE / 'simulated-rehearsal.md').write_text(card)
    print('Wrote fictional, human-curated rehearsal to checks/simulated-rehearsal.md')
