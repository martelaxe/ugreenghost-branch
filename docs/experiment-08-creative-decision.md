# Experiment 08 — creative decision

Research date: October 26, 2026. **Primary recommendation: REDESIGN around Creative Salvage**, a creator-facing proposal that turns selected abandoned project notes into two usable new directions and shows where documented restrictions change the choice. **Fallback: Knowledge Succession Rehearsal**, a safer text-only handoff practice. Neither is validated with users or on UGREEN hardware. The user prioritizes the Most Creative award, whose published criterion is Innovation & Differentiation; that explains selecting a higher-risk creativity candidate over the higher-scoring general-purpose fallback.

## What users struggle with

Twenty new primary user discussions and issue reports, distinct from Experiment 07 research links, are documented in [new user evidence](../research/08-task-aware-nas/new-user-evidence.md). They suggest three important problems:

1. **A collection can look complete while required material is absent or unprocessed.** A scanned archive with a missing page, import errors and inaccessible photo folders illustrate different mechanisms; a search miss is not evidence that an item does not exist.
2. **A file can be present but unusable without context.** Creative teams report relinking and handoff friction; photographs or releases can be separated from asset identifiers, and comparable records may need different treatment.
3. **A task can turn on a genuine ambiguity rather than a retrieval problem.** Different versions or same-name historical records can produce different answers; evidence for an exception can make an apparent omission legitimate.

These are qualitative, self-selected reports, with some indexed snippets; they establish neither prevalence nor willingness to pay for our ideas. See the linked report for each user's workaround, current features and uncertainties.

## The competition is closer than it first appears

