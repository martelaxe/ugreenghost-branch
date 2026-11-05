# Minimum-change organization decision

**I tested whether a specialized UGREEN Skill can organize NAS collections with fewer unnecessary changes than generic AI and existing organization workflows...**

**Verdict: NO ADVANTAGE.** On the three main fictional datasets, both the generic agent and the specialized-guidance agent produced equally correct minimum-change plans in two runs apiece. No additional safety, plan quality or measured tool-use advantage was demonstrated. The native UGREEN planner was **not** run, so no claim about its relative performance is justified. The already-compliant fourth control was cut short by a Codex usage limit.

## Problem and mechanism

A NAS owner may have an archive that is mostly organized and a new explicit policy. The useful operation is to preserve every already-compliant item, identify genuinely necessary changes, and defer conflicts, unreadable records and unsafe target collisions. Zero moves is not successful if required correctable changes remain; fewer changes matter only after policy and safety are satisfied.

The proposed reusable guidance asks the `file-agent` to inventory the authorized scope, classify using real evidence, retain compliant files, compare candidate destinations, defer unknown or prohibited moves, and present a reviewable proposal. A separately approved real change would require actual platform approval, verified safe collision behavior and completion verification. The tested guidance was research-only Markdown, not a packaged or runtime-validated UGREEN Skill.

UGREEN's documented `file-workflow:start` accepts `kind`, `target` and optional organization parameters and summarizes a planned `id` and `plan`. `run` is workflow-approved and summarizes counts. `batch-move`, filesystem `ls`/`find`/`stat` and gateway-approved `cpmv` are documented under `file-agent`. What is not documented includes exact plan detail, compliant-file detection, collision behavior, minimality, plan editing, atomic no-overwrite, dependable per-file verification or actual approval/resumption. The native planner could already support some requested behavior; we did not test it. [Platform audit](../research/min-change-organization/01-platform-capabilities.md).

