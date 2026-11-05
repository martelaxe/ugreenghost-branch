# Execution record

## Preflight and preregistration

`preflight/` retains a successful independent CLI run configured with `-m gpt-6-luna -c 'model_reasoning_effort="low"'`: it read the exact sample file under the read-only sandbox and captured output. Event logs do not echo backend model identity. Official documentation lists Luna and low effort, but that does not independently prove account routing.

`preregistration.json` records SHA-256 hashes and a timestamp for the private answer key, rubric, prompts, design, harness, fixture generator, source manifest and A/B diff. It was written before benchmark launches. `source-manifest.json` records all 44 source hashes per archive; `ab-diff.patch` is the sole A/B changed sentence. The evaluator rubric and archive author's key were not altered after seeing outcomes.

## Investigation execution

`process-status.json` records each of the 18 attempts, timing, requested model/effort, model-call metadata and usage. Each run got its own workspace under the recorded `/tmp/ugreen05-benchmark-*` directory with exactly its assigned 44 files, no symlinks, verified source hashes and no scoring materials. Workspaces remained intact and source files were rehashed after each run. Project and earlier experiment directories were temporarily mode-restricted and restored; original modes are recorded. Same-user sibling workspaces and Codex auth/backend remained shared, and a read-only sandbox is not a complete read-isolation boundary. Event logs show only workspace-relative evidence reads for G/P; H read its assigned workspace via the controller and supplied retrieved text to two sessions. No web or external data tool call was recorded.

The 12 G/P sessions each produced a final report and their command logs contain all 44 source texts. H inventoried all 44 files for each run with 0 present-file omissions/truncations, but its inventory cannot infer the contents or existence of the missing PDF cited inside another record. H candidate/verifier prompts, messages, JSONL, stderr, retrieval manifest and quote-gate status are in the corresponding `execution/<run>/` folders. Six H runs used 12 model sessions; all verifier outputs parsed, four were empty and two contained a retained candidate. These are substantive outcomes; there were no investigation retries.

All benchmark calls explicitly specified the same requested model and low effort. CLI-reported token counts include cached tokens and do not establish actual billing. `execution/evaluation-per-run.json` combines the scorer's per-dimension judgments with usage; `results/` contains unmodified final reports.

## Independent scoring and audit

After all 18 reports were saved, three fresh `codex exec` evaluator processes, requested as `gpt-6.1-sol` / `high`, scored six anonymized reports each against the frozen key and rubric. They were independent of the investigation sessions but share the same service and are not independent human raters. Their workspaces contained the relevant archive, key, rubric and reports named `case-01` through `case-06`. Method headings and absolute run paths were normalized where practical; output style and known archive can still reveal the method. The mapping, prompts, outputs, stderr, timings and evaluator-token usage are preserved in `blinding-map.json`, `blind-scorer-status.json` and `blind-scorer-{a,b,c}/`.

All scorer JSON parsed and score ranges/arithmetic were checked. The blind scorer credited evidence unit 3 for B-G2 and B-H2 despite the required source path being absent from each report. `evaluation-per-run.json` retains raw scores and records a 4-point recall correction for each under the pre-existing rubric. No other credited essential unit was missing one of its required source paths. The scorer's individual quote counts are model judgments, not a verified universal automatic parser. No other post-result rubric changes were made.

Project modes were restored after both the benchmark and blinded scorer completed. Failed/incomplete assessments would have been retained, and weak answers were not retried. Code in `implementation/` is research-only, not allowed inside a submitted UGREEN Skill.
