# Experiment 12: Project Rescue

Research-only fictional example, not an actual UGREEN NAS test. The 26-file `archive/` is the fixed source dataset; `initial-manifest.json` contains the baseline hashes; `answer-key.md` is separate and was never included in model workspaces. The existing project and earlier experiments were not changed.

- `mvp-results.md`: methodology, comparisons, safety tests, limitations.
- `model-runs-fixed/`: eight actual Codex model-only runs, prompts and outputs. `model-runs/`: initial environmental failures retained. Prompts contain no answer key. Temporary workspace paths in execution records no longer exist.
- `local-demo/`: real OS copy of a fictional file into a disposable fixture, snapshots, event and `before-after.md`. Approval and gateway events are simulation inputs; no human or platform approval is claimed.
- `local_demo.py`, `test_local.py`, `setup_fixture.py`, `run_models*.py`, `audit_citations.py`, `create_audit.py`: research scripts only; none are included in the Skill. `setup_fixture.py` generates the fixed fixture and its answer key; do not rerun if preserving the current frozen baseline.
- `static-check.json`: official checker output for `../../prototype/project-rescue/SKILL.md`.

Reproduce the deterministic local demonstration from project root with `python3 experiments/12-self-healing-archive/local_demo.py`, then `python3 experiments/12-self-healing-archive/test_local.py`. The demo removes and recreates only its own `local-demo/disposable-after/` directory. Running model trials again has cost and depends on Codex, model availability and the recorded temporary `bwrap` location. The local adapter uses fixture-specific paths and is not security-hardened production software. Read `mvp-results.md` before interpreting results.
