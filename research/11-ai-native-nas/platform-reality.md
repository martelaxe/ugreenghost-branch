# Platform reality: what the Skill can and cannot claim

Checked 2026-10-26 against [official rules](https://ugreenhackathon.devpost.com/rules), [Starter Kit](https://ai.ugreen.com/pages/hackathon-starter-kit), and installed `uliya-skill-kit` 0.7.3 `data/capability-catalog.json` 2.0.0. Catalog action names/owners below come from that file, including all nine CLI families; the table lists relevant actions, not an exhaustive action list. The [complete catalog](/home/martelaxe/ugreen-hackathon/resources/uliya-skill-kit/data/capability-catalog.json) is preserved in the project. `read / none` is catalog effect and approval metadata, not a grant to access someone else's files.

| CLI → registered agent | Relevant documented actions | Effect / approval, essential parameters | Meaningful limitation |
|---|---|---|---|
| `ug-filesystem` → `file-agent` | `find`, `cat`, `stat` | read / none; each requires `path` | Search is bounded; no promise of complete inventory or readable formats. `find` can accept `pattern`, `max-depth`, `limit`; no assumed continuation. |
| Same | `cpmv`, `del` | state-change / gateway; `cpmv` requires `src`,`dst`; `del` requires `path` | Writes are outside this MVP; approval and real completion belong to child workflow. `restore` does not establish arbitrary point-in-time recovery. |
| `ug-filemgr` → `file-agent` | `scan-dedupe`, `tag-add` | scan read / none with required `path`; tag-add state-change / gateway | A duplicate report does not establish an unneeded path or safe deletion. |
| `file-workflow` → `file-agent` | `batch-move`, `batch-del` | state-change / workflow | Optional child workflows, not permission for the parent to mutate or guarantee undo. |
| `ug-document` → `document-agent` | `qa`, `extract`, `reconcile` | read / none; `qa`/`extract` require `query`; `reconcile` has optional `query`,`file`,`max-files` | File format/identifier support, exact path extraction, excerpts, completeness and comparison reliability are not guaranteed. |
| Same | `writing` | mixed / gateway | Do not assume it is a read-only text generator or needs no approval. |
| `ug-knowledge` → `knowledge-agent` | `collect-evidence`, `audio-transcription` | read / none; collect requires `query` | No documented guarantee of source-level handoff, quote spans, audio format or exhaustive checks. |
| Same | `save-text` | state-change / workflow | Separate optional save after required approval; not part of MVP. |
| `ug-photo` → `photo-agent` | `search-picture`, `meta`, `vision-vlm` | read / none; optional real IDs/paths and VLM prompt | Multimodal correctness, returned IDs, file types and privacy behavior are unverified. |
| Same | `create-album` | state-change / workflow | Album creation is a write, not an automatic core output. |
| `ug-video` → `media-agent` | `search`, `subtitle-search` | search mixed / none and requires `type`; subtitle search read / none | Search can include playback; neither establishes arbitrary video parsing, editing or rendered artifacts. |
| `ug-music` → `media-agent` | `search` | mixed / none; requires `type` | Search may include playback; no guarantee of analysis of arbitrary audio files. |
| `ug-surveillance` → `security-monitor-agent` | `event-timeline` | read / none; requires `start-time`,`end-time` | Restricted surveillance data; not a file dependency graph, version history or general monitoring subscription. |

## Model, Skill and experts

The model performs synthesis and reasoning; a Uliya Skill supplies reusable trigger, task goal, allowed scope, expert routing, evidence/output and state/approval rules. The parent delegates via `delegate --target <registered-agent> --instruction '<self-contained task>'`; each child owns its documented CLI workflow. The parent does not directly call `cli.invoke`, invent returned fields or execute arbitrary code. Pass only real business results from completed experts to dependent tasks. Explicitly surface `completed`, `failed`, `cancelled`, `waiting_user`, `waiting_approval` and do not convert pending into success. No fixed reasoning chain is required by the standard, but real scope, completion and approval contracts are necessary.

UGREEN [Model Manager](https://ai.ugreen.com/pages/notice-on-model-manager) describes built-in semantic search, document analysis, knowledge Q&A, file management and model choices including local and cloud providers. The Starter Kit lists typical file, photo, knowledge and media workflows. Neither source proves exactly what a default Uliya assistant can accomplish without a Skill in every model/configuration, nor whether it already supports this proposed interaction. A Skill can package a repeatable task and supported delegation; it does not automatically add tools, enforce isolation, invent a UI or grant new permissions. Whether defaults and Skills differ in quality must be tested on actual hardware.

## Product and deadline implications

A scoped question about a proposed file move can use cataloged discovery, document reading and evidence collection; a text impact map is **conceptually** possible. No action establishes a complete dependency graph, app internals, external shares, live link semantics, sandbox simulation, restoration or historical snapshots. An uncited source or incomplete inventory must remain unknown. Static validation and Codex experiments do not verify any NAS return.

Round 1 closes **November 15, 2026, 11:45 p.m. Pacific** (November 16, 1:45 a.m. Mexico City); finalists get one assigned remote testing day before final submission. Round 1 requires the PDF and Markdown-only package described in the rules; no actual NAS run is required then. Speculation about what UGREEN's product team may want is ours, not a roadmap. Recheck official rules before submission.
