# Eight general NAS operations

These are proposed reusable procedures, not new filesystem primitives or verified UGREEN features. Numbers are **illustrative**, not measured, and count individual operation requests, not guaranteed expert invocations. Assume 100,000 files where useful; paths and user permissions must be explicit. The catalog does not guarantee bulk retrieval, complete listings, exact result fields, or stable snapshots. All stay read-only unless an independently approved supported action is safely possible.

## 1. Progressive tree reconciliation

- **Problem / request:** Check a partial migration: “Compare these two authorized folders and tell me which same-path files differ.”
- **Mechanism:** Enumerate both scopes, compare relative paths, then stat both common files; unequal size proves difference, equal size requires both hashes. Incomplete enumeration means unknown, not absence. No same-size/mtime identity inference.
- **Scale / Skill advantage:** Avoid expensive content reads for different-size pairs; reusable explicit evidence/coverage protocol may change agent behavior, not filesystem complexity. Generic Uliya can choose the same algorithm.
- **Result:** Counts plus path-by-path mismatches, missing paths and unknowns; no mutations.
- **Illustration:** 100k common pairs, 10k unequal sizes: 200k stats plus 180k hash operations vs 200k hashes; both need enumeration. File sizes decide bytes, not counts alone.
- **Prior art:** [rclone check](https://rclone.org/commands/rclone_check/) and [rsync](https://rsync.samba.org/ftp/rsync/rsync.1). Not a novel algorithm.
- **Feasibility:** `file-agent`: `ug-filesystem:ls`, `stat`, `sha256sum`; actual listing completeness, stat size, throughput and parent handoffs unverified.
- **Failure:** Equality-heavy trees add stat overhead; race between checks; truncation; absent permissions.
- **Falsifiable hypothesis:** same correct classification and paired identity hashes but fewer measured content bytes than generic; report metadata costs. **Tested once**; see results.

## 2. Coverage-first bounded discovery

- **Problem / request:** “Find files from my exported application across these folders; tell me where you could not look.”
- **Mechanism:** User defines scope and file signatures. Choose cheap supported path/name filters; maintain explicit searched, truncated, failed and unexplored subtrees. Escalate to content only for candidates. Never equate a negative partial search with absence.
- **Scale / Skill advantage:** Reduces irrelevant content reading and keeps coverage visible; requires no presumption that generic search is bad.
- **Result:** Candidate list plus a coverage ledger and next smallest scope to inspect.
- **Illustration:** 100k entries, 3k name candidates, at most 200 selected content reads by user-specified budget; content recall can be lower than complete search, list-call count depends on hierarchy and undocumented limits.
- **Prior art:** [QNAP Qsirch](https://www.qnap.com/en/how-to/tutorial/article/qsirch-the-quick-start-guide) and conventional indexers, generally far better for speed at scale.
- **Feasibility:** `file-agent` `ug-filesystem:find`, `ls`; possibly `document-agent` `ug-document:extract` for authorized selected files. No reliable pagination assumed.
- **Failure:** Relevant files use misleading names; hidden/inaccessible subtrees; model drops ledger entries.
- **Hypothesis:** At identical relevant-file recall, fewer content bytes than a generic agent, with every incomplete subtree disclosed. Requires a representative labeled corpus, not tested.

## 3. Role-aware exact duplicate review

- **Problem / request:** “Show truly identical files across these folders, and which roles they have before I decide what to do.”
- **Mechanism:** Group candidates by available sizes and verified SHA-256; ask users to assign roles such as backup or active project. Show uncertainty and deletion risks; do not presume a duplicate is dispensable.
- **Scale / Skill advantage:** A reusable comparison between byte identity and human purpose; generic agent can do it. Protects against interpreting deduplication as permission to delete.
- **Result:** Exact-hash groups with paths and user-supplied role labels; no deletion plan without separately supplied policy.
- **Illustration:** 100k size checks, potentially 80k hashes if only 80k lie in repeated size groups; worst case 100k hashes; role assessment may require many user interactions.
- **Prior art:** [fdupes](https://manpages.debian.org/bullseye/fdupes/fdupes.1.en.html), [Synology Storage Analyzer](https://www.synology.com/en-au/dsm/7.2/software_spec/storage_analyzer), [Immich](https://docs.immich.app/features/duplicates-utility/).
- **Feasibility:** `file-agent` `ug-filesystem:ls`, `stat`, `sha256sum`; hash groups, completion and size fields not guaranteed. No actual reclaimable block counts.
- **Failure:** Same bytes, distinct retention requirements; hard links, snapshots and access policies make reclaim estimates unreliable.
- **Hypothesis:** Against generic, equal digest accuracy and fewer unjustified deletion recommendations under a frozen role fixture; not tested.

## 4. Migration collision preflight

- **Problem / request:** “Before migrating this tree, show names that would collide on my destination.”
- **Mechanism:** Inventory original relative paths; apply user-confirmed destination case and normalization rules only as hypothetical comparison keys; group collisions and propose individual rename choices, without modifying sources.
- **Scale / Skill advantage:** A reviewable whole-tree risk plan before any copy; generic AI can reason through the same rules. Cost can exceed context for huge trees.
- **Result:** Explicit original paths per collision and stated assumptions; incomplete inventories block claims of complete safety.
- **Illustration:** 100k paths, O(N) path inventory, expected O(N) grouping with an actual index or O(N log N) sorting; no content reads. Number of list calls and ability to hold/group data are unknown.
- **Prior art:** [rclone check](https://rclone.org/commands/rclone_check/), OS/filesystem naming restrictions and synchronization tools; verify product-specific collision behavior rather than assume it.
- **Feasibility:** `file-agent` `ug-filesystem:ls`, `find`, potentially `stat`; no documented universal destination filesystem rule detector or bulk rename engine.
- **Failure:** Misstated target rules, Unicode normalization, unlisted permissions or a target changing after analysis.
- **Hypothesis:** Fewer unreported collisions versus generic, same authorized listings and correct target rules; not tested.

## 5. Evidence-bounded drift checkpoint

- **Problem / request:** “Compare this tree to my previously saved manifest and show what I must re-check.”
- **Mechanism:** Read a user-provided, dated manifest; compare path/metadata to current results; mark candidates for hash-based rechecking. Identical metadata is not proof of unchanged bytes; absent trust or digest, label unknown.
- **Scale / Skill advantage:** Exposes incremental attention priorities without pretending to implement a native change feed.
- **Result:** Changed, newly observed, previously listed but missing under complete coverage, and unknown records, with timestamp and scope.
- **Illustration:** 100k current entries and 100k old records imply O(N) list and compare, plus hashes for user-selected candidates; proving *all* unchanged may still require 100k hashes.
- **Prior art:** [restic](https://restic.readthedocs.io/en/stable/040_backup.html), [Syncthing](https://docs.syncthing.net/users/syncing.html), ZFS snapshots. Existing systems have better integration.
- **Feasibility:** `file-agent` `ls`, `stat`, `sha256sum`; saved manifest via documented `knowledge-agent` `ug-knowledge:save-text` only when applicable approval permits; persistence, size, path, reading and consistency unverified.
- **Failure:** Same size and mtime with different bytes; stale/partial/tampered manifest; no guaranteed snapshot.
- **Hypothesis:** Better uncertainty disclosure under deceptive metadata vs generic; fewer re-hashes only for a task that explicitly accepts unverified entries, not for complete integrity verification. Untested.

## 6. Safe organization no-op planner

- **Problem / request:** “Plan applying my explicit naming and folder policy here; leave files already compliant alone.”
- **Mechanism:** Derive proposed destination for each authorized item using an explicit supplied rule; exclude confirmed no-ops; expose collisions, unavailable scopes and policy ambiguity. Produce a reviewable plan without execution.
- **Scale / Skill advantage:** Avoids churn and reduces a large proposed action set; the policy itself remains user's, not invented by AI.
- **Result:** Rows: original path, proposed path, no-op/change/conflict/unknown, and reason.
- **Illustration:** 100k entries, 90k already compliant: 100k path checks, 10k candidate changes; no content reads if policy is metadata-only. Actual enumeration and context limits dominate.
- **Prior art:** conventional file managers and bulk rename tools; existing AI file organizers. Not a new underlying algorithm.
- **Feasibility:** `file-agent` `ls`, `find`, `stat`; writes need separate platform/operation approval and safe collision guarantees, not assumed. Proposal-only is credible.
- **Failure:** Implicit policy, destination collisions, case rules, metadata changes after planning, file used by other systems.
- **Hypothesis:** Fewer unnecessary proposed changes at equal policy accuracy versus generic agent; test on a frozen policy dataset, not performed.

## 7. Bulk-action verification ledger

- **Problem / request:** “For this explicitly approved set of operations, show which ones completed and which still need checking.”
- **Mechanism:** Maintain user-visible intended-action records, then reconcile only actual returned operation outcomes with re-observed destination/source metadata and hashes. Never interpret dispatched, waiting, or failed operations as success; no automatic retry for uncertain state.
- **Scale / Skill advantage:** A safety invariant over multiple steps; generic agents can follow it. No claim of atomicity or storage transactions.
- **Result:** A compact per-operation completed-and-verified / failed / pending / unknown ledger.
- **Illustration:** 1,000 actions: up to 1,000 operation outcomes and 2,000 post-check hashes plus per-path checks, no savings versus unverified actions; safety costs work.
- **Prior art:** mature copy/backup software logging, [rsync](https://rsync.samba.org/ftp/rsync/rsync.1), application transaction logs.
- **Feasibility:** `file-agent` `ug-filesystem:stat`, `sha256sum`, and `cpmv` only if platform safe semantics are confirmed; user and platform approvals as applicable. No guaranteed no-overwrite atomicity or durable workflow ledger.
- **Failure:** Missing return status, platform cancellation, changing source, unverified target, lost session; stop and reconcile, not retry blindly.
- **Hypothesis:** Lower false-success rate than generic on injected failed/pending outcomes; no such UGREEN test has run.

## 8. Read-budget evidence frontier (wild candidate)

- **Problem / request:** “With at most 1 GB of file reads, tell me exactly what can and cannot be verified about these two trees.”
- **Mechanism:** Estimate sizes from returned metadata; spend user-authorized content budget on selected pairs according to explicit priorities; separately report size-proven differences, hash-verified pairs, unknown pairs, and actual vs estimated consumption if reliably available. Never call a skipped equal-size pair identical. User can choose which unknowns to spend the next budget on.
- **Scale / Skill advantage:** The novel interaction is choosing an assurance frontier under a finite read budget; generic can do this and performance is unknown. Content reads are capped only if platform can enforce/preflight sizes and return actual accounting; otherwise budget is an estimate, not a hard limit.
- **Result:** A tiered proof/unknown frontier rather than a pretend complete comparison; concrete choice of next verification batch.
- **Illustration:** 100k matched pairs, 1 GB budget, 20k differing-size pairs determinable by metadata; number of verified other pairs depends on file-size distribution. O(N) enumeration/stat; byte bound unproven without enforcement.
- **Prior art:** [DuckDB Parquet pushdown](https://www.duckdb.org/docs/current/data/parquet/tips) uses cost avoidance, rclone verifies files; exact interactive budget workflow needs further search and may exist.
- **Feasibility:** `file-agent` `ls`, `stat`, `sha256sum`; operation byte telemetry, reservations, interruption, sequencing across calls and trustworthy size are unverified. Not a guaranteed capped operation.
- **Failure:** File grows between stat and hashing; one file exceeds the remaining limit; no actual read-byte counter; user interprets unknown as safe.
- **Hypothesis:** Under the same actual measured content-byte budget, finds more user-prioritized verifiable differences than generic, with zero unsupported identity claims; untested. This is different from #1 because its central interaction is choosing what can be known under a hard resource limit, but the requested limit cannot presently be guaranteed by UGREEN.
