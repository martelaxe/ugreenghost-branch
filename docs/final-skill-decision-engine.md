# Decision engine and transitions

This is the intended **model-interpreted** procedure in `prototype/final-flagship`, not a program or proven state machine. Conceptual labels below are presentation states; actual experts return `completed`, `failed`, `cancelled`, `waiting_user`, or `waiting_approval`. A parent must not invent a status.

| Stage / precondition | Owner and operation | Branch / transition | Output / interaction |
|---|---|---|---|
| Intent / invocation | parent | A proposed move, rename, deletion or consolidation → scope; otherwise clarify. | WAITING FOR USER if goal missing. |
| Scope / user input | parent | Require actual target, action, needed destination/name, and explicitly authorized roots; excluded path → ask, never read. | WAITING FOR USER; no fabricated path. |
| Target check / authorized | `file-agent`, `stat` / `find` | `completed` with target → bounded discovery; absent/inaccessible → stop target-specific claims. | BLOCKED or PARTIAL with actual evidence. |
| Discover / target present | `file-agent`, `find` / `ls` | Use real bounds; preserve returned candidate paths. Empty, limit-reached, inaccessible or unproven completeness → unknown rather than no dependencies. | Actual inventory and known gaps. |
| Examine / selected candidates | `document-agent`, `qa` / `reconcile` | Only real returned selected paths; classify exact references, ambiguous names, historic/context and contrary. No returned source → no invented citation. | Observations vs inferences. |
| Falsify / material uncertainty | `knowledge-agent`, `collect-evidence` | Ask a candidate-specific support + contrary question only if useful and scoped; preserve unknown if no result. | Referenced real evidence, where available. |
| Compare copies / explicitly requested | `file-agent`, `sha256sum` | Equal → matching bytes at check time; unequal → different bytes; missing → unknown. Role evidence independently assessed; never conclude safe deletion. | Hash comparison only where returned and mapped. |
| Synthesize / sufficient result | parent | Preserve supported findings and relevant contradictory evidence; one safe next action; no blanket safety claim. | COMPLETED for bounded review if substantiated, PARTIALLY COMPLETED when material limits apply; no action executed. |
| Expert failed/cancelled | any applicable expert | Do not run dependent steps; retain reliably returned earlier evidence. | FAILED or CANCELLED; partial earlier evidence identified. |
| Expert waiting | any applicable expert | `waiting_user` → ask for actual missing input; `waiting_approval` → surface and stop. | WAITING FOR USER or WAITING FOR APPROVAL, not completed. |
| Repeated request | parent + same experts | Treat as fresh since files may have changed; no assumed cache or prior approval. | New bounded review. |
| User requests actual change | outside this Skill | Explain the separate workflow, authorization and platform approval; never execute here. | Separate action pending; no assumed rollback or atomicity. |

No claim of fully identifying dependencies is justified without actual app integrations and a completeness contract. Exact hash reads can be costly; the Skill asks for them only for explicitly selected candidate copies and does not promise measurable resource improvement. Destination conflict is a relevant issue for later action, but this Skill performs no write and does not claim destination race protection. Exact output format and handoff propagation remain device unknowns.
