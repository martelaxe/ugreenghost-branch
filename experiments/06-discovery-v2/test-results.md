# Local regression and static validation

## Reproduce

From `/home/martelaxe/ugreen-hackathon`:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s experiments/06-discovery-v2/tests -v
PYTHONDONTWRITEBYTECODE=1 python3 experiments/06-discovery-v2/implementation/generate_examples.py
PYTHONDONTWRITEBYTECODE=1 python3 experiments/06-discovery-v2/implementation/generate_regression_observations.py
node /mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/scripts/check-skill.mjs prototype/surprise-me
```

The workstation-specific checker path points to the installed official UGREEN Skill Creation Tool 0.7.3. Its catalog is version 2.0.0. Results are retained in [`results/unit-tests.txt`](results/unit-tests.txt) [`results/regression-observations.json`](results/regression-observations.json), and [`results/static-validation.json`](results/static-validation.json). The checker returned exit **0**, `static-pass`, zero errors and zero warnings. It recorded `SKILL.md` SHA-256 `4a0d361e551e0afece395d7782dc74b911efcd0224681397cf0d2db71e748c78` and `references/report-format.md` SHA-256 `f82b2cf4ce92731932197ac6d376b67cf8569aeed20a2b315f5b123121185dc2`. This is a static structure/security check, not installation, successful expert delegation or NAS runtime proof.

## Results

All **32 local unit tests passed**. They use deterministic code and illustrative, manually supplied semantic-review results; no real model, expert or NAS was called.

| Required regression | Observed behavior |
| --- | --- |
| H-A1 empty verifier | Original Experiment 05 candidate and its five matching citations retained as `NEEDS VERIFICATION`; no claim that empty output means false. |
| H-B1 empty verifier | Original candidate and uncited restriction retained as unverified; no distribution recommendation. A separate mocked later review can attach the actual archived rights record, yielding a sourced `BLOCKED` state without altering the original candidate. |
| H-B2 uncited blocker | A purported positive review cannot promote the uncited restriction into a supported finding. |
| Supported opportunity | Mock retrieved sources plus explicit per-claim semantic judgments lead to qualified `SUPPORTED` and a non-executing review step. |
| Known restriction | A mocked, reviewed source-backed restriction yields `BLOCKED` and cites its source; an uncited one does not. |
| Negative control | No candidate produces no fabricated discovery. This unit case does not prove model behavior on a realistic negative archive. |
| Essential source missing | Candidate is retained internally but becomes `INSUFFICIENT EVIDENCE`. |
| Truncation / unknown coverage | Candidate cannot become `SUPPORTED`; counts, skipped paths and partial data remain explicit. |
| Failure / cancellation | Dependent stages stop; available candidate evidence is preserved. |
| Waiting for user / approval | Pending state is not treated as completion and the candidate is not presented as verified. |
| Simulated three-expert handoffs | Source paths and excerpts survive the illustrative file → document → knowledge sequence; incomplete document results stop the knowledge step. |

Additional tests cover unverifiable quotations, merely related evidence, duplicate IDs and reviews, missing semantic or blocker assessment, source-backed rejection, candidate immutability, limiting public results to three, and keeping unsafe original actions out of the user-facing recommendation. Local inventory detected the referenced missing `sleeve-sizes-2025.pdf` in the old A fixture using the explicitly limited PDF-name scan. This validates a known regression case, not general missing-file detection.

The three generated illustrative reports are [supported](examples/01-supported.md), [blocked](examples/02-blocked.md), and [insufficient](examples/03-insufficient.md). Their semantic judgments and source texts are synthetic. Static validation and these local tests do **not** establish real UGREEN agent contracts, NAS compatibility, reliable discovery accuracy or effectiveness for actual users.
