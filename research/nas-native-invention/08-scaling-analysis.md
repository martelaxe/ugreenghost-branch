# Scaling analysis: measured versus extrapolated

## What we observed

In the single 660-in-scope-file local experiment, the size-first guidance performed 621 stat and 541 SHA operations plus 4 listings, reading 5,336,064 content bytes. The generic performed 621 SHA operations plus 2 listings, reading 7,032,320 bytes. Both satisfied the exact answer-key gate. This is not a NAS measurement: data were deliberately small; the local tool emitted complete listings and sizes; its client script parallelized adapter subprocesses. Per-file execution had no correspondence guarantee with UGREEN expert calls. See [results](../../experiments/nas-native-invention/results.md).

## Analytical estimates, not tests

For N=100,000 common relative-path pairs, assuming both complete path lists and confirmed per-file sizes, and q=0.1 of pairs with unequal sizes: baseline full hashing requires 200,000 file hashes; size-first requires 200,000 stats + 180,000 hashes. Hash byte savings equal the actual total byte size of files skipped, not necessarily 10%. At q=0, size-first needs 200,000 stats **plus** the same 200,000 hashes: strictly more operations if stat is a distinct action. If equality could be determined only by hashing, metadata cannot safely eliminate those hashes. The local run's 24.1% byte reduction depends on its disproportionate sizes of the 40 size-mismatch pairs; it must not be extrapolated to other archives.

Enumerating two trees and representing the union costs at least O(N) output entries in an exhaustive approach; comparing path sets is expected O(N) with a conventional hash map, O(N log N) with a sort, plus O(N) intermediate state. A language model's context is not an external database, and a Markdown instruction does not implement that map. UGREEN makes no documented guarantee that 100k entries fit in one result, that summaries retain every item, or that a parent can efficiently maintain them. Number of model invocations, expert calls and retained tokens cannot be computed from the catalog; local subprocess batching is not evidence of UGREEN batching.

## Situations that break naive extrapolation

- **Deep hierarchy / inaccessible subtrees:** listing limits, access denials and unclear truncation can make even the set of missing paths unknown. Do not assert absent or complete.
- **Equal-size edits / duplicate clusters:** content inspection remains essential; hash comparison across names is a different task and can increase work. Matching mtime does not eliminate hashes.
- **Data changing mid-scan:** without a documented snapshot/consistent read, outputs describe observations at different instants. Revalidate before an action and disclose the race; checks are not atomic.
- **Repeated scans:** no documented change feed, Merkle index or persistent materialized view. A previous manifest can prioritize scrutiny but cannot safely prove unchanged content. Full verification still costs O(N) observations/bytes.
- **Incomplete results and model loss:** page/continuation not guaranteed; hierarchical subdivision may help only if a complete child list and stopping evidence are actually obtainable. Otherwise clearly stop at unknown.
- **Large media and I/O budgets:** `stat` can estimate size, but actual bytes read, file growth and interruptibility are unverified. A one-gigabyte cap cannot be guaranteed by instructions alone.

Before claiming scale: test real expert envelopes with returned size, completeness, error/cancellation, filtering and stable path mapping; then measure 1k, 10k, 100k in a safe permitted environment with multiple workloads and direct telemetry. If the platform cannot return coverage or batch results, promising a large-scale reconciler is premature.
