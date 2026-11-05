# Ghost Recovery Packet — Lantern Ledger CSV export

**Status:** RECLAIM CANDIDATE for investigation. This packet is a human-curated, portable rendering of the [actual revised local Skill-guided response](results-v2/export/skill/response.md); paths below refer to the preserved fictional fixture, not a UGREEN NAS. It is not a Git branch, patch, test result or recommendation to merge old code.

## Objective

Determine whether Lantern Ledger needs a CSV ledger export, whether an equivalent already exists, and whether any archived code is a useful reference.

## What the archive says

- The [laptop CSV renderer](fixtures/lantern/laptop/src/reports/rollupCsv.ts) produces a `date`, `label`, `amount` header and quotes cells. Its [historical sample check](fixtures/lantern/laptop/tests/rollupCsv.test.ts) tests a comma in a label; an [archived pilot log](fixtures/lantern/archive/logs/pilot-check.log) records a pass. **No test was run during this investigation.**
- The [pilot note](fixtures/lantern/laptop/notes/pilot.md) describes volunteer interest in spreadsheet downloads and an internal preview, and calls for a spreadsheet-formula review. The [fictional UI mock](fixtures/lantern/laptop/screenshots/pilot-ledger.png) shows an Export CSV button; it does not establish that it worked or shipped.
- The [later prototype](fixtures/lantern/archive/src/reports/rollupCsvV2.ts) joins values without CSV quoting and has no header. A separate [intermediate validation log](fixtures/lantern/archive/logs/report-check.log) records a comma failure but does **not** name the precise file responsible. Formula-injection handling was not tested.
- The [report plan](fixtures/lantern/archive/issues/report-plan.md) says the earlier prototype was deferred and a separate service repository was omitted. The selected [current toolbar](fixtures/lantern/current/src/ui/toolbar.ts) has no displayed export action, but the [current snapshot](fixtures/lantern/current/README.md) is not necessarily complete. We cannot say the product lacks export everywhere.

## Reasons for caution

Historical shipping status, current export behavior, compatibility, data access and security policy are unknown. Do not automatically select the later prototype or assume the passing historic log applies today. A separate [session-security review](fixtures/lantern/archive/issues/session-review.md) rejects the old remember-browser approach; it is unrelated to CSV and must not be revived as part of this work.

## Suggested investigation for a coding agent

1. With the owner's authorization, locate the current reporting service and determine whether equivalent export already exists.
2. Read both archived renderers, current record/UI code and the report plan; establish the intended data and permissions.
3. Review spreadsheet-formula handling with the owner before recommending any implementation. Treat historical code as reference material, not an approved patch.
4. If integration is later authorized, plan tests for CSV headers, commas, quotes, newlines, empty values, formula-like cells, access control and the actual download flow. Run tests only in an appropriate environment with separate authorization.

**Constraints:** No code, test, Git command, integration, save or external service was executed by the Skill in this local experiment. The separate service and deployed infrastructure were not available. No inference should be made about the entire product beyond the inspected sources.
