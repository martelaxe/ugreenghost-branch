# NAS-native invention lab — decision, 27 October 2026

**Tested candidate: NEEDS REFINEMENT.** A size-first folder reconciliation procedure read 24.12% fewer content bytes than a competent generic agent in one frozen local test, with identical correct results. It used 87.2% more instrumented operations and took longer in this particular run. The demonstration relied on a complete-list adapter and local client batching that UGREEN has not been shown to provide. This is a meaningful narrow observation, not proof of better real-NAS performance or a distinctive hackathon winner.

## The storage problem

On large NAS trees, exhaustive enumeration, content hashing and model context can all become bottlenecks. Search results can be truncated or incomplete; same-size or same-timestamp files can differ; many identical files serve different backup and user roles; large migration or reorganization plans can create collisions; and repeated checks are expensive without a trustworthy change index. The most important quality issue is distinguishing **verified difference, verified practical identity and unknown**. [Real bottlenecks](../research/nas-native-invention/02-real-storage-bottlenecks.md).

Useful prior mechanisms include metadata filtering before content reads, hierarchical enumeration, hashes and manifests, explicit uncertainty, and safe preflight; mature systems already implement most of them. Database pushdown, efficient duplicate finders and backup change detection are precedents, not novel inventions here. [Technical mechanisms](../research/nas-native-invention/03-optimization-techniques.md).

A Markdown Skill can plausibly ask an expert to work in stages and keep unverified items visible, but compliance depends on the model and expert returns. It does **not** add an executable optimizer, native index, bulk API, event watcher, trusted incremental hash tree, persistent state machine, verified pagination, atomic snapshot, or transaction guarantee. Completeness of listings, exact size fields, batch throughput and return envelopes are not verified. [Skill surface](../research/nas-native-invention/04-skill-optimization-surface.md).

## Eight operations and three finalists

1. **Progressive tree reconciliation:** compare two trees with cheap size checks before needed content hashes.
2. **Coverage-first bounded discovery:** find a bounded subset while exposing inaccessible or unsearched areas.
3. **Role-aware exact duplicate review:** identify byte-identical files but ask about their differing roles before any disposal.
4. **Migration collision preflight:** apply explicitly supplied target naming rules to reveal prospective conflicts.
5. **Evidence-bounded drift checkpoint:** compare an authorized prior manifest against observations, preserving uncertainty about unchanged content.
6. **Safe organization no-op planner:** show only policy-required changes and flag conflicts.
7. **Bulk-action verification ledger:** distinguish actions actually verified from failed, waiting or unknown work.
8. **Read-budget evidence frontier:** let a user choose what can be verified within a read budget and see the unknown remainder. An enforced hard limit is **not documented** on UGREEN.

The three strongest, technically distinct candidates are **progressive tree reconciliation**, **coverage-first discovery** and **no-op organization planning**. Each may be useful, but all have familiar competitors and the latter two remain untested. The most imaginative alternate is the read-budget frontier: it changes the user interaction from “compare everything” to “show me what can be proven with this much I/O.” It remains a speculative combination, and if UGREEN cannot enforce or reliably measure a byte budget, it can only be framed as an estimate. [Full eight](../research/nas-native-invention/05-eight-nas-operations.md), [three candidates](../research/nas-native-invention/07-three-finalists.md).

## What actually happened in the test

The generic agent and Skill-guided agent were fresh Codex processes given the same authorized two-tree comparison and local adapter. The Skill procedure and benchmark design were frozen before fixture generation; the generated answer key was frozen before the comparison. Both correctly classified 350 relative paths: 240 identical, 70 different, 20 source-only, 20 destination-only, and zero unverified. Both used actual paired hash operations for each claimed identical pair; a mechanical evaluator matched the 110 reported exceptions to the answer key.

| Metric | Generic | Skill-guided |
|---|---:|---:|
| Content bytes hashed | 7,032,320 | 5,336,064 |
| `list` / `stat` / `sha256` adapter operations | 2 / 0 / 621 | 4 / 621 / 541 |
| All adapter operations | 623 | 1,166 |
| Agent shell calls | 623 | 5 |
| Input tokens, cached portion included | 147,452 | 150,424 |
| Output tokens | 3,657 | 4,151 |
| Observed elapsed time | 37.590 s | 45.088 s |

The Skill instructions led to 1,696,256 fewer hash bytes. The generic agent nevertheless achieved exactly the same useful result. The guided run's shell-call savings came from a local Python client that batched/parallelized adapter calls; that execution mechanism is **not established as available to an official Markdown-only UGREEN Skill**. Two concurrent, single trials do not establish speed, model reliability, generalized accuracy or repeatability. No NAS device or real UGREEN expert was used. Operation logs do not record returned digests; the grader corroborated hash requests using immutable input-manifest digests, a weaker evidence trail than fully captured return values. [Full results and evidence](../experiments/nas-native-invention/results.md).

## Competitive and creative judgment

[rclone check](https://rclone.org/commands/rclone_check/) and [rsync](https://rsync.samba.org/ftp/rsync/rsync.1) already provide substantial tree comparison and synchronization capabilities. [Synology Storage Analyzer](https://www.synology.com/en-au/dsm/7.2/software_spec/storage_analyzer) and [fdupes](https://manpages.debian.org/bullseye/fdupes/fdupes.1.en.html) already address duplicates; dedicated backups and snapshot systems exceed a hypothetical text manifest. Exact overlaps vary by tool and task. A natural-language, evidence-explicit, user-directed interface could be valuable, but our trial has not shown it is unique or superior to those products. [Prior-art analysis](../research/nas-native-invention/06-prior-art-and-competitors.md).

The core method is reusable across ordinary folder collections; it does not rely on a person's hobby or a particular narrative. It is a general storage capability rather than semantic content analysis. Nevertheless, **a list of differences is a familiar experience**, and a 60-second demo would require showing actual correct evidence, a meaningful saved read cost and honest unknowns to be memorable. Current evidence does not support presenting it as a strong Most Creative entry.

## UGREEN reality and next move

`file-agent` is documented as owning `ug-filesystem:ls`, `stat`, and `sha256sum`; the parent must delegate using actual user-authorized scopes and consume real completed expert outputs. Read-only reconciliation needs source authorization; writing or running a storage workflow requires the applicable explicit user and platform approvals and separately confirmed safety semantics. A pre-check and a requested `overwrite=false` do not establish atomic no-overwrite. Missing result fields, incomplete lists, expert failures, cancellation and pending approval must stop relevant claims or actions.

**Recommended next step:** test a small real UGREEN expert pilot of size-first reconciliation, with a deliberately same-size changed file and a limited/inaccessible scope. Check whether the parent can receive reliable per-path size, path, actual digest and coverage/failure information, and measure actual requests if telemetry exists. If those essentials are missing, do not promise a scalable reconciliation Skill. Separately preserve the read-budget frontier as the most creative hypothesis; only pursue it if the platform can enforce or honestly account for a real I/O budget.

**Submission threshold:** unsuitable as a competitive entry if it cannot show reliable coverage and practical expert handoffs, if extra metadata calls overwhelm any measurable benefit, if ordinary rclone/UGREEN already offers the same user experience, or if the core result requires the local Python client. It is not yet ready to claim real NAS scalability, distinctive innovation or validated performance.

Scaling estimates and known failure cases are in [scaling analysis](../research/nas-native-invention/08-scaling-analysis.md). This work did not build a final Skill, proposal, PDF, ZIP, or NAS deployment.
