# Three finalists: distinct optimization targets

All demonstrations below are proposed Uliya sequences, not observed runtime results. Paths are authorized user inputs; all operations are delegated by the parent to their owning expert. No custom HTML, scripts or unsupported API. Runtime timings, exact response shapes, completeness and batching are unknown; a 60-second script is a *storyboard* with a pre-sized small fixture, not a latency guarantee.

## 1. Progressive tree reconciliation — minimize content read

1. **Request:** “Compare these two folders; tell me exactly what is different and what you could not verify.”
2. **Documented operations / owner:** `file-agent`: `ug-filesystem:ls`, `ug-filesystem:stat`, `ug-filesystem:sha256sum`. `find` may help scoped discovery, not as an assumed complete recursive index. Parent receives expert results and does not run specialist commands.
3. **Algorithm:** List both approved roots; check completeness evidence. Compare relative-path sets. For common paths, stat both, identify unequal sizes; hash both when sizes equal. Record child failure, omitted records, limited results, changed inputs and any unknowns.
4. **Expected benefit:** Save content bytes on unequal-size pairs, but pay for stats; no benefit on same-sized differences.
5. **Failures:** No trustworthy completeness/size fields; lots of equal-sized files; very large lists; file changes between steps; missing expert responses.
6–8. **Generic Uliya / generic AI / Skill:** Generic behavior is untested on Uliya; a generic Codex **did** solve the comparison by hashes in the local test. Skill makes a candidate method and evidence rules repeatable, but does not guarantee a different model follows them or that it is efficient on NAS.
9. **Workload:** A user migrating 100k regular files and checking two authorized trees, with a known mix of changed and unchanged sizes.
10. **Pass:** Correct union and all differences, both real hashes for every identity, no unapproved reads, accurately flagged unknowns, fewer measured content bytes under same task. **Fail:** false identity, false absence, hidden partial results or no content-byte advantage; include additional metadata/elapsed cost. Only one local trial performed.
11. **60-second storyboard:** Show two small fixture folders; ask compare; present one unequal-size difference and one matching-hash pair plus an explicit coverage status, with actual paths and expert response evidence. If expert results lack support, demonstrate “unknown” instead. This is a complete result only if the platform proves coverage.

## 2. Coverage-first bounded discovery — minimize irrelevant reading

1. **Request:** “Find files relevant to these explicit filename patterns under my authorized archive; tell me which places you could not check.”
2. **Operations / owner:** `file-agent` `ug-filesystem:find` and/or `ug-filesystem:ls`; optional `document-agent` `ug-document:extract` only for selected authorized documents.
3. **Algorithm:** Clarify exact user scope/patterns; search cheap metadata first; collect examined, missing, failed and limited subtrees; request bounded content reads only when necessary; never assert archive completeness if the expert cannot establish it.
4. **Expected benefit:** Fewer irrelevant document reads, clearer evidence and uncertainty; pruning may lower recall.
5. **Failures:** Non-descriptive filenames, truncation without a usable partition strategy, incompatible document types, enormous candidate sets.
6–8. **Generic / Skill:** Generic Uliya is not measured and might do the same. A generic AI can choose filters and a ledger; reusable instructions provide an explicit selection and uncertainty protocol, a hypothesis, not a proven gain.
9. **Workload:** 100k documents, 3k matching names and 200 carefully budgeted reads; real recall must be labeled independently.
10. **Pass:** Equal or higher known relevant-file recall at fewer document bytes, with every known coverage gap disclosed; a reliable result requires a corpus with independently labeled relevant files and failure injection. Not tested here.
11. **60-second storyboard:** User selects one folder and two known filename patterns; expert lists small sample; user sees found candidates plus one deliberately inaccessible or limited area clearly marked “not checked.” Do not show imaginary pagination or assume the expert produces coverage fields.

## 3. No-op organization plan — minimize unnecessary proposed changes

1. **Request:** “Apply this explicit folder/naming policy as a plan, and show me what already complies.”
2. **Operations / owner:** `file-agent`: `ug-filesystem:ls`, `find`, optionally `stat`. Read-only plan; any later `ug-filesystem:cpmv` requires separate authorized action and documented platform approval plus verified safe collision behavior.
3. **Algorithm:** Enumerate the user-specified scope, map actual paths under the user-supplied rule, drop identical destination/source paths from proposed actions, flag destination collisions and unknown case rules, disclose incomplete inventory. Do not execute changes.
4. **Expected benefit:** A concise plan for 10k changes out of 100k files rather than a bulk operation touching all 100k; no-op classification itself still requires inventory.
5. **Failures:** Ambiguous naming rule, destination filesystem normalization and overwrite behavior, disappearing files, inaccessible paths, context capacity.
6–8. **Generic / Skill:** Generic Uliya could already do this; no test establishes otherwise. A reusable Skill requires accurate no-op counting and explicit collision review, a possible reliability improvement, not a native transaction manager.
9. **Workload:** 100k entries, 90k compliant, 10k noncompliant, a handful of path and case collisions.
10. **Pass:** 100% true no-ops excluded from action list, all seeded collisions surfaced or unknown, no unsafe changes; compare false proposed changes and completeness with generic. Not tested.
11. **60-second storyboard:** With a small folder and explicit rule, show existing compliant entries and a proposed short change list including one collision flagged for user decision. Do not imply changes were made or approve them on the user's behalf.

**Creative alternate:** the untested read-budget evidence frontier (#8) is more unusual but is not selected as a deployable finalist because the present catalog does not establish a hard content-byte cap or trusted byte accounting.
