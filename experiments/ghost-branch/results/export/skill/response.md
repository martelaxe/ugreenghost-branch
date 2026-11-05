The old CSV export appears to have been an **internal prototype that was deferred** when the ledger UI migration took priority. The planning note does not say it shipped, and it leaves open whether another service later added export. The available current snapshot does not establish that answer. [Pilot note](/tmp/ghost-local-pdflmed0/laptop/notes/pilot.md:1), [report plan](/tmp/ghost-local-pdflmed0/archive/issues/report-plan.md:1)

## Ghost Recovery Packet

- **Project and candidate:** Lantern Ledger community ledger CSV export, represented by the laptop rollup prototype and a conflicting intermediate report prototype.

- **Classification: UNCERTAIN.** The laptop source contains a potentially useful CSV renderer, but shipping status, current coverage, integration, and spreadsheet safety are unresolved. The later prototype differs materially and has a recorded validation failure.

- **Scopes and limits:** Inspected relevant files in the authorized `current/`, `laptop/`, and `archive/` folders. The [current README](/tmp/ghost-local-pdflmed0/current/README.md:2) describes a snapshot rather than a necessarily complete checkout; the [laptop scope note](/tmp/ghost-local-pdflmed0/laptop/notes/scope.md:1) says the backup is incomplete. The separate service repository mentioned in the report plan was not included. No conclusion about the entire deployed product is supported.

- **What was found:**
  - [Laptop renderer](/tmp/ghost-local-pdflmed0/laptop/src/reports/rollupCsv.ts:1) produces a `date,label,amount` header and quotes cells, doubling embedded quotes. The [historical sample](/tmp/ghost-local-pdflmed0/laptop/tests/rollupCsv.test.ts:1) checks a label containing a comma; a [historical log](/tmp/ghost-local-pdflmed0/archive/logs/pilot-check.log:1) records that check passing.
  - [Intermediate prototype](/tmp/ghost-local-pdflmed0/archive/src/reports/rollupCsvV2.ts:1) joins values with commas without the laptop version’s cell quoting or header. Its [validation log](/tmp/ghost-local-pdflmed0/archive/logs/report-check.log:1) records a failure for labels containing commas and says formula injection was not tested. Neither source declares itself authoritative.
  - The supplied [pilot screenshot](/tmp/ghost-local-pdflmed0/laptop/screenshots/pilot-ledger.png) visually shows an “Export CSV” button and ledger rows. It does not establish that the button worked or that the feature was released.
  - The inspected [current toolbar](/tmp/ghost-local-pdflmed0/current/src/ui/toolbar.ts:1) lists Add record and Search. The inspected [records route](/tmp/ghost-local-pdflmed0/current/src/routes/records.ts:1) returns titles; these observations do not rule out an export elsewhere.

- **Value and caution:** The pilot note records volunteer interest in spreadsheet review, but calls for formula-handling review before integration. The recorded comma failure and conflicting implementations make automatic restoration inappropriate. The historical passing log is not evidence of a present-day test result.

- **Open questions:** Does the separate service or another current component already export equivalent data? Which records, permissions, filenames, and download behavior are intended? What spreadsheet formula policy should apply? Are the old row fields compatible with today’s data model?

- **Proposed coding-agent investigation:** With appropriate authorization, inspect the named renderer, intermediate prototype, current record and UI code, and the report plan; locate any current export service; compare behavior and dependencies; and resolve the intended security and product requirements with the owner before proposing an implementation.

- **Tests before integration:** Test CSV parsing for commas, quotes, line breaks, empty values and Unicode; spreadsheet formula handling; authorization and data selection; and the actual download flow. Compare the result with any existing export. **No code or tests were run in this investigation.**

- **Constraints:** This packet is an in-chat handoff only. No code execution, writes, Git operations, service calls, or integration were performed; those require separate authorization and an appropriate workflow. No UGREEN expert or NAS execution is claimed.