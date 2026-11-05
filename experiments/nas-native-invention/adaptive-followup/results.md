# Adaptive verification follow-up: results

**Decision: STOP THIS DIRECTION** as an optimization submission candidate on current evidence. The frozen adaptive method did not beat both fixed strategies on any local median elapsed-time workload. A fresh generic agent independently implemented static size-first filtering and matched the guided agent's correctness and uncertainty handling. The guided agent used fewer local adapter operations, but more bytes. There is no demonstrated overall improvement, and UGREEN runtime contracts remain unverified. This does not establish that all frontier interfaces are worthless; it means this work has not established a distinctive one worth installing.

## Frozen test, inputs and reproducibility

[Design](design.md), [generic prompt](generic-prompt.md), [frozen adaptive procedure](frozen-procedure.md), [schema](output-schema.json), [pre-fixture hashes](frozen-before-fixture.sha256), [input/key hashes](frozen-inputs.sha256), [fixture generator](tools/fixture.py), [local adapter](tools/adapter_core.py), [reference runner](tools/reference.py), [agent runner](tools/agent_runner.py) and [evaluator](tools/evaluate.py) are preserved. The frozen files and generated key were checked by `sha256sum -c`. `python3 experiments/nas-native-invention/adaptive-followup/tools/evaluate.py` regrades existing outputs without another model run. The generator/runner are included for inspection; do not overwrite the original fixture or runs to reproduce in place.

Five authorized two-tree fixtures contain 464 relative paths, 928 in-scope regular files plus one out-of-scope synthetic protected file. Small: 120 pairs of ~2 KiB; large: 24 pairs of ~2 MiB; mostly matching: 120 pairs; mostly different: 120 pairs; incomplete: 80 pairs. In the latter, local adapter **simulates** an omitted destination item, an explicit incomplete-list response, and denial of one known item. All timestamps match by design; equal-size changed bytes are present. No actual inaccessible OS directory is tested. All paths are nested. [Answer key](answer-key/key.json) is outside the agent's permitted workspace. Input manifest hashes and sizes were unchanged afterwards; access times and full metadata were not independently checked.

Three deterministic reference strategies ran each workload three times, rotated order, serially, with the same Python adapter library. `direct` hashes both files; `metadata` stats both and hashes same-sized files; `adaptive` takes a fixed eight-pair sample, both stat and hash, then picks a branch using the frozen 256 KiB-per-stat **hypothetical** threshold. The sample always does hashes even when size differs, so sampling itself can waste reads. The reference hashes full file bytes, not a truncated shortcut. [All reference results](reference-results.json) and individual returned-result events are saved in `runs/reference/`.

## Controlled strategies: real local measurements

Median seconds are three sequential runs on the same local fixture, rotated by strategy. These are in-process Python measurements with warm/cache effects, not UGREEN expert timings. Counts and bytes are identical across repetitions. **Every strategy passed the frozen path-classification key in every run**, including two unverified paths in the incomplete workload; the incomplete directory scope remains globally unknown.

| Workload | Direct: ops / bytes / median seconds | Static metadata: ops / bytes / median seconds | Adaptive: branch, ops / bytes / median seconds |
|---|---:|---:|---:|
| Many small | 242 / 520,788 / 0.0327 | 410 / 364,358 / 0.0472 | direct; 258 / 520,788 / 0.0337 |
| Fewer large | 50 / 100,669,714 / 0.0619 | 70 / 41,944,500 / 0.0326 | metadata; 82 / 67,112,428 / 0.0482 |
| Mostly matching | 242 / 1,992,858 / 0.0334 | 470 / 1,892,888 / 0.0554 | direct; 258 / 1,992,858 / 0.0351 |
| Mostly different | 242 / 1,998,834 / 0.0328 | 326 / 697,180 / 0.0376 | direct; 258 / 1,998,834 / 0.0352 |
| Incomplete/denied | 160 / 1,296,133 / 0.0220 | 286 / 1,046,354 / 0.0335 | direct; 176 / 1,296,133 / 0.0232 |

Static filtering reduced hashed bytes on all five, but was only fastest on the large fixture in this local test; direct did fewer operations everywhere. Adaptive used fewer bytes than direct only on the large fixture and was neither fastest nor lowest-byte method on any workload. The illustrative threshold does not minimize local seconds, and sampling imposes work. These tiny, repeat-measured local numbers are not statistical guarantees; device caching, throughput, sizes and call boundaries change the result.

## Hypothetical operation-cost sensitivity — not UGREEN results

For illustration only, add an assumed serialized 1, 10 or 100 ms per instrumented operation to the measured local median. This double-counts any latency already inherent in the local call and ignores actual remote work, batching, concurrency and read bandwidth. Its purpose is sensitivity, not prediction.

