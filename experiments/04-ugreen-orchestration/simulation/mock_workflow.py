"""Deterministic research simulation; this is not a UGREEN runtime or a Skill.

Only {ok, data/error} is documented as a generic CLI result envelope. The
outer status wrapper and every data field below are illustrative adapter
assumptions, not an assertion about real expert output.
"""
from __future__ import annotations

from copy import deepcopy
from pathlib import PurePosixPath
from typing import Any
import json
import sys

SCOPE = '/fictional/harbor'
FILES = {
    f'{SCOPE}/reading-room.txt': 'The reading group reports that the historic harbor handout is difficult to follow in discussion.',
    f'{SCOPE}/archive.txt': 'The studio owns a historic harbor schematic and permits attributed internal prototypes.',
    f'{SCOPE}/technique.txt': 'Staff previously made raised diagrams by stacking approved acrylic shapes.',
    f'{SCOPE}/equipment.txt': 'Laser L-2 passed inspection and can process the approved acrylic stock.',
    f'{SCOPE}/allocation.txt': 'The manager may approve up to four existing staff hours for an internal prototype.',
}
FAILED_LASER = 'Laser L-2 failed inspection and must remain unavailable until repaired and cleared.'
ROLES = {
    'need': (f'{SCOPE}/reading-room.txt', FILES[f'{SCOPE}/reading-room.txt']),
    'asset_rights': (f'{SCOPE}/archive.txt', FILES[f'{SCOPE}/archive.txt']),
    'technique': (f'{SCOPE}/technique.txt', FILES[f'{SCOPE}/technique.txt']),
    'equipment': (f'{SCOPE}/equipment.txt', FILES[f'{SCOPE}/equipment.txt']),
    'approval': (f'{SCOPE}/allocation.txt', FILES[f'{SCOPE}/allocation.txt']),
}
REQUIRED_ROLES = frozenset(ROLES)
HYPOTHESIS = 'Explore a small raised historic-harbor discussion aid using the existing schematic and acrylic technique.'


def ok(data: Any) -> dict[str, Any]:
    return {'status': 'completed', 'result': {'ok': True, 'data': data}}


def fake_scenario(name: str) -> dict[str, Any]:
    """Build fictional agent outputs; candidates and exact citations are prewired."""
    docs = dict(FILES)
    if name == 'critical_blocker':
        docs[f'{SCOPE}/equipment.txt'] = FAILED_LASER
    if name == 'missing_source':
        del docs[f'{SCOPE}/archive.txt']
    paths = sorted(docs)
    evidence = []
    for role, (path, quote) in ROLES.items():
        if path not in docs:
            continue
        evidence.append({'role': role, 'path': path, 'quote': docs[path] if role == 'equipment' else quote})
    fixture = {
        # Examples only: actual CLI data structure and coverage format unknown.
        'file-agent': ok({'paths': paths, 'coverage': {'complete': True}}),
        'document-agent': ok({'documents': [{'path': path, 'text': docs[path], 'complete': True} for path in paths], 'coverage': {'complete': True}}),
        'knowledge-agent': ok({'evidence': evidence, 'coverage': {'complete': True}, 'blocker': None}),
    }
    if name == 'critical_blocker':
        fixture['knowledge-agent']['result']['data']['blocker'] = {'path': f'{SCOPE}/equipment.txt', 'quote': FAILED_LASER}
    elif name == 'truncated_evidence':
        row = next(d for d in fixture['document-agent']['result']['data']['documents'] if d['path'].endswith('archive.txt'))
        row['text'] = 'The studio owns a historic harbor schematic'
        row['complete'] = False
        fixture['document-agent']['result']['data']['coverage']['complete'] = False
    elif name == 'expert_failure':
        fixture['document-agent'] = {'status': 'failed', 'result': {'ok': False, 'error': {'code': 'MOCK_READ_FAILED', 'message': 'Fictional document read failed.'}}}
    elif name == 'approval_pending':
        # Deliberately hypothetical; the mocked normal workflow is read-only.
        fixture['knowledge-agent'] = {'status': 'waiting_approval', 'result': None}
    elif name != 'supported_discovery' and name not in ('missing_source', 'critical_blocker', 'truncated_evidence'):
        raise ValueError(f'Unknown scenario: {name}')
    return fixture


