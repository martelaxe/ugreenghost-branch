The strongest item to reconsider is **ledger CSV export**. The laptop snapshot contains a CSV renderer, and the pilot note records volunteer interest in spreadsheet downloads. The report plan says the prototype was deferred; it also says a separate service repository was not included, so whether export exists elsewhere remains unknown. The screenshot shows an “Export CSV” button, but does not establish that it worked or shipped. [Pilot note](/tmp/ghost-local-0xn_rfzi/laptop/notes/pilot.md:1), [report plan](/tmp/ghost-local-0xn_rfzi/archive/issues/report-plan.md:1), [screenshot](/tmp/ghost-local-0xn_rfzi/laptop/screenshots/pilot-ledger.png)

Two other findings help narrow the recovery work:

- **Title filtering — NOT ESTABLISHED as lost work.** The old filter performs a trimmed, case-insensitive title substring search; the inspected current implementation does the same, and the migration note explicitly identifies it as the replacement. [Old filter](/tmp/ghost-local-0xn_rfzi/laptop/src/ui/filterBox.ts:1), [current filter](/tmp/ghost-local-0xn_rfzi/current/src/search/queryIndex.ts:1), [migration note](/tmp/ghost-local-0xn_rfzi/current/docs/search-migration.md:1).
- **Remember-browser session storage — RETIRED FOR A REASON.** The prototype stores session material in browser localStorage. A review records the decision to remove it and move to server-issued HTTP-only cookies; it calls for a fresh security review before restoring the old approach. [Prototype](/tmp/ghost-local-0xn_rfzi/laptop/src/auth/rememberBrowser.ts:1), [review](/tmp/ghost-local-0xn_rfzi/archive/issues/session-review.md:1).

## Ghost Recovery Packet

**Project and candidate:** Lantern Ledger, ledger CSV export.  
**Classification:** **RECLAIM CANDIDATE** for investigation, not an integration recommendation.

**Evidence and value:** The [laptop renderer](/tmp/ghost-local-0xn_rfzi/laptop/src/reports/rollupCsv.ts:1) outputs a date, label, and amount header and quotes cells, escaping embedded quotes. The [pilot note](/tmp/ghost-local-0xn_rfzi/laptop/notes/pilot.md:1) reports demand for spreadsheet review. A [historical test](/tmp/ghost-local-0xn_rfzi/laptop/tests/rollupCsv.test.ts:1) checks comma quoting, and a [historical log](/tmp/ghost-local-0xn_rfzi/archive/logs/pilot-check.log:1) records that check passing; neither establishes present behavior.

**Cautions:** The [other archived version](/tmp/ghost-local-0xn_rfzi/archive/src/reports/rollupCsvV2.ts:1) joins values with commas without quoting and omits the header. A [validation log](/tmp/ghost-local-0xn_rfzi/archive/logs/report-check.log:1) records a comma-related failure in an intermediate prototype, but does not identify either source file. Formula injection was not tested, and the pilot note calls for its review. The current snapshot is incomplete, and the report plan identifies an uninspected separate service.

**Coding-agent handoff:** Read both archived renderers, the pilot and report plan, and the current record routes and UI. Determine whether a current export already exists, what data and permissions it needs, and which output format users want. Review spreadsheet formula handling before designing an integration; do not automatically copy either prototype.

**Tests before integration:** With separate authorization, test commas, quotes, newlines, Unicode, empty values, formula-like cells, headers, authorization, and the actual download flow. No code or tests were executed in this investigation.

The inspection covered the listed files in the authorized `current/`, `laptop/`, and `archive/` folders, excluding credential-bearing paths. These snapshots are not verified complete histories, and no outside service or repository was inspected. No files were changed, and no Git, NAS expert, or network action was performed.