[Nextcloud Assistant](https://docs.nextcloud.com/server/stable/user_manual/en/ai_assistant.html) already documents chained tools and custom Skills. [Open WebUI](https://docs.openwebui.com/features/workspace/knowledge/) and QNAP offer source retrieval/AI experiences. [Invoice-agent](https://github.com/superintelligenceco/invoice-agent) and [Woodrow](https://www.woodrow.ai/agent-workflows/ap-invoice-processing) describe invoice matching, missing data and review states. [Adobe Experience Manager Assets](https://business.adobe.com/products/experience-manager/assets/digital-rights-management.html) advertises finding assets for reuse and rights management. These are documented or vendor-reported features, not hands-on independent product tests.

Our own generic Codex baseline already searched two authorized folders, found a missing invoice, rejected a wrong-year record, identified a legitimate exception, compared conflicting revisions and handled a limited scope. The [competitor matrix](../research/08-task-aware-nas/competitor-reality-check.md) identifies exactly which other behaviors were and were not established. The official gallery remains unpublished; one individually accessible [ClaimReady](https://devpost.com/software/claimready-home-inventory) entry overlaps with home-inventory evidence work. We cannot comprehensively survey all UGREEN entries or Skills.

## Ideas and selection

The [creative universe](../research/08-task-aware-nas/creative-concepts.md) contains **24 distinct proposed user outcomes**, eight in each requested tier. Some share techniques and may overlap existing products. The [combination study](../research/08-task-aware-nas/unexpected-combinations.md) presents eight further combinations. The strongest combination is **creative reuse + an explicit rights blocker + a fallback pitch**: the output remains useful even when the first exciting path cannot safely proceed. This is a hypothesis about user value and novelty, not a demonstrated invention.

Five strongest concepts, from the [six-candidate ranking](../research/08-task-aware-nas/candidate-ranking.md):

1. **Knowledge Succession Rehearsal:** another person practices a real task using the owner's selected handoff notes and identifies unresolved steps.
2. **Creative Salvage:** propose new creative directions grounded in existing notes and asset terms, holding any restricted or uncertain reuse.
3. **Missing Piece:** assemble a requested result while distinguishing truly expected, legitimate exceptions and unresolved records.
4. **Fork & Finish:** show conditional completed reports reflecting disputed versions, then ask which assumption to adopt.
5. **Decision Replay:** compare documented evidence and alternatives behind a decision, with no claim to know what a person thought or saw.

**Finalists:** Creative Salvage, Succession Rehearsal and Fork & Finish. Surprise Me remains an evidence-handling foundation and optional fallback, not the main pitch. The five scores are subjective under the official four equally weighted dimensions; small differences are not statistically meaningful. Creative Salvage is recommended despite Succession's higher estimated overall score because its proposed demonstration may score better on the specifically requested creativity criterion.

## The best proposed demonstration

A fictional filmmaker asks for two pitches using authorized old-project and rights notes. The assistant finds an appealing unused scene, then presents a source-backed exhibition restriction that puts use on hold; it offers another idea grounded in a separately identified, apparently permissible source. The creator chooses which route to investigate. The result is two short text pitches, exact evidence, uncertainties and one safe next step—not a generated video or automatic legal clearance. The [storyboards](../research/08-task-aware-nas/demo-storyboards.md) contain exact prompts, inputs and timelines. Whether creators or judges actually find this surprising is untested.

The strongest defensible contrast with generic Codex is currently an **intended workflow**, not a proven capability: a reusable, bounded NAS Skill would ask documented experts for source material and show creative alternatives plus restrictions in a single user-facing decision. A well-prompted generic assistant with the same files can attempt exactly this; a mounted NAS may give it equivalent access. No distinctive technical mechanism or measurable improvement is established.

## What was actually tested

Four small adversarial invoice cases were preregistered; eight fresh `codex exec` processes ran, one generic and one specialized per case, with the same files, task, requested model and effort. Both handled the main case facts. The subjective author-scored totals were **38/40 generic and 35/40 specialized**; the specialized conflict report used five broken absolute citation links. The generic report asked one unnecessary confirmation; the specialized condition asked one in another case and misattributed a scope detail. This is one run per case—not a statistically significant comparison, general accuracy measurement, or evidence that generic always wins. No specialized improvement was demonstrated.

Workspaces held only assigned fictional inputs, but `read-only` is not a full read-isolation boundary; key permissions were restricted only after process launch. Logged commands stayed in the workspaces, yet complete blinding cannot be guaranteed. The evaluator knew the condition names. One-shot CLI output does not prove user-interaction continuation. Full raw reports, errors, events, prompts, hashes, exact scores and limitations are in [test results](../experiments/08-task-aware-nas/test-results.md) and [benchmark design](../experiments/08-task-aware-nas/benchmark-design.md). No UGREEN agents, real users or creative-idea quality were tested.

## UGREEN reality and decision

The installed catalog documents file discovery, document extraction/comparison, knowledge evidence collection, photo operations and approval-gated saving. The parent delegates to registered experts rather than executing their commands itself. What remains unverified: actual return fields, reliable path/excerpt provenance across handoffs, multi-turn user-decision persistence, incomplete results and truncation reporting, photo-to-document identity, format support and performance on a large archive. The [feasibility map](../research/08-task-aware-nas/capability-feasibility.md) identifies actions, parameters, effects and boundaries. No UGREEN device was used.

**Missing Piece: REDESIGN as a supporting evidence and exception-handling pattern, not an invoice-centered innovation claim.** Its core was reproduced by generic Codex and resembles existing invoice workflows. **Succession remains in contention** as the fallback. **Surprise Me remains a source of reusable safeguards**, but previous generic benchmarks and current research weaken its broad pitch.

**Creative Salvage: REDESIGN, not GO.** Before selecting it for submission, it must show (1) useful, traceable pitches from authentic creator-relevant examples; (2) no fabricated links or unsafe reuse recommendations; (3) a meaningful preference or task benefit against a competent generic baseline under equal inputs; and (4) at least a plausible documented UGREEN path, with actual expert-return and state behavior tested when device access is available. A close competitor offering the same experience, creator indifference, ungrounded ideas, fabricated rights or inaccessible necessary agent data would justify **STOP** or a pivot to Succession Rehearsal.

**Next engineering milestone:** create one small fictional creative-project archive with two rival briefs, an explicit restriction, an unrelated decoy, a usable independently documented alternative and a missing rights record. Run matched fresh generic and specialized Codex sessions without answer-key access, then have real creators blindly judge whether either output changes what they would pursue; predeclare source, identity and rights failure criteria. Do not claim user validation until real people participate. Separately obtain sanitized real UGREEN expert outputs when available, focusing on source IDs, excerpts and state handling.

The most likely reason the recommended concept loses is that judges see a familiar generic brainstorm combined with standard rights review. No convincing advantage over an equally capable generic assistant or creative DAM has yet been shown. The [originality red team](../research/08-task-aware-nas/originality-red-team.md) spells out this and other objections.

Round 1 deadline remains November 15, 2026, at 11:45 p.m. Pacific (November 16, 1:45 a.m. Mexico City); [official rules](https://ugreenhackathon.devpost.com/rules). No final PDF, ZIP or new Skill was created.
