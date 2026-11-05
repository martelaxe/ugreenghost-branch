# Decisive follow-up: NAS verification optimizer

**Recommendation: STOP THIS DIRECTION.** Do not develop the tested adaptive tree verifier or a verification-frontier Skill as a hackathon submission candidate on current evidence. The generic agent produced the same correct result and disclosed the same simulated coverage gaps; the proposed guidance shifted costs rather than delivering an overall measured advantage. The established tools and workflow overlap is substantial. This decision is specific to the tested approach and does not invalidate all other NAS-native ideas.

## What we tested

We froze a guided procedure and benchmark plan before generating five disposable two-tree workloads: many small files, fewer large files, mostly matching files, mostly different files, and incomplete/denied entries. We compared three deterministic strategies with real local operation, SHA-byte and elapsed measurements over three rotated runs per workload. We separately ran two fresh Codex processes, a competent generic agent and one with the exact frozen guidance, on the same five workloads and the same adapter. No actual UGREEN experts or NAS hardware were used.

The earlier byte reduction came largely from 40 different-sized pairs totaling 1,699,840 bytes; static filtering incurred an extra size request on nearly every matched file while still hashing all equal-size pairs. File size distribution, process scheduling and model choices matter. The earlier five guided shell calls hid many actual operations performed by a local Python client. Its observed elapsed time cannot establish why a NAS would be faster or slower.

## The result

The direct strategy needed the fewest underlying operations on every workload. Static metadata-first read fewer file bytes on every workload and was quickest for our large local files, but it did more calls. The adaptive heuristic sampled eight pairs and then chose a branch; its median local time never beat both fixed strategies. A hypothetical serialized call-cost model changed the tradeoff but did not measure UGREEN latency. A real platform could expose sizes with listings, batch operations, cache data or incur different costs.

The generic Codex agent independently chose metadata-first and the guided agent used the prescribed sampling heuristic. Both correctly classified **464 of 464 known relative paths**, reported all paired-hash/metadata counts correctly and disclosed the simulated incomplete listing and denied file. Their complete comparison is:

| Metric | Generic | Guided |
|---|---:|---:|
| Instrumented local operations | 1,565 | 1,030 |
| Content bytes hashed | 45,947,328 | 68,726,362 |
| Observed process time | 96.620 s | 91.224 s |
| Incorrect path classifications | 0 | 0 |

Guidance reduced local operation count by **34.2%**, but increased content reads by **49.6%**. Single concurrent runs cannot establish a reliable speed advantage, and both used Python batching not documented for UGREEN Skills. The guided procedure did not beat the generic across cost dimensions, nor show a correctness or frontier-clarity advantage. The generic prompt already required an honest frontier, so the comparison does not measure whether an uninstructed assistant would reliably provide one. See the [full results](../experiments/nas-native-invention/adaptive-followup/results.md).

## Frontier and UGREEN limits

A separate local, post-hoc probe demonstrated the conceptual interaction: examine five file pairs, see four verified and one denied, then choose one more pair while the other known files and incomplete destination scope remain unknown. This is a bounded **file-selection** example, not a tested human experience or strict disk-I/O cap.

The catalog assigns `ug-filesystem:ls`, `find`, `stat` and `sha256sum` to `file-agent`; a parent can delegate authorized read requests. What is **not** documented includes a guaranteed complete/truncated-list signal, exact stat size schema, paired result mapping, byte-read telemetry, persistent frontier, user-visible pause/resume, optimized batching, or an enforced disk-read budget. Thus the local adapter's exact frontier cannot be assumed observable on a real device. Missing evidence must remain unknown, including an entire scope when completeness cannot be established. [Technical review and operation mapping](../research/nas-native-invention/adaptive-verification-review.md).

## Existing alternatives and what would change this decision

[rsync](https://rsync.samba.org/ftp/rsync/rsync.1) already supports default size/time quick checks and checksum-based checks on matching-size files. Our local dry run found its default quick check missed 24 deliberately same-size/same-time changes; `--checksum` detected all 102 changes. This is a behavioral comparison, not a matching SHA-256 or performance benchmark. [rclone check](https://rclone.org/commands/rclone_check/) also offers mature file comparison and hash or download-based modes; it was researched but not installed or tested here.

Reopen the verification-frontier idea only if new evidence shows **both** (1) actual UGREEN expert returns can support truthful, useful coverage/evidence states and (2) real users or a controlled comparison show a meaningful benefit over generic Uliya and existing tools. A deterministic local interface sketch alone is not that evidence. Until then, do not promise faster verification, hard budgets, a scalable persistent index, a distinctive new algorithm, or a deployable UGREEN feature.

No Skill, PDF, ZIP or submission was created. Original experiments were preserved.
