# SKILL.md execution model

Sources: installed `docs/skill-development-standard.md`, `SKILL.md`, `references/{skill-format,expert-orchestration,cli-usage-rules,safety-and-approval,completion-and-errors}.md`, `data/capability-catalog.json`. The Skill is a Markdown procedure interpreted by a model; the standard authorizes delegation, not arbitrary executable code. Static checks do not make advisory behavior deterministic.

| Requested behavior | Status | What documentation actually supports |
|---|---|---|
| Branch based on returned facts | DOCUMENTED WITH CONDITIONS | Markdown can instruct the parent to conditionally delegate or ask; correct adherence and returned facts are runtime-dependent. |
| Repeated bounded search | PLAUSIBLE BUT UNVERIFIED | A Skill can specify a maximum and stop condition; no enforced loop construct or guaranteed pagination/completeness. |
| Multi-step model reasoning | DOCUMENTED WITH CONDITIONS | Orchestration and synthesis are the purpose of the workflow; correctness or added intelligence beyond generic Uliya is not established. |
| Sequential delegation | DOCUMENTED WITH CONDITIONS | `delegate` to each CLI's owner and pass verified results; shape/availability remain unverified. |
| Parallel delegation | UNKNOWN | No concurrency/join semantics or isolation guarantee in inspected authoring references. Independent work may be requested but do not promise parallelism. |
| User clarification | DOCUMENTED WITH CONDITIONS | Public `waiting_user` exists; exact UI, state retention and resumption not specified. |
| User and gateway/workflow approval | DOCUMENTED WITH CONDITIONS | Child performs platform approval for labeled operations; `waiting_approval` is a non-complete state. Exact approval UI, tokens and resume behavior unknown. |
| Failure / cancellation / partial work | DOCUMENTED AS INSTRUCTIONS | Must explicitly handle five delegation statuses and preserve partial results; per-action envelopes, compensation and network failure behavior unknown. |
| Information across handoffs | DOCUMENTED WITH CONDITIONS | Parent may pass verified results in self-contained delegations; schemas and stable IDs unknown. Never invent evidence. |
| State across separate chats | UNKNOWN | No documented durable parent state, session identity or automatic carryover. A user may separately supply saved content. |
| Persisted text/artifacts | DOCUMENTED WITH CONDITIONS | `save-text` is workflow-approved and returns a described `outputFile`/`verified`; real result, file collision behavior and retrieval remain unverified. No generic database primitive. |
| Resume after interruption/approval | UNKNOWN | Status labels alone do not promise durable resume, retry identity or exactly-once execution. |
| Idempotency | UNKNOWN | No general idempotency keys, transactional guarantees or safe repeat semantics. |
| Scheduled execution / triggers / watchers | UNSUPPORTED IN CATALOG | No exposed action registers a timer, watcher, webhook or event-driven workflow. Querying past camera events is not monitoring for future changes. |
| Long-running jobs | UNKNOWN | Some actions indicate `submitted`/`partial`, and file-workflow has `start`/`run`; no universal job polling, limits or restart semantics established. |
| Media playback and analysis in one turn | DOCUMENTED WITH CONDITIONS | Parent can request media-agent and other expert work sequentially, but playback is state-changing and exact result-to-player mapping and real output availability are unknown. No synchronized interaction. |
| Automatically react later to changed data | UNSUPPORTED IN CATALOG | A later user request can start another evaluation; unattended watchers and background activation are not documented. |

A Skill packages a reusable trigger, scoped sequence, good failure handling and consistent choices. It does not itself introduce new tools, a signal processor, privileged access, a UI or an inherently stronger model. A competent generic Uliya assistant with the same tools may reproduce a workflow; no comparative user study has established an advantage. Cross-agent routing is a documented authoring pattern, not proof all expected result fields propagate.
