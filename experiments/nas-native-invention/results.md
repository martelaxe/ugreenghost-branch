# Local comparison results — 2026-10-27

**Verdict: NEEDS REFINEMENT.** A pre-specified content-byte advantage occurred once in a controlled local fixture, but underlying operation count rose sharply, elapsed time was longer, and the guided agent depended on a local Python batching/concurrency method not established for a Markdown-only UGREEN Skill. This is not evidence of overall NAS efficiency or creative differentiation. No real UGREEN agent was invoked.

## Reproduction and frozen materials

See [benchmark design](benchmark-design.md), [generic prompt](baseline-prompt.md), [frozen candidate](candidate-instructions.md), [pre-run hashes](pre-run-hashes.sha256), [fixture generator](benchmark-tools/generate_fixture.py), [adapter](benchmark-tools/nas_adapter.py), [runner](benchmark-tools/run_benchmark.py), [evaluator](benchmark-tools/evaluate.py), [answer key](answer-key/answer-key.json), [input manifest](fixture/input-manifest.json), [metrics JSON](measurements.json), and [post-run unchanged verification](post-run-input-check.json). Prompts and answer key were frozen before model runs; evaluator was written afterwards to grade the fixed outputs. The root contains 663 regular files: 660 within the two roots, plus 3 protected outside scope; 350 unique relative paths. The adversarial cases include 30 equal-size/equal-mtime changed pairs, 40 different-size pairs, one-sided files and similarly named/cross-name copies. Cross-name duplicates are distractors: this is a **same-relative-path** reconciliation, not a deduplication benchmark.

Two independent fresh `codex exec` processes requested `gpt-6.1-sol`, low reasoning, identical task and output schema. G received the baseline; S received baseline plus frozen procedure. Both had the same permitted local adapter and fixture. Each was run once, concurrently; no rerun-to-win. Actual model event logs, agent prompts and responses, adapter events and stderr are under [runs/G](runs/G/) and [runs/S](runs/S/). To re-evaluate without another model run: `python3 experiments/nas-native-invention/benchmark-tools/evaluate.py` from the project root. Generator and runner are provided for transparency; rerunning them is a new experiment, not the same independent trial.

## Measured outputs

| Metric | Generic G | Skill-guided S |
|---|---:|---:|
| Correct path counts: identical / different / source-only / destination-only / unknown | 240 / 70 / 20 / 20 / 0 | 240 / 70 / 20 / 20 / 0 |
| Wrong or missing non-identical-path entries | 0 of 110 | 0 of 110 |
| Claimed identical pairs with successful SHA calls for both sides | 240 of 240 | 240 of 240 |
| Lists / per-file stats / SHA operations | 2 / 0 / 621 | 4 / 621 / 541 |
| **Total instrumented adapter operations** | **623** | **1,166** |
| Actual bytes read by adapter for hashing | 7,032,320 | 5,336,064 |
| Agent shell tool calls | 623 | 5 |
| Usage-reported model input tokens (cached portion included) | 147,452 (112,384 cached) | 150,424 (114,432 cached) |
| Usage-reported output tokens | 3,657 | 4,151 |
| Wall time (concurrent local processes) | 37.590 s | 45.088 s |
| Adapter failures / out-of-scope side attempts | 0 / 0 | 0 / 0 |
| Fixture content manifest unchanged | yes | yes (shared pre/post check) |

S read **1,696,256 fewer content bytes, 24.12% less**. It made **543 more instrumented calls, 87.2% more**. It made 621 stats, including one preliminary stat and 620 for common paths; repeated exploratory calls also account for extra list and hash. G hashed one extra source-only file. Different file sizes and the fixed fixture control the byte reduction. Both also correctly handled all 30 same-size/same-mtime changed pairs by hashing; this evidence is verified from operation events and manifest-derived classifications, not just reported counts.

The shell-tool count is **not** the NAS cost: S sent a single Python client that used `ThreadPoolExecutor` to perform many adapter calls, while G issued shell calls individually. Python client scripts, concurrency and bulk operations are not supported by a Markdown-only Skill merely because they exist locally. Even local elapsed comparison is affected by concurrent execution, process scheduling, storage caches and model behavior; S was slower in the observed run, and no statistical speed conclusion follows. Token reports are descriptive usage fields, not inferred costs or UGREEN context usage.

## Validity and limitations

- The grader compares all 110 exceptions and counts to the independent frozen key. It reconstructs default identical paths, requires recorded successful hashes for both sides, and verifies digests against the independently frozen input manifest. The adapter log records success, path, and byte count **but not returned digest values**; we cannot independently replay what each model actually received from those logs. Frozen manifest evidence and instrumented hashes support the verification but are not a perfect transcript of all returned digest values.
- The adapter reports a complete recursive list and exact size fields. Those are **test conveniences** not guaranteed by UGREEN; no truncation, errors, cancellation or mutation races were injected in this trial. The 0 unknowns only describes this complete fixture.
- Agent event commands were inspected: G used the adapter for hash/list calls; S used those operations and a local adapter-calling Python client. No out-of-scope adapter calls were logged. Post-hash manifests prove contents unchanged, not independently that no non-adapter reads occurred. The agent was instructed not to bypass the adapter; host root was read-only and prior project/session paths masked but not every visible host path was hidden. Network isolation was not independently proven. Therefore this is a controlled **local** comparison, not a perfect hermetic or instrumented UGREEN environment.
- Exactly one trial per condition, synthetic small files and one data distribution. No independent human evaluation, real authorization gateway, natural NAS workload, persistent index or supported concurrency test. The fixed candidate wasn't adapted after seeing outcomes. Its nonzero byte saving meets the **pre-registered efficiency metric**; extra calls, slower observed time and lack of platform evidence prevent a general “faster/better” claim.
- No changes or actual writes to NAS; [post-run manifest](post-run-input-check.json) verifies fixture file bytes remained unchanged. The task did not test live concurrent updates or whether access timestamps changed.

## Next discriminating test

On a permitted real NAS, compare expert-delivered complete listing and size semantics and then ask a bounded 20–50-pair pilot to report actual child outcomes, unresolved coverage, and measured I/O if trustworthy telemetry exists. Include a no-size-change control and test expert failure. If size/coverage or practical per-file handoff cannot be established, keep this as a local algorithm study and do not sell it as an efficient large-scale UGREEN feature.
