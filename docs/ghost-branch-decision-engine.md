# Ghost Branch decision engine

This is a Markdown policy interpreted by a model, not a program or guaranteed state machine.

| Stage | Input / owner | Decision and observable output |
|---|---|---|
| Interpret mode | Parent; owner request | Discovery, focused feature investigation, or selected-candidate packet. Missing target/scopes → `waiting_user` or ask. |
| Bound scope | Parent + user | Require authorized current and archived folders. Unknown/denied folder stays uninspected. Avoid secrets, `.env`, keys and unrelated private material. |
| Find | `file-agent`: `ug-filesystem:find`/`ls` | Request at most 100 paths/30 selected source files by default. Empty → report no results within scope. Caps are requests, not proof of coverage. |
| Read / normalize | `file-agent`/`document-agent`, optionally `photo-agent` | Work only with real returned paths/content. Screenshot is UI appearance, not execution; preserve source type and unverified fields. |
| Compare | `document-agent` or source returned by `file-agent` | Search current selected evidence for actual equivalent behavior; a different filename is not proof of disappearance. |
| Challenge | `knowledge-agent` optionally; actual notes/logs | Seek retirement/security/test failures and alternate versions. An empty or failed verification is not a rejection. |
| Classify | Parent | Source-backed promising implementation and no known decisive blocker → **RECLAIM CANDIDATE** for investigation. Explicit sourced retirement or security decision → **RETIRED FOR A REASON**. Conflict/missing key evidence or screenshot only → **UNCERTAIN**. Equivalent/current or insufficient evidence for distinct missing work → **NOT ESTABLISHED**. Categories are advisory. |
| Handoff | Parent | Report exact actual paths, facts vs inferences, arguments for/against, scope gaps and future tests; no code integration, Git operations or tests performed. |
| Optional save | `knowledge-agent` `ug-knowledge:save-text` | Explicit destination/request + documented workflow approval; require safe collision semantics and actual completion. Unknown → preview only; never auto-retry. |
| Completion/failure | All children | Only `completed` plus real required evidence supports dependent steps. `waiting_user`, `waiting_approval`, `failed`, `cancelled` remain visible and stop the affected branch; retain earlier evidence. |

Policy must not infer global absence, shipped status, causality from timestamps or safety of old code. It should not disclose credentials. These are model instructions, not a proof they are enforced by the platform. [Policy-only unit tests](../experiments/ghost-branch/policy-test-output.txt) exercise a separate local simulation; they do not execute the Skill.
