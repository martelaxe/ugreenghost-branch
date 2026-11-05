# Proposed Workflow S2 — untested

This revision is a design proposal based on observed labeling differences, input limits and output length, not a proven improvement. It has not been evaluated on these archives or on a holdout.

1. **Set the user-authorized scope and budget.** Record folders, file types and date, limit the amount read, and report missing or inaccessible sources.
2. **Retrieve a compact evidence ledger.** For each relevant source record a real path, a short supported fact, date/rights/capacity and retrieval coverage. Distinguish metadata from full content, and stop if key sources are absent.
3. **Generate at most three materially different combinations.** Each is a hypothesis linking a need to assets and a specific first action. Record which essential facts are observed and which need verification; do not require arbitrary five-source counting in production.
4. **Run a blocking check before ranking.** Examine current safety, rights, dates, resource availability and user approval. A physical action prohibited by a current source is `blocked`, even when an information-gathering action remains safe.
5. **Use three explicit dispositions:** `ready to request approval` for an evidence-supported bounded step; `investigate` for a safe check that could resolve material unknowns; `blocked` for a current decisive obstacle. These labels never mean that rights or safety are independently guaranteed.
6. **Return a short evidence-grounded card per candidate:** why useful, source paths, specific proposed first step, missing facts, blocker and approval requirements; make rejected or stale options optional. No speculative financial claims or unsupported numerical benefits.
7. **Avoid side effects by default.** Do not move, share, delete, write or contact anyone without the appropriate platform and user approval. Report incomplete coverage and any failed expert state.

Changes from S: explicit bounded retrieval; smaller candidate set; separate planning from readiness to act (motivated by B G/S terminology); concrete stop conditions and human approval; shorter output; a clear distinction between a source citation and validated usefulness. Do not claim the experiment proves these changes improve accuracy or reduce costs.

## Holdout plan

Have a different dataset author create at least six archives across different domains with authentic-looking but consented/synthetic mixed formats, including multiple distinct positives, restricted conditions, negatives and genuinely ambiguous cases. Freeze an independently reviewed rubric and prompts first. Run matched G, S and S2 using the same model and settings, several independent repetitions, randomized run order and read-restricted workspaces. Have two evaluators blind to workflow labels score claims against a separate fact ledger, adjudicate disagreements, audit false positives/false negatives and report retrieval coverage, time/tokens and calibration. Test UGREEN orchestration separately on a real supported environment. Do not use Experiment 03 as the holdout.