| Workload | Strategy | At +1 ms/op | At +10 ms/op | At +100 ms/op |
|---|---|---:|---:|---:|
| Small | Direct | 0.275 s | 2.453 s | 24.233 s |
| Small | Static metadata | 0.457 s | 4.147 s | 41.047 s |
| Small | Adaptive | 0.292 s | 2.614 s | 25.834 s |
| Large | Direct | 0.112 s | 0.562 s | 5.062 s |
| Large | Static metadata | 0.103 s | 0.733 s | 7.033 s |
| Large | Adaptive | 0.130 s | 0.868 s | 8.248 s |
| Mostly matching | Direct | 0.275 s | 2.453 s | 24.233 s |
| Mostly matching | Static metadata | 0.525 s | 4.755 s | 47.055 s |
| Mostly matching | Adaptive | 0.293 s | 2.615 s | 25.835 s |
| Mostly different | Direct | 0.275 s | 2.453 s | 24.233 s |
| Mostly different | Static metadata | 0.364 s | 3.298 s | 32.638 s |
| Mostly different | Adaptive | 0.293 s | 2.615 s | 25.835 s |
| Incomplete | Direct | 0.182 s | 1.622 s | 16.022 s |
| Incomplete | Static metadata | 0.319 s | 2.893 s | 28.633 s |
| Incomplete | Adaptive | 0.199 s | 1.783 s | 17.623 s |

## Generic vs frozen-guidance agents

Each was a fresh `codex exec` process requesting `gpt-6.1-sol`, low reasoning, the identical five input scopes and subprocess adapter. Both had the same option to write a local client, same safety constraints, output schema and task, including explicit truthful-frontier requirements. G independently chose static metadata-first for every workload. S chose adaptive direct except large, where it chose metadata-first. Two runs were concurrent and are not independently repeated.

| Workload | Generic ops / bytes | Guided ops / bytes | Both output and coverage correct? |
|---|---:|---:|---|
| Small | 413 / 366,406 | 258 / 520,788 | Yes |
| Large | 70 / 41,944,500 | 80 / 62,917,749 | Yes |
| Mostly matching | 470 / 1,892,888 | 258 / 1,992,858 | Yes |
| Mostly different | 326 / 697,180 | 258 / 1,998,834 | Yes |
| Incomplete | 286 / 1,046,354 | 176 / 1,296,133 | Yes |
| **Total** | **1,565 / 45,947,328** | **1,030 / 68,726,362** | **Yes** |

G logged two additional lists, one extra stat and one extra hash during its initial probing of the small fixture. Across all five, S used 535 fewer operations (34.2%) and read 22,779,034 more bytes (49.6%). Two simulated access-denied operations were logged for each agent. Each correctly supplied all 464 observed path states, both listing-completeness values, paired-metadata/hash counts, and an incomplete-coverage explanation; neither invented an identity or marked the omitted destination path absent. The two 80-path incomplete statuses marked unverified are a lower bound on uncertainty, not complete knowledge of unlisted destination files.

G reported 96.620 s, four shell tool calls, 168,063 input tokens (138,496 cached) and 9,332 output tokens. S reported 91.224 s, four shell tool calls, 128,426 input tokens (102,656 cached) and 10,566 output tokens. These are individual concurrent process durations including model, subprocess and scheduling overhead. No reliable speed or token generalization follows. Both agents used local Python client programs and threading: **their batching, concurrency and adapter call granularity are not documented UGREEN Skill capabilities**.

Subtle reproducibility limitation: the frozen instruction said “evenly spaced” but did not specify how fractional indexes are rounded. Reference adaptive used floor; guided Codex used `round`, so the large workload's sampled paths and bytes differ (67,112,428 vs 62,917,749). No post-hoc correction was made. Guided Codex also regenerated the 120-item small source listing from its observed filename pattern to cache the first response; it happened to reproduce the actual returned list, but extrapolating path patterns would be fragile on other datasets. The model's operation logs include returned digests; the grader compares those actual digests and sizes with claimed evidence, not just summary counts. Full outputs, scripts and operation logs: [G](runs/G/), [S](runs/S/), [mechanical audit](evaluation.json).

Isolation: outer bubblewrap mounted the host and fixture read-only, masked the project and known session/history paths, and allowed only test output writes plus selected runtime binds. Some host paths and the adapter's simulated-fault config remained visible, and network isolation was not independently proven. Agent commands were inspected; they used the adapter for fixture operations and no unauthorized scope calls were logged. This is a constrained local experiment, not proof of a hermetic UGREEN process.

## Optional frontier probe and external reference

A separately labeled **post-hoc** local probe simulated a user asking to check five common paths and then one additional path. After five: two verified-identical, two verified-different, one denied, 75 other known paths unresolved, and unknown destination coverage. After one more: three verified-identical, two verified-different, one denied, 74 other known paths unresolved; destination coverage remained unknown. See [actual artifacts](runs/frontier-probe/output.json) and [events](runs/frontier-probe/events.jsonl). The cap is on selected paths, not proven disk I/O; no person evaluated the experience.

Local `rsync -rni` dry-run flagged 78/102 changed paths in the mostly-different fixture, missing 24 equal-size/equal-mtime edits; `rsync -rnic` flagged all 102. Version and raw output are in [rsync logs](runs/rsync/). This is not an apples-to-apples SHA verification or timing comparison. [rclone check documentation](https://rclone.org/commands/rclone_check/) was reviewed; rclone was not installed or executed. [UGREEN capability review](../../../research/nas-native-invention/adaptive-verification-review.md) explains why exact frontier counts, completeness and a hard I/O cap remain uncertain on device.