def incomplete(reason: str, evidence: list[dict[str, str]], states: list[str], missing: list[str] | None = None) -> dict[str, Any]:
    observed = [{'path': item['path'], 'quote': FAILED_LASER} for item in evidence
                if item.get('path') == f'{SCOPE}/equipment.txt' and FAILED_LASER in item.get('quote', '')]
    return {
        'disposition': 'incomplete',
        'discovery': None,
        'evidence': evidence,
        'coverage': {'status': 'incomplete', 'details': reason},
        'uncertainty': ['A discovery cannot be established from the available completed mock results.', 'Blockers have not been comprehensively assessed.'],
        'critical_blockers': observed or None,
        'missing_roles': sorted(missing or []),
        'safe_next_action': 'Resolve the stated missing evidence or expert state before drawing a conclusion.',
        'expert_states': states,
        'notice': 'Fictional deterministic simulation; no NAS or real agent was accessed.',
    }


def invoke_fixture(agent: str, fixture: dict[str, Any], calls: list[str]) -> tuple[dict[str, Any] | None, str | None]:
    calls.append(agent)
    response = fixture.get(agent)
    if not isinstance(response, dict):
        return None, f'{agent}: missing or malformed response'
    status = response.get('status')
    if status != 'completed':
        return None, f'{agent}: {status if isinstance(status, str) else "unknown status"}'
    result = response.get('result')
    if not isinstance(result, dict) or result.get('ok') is not True or not isinstance(result.get('data'), dict):
        return None, f'{agent}: completed without a valid successful mock result'
    return result['data'], None


def coverage_complete(data: dict[str, Any]) -> bool:
    coverage = data.get("coverage")
    return isinstance(coverage, dict) and coverage.get("complete") is True


def in_scope(path: Any) -> bool:
    return (isinstance(path, str) and path.startswith(SCOPE + "/") and "\\" not in path
            and ".." not in PurePosixPath(path).parts and str(PurePosixPath(path)) == path)


