# UGREEN ecosystem deep dive — decision

**Research date:** 27 October 2026. **Verdict: NO VIABLE CANDIDATE.** The most consequential opportunity is verifying recoverability, but the documented expert interface does not expose the essential backup-restore operation, and our remaining supported fragment resembles existing verification or a competent generic request. This is a judgment under the brief's strict selection gate, not a finding that user needs are solved or all possible Skills are uninteresting. **No new Skill, benchmark, PDF, ZIP, publication or NAS operation was created.**

## What the evidence says

1. **Important UGOS functionality.** On supported iDX firmware, [AI File Organization](https://support.ugnas.com/detail/article/en-US/877) proposes a plan; the user may adjust destinations and individual files, select collision handling and confirm. It handles up to 2,000 files per operation. [File Version Explorer](https://support.ugnas.com/detail/article/en-US/316) provides retained file histories, date-based folder views and restore options after versioning is enabled. [Sync & Backup](https://support.ugnas.com/detail/article/en-US/401) provides task and restore interfaces; exact modes and product versions matter.

2. **What we overlooked.** The actual [October 23 community FAQ](https://community.ugreen.com/nas/pagesD/circle/post?id=1210), accessed in Chromium, explicitly distinguishes a successful backup from a working restore. It advises periodically restoring and opening sample files. The [FAQ analysis](../research/ugreen-ecosystem-deep-dive/02-faq-deep-analysis.md) records the sections and scope. File Version Explorer is especially close to the user's original wish to see previous file states by date: its documented default retention is eight versions, maximum 32; it is not unlimited history and requires retention. Disabling retention deletes the stored versions.

3. **Already-solved portions of our earlier ideas.** Organization planning, user confirmation, natural-language file search, cited document comparison, file versions, backup tasks and photo timelines already exist in various UGOS apps or [published Skill descriptions](../research/ugreen-ecosystem-deep-dive/06-existing-skills.md). Native UI features are not proof that the same operation or guarantees are exposed to Uliya. The published listings do not establish our exact minimum-change optimizer, unexpected-discovery workflow or contextual-recovery semantics.

4. **Most substantial FAQ problems.** Recovery without a tested restore; loss of application state/configuration during migrations and updates; confusing permissions and inaccessible folders; phone-photo backup failures or limitations; application-dependent storage growth; and mismatches between live surveillance, recording mode and saved events. Disk wakeups and transfer speed are also hard to diagnose without workload and device context. [Detailed FAQ analysis](../research/ugreen-ecosystem-deep-dive/02-faq-deep-analysis.md).

5. **Applications owners use.** Native Photos, Files, Sync & Backup, Theater and surveillance coexist with Plex/Jellyfin, Nextcloud, backup programs such as Kopia/restic/Duplicati, Home Assistant, Vaultwarden, DNS blockers, monitoring and VPN tools. [UGREEN's applications guide](https://ai.ugreen.com/blogs/knowledge/top-7-nas-applications-for-performance) discusses these categories, but hardware, permissions and device support differ. [Ecosystem map](../research/ugreen-ecosystem-deep-dive/01-nas-ecosystem-map.md).

6. **Difficult dependencies.** An application can need files, database state, configuration, image versions, bind mounts or named volumes, keys, network settings and a tested recovery procedure. [Nextcloud](https://docs.nextcloud.com/server/latest/admin_manual/maintenance/backup.html) and [Docker](https://docs.docker.com/engine/storage/) document distinct pieces. A NAS retaining some files does not prove the whole application is recoverable. [Application analysis](../research/ugreen-ecosystem-deep-dive/03-application-dependencies.md).

7. **Frequency versus anecdotes.** The FAQ's inclusion of these topics and multiple user discussions support that the issues arise, but the sources do not measure prevalence. Individual Reddit reports of reuploads, phone battery usage or constrained restores are self-selected and may concern unknown models, modes or firmware; they do not establish a current universal bug. In particular, the user report about a restore destination appears in tension with the FAQ's suggested sample restore; scope and version need resolution. [Source-level notes](../research/ugreen-ecosystem-deep-dive/02-faq-deep-analysis.md).

8. **What an AI Skill might address.** With permission, it could compare an already-restored, small sample against selected originals, or inspect sanitized configuration and identify declared dependencies for which evidence was not supplied. It could report actual file results, limits and next checks. These are useful **partial** tasks; neither proves a working complete backup or application. [Candidate analysis](../research/ugreen-ecosystem-deep-dive/08-opportunities-and-selection.md).

9. **What the catalog does not expose.** Among the inspected 78 operations, no documented backup job/restore, Docker lifecycle or live volume inspection, database consistency, SMART telemetry, effective ACL inspection, or generic app-health test was found. Filesystem enumeration, hashing, document reading and evidence collection are documented under specific experts. Actual return schemas, completeness and hardware behavior are still unverified. Absence from this catalog does not imply UGOS lacks the feature. [Feasibility table](../research/ugreen-ecosystem-deep-dive/05-real-skill-feasibility.md).

10. **Published Skill patterns.** First-party descriptions already advertise file-organization previews, confirmation and undo, duplicate cleanup, and source-attributed comparison. Some inspected third-party `SKILL.md` files use staged procedures, evidence checks and recovery drills, but rely on Rust, PowerShell, scripts or external services unavailable by assumption to a Markdown-only Uliya Skill. The first-party source files were not recovered: their pages establish publisher claims only, not audited implementations. [Marketplace review](../research/ugreen-ecosystem-deep-dive/06-existing-skills.md).

11. **Remaining gaps.** Potential gaps include confidence in real restore results; application-level recoverability; identifying which apps depend on a file before a move; phone-to-NAS completeness; explaining disk activity; and correlating media or camera data across applications. These are evidence-grounded **frictions**, not proof that any one solution is absent from the wider market. [Ten-row matrix](../research/ugreen-ecosystem-deep-dive/04-product-gap-matrix.md).

12. **Strongest opportunities examined.** We tested the fit of three hypotheses against the selection criteria: sample-restore verification, app dependency preparation and media identification support. None met the bar for a serious end-to-end, distinct, implementable Skill. [Analysis and faithful unexecuted 60-second storyboards](../research/ugreen-ecosystem-deep-dive/08-opportunities-and-selection.md).

13. **Best combination.** Sample-restore verification is the most important *problem* and a bounded file-comparison fragment is plausible. It fails the competition candidate gate because restore is user-operated, hashes do not establish usability and the distinct Skill advantage is unproven. Application dependency preparation has high user value but even more inaccessible dependencies.

14. **Comparison with alternatives and generic Uliya.** Native backup tools can perform specific backup/restore tasks; repository tools can check repository integrity; generic Uliya could be asked to compare selected files and disclose limitations. A reusable Skill might standardize the process, but no evidence shows that standardization changes outcomes here. Our prior generic comparisons and verification experiments caution against assuming it does. [Prior experiment check](../research/ugreen-ecosystem-deep-dive/07-prior-experiment-check.md).

15. **Prototype?** No. None of the assessed hypotheses satisfies the requested value, differentiation, official feasibility and non-report gates. The earlier failures were not rerun or overwritten.

16. **Actual validation.** This was document, browser, marketplace and installed-catalog research. No new Skill or generic-agent comparison was built or run; no NAS expert operation, restore, performance measurement or hardware test was conducted.

17. **Next decision.** Stop this Skill direction on current evidence. If an authoritative UGREEN source later establishes a registered expert operation for a user-approved sample restore to a separate location with trustworthy completion and version provenance, reassess the possibility. That one answer would not by itself prove application recoverability or creative differentiation.

## Research files

- [Ecosystem map](../research/ugreen-ecosystem-deep-dive/01-nas-ecosystem-map.md)
- [FAQ and real-user analysis](../research/ugreen-ecosystem-deep-dive/02-faq-deep-analysis.md)
- [Application dependencies](../research/ugreen-ecosystem-deep-dive/03-application-dependencies.md)
- [Product gap matrix](../research/ugreen-ecosystem-deep-dive/04-product-gap-matrix.md)
- [Skill feasibility and boundaries](../research/ugreen-ecosystem-deep-dive/05-real-skill-feasibility.md)
- [Published Skill comparisons](../research/ugreen-ecosystem-deep-dive/06-existing-skills.md)
- [Previous experiments cross-check](../research/ugreen-ecosystem-deep-dive/07-prior-experiment-check.md)
- [Opportunity evaluation and decision](../research/ugreen-ecosystem-deep-dive/08-opportunities-and-selection.md)
- [Research log and source access](../research/ugreen-ecosystem-deep-dive/research-log.md)
