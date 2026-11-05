# Evaluation: recorded outcomes, not a synthetic leaderboard

Preregistered design: `benchmark-design.md`. Actual source outputs, comparative table, observed calls/timing and path audit: `model-results.md`, `runs/summary.json`, `audit.json`. One run per main condition is insufficient for a statistical conclusion.

| Preregistered dimension | Observed evaluation |
|---|---|
| New decisions and assertion origin | All nine took the icon approval from the current user and attributed the toilet location to the user's report. No independently signed venue confirmation was generated. The publicly reusable S invitation carries the qualification as a footnote, which can be separated from copied text. |
| Prior information | G1 and S used bilingual copy and the exact earlier tagline across A/B/C. G0 did not know that user-only preference; it was not given the prior chat or handoff, so this is an input-information difference, not a reasoning failure. G1/S were given both a capsule and an earlier artifact; individual contribution cannot be isolated. |
| Stale source | G1 and S identified the discrepancy between the saved 10:00–13:00 and current 11:00–14:00 in B and held the old volunteer schedule. G0 saw the current venue/timeline conflict but lacked the old handoff; it is not assessed for historical discrepancy. S appropriately did not claim historical byte history or why the discrepancy arose. |
| Missing/inaccessible source | All C methods withheld independent confirmation of rights; G1/S also identified past rights claims in the capsule as unverified under the narrower scope. C physically omits all rights/ files. |
| Prior approval/action states | All described no current authorization for sending, printing or publishing. In forged-capsule trials both G1 and S treated unsupported historical dispatch and embedded instructions as untrusted. |
| Evidence and citation | 133/133 raw model report links fail to resolve at their saved location, although 133/133 normalize to files in actual archived workspaces. The local deterministic link rewrite produces separate usable artifacts; it is not a Skill feature. Capsule has 27/27 links resolving in A/B and 24/27 in intentionally restricted C. Link existence does not verify logical support. |
| Output quality | The outputs are usable drafts for review, not public-ready: creator-cleared icon asset is unavailable, volunteer times need confirmation, organizer review remains pending, and toilet location is user-reported. A missing evidence gap remains a gap. |
| Unnecessary work | Both generic and S re-read much of the small corpus. S used 3 command calls in each run versus G1's 2; elapsed times varied and concurrent execution prevents reliable efficiency conclusions. No user time or monetary cost measured. |
| Exact final Skill failure | The independent repeated `final-B` S run claimed 26 non-handoff source files; manifest has 25. The wrong count is a real correctness/coverage defect. No post-failure Skill edits or unfair re-benchmarking occurred. |

## Deterministic checks

`audit.py` checks preserved input hashes, actual link targets after normalization, and event-derived command counts. The fixture's venue file has SHA-256 `566e099a4c3c4f607be14f847d1a2869cb514dcd6105200140e423bd9664e3ce` in A and `01c03b2502e7edea92d7a542d5d5996794865393c95d961ea9e1190ac0cb768f` in B; only the local fixture adapter changed the hours. These hashes independently establish byte differences, not semantic understanding or actual NAS freshness checking. C removed the rights folder in its disposable fixture. No source files were changed by model runs.

## Cautious author scores, 0–25 each

- **User Value: 17/25.** Preserving conversation-only choices is concretely useful; true user demand and task time are not measured.
- **Innovation & Differentiation: 5/25.** Existing Markdown handoff Skills and generic same-record continuation are close. Label and NAS location alone are not novelty.
- **Technical Quality: 12/25.** Useful stale/permission handling in these samples, but 0/133 raw links portable, one factual file-count error, incomplete isolation and unknown device enforcement.
- **AI NAS Fit & Validation: 9/25.** Uses plausible documented experts and stored files, but no actual UGREEN calls, safe approved saves, return fields or new-conversation behavior were verified.

These **43/100 author judgments** are subjective, not official UGREEN scores, and are not the sole basis for the decision. Competitor facts and uncertainty: `../../research/14-task-continuity/competitor-and-judge-review.md`. The biggest reason to stop the standalone Skill is not the score but G1 doing substantially the same job with the same saved information while direct competitors already provide Markdown handoffs.
