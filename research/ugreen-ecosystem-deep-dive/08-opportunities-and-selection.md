# Opportunity selection: three investigated hypotheses, zero qualifying candidates

The brief requires broad utility, differentiation, more than a generic report, a credible demo and documented implementation or just one narrow unresolved behavior. The three rows are **hypotheses investigated and rejected at that gate**, not three production-ready ideas. More detail and evidence: [problem matrix](04-product-gap-matrix.md), [expert feasibility](05-real-skill-feasibility.md), [prior experiments](07-prior-experiment-check.md). No new benchmark was performed.

## 1. A user-performed restore followed by scoped verification

- **Problem and evidence:** the [UGREEN FAQ](https://community.ugreen.com/nas/pagesD/circle/post?id=1210), sections 3.5–3.6, distinguishes successful backup jobs from actually retrieving and opening a sample. A [user's restore-mode complaint](https://www.reddit.com/r/UgreenNASync/comments/1x71ect/fiy_you_cannot_restore_induvial_files_from_a/) suggests difficulties in a particular setup; it is an unverified isolated report, not proof of universal inability.
- **Request:** “I restored these sample files to this folder. Compare them with these originals and tell me exactly what is and is not verified.”
- **Existing:** native [Sync & Backup](https://support.ugnas.com/detail/article/en-US/401), [Kopia verification](https://kopia.io/docs/advanced/consistency/) and [restic check](https://restic.readthedocs.io/en/stable/045_working_with_repos.html). Repositories and filesystem copies have different validation mechanisms.
- **Potential contribution:** keep explicit per-file coverage and identify a mismatch or missing sample; can reveal problems before a real emergency. It does not establish all files or application usability.
- **Mechanism:** parent receives user-authorized original and manually restored scopes; `file-agent` uses bounded `ug-filesystem:ls`/`find`, then `sha256sum` on observed paired files, with missing/inaccessible/limited cases reported; parent presents actual returns and uncertainty. It cannot initiate backup restore through a cataloged expert. Bytes do not verify application startup or metadata in all modes.
- **Visible outcome / scale:** a comparison of selected file pairs and unknowns. At scale, sampling trades confidence for time and I/O, neither measured nor guaranteed on UGREEN. Actual amount of work depends on agent limits and results.
- **Generic advantage:** none established. Generic Uliya can be asked to enumerate and compare; a checklist does not create a new primitive. Earlier adaptive/checksum work failed to prove general benefit.
- **Risk and falsification:** missing or extra files, snapshot/source changes, partial listing, differing source versions, repository-specific metadata and not opening files. Compare blind generic versus a frozen Skill on a tricky known sample; no outcome advantage means stop. Never claim a whole backup works.
- **Honest 60 seconds:** user restores a small test sample themselves beforehand using a verified supported app mode. They ask Uliya to compare two authorized small folders; show actual returned results and incomplete scope. If expert returns are unavailable, no completed comparison should be shown. This is a demo design, not a performed UGREEN run.
- **Gate:** user value high for sampled files; differentiation low; safety depends on read authorization and honest coverage; NAS relevance high; technical feasibility **partial**. Rejected: a bounded comparison alone is not the differentiated end-to-end recovery outcome requested.

## 2. Inspect declared application dependencies before a migration

- **Problem and evidence:** [Nextcloud backup documentation](https://docs.nextcloud.com/server/latest/admin_manual/maintenance/backup.html) names data, configuration and database among recovery needs; [Docker storage documentation](https://docs.docker.com/engine/storage/) distinguishes volumes from host bind mounts. This is a meaningful multi-component problem. A [self-hoster discussion](https://www.reddit.com/r/selfhosted/comments/1rz89tt/good_backup_does_not_mean_good_recovery/) illustrates it, without establishing prevalence.
- **Request:** “Using this redacted Compose file and these selected backup folders, show which declared components I have not supplied evidence for before I migrate.”
- **Existing:** app-specific restore/backup procedures, Docker documentation and marketplace [HA Git Backup](https://skills.ugreen.com/us/skills/1024); prior Rebuild Kit and generic agent workflows.
- **Potential contribution:** connect a project's declared mounts or configuration to observed paths, with missing evidence clearly identified. It could reduce preparation omissions, but a declared path being present is not a valid database backup.
- **Mechanism:** authorized redacted configuration through `document-agent` `ug-document:extract`/`qa`; actual observed candidate paths to `file-agent` `ug-filesystem:find`/`stat`; parent maps evidence to declarations and reports inaccessible/ambiguous entries. No Docker, app health, live-volume, backup-job or secret-validation operation was found in the catalog. Never copy secrets into the report.
- **Visible outcome / scale:** a source-linked, limited preparation checklist. Persistent, multi-app storage makes the problem relevant, but the outcome is still a report and cannot certify recovery.
- **Generic advantage:** no demonstrated advantage over generic Uliya with the same files; almost the same idea was considered in Experiment 11 and continuity experiments.
- **Risk and falsification:** a Compose file may be outdated, environment interpolated elsewhere, actual volumes inaccessible, database migrations incompatible and the configuration itself sensitive. A comparison against generic Uliya with decoy outdated config and a missing named volume would invalidate the design if it offers no additional correct detection or inappropriate assurance.
- **Honest 60 seconds:** show user-provided sanitized config and a bounded authorized backup directory; request a comparison; show only cited returned evidence and the live-runtime/DB unknowns. No fabricated application readiness indicator. Not performed on NAS.
- **Gate:** user value high; differentiation low–uncertain; safety possible for read-only sanitized material; NAS relevance high; feasibility is partial and has multiple missing contracts. Rejected under the report-only and single-narrow-unknown gates.

## 3. Resolve a media item that Theater identified incorrectly

- **Problem and evidence:** [UGREEN FAQ](https://community.ugreen.com/nas/pagesD/circle/post?id=1210) §4.3 explains mismatched movie metadata and manual correction; this is official support evidence of a possible problem, not proof of widespread frequency.
- **Request:** “This local film has the wrong identification. Compare its accessible filename and accompanying notes with the Theater listing and tell me what to check.”
- **Existing:** Theater's manual rematch and naming guidance; [Media Library Organizer](https://skills.ugreen.com/us/skills/1210) uses shell and TMDB, in a different execution environment.
- **Potential contribution:** connect user-owned sidecar evidence with a suspect match, while acknowledging that similar names do not prove identity.
- **Mechanism:** `media-agent` `ug-video:search` using an actual `type` and supplied keyword; `file-agent` `ug-filesystem:find`/`cat` on authorized files; optionally `document-agent` `ug-document:qa` on selected documents. Parent compares only returned evidence. No cataloged Theater metadata correction or complete runtime synchronization operation was identified.
- **Visible outcome / scale:** a suggestion for the user to review manually. A large library makes ambiguity painful, but one sample does not prove batch effectiveness.
- **Generic advantage:** none established, and native manual rematch may already fix the case quickly.
- **Risk and falsification:** sidecar text can be wrong; search index may be stale; external metadata may be unavailable. If a normal Theater rematch or generic Uliya prompt handles the case in the same time and quality, the Skill has no demonstrated value.
- **Honest 60 seconds:** query an existing accessible item, show returned listing alongside a real authorized sidecar and propose a manual review. No invented automated correction or outside metadata lookup. Not executed on NAS.
- **Gate:** user value moderate; differentiation low; safety manageable read-only; NAS relevance plausible; end-to-end correction unavailable through the inspected catalog. Rejected.

## Decision

**NO VIABLE CANDIDATE.** The strongest **problem** is recovery readiness, but no inspected, differentiated Skill can both perform or validate the essential recovery and meet the brief's generality and feasibility criteria. This is not a claim that the problem is solved, no useful fragment exists, or a future UGREEN release cannot enable one. It is a decision against another Skill experiment on present evidence.

The most useful single external technical question is: **Can a registered Uliya expert initiate a user-approved restore of selected backup content to a separate location and return authoritative completion and source/version provenance?** No such operation appeared in the inspected catalog. Even a positive answer would require a separate evaluation of restore modes, safety, application consistency, generic-agent overlap and actual user value; it would not itself establish originality.