Rule-based tools already address related work. [QNAP Qfiling](https://www.qnap.com/en-uk/how-to/tutorial/article/how-to-use-qfiling) documents filing rules, destination previews and skip/overwrite/rename conflict choices. [Hazel](https://www.noodlesoft.com/manual/hazel/work-with-folders-rules/create-edit-rules/preview-a-rule/) previews rule matches; [File Juggler](https://www.filejuggler.com/documentation/interface/) shows matching/processed files. [Ansible](https://docs.ansible.com/projects/ansible/latest/module_plugin_guide/modules_intro.html) documents the broader desired-state/no-op principle. These are not identical to our specific policy, but minimal-change organization is not a new algorithm. [Competitors](../research/min-change-organization/03-competitor-review.md).

## Fixtures and results

The policy accepts **two** existing compliant folder trees and requires classification from file contents, not guessed extensions. A deterministic evaluator accepts either permitted free destination. User instructions prohibit overwrites, renames and arbitrary resolution of over-contested destinations. Test data contain text/CSV/JSON, real small PNGs, deliberately misleading `.pdf`/`.jpg` extensions, same-name conflicts, byte duplicates and different date formats. C also has contradictory metadata and a conflicting historic-folder rule. These are synthetic records, not general document collections.

| Fixture | Records | Already compliant | Minimum required moves | Correct deferrals | Generic G1/G2 | Guided S1/S2 |
|---|---:|---:|---:|---:|---|---|
| A: mostly organized | 186 | 160 | 18 | 8 | 18 moves; 160 keep; 8 defer | Same |
| B: heavily disorganized | 186 | 41 | 137 | 8 | 137 moves; 41 keep; 8 defer | Same |
| C: conflicting/ambiguous | 186 | 80 | 80 | 26 | 80 moves; 80 keep; 26 defer | Same |

All 12 main plans had zero unnecessary or missed moves, wrong/prohibited destinations, collisions and source-scope violations under the frozen key; each correctly deferred the 12 known C records where “organize everything” conflicted with “do not move out of historic.” Classification relied on actual returned local read results. Eighty-six percent of fixture A's files were independently confirmed compliant (160/186); eight other files remained unresolved, not automatically compliant.

Each G and S run performed 188 local adapter operations, reading 13,149 bytes in A, 13,139 in B and 13,198 in C. Four binary read failures per main run were correctly deferred. Across six completed main runs, mean elapsed time was 37.73 s for G and 37.83 s for S; mean reported input tokens were 97,946 for G and 109,692 for S. The two runs per cell were concurrent with other experiments and use local Python adapter clients; differences are descriptive and are not real NAS or billing measurements.

An independent evidence parser rechecked the key and small contested assignments; evaluator tests confirm that zero moves, an unsafe collision and a missing row fail. The evaluator scores move selection and whether deferrals have nonempty reasons, but does not fully grade their semantic explanations. Scores are anonymous and mechanical, but the condition mapping remained in the same scoring process; this was not a fully independent human blind review.

Dataset D, the 24-file no-op control, has one completed generic run with 24 keeps and zero moves. One further generic and one guided run produced complete-looking plan artifacts but their Codex processes failed before final completion because the account hit its usage limit; a second guided run produced no plan. Those partial artifacts are not counted as completed runs. See [detailed results](../experiments/min-change-organization/results.md).

No actual moves or approvals occurred. Disposable agent copies and original fixture file bytes remained unchanged. The local adapter's complete listing, UTF-8 reading, structured errors and Python client batching are not documented UGREEN return or execution guarantees. Large-archive scaling, real document formats, simultaneous changes, partial execution and native expert behavior remain untested.

## Demonstration and product assessment

A faithful 60-second proposal-mode demonstration could show fixture A's **160 retained files, 18 proposed changes and 8 deferrals**, with one already-compliant file, one move and one collision/unknown item. On actual UGREEN hardware, those claims can only be made if complete inventory, usable content evidence and results really arrive. Nothing in this experiment establishes an approved or verified NAS move.

The result is not stronger than [Project Rescue V2](experiment-16-project-rescue-decision.md) as a demonstrated action-oriented candidate: Rescue had a local source-preserving copy and hash-verified outcome, although generic Codex matched its reasoning and atomic no-overwrite on UGREEN is also unverified. Neither project has established a compelling creative advantage. The present idea should not move forward merely because its report is clearer or its prompt longer.

## Evidence paths

- [Full results and demonstration](../experiments/min-change-organization/results.md)
- [Platform audit](../research/min-change-organization/01-platform-capabilities.md), [optimization definition](../research/min-change-organization/02-problem-definition.md), [competitor review](../research/min-change-organization/03-competitor-review.md)
- [Frozen design](../experiments/min-change-organization/design.md), [generic prompt](../experiments/min-change-organization/prompts/generic.md), [guided procedure](../experiments/min-change-organization/prompts/specialized-procedure.md), [user policy](../experiments/min-change-organization/prompts/policy-common.md), [C policy conflict](../experiments/min-change-organization/prompts/policy-C-extra.md)
- [Fixture generator](../experiments/min-change-organization/tools/generate.py), [local adapter](../experiments/min-change-organization/tools/adapter.py), [agent runner](../experiments/min-change-organization/tools/run_agents.py)
- [Evaluator](../experiments/min-change-organization/evaluator/evaluate.py), [independent oracle](../experiments/min-change-organization/evaluator/independent_oracle.py), [unit tests](../experiments/min-change-organization/evaluator/test_evaluator.py), [score summary](../experiments/min-change-organization/evaluator/score-summary.txt), [fixture verification](../experiments/min-change-organization/evaluator/fixture-check.json)
- Fixture copies and manifests: `experiments/min-change-organization/fixtures/`; answer keys: `experiments/min-change-organization/answers/`; raw prompts, logs, scripts, plans and execution records: `experiments/min-change-organization/runs/`.

No PDF, ZIP, final competition submission, real NAS change, commit, push or publication was created.
