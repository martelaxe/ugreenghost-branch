# Minimum-change organization: controlled results

**Verdict: NO ADVANTAGE.** For the three main local fixtures, two fresh generic runs and two frozen-guidance runs each independently produced the same minimum move counts, kept every known compliant record, and deferred all expected uncertain or prohibited cases. There was no measured difference in underlying adapter operations or content bytes. This is a synthetic local plan-quality comparison, not a UGREEN runtime test or proof that either approach would reliably handle natural archives.

## Scope, frozen materials and reproducibility

[Design](design.md), [generic prompt](prompts/generic.md), [specialized procedure](prompts/specialized-procedure.md), [user policy](prompts/policy-common.md), [conflicting addition](prompts/policy-C-extra.md), [frozen-design hashes](frozen-design.sha256), [frozen data/key hashes](frozen-data.sha256), [generator](tools/generate.py), [adapter](tools/adapter.py), [runner](tools/run_agents.py), [evaluator](evaluator/evaluate.py), [independent oracle](evaluator/independent_oracle.py), [evaluator unit tests](evaluator/test_evaluator.py), [anonymous scores](evaluator/blind/scores.json), [mapping](evaluator/blind/mapping-after-scoring.json) and [full audit](evaluator/audit.json) are saved. Exact prompts, actual policy, final messages, client programs, operation logs, execution records and raw plans are in `runs/A/`, `runs/B/`, `runs/C/`, `runs/D/`, with `G1`, `G2`, `S1`, `S2` under each. Data are in `fixtures/A/`–`fixtures/D/`; separate frozen ground truths in `answers/A.json`–`answers/D.json`.

Hashes were frozen before the generated data and before runs as specified, then checked. The independent oracle was authored after generation but before any plan scoring: it re-parsed the fixture evidence and checked the independent key in all 582 records, including enumerating the small competing-destination subsets. Evaluator unit tests passed cases for perfect plan, zero-move failure, unsafe destination, missing row, occupied destination, scope violation and missing successful read.

Plan artifacts were copied to anonymous case labels and graded mechanically, without model-judge scores. **Blinding limitation:** copying and scoring occur sequentially in the same process, which holds the condition mapping; this is anonymous deterministic scoring, not a fully independent, double-blind human review. Automated scores validate whether a deferral has a nonempty reason, not whether its text is semantically complete. The supplemental audit checks collision-related keywords and manually inspected representative C conflict notes; it is not a full semantic audit of every explanation.

## Fixtures and objective

The user policy accepts both `sorted/CATEGORY/YEAR` and `historic/CATEGORY/YEAR`, instructs the agent to leave either compliant layout alone, derive unique category and year from readable content, defer unreadable or contradictory metadata, preserve names and never overwrite. Multiple sources competing for fewer free paths are deliberately deferred as a group. Dataset C adds a conflict between organizing everything and forbidding moves out of `historic/`.

| Fixture | Records | Confirmed compliant, must stay | Minimum safe required moves | Must defer |
|---|---:|---:|---:|---:|
| A: mostly organized | 186 | 160 | 18 | 8 |
| B: heavily disorganized | 186 | 41 | 137 | 8 |
| C: conflicting/ambiguous | 186 | 80 | 80 | 26 |
| D: already compliant control | 24 | 24 | 0 | 0 |

A's 160/186 confirmed compliant records are **86.0%**; the other eight include four undecodable PNGs and four collision/competition cases. The C deferrals include unreadable or contradictory record fields, 12 known noncompliant `historic/old/` files with conflicting user instructions, and collision/competition cases. No zero-move plan can pass A–C because a correct plan must propose all independently actionable moves.

Fixtures contain actual UTF-8 text, JSON, CSV and valid PNG image bytes, with some deliberately misleading `.pdf`/`.jpg` names containing text; they do **not** include genuine PDF or JPEG document extraction. Several different date conventions contain an unambiguous four-digit year; same-basename files include same-byte duplicates and different contents. These data are fictional and machine-readable, not representative natural multi-format archives. The local adapter offers a complete list and UTF-8 reads; real UGREEN expert completeness, structured error fields and actual supported-format extraction are unverified.

## Completed comparison: G vs S

The generic agent was given the same full policy and explicit ordinary safety, efficiency and minimum-change requirements. S received the same prompt plus the frozen research-only minimum-change guidance. Both used `gpt-6.1-sol`, low reasoning, isolated read-only fixture copies and identical list/read tools. They could create an adapter-calling local Python client; this is a **test convenience**, not an established executable capability for a UGREEN Markdown Skill. The specialized text was evaluated as frozen guidance, not validated or executed as a packaged official SKILL.md.

