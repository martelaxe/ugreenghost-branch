# Experiment 13: task-oriented NAS artifacts

The main result is a set of **real local Codex outputs**, not a UGREEN execution. Four fictional archives: A (12 files), B (10), C (10), W original and W future (11 each). Each has a frozen manifest; the separate answer keys are outside investigator archives. G, M and T prompts and results are kept in `prototypes/{A,B,C}/runs/{G,M,T}/`, `wow-case/runs/` and `wow-case/future/runs/`. Original W is historical and its limitation is preserved. The future variant is a separate fixture.

- `comparison-results.md`: complete methodology, outcomes, limitations and link audit.
- `robustness-results.md`: final-Skill tests, explicit injection exposure and the adversarial citation portability failure.
- `judge-reviews/`: three blinded simulated reviewer processes, not human judges; color mapping and reviewer hallucinations in `../../research/13-taskspaces/judge-simulation.md`.
- `wow-case/future/runs/T/response.md`: complete local invitation and handoff, not a real public release.
- `prototypes/A/local-organization/`: local Python copied one fictional receipt into a created folder with synthetic approval inputs; not a NAS action.
- `static-check.json`: official checker output for the new Skill.
- `human-evaluation.md`: optional next test design; no contact has been made.

Reproduce link audit with `python3 experiments/13-taskspaces/audit_outputs.py`; deterministic fixtures with `python3 experiments/13-taskspaces/test_contracts.py`; local grouping with `python3 experiments/13-taskspaces/local_organization.py`. The local grouping script removes and recreates its own `prototypes/A/local-organization/disposable/` fixture only. Model scripts depend on Codex access and an existing temporary `bwrap` path; reruns cost time and may vary. Do not run `create_fixtures.py` over frozen evidence unless intentionally recreating the original set. No final package, PDF, publish, commit, or real user data was used.
