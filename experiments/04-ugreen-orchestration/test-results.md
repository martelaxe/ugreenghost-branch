# Local simulation and static-check results

## Run

From the project root:

```sh
python3 -m unittest discover -s experiments/04-ugreen-orchestration/simulation -v
python3 experiments/04-ugreen-orchestration/simulation/mock_workflow.py
node /mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/scripts/check-skill.mjs experiments/04-ugreen-orchestration/draft/evidence-discovery-draft
```

Python 3 standard library only; Node is used solely to run UGREEN's installed checker. The paths are specific to this workstation. Actual outputs are retained in [`results/unit-tests.txt`](results/unit-tests.txt), [`results/scenario-outputs.json`](results/scenario-outputs.json), and [`results/static-check.json`](results/static-check.json). The first checker attempt, preserved as `results/static-check-initial.json`, returned two errors because the sample template headings did not match its parser's exact required headings; these were corrected in the draft. The final check returned exit **0**, `static-pass`, zero errors/warnings and a checked Skill SHA-256 of `77a5a70a03116991ed250669e845f925811c260285e170813618881b612b1c08`.

## Required cases

| Case | Mock outcome | Key check |
| --- | --- | --- |
| Fully supported discovery | `hypothesis`, 5 exact fixture citations | Claims remain tentative; next action requests manager review. Coverage is `complete_for_mock_scope`, not real NAS coverage. |
| Critical blocker | `blocked`, with the failed laser's exact path and text | Recommendation changes to no operation until repair and clearance; a separate non-fabrication review is conditional on approval. |
| Missing essential source | `incomplete`, 4 citations | Missing `asset_rights` prevents any discovery or action recommendation. |
| Truncated evidence | `incomplete`, 4 fully returned source texts | The incomplete archive file is named; knowledge collection does not run; other complete source texts are retained without claiming a finding. |
| Expert failure | `incomplete`, no document evidence | A failed document expert stops the knowledge stage and reports the failure. |
| Approval pending | `incomplete`, 5 previously returned source texts | `waiting_approval` does not count as completion; no final discovery is issued. This is a deliberately hypothetical state, not a claim that a read action requires approval. |

All **17 unit tests passed**. In addition to the required cases they cover unknown or null coverage, a fake citation, a skipped document, an unreported contradictory blocker, out-of-scope/traversal paths, cancelled status, a known blocker surviving a pending stage, and a `completed` status with a failed result envelope.

## Interpretation

The mock's candidate, essential roles, fictional documents, blocker and evidence are preselected in code. It can demonstrate conditional handling, citation matching against supplied mock text, and stop rules under the assumed adapter contract. It does **not** generate a discovery, call an AI model or expert, prove the real response shapes, validate semantic truth, establish actual completeness, verify symlink containment on a NAS, or establish user value. Exact substring matching only checks a quote against the mock's returned text; it is not independent source verification or proof of inference correctness.
