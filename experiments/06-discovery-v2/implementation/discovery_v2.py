"""Research-only deterministic evidence/state engine. Not a UGREEN runtime.

Review payloads are simulated external judgments; exact matches do not prove
semantic entailment. No model, network, NAS agent, or action executor is used.
"""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path, PurePosixPath
from typing import Any
import os
import re

STATES = {'SUPPORTED', 'NEEDS VERIFICATION', 'BLOCKED', 'REJECTED', 'INSUFFICIENT EVIDENCE'}
READABLE = {'.txt', '.md', '.csv', '.json'}


def inventory(root: Path, selected: list[str] | None = None, max_bytes: int = 8000) -> tuple[dict[str, str], dict[str, Any]]:
    """Read only explicitly enumerated local evidence; make no global coverage claim."""
    root = root.resolve(strict=True)
    if not root.is_dir() or max_bytes < 1:
        raise ValueError('Expected an existing directory and positive byte limit')
    discovered: list[str] = []
    skipped: list[dict[str, str]] = []
    failures: list[dict[str, str]] = []
    def walk_error(exc: OSError) -> None:
        failures.append({'path': str(exc.filename or '<unknown>'), 'reason': 'enumeration failed'})
    for directory, dirs, files in os.walk(root, followlinks=False, onerror=walk_error):
        base = Path(directory)
        for d in list(dirs):
            p = base / d
            if p.is_symlink():
                skipped.append({'path': p.relative_to(root).as_posix(), 'reason': 'symlink directory'})
                dirs.remove(d)
        for name in files:
            p = base / name
            rel = p.relative_to(root).as_posix()
            discovered.append(rel)
            if p.is_symlink():
                skipped.append({'path': rel, 'reason': 'symlink file'})
    discovered.sort()
    requested = sorted(set(discovered if selected is None else selected))
    sources: dict[str, str] = {}
    truncated: list[str] = []
    for name in requested:
        if (not isinstance(name, str) or not name or '\\' in name or PurePosixPath(name).is_absolute()
            or '..' in PurePosixPath(name).parts or str(PurePosixPath(name)) != name):
            failures.append({'path': str(name), 'reason': 'invalid or out-of-scope path'}); continue
        p = root / name
        if name not in discovered:
            failures.append({'path': name, 'reason': 'selected file missing or not discoverable'}); continue
        if p.is_symlink() or any((root / parent).is_symlink() for parent in PurePosixPath(name).parents if str(parent) != '.'):
            skipped.append({'path': name, 'reason': 'symlink'}); continue
        if p.suffix.lower() not in READABLE:
            skipped.append({'path': name, 'reason': 'unsupported extension'}); continue
        try:
            with p.open('rb') as f:
                raw = f.read(max_bytes + 1)
            if len(raw) > max_bytes:
                raw = raw[:max_bytes]; truncated.append(name)
            sources[name] = raw.decode('utf-8')
        except (OSError, UnicodeDecodeError):
            failures.append({'path': name, 'reason': 'unreadable or incomplete UTF-8'})
    # Illustrative conservative PDF-reference scan. A name is not proof of a missing path
    # when duplicate basenames or inaccessible directories might exist.
    pdf_names = {m.group(0) for text in sources.values() for m in re.finditer(r'(?<![\w.-])[\w-]+(?:[.-][\w-]+)*\.pdf\b', text, flags=re.I)}
    present_basenames = {PurePosixPath(p).name.lower() for p in discovered}
    missing_refs = sorted(n for n in pdf_names if n.lower() not in present_basenames)
    selected_unread = sorted(set(requested) - set(sources))
    coverage = {
        'discovered_paths': discovered, 'selected_paths': requested, 'read_paths': sorted(sources),
        'skipped': skipped, 'failed': failures, 'truncated_paths': sorted(truncated),
        'referenced_missing_names': missing_refs, 'reference_scan': 'PDF basenames only; references and hidden files may be missed',
        'counts': {'discovered': len(discovered), 'selected': len(requested), 'read': len(sources)},
        'known_processing_limit_bytes_per_file': max_bytes,
        'scope_coverage': 'unknown beyond observed local workspace and recognized reference names',
        'critical_unknown': bool(skipped or failures or truncated or missing_refs or selected_unread or set(requested) != set(discovered)),
    }
    return sources, coverage