def run(fixture: dict[str, Any]) -> dict[str, Any]:
    """Conservatively gate a preselected fictional candidate, not discover one."""
    calls: list[str] = []
    verified: list[dict[str, str]] = []
    inventory, error = invoke_fixture('file-agent', fixture, calls)
    if error:
        return incomplete(error, verified, calls)
    assert inventory is not None
    paths = inventory.get('paths')
    if (not isinstance(paths, list) or not paths or any(not in_scope(p) for p in paths)
        or len(paths) != len(set(paths)) or not coverage_complete(inventory)):
        return incomplete('file-agent: empty, invalid, out-of-scope or incomplete inventory', verified, calls)

    documents, error = invoke_fixture('document-agent', fixture, calls)
    if error:
        return incomplete(error, verified, calls)
    assert documents is not None
    rows = documents.get('documents')
    if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
        return incomplete('document-agent: malformed document results', verified, calls)
    # Require one complete document per discovered path; no inferred coverage.
    source_map: dict[str, str] = {}
    partial_documents: list[dict[str, str]] = []
    incomplete_paths: list[str] = []
    for row in rows:
        path, text = row.get('path'), row.get('text')
        if not isinstance(path, str) or path not in paths or path in source_map or not isinstance(text, str):
            return incomplete('document-agent: unknown, duplicate or malformed source', verified, calls)
        if row.get('complete') is not True:
            incomplete_paths.append(path)
            continue
        source_map[path] = text
        partial_documents.append({'role': 'document_content', 'path': path, 'quote': text})
    if incomplete_paths:
        return incomplete('document-agent: content incomplete for ' + ', '.join(incomplete_paths), partial_documents, calls)
    if not coverage_complete(documents) or set(source_map) != set(paths):
        return incomplete('document-agent: incomplete or unknown coverage', partial_documents, calls)

    knowledge, error = invoke_fixture('knowledge-agent', fixture, calls)
    if error:
        return incomplete(error, partial_documents, calls)
    assert knowledge is not None
    citations = knowledge.get('evidence')
    if not isinstance(citations, list) or not coverage_complete(knowledge):
        return incomplete('knowledge-agent: missing evidence or incomplete/unknown coverage', verified, calls)
    roles: set[str] = set()
    for item in citations:
        if not isinstance(item, dict):
            return incomplete('knowledge-agent: malformed evidence', [], calls)
        role, path, quote = item.get('role'), item.get('path'), item.get('quote')
        if (not isinstance(role, str) or role not in REQUIRED_ROLES or role in roles or not isinstance(path, str) or path not in source_map
            or path != ROLES[role][0] or not isinstance(quote, str) or not quote or quote not in source_map[path]):
            return incomplete('knowledge-agent: unverified, mismatched or duplicate citation', [], calls)
        roles.add(role)
        verified.append({'role': role, 'path': path, 'quote': quote})
    missing = REQUIRED_ROLES - roles
    if missing:
        return incomplete('knowledge-agent: essential evidence missing', verified, calls, sorted(missing))

    blocker = knowledge.get('blocker')
    if blocker is not None:
        if (not isinstance(blocker, dict) or blocker.get('path') not in source_map
            or not isinstance(blocker.get('quote'), str) or not blocker['quote']
            or blocker['quote'] not in source_map[blocker['path']]):
            return incomplete('knowledge-agent: blocker cannot be verified', verified, calls)
        if blocker.get('path') != f'{SCOPE}/equipment.txt' or blocker.get('quote') != FAILED_LASER:
            return incomplete('knowledge-agent: unsupported blocker interpretation', verified, calls)
        return {
            'disposition': 'blocked', 'discovery': HYPOTHESIS, 'evidence': verified,
            'coverage': {'status': 'complete_for_mock_scope', 'details': 'All discovered fixture texts and required evidence roles were returned.'},
            'uncertainty': ['Usefulness and participant interest are untested; no external pilot is approved.'],
            'critical_blockers': [deepcopy(blocker)],
            'safe_next_action': 'Do not operate L-2; seek manager approval for a non-fabrication review and verify repair and clearance before fabrication.',
            'expert_states': calls, 'notice': 'Fictional deterministic simulation; no NAS or real agent was accessed.',
        }
    # An illustrative guard: no-blocker cannot override a contradictory known mock source.
    equipment = source_map.get(f'{SCOPE}/equipment.txt', '')
    if FAILED_LASER in equipment:
        return incomplete('document evidence contradicts missing blocker report', verified, calls)
    if equipment != FILES[f'{SCOPE}/equipment.txt']:
        return incomplete('equipment state is not recognized by this fixture', verified, calls)
    return {
        'disposition': 'hypothesis', 'discovery': HYPOTHESIS, 'evidence': verified,
        'coverage': {'status': 'complete_for_mock_scope', 'details': 'All discovered fixture texts and required evidence roles were returned.'},
        'uncertainty': ['Usefulness, fabrication time and participant interest are untested; manager approval remains necessary.'],
        'critical_blockers': [],
        'safe_next_action': 'Ask the manager to review a bounded internal prototype; verify stock and operator availability before fabrication.',
        'expert_states': calls, 'notice': 'Fictional deterministic simulation; no NAS or real agent was accessed.',
    }


def main() -> None:
    names = ['supported_discovery', 'critical_blocker', 'missing_source', 'truncated_evidence', 'expert_failure', 'approval_pending']
    if len(sys.argv) > 1:
        names = sys.argv[1:]
    print(json.dumps({name: run(fake_scenario(name)) for name in names}, indent=2))


if __name__ == '__main__':
    main()
