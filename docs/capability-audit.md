# Initial UGREEN capability audit

Source: the official [UGREEN starter kit](https://ai.ugreen.com/pages/hackathon-starter-kit), downloaded 2026-10-26; creation kit 0.7.3, public capability catalog 2.0.0. The kit is stored under `resources/uliya-skill-kit/`. This is a catalog-level audit, not a NAS test.

| Proposed action | Catalog entries | What we know |
| --- | --- | --- |
| Discover files | `ug-filesystem:find` and `ls` -> `file-agent` | Read operations; parameters and access need to be checked for the exact use case. |
| Inspect content | `ug-filesystem:cat` -> `file-agent`; `ug-document:extract` -> `document-agent` | Listed as reads. Format support, content limits, and performance require confirmation. |
| Compare documents | `ug-document:reconcile` -> `document-agent` | Listed as read. Whether it delivers our kind of surprise, citations, and uncertainty is unverified. |
| Save a report | `ug-knowledge:save-text` -> `knowledge-agent` | Listed as a state change requiring workflow approval. Availability and exact output need runtime validation. |
| Organize | `ug-filesystem:cpmv` -> `file-agent`; `file-workflow:batch-move` -> `file-agent` | State changes use gateway/workflow approval. Exact semantics, conflict handling, and auditability need validation. |
| Restore a previous organization | `ug-filesystem:restore` -> `file-agent` | A restore action exists, but its catalog description is not specific enough to establish what it restores. No catalog entry found that establishes a dated folder-structure history or selective rollback. Do not promise either. |

The catalog documents actions, not a working deployment. An orchestration Skill delegates to registered agents; the parent Skill must not directly execute CLI actions. The official competition package excludes custom executable scripts and binaries. The local synthetic experiment is separate from that package.

Next: read the full parameters and examples for a narrow discovery workflow; check supported document formats and verify how references/evidence appear in results. Ask UGREEN if time-based history and selective restoration are available.
