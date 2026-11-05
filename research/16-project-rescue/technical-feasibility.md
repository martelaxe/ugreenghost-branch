# Technical feasibility and action safety

Checked 2026-10-27: installed Uliya Skill Creation Tool 0.7.3, catalog 2.0.0 and orchestration, safety, approval and completion references; [official rules](https://ugreenhackathon.devpost.com/rules) and [starter kit](https://ai.ugreen.com/pages/hackathon-starter-kit). The catalog assigns `ug-filesystem` exclusively to `file-agent`, `ug-document` exclusively to `document-agent`; the parent delegates and does not invoke their CLIs. The child chooses actual calls. No NAS expert return is fabricated.

| Behavior | Status | Basis and limitation |
|---|---|---|
| Discovery/read | DOCUMENTED | `find`: required `path`, optional `pattern`, `type`, `max-depth`, `limit`; `ls`: `path`, `recursive`, `max-depth`, `limit`; `cat`: `path`, `offset`, `length`. Results can be partial; returned coverage is not guaranteed. |
| Path and bytes | DOCUMENTED | `stat` and `sha256sum` accept `path`. File permissions, resolved-path and hash propagation on device are unknown. |
| Interpret candidate evidence | DOCUMENTED | `ug-document:extract` and `qa` require `query`, may take `file`, `max-files`, `body-cap`; `reconcile` supports `query`, `file`, `max-files`. Text versus SVG extraction and source excerpts at parent remain unverified. |
| Copy operation | DOCUMENTED | `ug-filesystem:cpmv` requires `src`, `dst`; optional `type`, `action-type`, `overwrite`. Its effect is state-change, approval gateway. Destination interpretation and actual collision handling not established. |
| Scoped owner consent | IMPLEMENTED IN SKILL | Scope authorization and separate exact-action consent are instructions, not a demonstrated runtime enforcement mechanism. |
| Platform approval and resume | UNKNOWN | Catalog identifies gateway, but UI, approval signals, resume and parent propagation are not guaranteed here. Pending is not completion. |
| Atomic no-overwrite | UNKNOWN | Neither a prior absent `stat` nor `overwrite=false` proves a race-free check-and-create. No authoritative atomic guarantee found; stop at proposal unless child/platform establishes it for the exact operation. No hypothetical confirmation API is assumed. |
| Source unchanged and destination readback | DOCUMENTED OPERATIONS; RUNTIME UNKNOWN | Capture source hash before approval, recheck before copy, then inspect and compare both hashes afterward; a hash does not establish semantic identity or application repair. Source can change during copy; post-check detects a mismatch but cannot undo it. |
| Local copy and synthetic approval | LOCALLY SIMULATED | Disposable local `O_EXCL` copy and synthetic flags are separate Python research tests, not NAS execution; see demo. |
| Arbitrary undelete, rollback, universal dependency graph, custom scripts in Skill | UNSUPPORTED | No documented guarantee; do not promise. |

**Safety distinction:** (A) destination absent at time of check can become present afterward; (B) requesting `overwrite=false` expresses desired behavior but its implementation is undocumented; (C) an atomic exclusive-create guarantee prevents replacing a concurrent destination. Only C is adequate to proceed. If path resolution, scope, candidate identity, source hash, platform approval or C is unknown, stop. Resolve paths and symlinks before operating; inability to establish confinement means stop. Handle `completed`, `failed`, `cancelled`, `waiting_user`, `waiting_approval` independently, and preserve partial evidence. This is a design constraint, not evidence UGREEN supports C.
