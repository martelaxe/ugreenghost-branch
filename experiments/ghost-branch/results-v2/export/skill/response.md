The available evidence says the old CSV export was an **internal prototype that was deferred** when the ledger UI migration took priority. The records do not establish that it shipped, or whether an export was later added in the separate service repository that is missing from these snapshots. [Pilot note](laptop/notes/pilot.md:1) · [Report plan](archive/issues/report-plan.md:1)

## Ghost Recovery Packet

**Project and candidate:** Lantern Ledger’s historical ledger-summary CSV export.

**Classification: RECLAIM CANDIDATE.** The laptop snapshot contains a specific CSV renderer and evidence of volunteer interest, making further investigation worthwhile. Its integration, spreadsheet safety, compatibility, and relationship to any current export remain unverified.

**Scopes and limits:** Inspected the authorized `current/`, `laptop/`, and `archive/` folders using local read-only tools. The current folder identifies itself as an incomplete source snapshot, and the laptop backup as a subset of experiments. The report plan says a separate service repository was not included. No UGREEN expert or NAS execution was used. [Current README](current/README.md:2) · [Laptop scope note](laptop/notes/scope.md:1) · [Report plan](archive/issues/report-plan.md:1)

**What was found:**

- The [laptop renderer](laptop/src/reports/rollupCsv.ts:1) emits a `date,label,amount` header and quotes cells, doubling embedded quotation marks. The [historical sample](laptop/tests/rollupCsv.test.ts:1) checks a label containing a comma; a [pilot log](archive/logs/pilot-check.log:1) records that check passing in 2024. This is historical evidence, not a current test result.
- The [pilot note](laptop/notes/pilot.md:1) records an internal prototype and volunteers wanting spreadsheet downloads. It records no release or deployment.
- The supplied [screenshot](laptop/screenshots/pilot-ledger.png) shows a community ledger and an “Export CSV” button. It establishes visual appearance only, not functionality or release.
- A separate [archive prototype](archive/src/reports/rollupCsvV2.ts:1) joins values with commas without quoting and omits the header. The file says neither version is authoritative.
- In the inspected current snapshot, the [toolbar](current/src/ui/toolbar.ts:1) lists “Add record” and “Search”; the inspected [records route](current/src/routes/records.ts:1) returns titles. These observations do not establish that export is absent elsewhere in the product.

**Reasons for caution:** The pilot note calls for a spreadsheet formula-handling review before integration. An [intermediate prototype log](archive/logs/report-check.log:1) records a failure involving embedded commas and says formula injection was not tested. That log does not identify a source file, so its failure cannot be attributed to the archived V2 file. The V2 source independently shows unquoted comma joining. Neither historical version is established as safe or authoritative.

**Open questions:**

- Does the separate service or another current component already provide an equivalent export?
- Which records, permissions, columns, and download behavior should the current product support?
- What handling is required for spreadsheet formulas, quoting, newlines, and the current data model?
- Which historical implementation, if either, is a useful starting point?

**Proposed coding-agent investigation:** With separate authorization, inspect the named renderers, current UI and record paths, and the report-plan objection; locate any current export and its dependencies; compare intended behavior with the owner’s requirements. Review spreadsheet safety and resolve the missing service evidence before choosing an implementation. Do not automatically apply or merge archived code.

**Tests before integration:** Plan tests for embedded commas, quotation marks and newlines; spreadsheet-formula inputs; headers and field types; authorization; and the actual download flow. No code or tests were run during this investigation.

**Constraints:** This packet is an in-chat investigation handoff. No source was changed, code executed, Git operation performed, service contacted, or integration attempted. Those actions require separate authorization and an appropriate workflow.