Each main condition produced exactly the same scored outcome in both replicates:

| Fixture | G1, G2: keep / necessary move / defer | S1, S2: keep / necessary move / defer | Unnecessary moves / missed moves / wrong or unsafe moves in each run |
|---|---|---|---|
| A | 160 / 18 / 8 | 160 / 18 / 8 | 0 / 0 / 0 |
| B | 41 / 137 / 8 | 41 / 137 / 8 | 0 / 0 / 0 |
| C | 80 / 80 / 26 | 80 / 80 / 26 | 0 / 0 / 0 |

All 12 main runs had full row coverage, zero source-scope violations, no proposed absolute or parent-traversal targets, no occupied or duplicate target collisions, no unnecessary renames, and no classification without a successful read. On C, all four agents explicitly named the historic-policy conflict. The four expected collision/competition deferral reasons in each main run matched a collision-related keyword; this heuristic alone is not semantic proof. Every plan stated it was proposed only. No file was moved; there is no actual execution success or after-move state to score.

Each main run made **188** adapter operations and read the same content bytes for its respective fixture: A **13,149**, B **13,139**, C **13,198**. Four simulated binary read failures per main run corresponded to unknown PNG content and were correctly deferred; listing and all other reads completed. No reported operation/token cost here is a billed cost or UGREEN tool-call count. The plans proposed changes affecting 28, 67 and 64 distinct source-or-destination directory paths for A, B and C, respectively; these are plan-derived counts, not changed directories.

| Fixture | Generic elapsed seconds (run 1, run 2) | Guided elapsed seconds (run 1, run 2) | Generic input tokens | Guided input tokens |
|---|---|---|---|---|
| A | 28.622, 35.768 | 31.181, 22.584 | 83,612; 139,216 | 84,785; 110,749 |
| B | 36.808, 41.786 | 38.450, 36.182 | 85,496; 96,482 | 132,977; 86,375 |
| C | 39.957, 43.440 | 48.674, 49.919 | 86,236; 96,637 | 114,151; 129,112 |

Input tokens include cached tokens as provided in the event usage reports; output tokens and cached amounts are preserved in execution records. Means across the six completed G runs: 37.73 s and 97,946 input tokens; six S runs: 37.83 s and 109,692 input tokens. Four independent sessions ran concurrently, so scheduling, model and tool orchestration dominate. Two trials per cell do not establish statistical runtime, token or efficiency differences.

## No-op control and interruption

D G1 completed successfully with 24 keeps and zero moves, reading 1,711 bytes in 25 adapter operations. G2 and S1 generated mechanically correct 24-keep plan artifacts, but **their Codex turns failed before final completion** because the account hit its usage limit; these are partial artifacts, not successful independent completions. S2 failed from the same limit before any plan or tool call. No runs were retried. Thus no completed guided no-op comparison is available. G2/S1 partial plans can be examined in their run directories, but must not be counted as completed agents. The no-op-control limitation does not change the 12 completed A–C comparisons.

## Native UGREEN arm and execution limits

N is **NOT RUNTIME-VALIDATED**. The official catalog documents a planned `file-workflow:start` summary, workflow-approved `run`, and batch operations; it does not establish a minimum-change objective, plan-edit API, collision semantics, per-file verification or safe overwrite behavior. We did not invent a native planner result or score it against G/S. [Platform audit](../../research/min-change-organization/01-platform-capabilities.md).

The local copies were mounted read-only; per-run hashes confirmed their contents unchanged, and [fixture-check.json](evaluator/fixture-check.json) confirms original fixture content hashes unchanged. File access times/full metadata were not independently checked. Outer bubblewrap masked the project and known histories and restricted fixture writes; host paths remained visible and network isolation was not independently verified. The automated command audit found no `/tmp/work` references in logged model commands, but cannot prove absence of every possible unlogged access. Input was not moved, no user or gateway approval was simulated, and no real UGREEN service was invoked.

## A faithful potential 60-second demonstration

Use the fixed A policy and a real approved small folder, **only if** UGREEN's actual returns support reliable completeness and content evidence. In the local fixture, show 160 already compliant, 18 necessary proposals, and 8 requiring decisions. Show a sample already-valid item in each acceptable tree, one safe relocation and the disputed collision/unknown evidence; ask for review. The 86.0% figure is 160 of 186 in **this local fixture only**. No move, approval or real-device execution is claimed. Without returned complete inventory and dependable per-file results, present only an explicitly partial plan. Existing rule-based tools already offer closely related behaviors; this demonstration establishes neither novelty nor generic-agent improvement.