def match_evidence(candidate: dict[str, Any], sources: dict[str, str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for evidence in candidate.get('evidence', []):
        row = deepcopy(evidence)
        path, excerpt = row.get('path'), row.get('excerpt')
        row['retrieved'] = isinstance(path, str) and path in sources
        row['exact_match'] = bool(row['retrieved'] and isinstance(excerpt, str) and excerpt and excerpt in sources[path])
        row['semantic_assessment'] = 'unknown'
        rows.append(row)
    return rows


def adapt_exp05(raw: dict[str, Any], index: int) -> dict[str, Any]:
    """Wrap one archived Exp05 candidate without pretending its quotes are entailed."""
    evidence = []
    for i, c in enumerate(raw.get('citations', [])):
        if isinstance(c, dict):
            evidence.append({'id': f'e{i+1}', 'claim_id': 'hypothesis', 'path': c.get('path'), 'excerpt': c.get('quote'), 'relation': 'related'})
    return {'id': f'candidate-{index}', 'discovery': raw.get('hypothesis', ''), 'why_matters': '',
            'claims': [{'id': 'hypothesis', 'text': raw.get('hypothesis', ''), 'material': True}],
            'evidence': evidence, 'reported_blocker': raw.get('blocker', ''),
            'original_next_action': raw.get('next_action', ''), 'original_candidate': deepcopy(raw)}


def classify(candidate: dict[str, Any], evidence: list[dict[str, Any]], coverage: dict[str, Any], review: Any, expert_state: str = 'completed') -> dict[str, Any]:
    """Conservative classification; no inferred positive review from absence."""
    result = {'candidate': deepcopy(candidate), 'evidence': deepcopy(evidence), 'review': deepcopy(review),
              'state': None, 'explanation': '', 'blockers': [], 'unverified_blocker': candidate.get('reported_blocker', ''),
              'safe_next_action': 'Review the source evidence and obtain any required approval before taking action.'}
    valid = [e for e in result['evidence'] if e.get('retrieved') is True and e.get('exact_match') is True]
    valid_paths = {e.get('path') for e in valid if isinstance(e.get('path'), str)}
    # Evidence of a negative control needs an explicit report, not a fabricated candidate.
    enough_context = len(valid_paths) >= 2 and bool(candidate.get('discovery'))
    if expert_state != 'completed':
        result.update(state='NEEDS VERIFICATION' if enough_context else 'INSUFFICIENT EVIDENCE', explanation=f'Verification not completed: {expert_state}; candidate retained without an established conclusion.')
        return result
    if not isinstance(review, dict) or review.get('candidate_id') != candidate.get('id') or not isinstance(review.get('explanation'), str) or not review['explanation'].strip():
        if enough_context:
            result.update(state='NEEDS VERIFICATION', explanation='No valid per-candidate verification with explanation; candidate retained as an unverified hypothesis.')
        else:
            result.update(state='INSUFFICIENT EVIDENCE', explanation='Fewer than two independently retrieved cited sources or no candidate description.')
        return result
    if review.get('disposition') not in STATES:
        result.update(state='NEEDS VERIFICATION' if enough_context else 'INSUFFICIENT EVIDENCE', explanation='The per-candidate review lacks a valid structured disposition.')
        return result
    assessments = review.get('assessments')
    if not isinstance(assessments, dict):
        result.update(state='NEEDS VERIFICATION', explanation='Semantic assessments were not provided; quote existence does not establish support.')
        return result
    by_id = {e.get('id'): e for e in valid if isinstance(e.get('id'), str)}
    if len(by_id) != len(valid):
        result.update(state='NEEDS VERIFICATION', explanation='Duplicate or missing evidence identifiers prevent reliable claim mapping.')
        return result
    for e in result['evidence']:
        e['semantic_assessment'] = assessments.get(e.get('id'), 'unknown') if e.get('retrieved') and e.get('exact_match') else 'not verified'
    # A decisive blocker is accepted only when the cited source was retrieved and
    # the reviewer explicitly states that the citation supports that blocker.
    blockers = review.get('blockers', [])
    if not isinstance(blockers, list):
        result.update(state='NEEDS VERIFICATION', explanation='Blocker review is malformed.')
        return result
    for blocker in blockers:
        if not isinstance(blocker, dict):
            result.update(state='NEEDS VERIFICATION', explanation='Blocker review is malformed.'); return result
        evidence_id = blocker.get('evidence_id'); item = by_id.get(evidence_id)
        if (not isinstance(blocker.get('text'), str) or not blocker['text'].strip() or item is None
            or item.get('claim_id') != blocker.get('claim_id') or assessments.get(evidence_id) != 'supports'):
            result.update(state='NEEDS VERIFICATION', explanation='A reported blocker lacks retrieved source evidence or explicit semantic support.'); return result
        result['blockers'].append({'text': blocker['text'], 'path': item['path'], 'excerpt': item['excerpt'], 'evidence_id': evidence_id})
    if result['blockers']:
        result.update(state='BLOCKED', explanation=review['explanation'], safe_next_action='Do not take the blocked action; review the cited restriction and seek the relevant authorization or clearance.')
        return result
    if not enough_context:
        result.update(state='INSUFFICIENT EVIDENCE', explanation='Fewer than two independently retrieved cited sources or no candidate description.')
        return result
    material_ids = [c.get('id') for c in candidate.get('claims', []) if isinstance(c, dict) and c.get('material') is True]
    if not material_ids or any(not isinstance(c, str) or not c for c in material_ids) or len(material_ids) != len(set(material_ids)):
        result.update(state='NEEDS VERIFICATION', explanation='Material claims were not explicitly identified.'); return result
    if review.get('disposition') == 'REJECTED':
        contradiction = any(e.get('claim_id') in material_ids and assessments.get(e.get('id')) == 'contradicts' for e in valid)
        if contradiction:
            result.update(state='REJECTED', explanation=review['explanation'], safe_next_action='Do not act on this rejected candidate; retain the cited contradiction for review.')
        else:
            result.update(state='NEEDS VERIFICATION', explanation='Rejection lacks a retrieved, semantically assessed contradiction.')
        return result
    if review.get('blocker_search_complete') is not True:
        result.update(state='NEEDS VERIFICATION', explanation='The reviewer did not explicitly complete the blocker review.'); return result
    if candidate.get('reported_blocker'):
        result.update(state='NEEDS VERIFICATION', explanation='A reported blocker has not been resolved with a cited source and semantic review.')
        return result
    if coverage.get('critical_unknown', True):
        result.update(state='NEEDS VERIFICATION', explanation='Coverage or essential source completeness is unknown or incomplete.')
        return result
    supported = all(any(e.get('claim_id') == claim and e.get('relation') == 'supports' and assessments.get(e.get('id')) == 'supports' for e in valid) for claim in material_ids)
    if review.get('disposition') == 'SUPPORTED' and supported:
        result.update(state='SUPPORTED', explanation=review['explanation'], safe_next_action='Ask the user to review the cited evidence and authorize any subsequent action.')
    else:
        result.update(state='NEEDS VERIFICATION', explanation='Not all material claims have retrieved citations and explicit semantic support.')
    return result


def investigate(candidates: list[dict[str, Any]], sources: dict[str, str], coverage: dict[str, Any], reviews: Any, expert_state: str = 'completed') -> dict[str, Any]:
    # Empty or unstructured reviewer output does not delete candidates.
    review_map: dict[str, Any] = {}
    duplicated: set[str] = set()
    if isinstance(reviews, list):
        for item in reviews:
            if not isinstance(item, dict) or not isinstance(item.get('candidate_id'), str):
                continue
            candidate_id = item['candidate_id']
            if candidate_id in review_map:
                duplicated.add(candidate_id)
            review_map[candidate_id] = item
    for candidate_id in duplicated:
        review_map[candidate_id] = None
    records = []
    for candidate in candidates:
        review = review_map.get(candidate.get('id'))
        evidence_candidate = deepcopy(candidate)
        evidence_candidate['evidence'] = [dict(deepcopy(e), origin='candidate') for e in candidate.get('evidence', []) if isinstance(e, dict)]
        if expert_state == 'completed' and isinstance(review, dict) and 'additional_evidence' in review:
            new_evidence = review['additional_evidence']
            if not isinstance(new_evidence, list) or not all(isinstance(e, dict) for e in new_evidence):
                review = None
            else:
                evidence_candidate['evidence'].extend(dict(deepcopy(e), origin='review') for e in new_evidence)
        records.append(classify(candidate, match_evidence(evidence_candidate, sources), coverage, review, expert_state))
    # Keep unreviewed proposed actions in the internal candidate record only.
    # A public report must not accidentally present a blocked candidate's
    # original action as a recommendation.
    public = []
    for row in records[:3]:
        candidate = row['candidate']
        public.append({
            'state': row['state'],
            'discovery_hypothesis': candidate.get('discovery', ''),
            'why_it_might_matter_unverified': candidate.get('why_matters', ''),
            'explanation': row['explanation'],
            'evidence': deepcopy(row['evidence']),
            'sourced_blockers': deepcopy(row['blockers']),
            'reported_blocker_unverified': row['unverified_blocker'],
            'safe_next_action': row['safe_next_action'],
            'suggested_file_groupings': [],
        })
    return {'candidates': records, 'coverage': deepcopy(coverage), 'user_facing': public,
            'empty_message': 'No meaningful discovery is sufficiently supported by the available evidence.' if not records else None,
            'notice': 'Local deterministic simulation; semantic judgments are supplied fixtures, not verified truth or NAS execution.'}


def render_report(result: dict[str, Any]) -> str:
    """Render safe public fields. Exact output is still a local simulation."""
    lines = ['# Illustrative discovery report — local simulation', '',
             'This is fictional; no NAS, real expert, user action, or independent semantic verifier was used.']
    if not result['user_facing']:
        lines += ['', '## Discovery', result.get('empty_message') or 'No sufficiently supported discovery was established.']
    for row in result['user_facing']:
        lines += ['', f"## Discovery — {row['state']}", row['discovery_hypothesis'],
                  '', '## Why it might matter', row['why_it_might_matter_unverified'] or 'Not established.',
                  '', '## Evidence']
        if not row['evidence']:
            lines.append('No source evidence is available.')
        for e in row['evidence']:
            lines.append(f"- {e.get('path', 'unknown source')}: {e.get('excerpt', '')} "
                         f"(retrieved={e.get('retrieved')}, exact_match={e.get('exact_match')}, "
                         f"relation={e.get('relation', 'unknown')}, semantic assessment={e.get('semantic_assessment', 'unknown')}).")
        lines += ['', '## Blockers and uncertainty', row['explanation']]
        for blocker in row['sourced_blockers']:
            lines.append(f"- Sourced blocker: {blocker['text']} ({blocker['path']}: {blocker['excerpt']})")
        if row['reported_blocker_unverified']:
            lines.append('Unverified reported blocker: ' + row['reported_blocker_unverified'])
        lines += ['', '## Recommended next action', row['safe_next_action']]
    cov = result['coverage']
    counts = cov.get('counts', {})
    lines += ['', '## Investigation coverage',
              f"Discovered: {counts.get('discovered', 'unknown')}; selected: {counts.get('selected', 'unknown')}; read: {counts.get('read', 'unknown')}.",
              'Discovered paths: ' + str(cov.get('discovered_paths', 'unknown')),
              'Selected paths: ' + str(cov.get('selected_paths', 'unknown')),
              'Read paths: ' + str(cov.get('read_paths', 'unknown')),
              'Skipped: ' + str(cov.get('skipped', 'unknown')),
              'Failed: ' + str(cov.get('failed', 'unknown')),
              'Truncated: ' + str(cov.get('truncated_paths', 'unknown')),
              'Referenced but not found: ' + str(cov.get('referenced_missing_names', 'unknown')),
              str(cov.get('scope_coverage', 'Scope coverage unknown.')),
              '', '## Optional suggested groupings', 'No grouping suggested; no files were moved.']
    return '\n'.join(lines) + '\n'
