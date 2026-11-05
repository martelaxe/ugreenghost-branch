# Competitors and preliminary judge assessment

Sources reviewed 2026-10-26. This is research judgment, not actual hackathon judging. Consult [official rules](https://ugreenhackathon.devpost.com/rules) for the four equally weighted criteria and Round 1 versus Round 2.

## Existing products

- [Session Handoff skill](https://github.com/crd/session-handoff) explicitly describes a Markdown handoff carrying decisions, artifacts, pending steps and resumption, including checking for divergent/stale state. This is a particularly close match; advertised repository behavior, not our independent execution. It is aimed at coding sessions and cannot be assumed to run under UGREEN's Skill constraints.
- [Handoff Skill](https://github.com/jumpifequal/handoff-skill) describes vendor-neutral Markdown preserving decisions, work-in-progress, provenance and next action for another model. Another close functional overlap; not independently tested.
- [OpenGrove Handoff](https://github.com/open-grove/handoff) describes portable, resumable Markdown handoffs across several agents via a share service; unlike our concept it can involve external upload, and its capabilities are vendor-described.
- [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence) documents thread checkpoints and cross-thread stores. That is implemented application infrastructure, more than a Markdown handoff, and is not directly available as an arbitrary UGREEN Skill runtime.
- [Nextcloud Assistant](https://docs.nextcloud.com/server/stable/user_manual/en/ai_assistant.html) documents contextual conversations and file-based Skills. Its overlapping exact cross-agent handoff workflow is not established here; it is a relevant file-aware alternative.
- [VS Code agent memory](https://code.visualstudio.com/docs/agents/run/memory) describes session and persistent instruction/memory mechanisms for coding agents; use and scope differ from a UGREEN NAS application.
- [Filesystem-based memory research](https://arxiv.org/abs/2607.26637) reports search-cost benefits for some organized large stores but does not establish that organization itself improves answers. It is research, not UGREEN validation.

A saved Markdown handoff is an existing pattern, not a novel invention. This project could offer convenience from an appliance's existing storage and permissions only if a later session retrieves the actual file, rechecks actual sources and safely captures user decisions. Explicit path selection and approval are still needed. The record is shared storage content—not proof of automatic state sync, conversational memory, or an agent runtime. No global novelty or direct product superiority is established. A visually clear fresh-session continuation is more memorable than another summary, but generic file-aware agents and existing handoff Skills can already do it. The Round 1 deadline is 15 November 2026 11:45 p.m. Pacific; device access is not required for Round 1, but Round 2 requires real device execution.

## Equal-weight provisional scores

The final author-assessed 0–25 scores and their supporting local evidence are recorded in `evaluation-results.md` and the decision memo after execution. There is no official subrubric, no real judge or human participant, and scores cannot establish creativity. Particular reservations are close competitors, no automatic record discovery, prompts versus enforced controls, actual `save-text` semantics and user effort. The author will not choose a project solely on such scores.

After the local runs, the author's cautious assessment is User Value **17/25**, Innovation **5/25**, Technical Quality **12/25**, AI NAS Fit & Validation **9/25** (43/100). See the evidence and caveats in [evaluation results](../../experiments/14-task-continuity/evaluation-results.md). The two most serious demonstrated reliability problems are nonportable raw source links and a wrong file count in a repeated Skill-guided result. The closest competitor overlap plus G1's comparable results are stronger grounds for the recommendation than any subjective total.
