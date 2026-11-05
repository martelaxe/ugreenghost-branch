# Experiment 05 — Evidence contracts and intelligence multiplier

- [Decision memo](decision-memo.md), [comparative evaluation](comparative-evaluation.md), and [UGREEN contract audit](ugreen-contract-audit.md).
- [Contract gaps](ugreen-contract-gaps.md), [implementation map](ugreen-implementation-map.md), [model availability](model-availability.md), [benchmark design](benchmark-design.md), [rubric](evaluation-rubric.md), [harness design](harness-design.md), and [failure analysis](failure-analysis.md).
- `datasets/a`, `datasets/b`, `datasets/c`: fictional held-out evidence; `private/answer-key.md` is the preregistered answer, not supplied to investigators.
- `results/`: 18 raw final reports. `execution/`: source hashes, A/B diff, preregistration, process and scorer records, anonymization map, prompts, raw model/command events, per-run scores and harness logs. `preflight/`: technical model/sandbox check.
- `implementation/`: domain-independent **local research** harness, tests and launchers; not a UGREEN Skill and not a submission package.

The six H reports represent two separate weak-model calls each. See `comparative-evaluation.md` for false-negative and citation failures. No UGREEN NAS was accessed.
