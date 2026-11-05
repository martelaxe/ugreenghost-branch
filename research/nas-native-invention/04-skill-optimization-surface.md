# Optimization surface through Markdown orchestration

| Hypothesis | Documented expert calls | Plausible instructions vs hard runtime requirement |
|---|---|---|
| Progressive discovery | `file-agent` `find`, `ls`, `stat`; `document-agent` extract/QA | Ask for metadata first and selectively read. Success depends on actual returned path and size, correct model planning and no excluded necessary file. No cost planner. |
| Hierarchical processing | `find`/`ls` with `max-depth`, `limit` | Ask for bounded directory-by-directory scans and report unknown. No promised continuation, stable cursor or complete enumeration, and a model may lose counts. |
| Candidate selection | `stat`, `sha256sum`, `ug-filemgr:scan-dedupe` | Length mismatch can reject byte identity; equal size cannot. `scan-dedupe` return schema is unspecified. Proof needs actual hashes, not model assertion. |
| Persistent manifest | `knowledge-agent` `save-text` workflow approval; file-agent `cat` | Possible save/read if returned real path and permitted. No certified schema, atomic replacement, currentness, trusted invalidation, no-overwrite or background updates. |
| Action preflight | `file-workflow:start` read/plan; `run` workflow; `cpmv` gateway | User-readable proposal is plausible. Need actual plan details and explicit approval; no documented atomic no-overwrite, rollback or idempotent resume. Stay proposal-only when safety cannot be confirmed. |
| No-op | Read metadata/hashes, decline mutations | The parent can decide not to write. A model must not infer equivalence from size/time alone. |
| Adaptive investigation | Parent requests next scoped expert query | Only the instruction is available; no dynamic query optimizer, objective function or guaranteed decisions. Report unreviewed scope. |
| Failure-aware work | Public `completed`, `failed`, `cancelled`, `waiting_user`, `waiting_approval` | Report and halt dependent operations, but exact result schema, error cause, persistence and resume guarantees remain unknown. |

All operations must be delegated to their catalog owner. A parent Skill does not invoke child CLI directly and cannot run this experiment's adapter/client Python. A read-only core avoids accidental writes; explicit user intent plus actual gateway/workflow approval is required for relevant changes. Platform latency, exact context cost and all real expert envelopes remain unmeasured.
