# Execution record — Experiment 03

## Scope and frozen design

- CLI help was inspected before launching; CLI version `codex-cli 0.164.0-alpha.11.1`; sandbox helper `bubblewrap 0.9.0` was copied from a locally extracted Ubuntu package.
- Final preregistration is in `preregistration.json`, including UTC timestamp and SHA-256 hashes for plan, answer key, rubric, both prompts, manifest, A/B diff and fixture generator. A prior preregistration was superseded **before any investigator** because the negative-control archive was made more independent; `preregistration-pre-revision.json` preserves that history. Final frozen hashes were rechecked after all runs.
- `source-manifest.json` records hashes for each of the 60 paths in all three archives. `ab-diff.patch` records the sole A/B changed sentence. The final preregistration lists the 53 paths differing between A and C. Original source hashes were rechecked after execution.
- 12 retry workspaces were each copied under `/tmp/ugreen03-retry-kgbzpo7f`, with exactly 60 evidence files and no symlinks; post-run hashes and membership were checked for every copy. Prompts, results, rubrics and keys were outside workspaces. The generator is local research tooling, not a Skill package.

## Technical failures and retries

The initial 12 fresh sessions are saved as `*-events.jsonl`, `*-stderr.log`, `*-status.json` and `../results/*.md` without `-retry`. An attempted extra outer bubblewrap mask hid the project but the Codex unified shell tool returned `Failed to create unified exec process: Permission denied (os error 13)` for every attempted command. Each process misleadingly returned exit 0 and `turn.completed`; **none actually read the files**. No substantive result from these attempts was used. The precise cause is not established.

Each failed attempt was retried once with a new independent session and the already-successful Codex read-only sandbox, without the extra outer wrapper. To protect research materials while retries ran, the project directory and three prior temporary experiment roots were set temporarily to mode 000 and then restored to their original modes in the launcher `finally` block. Their original modes and restoration status are in `retry-status.json`. All retries have unique session IDs and completed with successful file-reading commands; C-S1 first tried `python` (exit 127), then used `python3` successfully in the same session. This is a recovered command-level failure, not a restarted investigator. The logs show 60 evidence filenames per retry, source and workspace hashes passed, and no web/MCP tool calls were recorded.

## Settings and sessions

Every retry used a fresh `codex exec` with `--ignore-user-config --ephemeral --skip-git-repo-check --sandbox read-only -c 'web_search="disabled"' --cd <assigned-workspace> --output-last-message <run-local-report> --json -`; the frozen G or S prompt was supplied as stdin. The exact argument arrays and prompt hashes are in `retry-status.json`. Four ran at a time, ordered as a six-cell pass then reverse-order second pass. No session was resumed or forked; no parent chat or answer-key material was supplied as a prompt. We used the CLI default model and reasoning configuration uniformly, but the event stream did not expose their identifiers; do not infer the precise model from the host or UI.

| Run | Session ID | Duration (s) | Exit | Input / cached / output tokens | Evidence file read commands |
| --- | --- | ---: | ---: | --- | ---: |
| archive-a-g1 | `01a17a42-5785-7943-b7b1-362755297af7` | 50.062 | 0 | 57988 / 46336 / 1760 | 2 |
| archive-a-g2 | `01a17a44-b5ea-7c80-9bee-34e22a970d26` | 60.588 | 0 | 57856 / 46336 / 1742 | 2 |
| archive-a-s1 | `01a17a42-578b-78a0-a7f7-b925c7cde6e2` | 79.295 | 0 | 58219 / 46464 / 2288 | 2 |
| archive-a-s2 | `01a17a44-29cf-78a3-8479-b5ac02c4251c` | 71.58 | 0 | 54308 / 45440 / 2194 | 3 |
| archive-b-g1 | `01a17a42-5785-77c3-b374-bf14a09a4bac` | 59.881 | 0 | 40114 / 34304 / 1812 | 2 |
| archive-b-g2 | `01a17a44-4f33-7ec2-a97f-3836ff09b5d2` | 61.713 | 0 | 57980 / 46336 / 1654 | 2 |
| archive-b-s1 | `01a17a43-238b-7600-b228-73cfb8e83ee9` | 63.621 | 0 | 56267 / 47232 / 1939 | 3 |
| archive-b-s2 | `01a17a43-a3b0-7121-b97b-6e0b80930090` | 70.226 | 0 | 57403 / 47360 / 2147 | 3 |
| archive-c-g1 | `01a17a42-5784-79d3-9a79-0f5a355b5c78` | 52.266 | 0 | 77425 / 57728 / 1668 | 3 |
| archive-c-g2 | `01a17a44-4e6b-73e2-bba9-f0a2ec66f319` | 50.138 | 0 | 39891 / 34304 / 1588 | 2 |
| archive-c-s1 | `01a17a43-2c2f-75d3-820c-e2c195746c7e` | 70.935 | 0 | 98882 / 86656 / 2386 | 3 |
| archive-c-s2 | `01a17a43-49ee-7532-8b50-7c8e47ac6297` | 63.169 | 0 | 55740 / 49792 / 2403 | 3 |

All 12 retry turns completed, produced a nonempty report, had at least one successful evidence-reading command and preserved workspace contents. The two reports per cell remain raw, unedited CLI outputs at `../results/*-retry.md`. Token counts are CLI reported; input includes cached input. Durations are wall-clock under concurrent load. Individual timestamps, reasoning-output token counts, exact commands and outcomes are retained in the JSON status and JSONL event files. Stderr contains Codex state-database discrepancy/fallback warnings.

## Isolation and reproducibility limits

The project permission restriction makes its files inaccessible under normal same-user permission checks while the experiment runs; there is no proof that every hidden runtime mechanism obeyed the investigator prompt or lacked other access. Codex read-only sandboxing restricts writes, not all reads. The twelve retry workspaces share a parent directory and same user account, so another workspace was not blocked by filesystem permissions. Investigators were instructed not to access outside their workspaces; reviewed shell commands used only workspace-relative files, except `pwd`, and no external tools were recorded. The process shared Codex authentication, a state database, system instructions and the model provider. This is blinding by process separation, project permission restrictions and observed commands, not a formally isolated or independently administered environment.

No attempt was made to hide normal host runtime files, model identity, system instructions, or the fact that files are an archive. Web search was disabled; Codex necessarily contacted its model provider. No real UGREEN runtime was used. Private rubric and answer key remained unavailable to investigators via the project path during retry execution. User folder modes were restored.

`tools/build_fixtures.py` and both launcher scripts preserve the approach, but their temporary directory and installed Codex/bubblewrap paths are host-specific; retry is deliberately guarded to require the first technical-failure logs. The scripts should be adapted for a fresh machine and the permissions side effect reviewed; do not overwrite frozen records or rerun S2 on this set and treat it as holdout evidence.
