# Before You Move — honest demo plan

**20 seconds:** “You want to delete duplicate files. They contain the same bytes, but one is the source for a project and the other has an unknown archival role. Before You Move helps you review what might be affected before deciding.” This is a proposed story using fictional test data, not a recorded NAS result.

**60 seconds:** (0–10) show the two authorized copies and ask “Before I delete one, what should I know?” (10–35) show actual Uliya results, if returned: equal hashes and a directly sourced project reference to the working path. (35–50) show the archive role is unresolved, including the actual supporting note. (50–60) show the recommendation to confirm retention/backup and that nothing was deleted. If any results are unavailable, show the uncertainty instead of inventing them. The local generic baseline also found this core distinction; the potential advantage is reusable user invocation, not a novel hash algorithm.

**Three minutes:** introduce the long-lived collection and initial request; show authorization and two selected copies; show returned evidence distinguishing byte identity from roles; show an ambiguous or inaccessible reference causing a limitation; explain the next safe decision. Demonstrate the separate move-reference mode only if it fits without making the main story unclear. Show actual device results and any errors in the finalist video. No custom UI, external scripts or fake statuses.

**Synthetic data:** two identical text assets, a layout note with a resolvable relative path to one, and a note stating the other's role is unknown; see [fixtures](../experiments/final-flagship-tests/fixtures/copies). Avoid real user data or credentials.

**Cataloged operations:** `file-agent` may use `ug-filesystem:find`, `ls`, `cat`, `stat`, `sha256sum`; `document-agent` may use `ug-document:qa`/`reconcile`; optionally `knowledge-agent` `ug-knowledge:collect-evidence`. Requests must use real authorized paths and completed prior results. These are not executed in the local Codex tests.

**Must validate on NAS:** actual expert status and path/evidence propagation, usable supported text formats, selected hashes, bounded listing and missing/inaccessible results, scope handling and user-visible output. Clarify configured model provider/data flow. No platform approval or copy/move operation is part of this demo.

**Do not claim:** complete dependency graph, application failure verified, zero undetected references, proven deletion safety, automatic monitoring, privacy/offline guarantees or measured time savings. The report is a preview, not a recovery or an executed action.
