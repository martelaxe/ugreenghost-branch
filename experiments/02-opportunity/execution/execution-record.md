# Execution record — Experiment 02

## Setup and preregistration

- Evaluation date: 26 October 2026. Preregistration time and SHA-256 digests are in `preregistration.json`; the prompt and manifests were fixed before starting either investigator. The hashes were verified again after both runs.
- Two source variants each contain 22 files. `source-manifest.json` records SHA-256 hashes; `variant-diff.patch` records the only difference, a single creator-permission clause in `03-rights/vale-archive-agreement.txt`.
- Temporary workspaces were `/tmp/ugreen-opportunity-02-fttklbkb/archive-a` and `/tmp/ugreen-opportunity-02-fttklbkb/archive-b`. Each was independently copied and checked to contain exactly its 22 files and no symlinks. No instructions, answer key, rubric, other variant or prior results were placed inside. SHA-256 hashes and workspace file lists matched after the runs; source dataset hashes also remained unchanged.
- The CLI help was consulted. CLI version: `codex-cli 0.164.0-alpha.11.1`. A locally extracted Ubuntu `bubblewrap 0.9.0`, previously tested in a read-only sandbox, was supplied in PATH; it was not installed system-wide.
- Both fresh processes were launched concurrently with the identical exact `prompt.txt` through stdin, `--ignore-user-config --ephemeral --skip-git-repo-check --sandbox read-only -c 'web_search="disabled"' --cd <assigned-workspace> --output-last-message <report> --json -`. Their actual argument arrays, start times, PIDs and exit codes are in `process-status.json`. No parent conversation was explicitly passed.

## Runs

- **archive-a:** new ephemeral session `01a17a32-fa70-7721-b19f-88446a705c6a`, PID 314930, started 2026-10-26T21:52:03.313065+00:00, completion observed 2026-10-26T21:52:50.892271+00:00; exit 0; `turn.completed` present. Model identifier was not supplied by the CLI event stream; the default model was used. 4 completed shell commands, 0 other completed tool events. The commands inventoried and read relative workspace files; details are in `archive-a-events.jsonl`. CLI report: `../results/archive-a-report.md`.
- **archive-b:** new ephemeral session `01a17a32-fa71-7481-9b2b-1b32fe7bdc1b`, PID 314931, started 2026-10-26T21:52:03.314344+00:00, completion observed 2026-10-26T21:52:50.892446+00:00; exit 0; `turn.completed` present. Model identifier was not supplied by the CLI event stream; the default model was used. 2 completed shell commands, 0 other completed tool events. The commands inventoried and read relative workspace files; details are in `archive-b-events.jsonl`. CLI report: `../results/archive-b-report.md`.

Each stderr log contains startup warnings about a state database discrepancy and fallback; both sessions nevertheless completed and their recorded file-reading commands returned exit code 0. Process exit 0 and `turn.completed` establish execution completion only; substantive success was evaluated separately against the preregistered rubric. The JSONL event logs include the investigator's commands and their outputs, and the report files are the CLI-produced final messages.

## Isolation and interpretation limits

Read-only sandboxing is a write restriction, not full read isolation: it does not itself prevent the process from reading other filesystem paths. The exact prompt prohibited outside access, and the recorded shell commands operated on relative workspace paths. The logs cannot prove that all underlying runtime components were unable to read outside files. No web search or external tool call appears in either event log; web search was disabled and user config ignored, but Codex itself necessarily contacted its model provider and used standard runtime/system instructions and existing authentication. No model identifier was available in the recorded CLI events. The temporary workspaces are separate but same-host and share the Codex installation/authentication; this is not an independently administered or cryptographically isolated environment.

These results concern local Codex on synthetic files, not UGREEN NAS or its official expert-agent runtime.
