"""Illustrative expert handoffs. The result fields here are invented mock fields.

No real UGREEN agent, network, model, CLI action, or approval is invoked.
"""
from copy import deepcopy
from typing import Any
from discovery_v2 import investigate


def run_mock_handoffs(file_result: dict[str, Any], document_result: dict[str, Any], knowledge_result: dict[str, Any], candidates: list[dict[str, Any]]) -> dict[str, Any]:
    calls: list[str] = []
    sources: dict[str, str] = {}
    coverage: dict[str, Any] = {'scope_coverage': 'unknown: simulated envelopes only', 'critical_unknown': True,
                                'discovered_paths': [], 'selected_paths': [], 'read_paths': [],
                                'skipped': [], 'failed': [], 'truncated_paths': [], 'referenced_missing_names': []}
    def stop(reason: str, status: str) -> dict[str, Any]:
        coverage['failed'].append({'stage': reason, 'status': status})
        result = investigate(candidates, sources, coverage, [], expert_state=status)
        result['calls'] = calls[:]
        result['handoff_notice'] = 'Mock fields and envelopes are illustrative and not real UGREEN output.'
        return result
    calls.append('file-agent')
    if file_result.get('status') != 'completed':
        return stop('file-agent', str(file_result.get('status', 'unknown')))
    paths = file_result.get('paths')
    if not isinstance(paths, list) or not paths or any(not isinstance(p, str) for p in paths) or len(set(paths)) != len(paths):
        return stop('file-agent', 'invalid inventory')
    coverage['discovered_paths'] = paths[:]
    coverage['selected_paths'] = paths[:]
    calls.append('document-agent')
    if document_result.get('status') != 'completed':
        return stop('document-agent', str(document_result.get('status', 'unknown')))
    rows = document_result.get('documents')
    if not isinstance(rows, list):
        return stop('document-agent', 'invalid document result')
    for row in rows:
        if not isinstance(row, dict) or row.get('path') not in paths or not isinstance(row.get('text'), str) or row['path'] in sources:
            return stop('document-agent', 'invalid or unexpected source')
        if row.get('complete') is not True:
            coverage['truncated_paths'].append(row['path'])
            continue
        sources[row['path']] = row['text']
    coverage['read_paths'] = sorted(sources)
    coverage['critical_unknown'] = (set(paths) != set(sources) or bool(coverage['truncated_paths'])
                                    or file_result.get('coverage_complete') is not True
                                    or document_result.get('coverage_complete') is not True)
    if coverage['critical_unknown']:
        return stop('document-agent', 'incomplete evidence')
    calls.append('knowledge-agent')
    if knowledge_result.get('status') != 'completed':
        return stop('knowledge-agent', str(knowledge_result.get('status', 'unknown')))
    reviews = knowledge_result.get('reviews')
    if knowledge_result.get('coverage_complete') is not True:
        coverage['critical_unknown'] = True
    result = investigate(candidates, sources, coverage, reviews, expert_state='completed')
    result['calls'] = calls[:]
    result['handoff_notice'] = 'Mock fields and envelopes are illustrative and not real UGREEN output.'
    return result
