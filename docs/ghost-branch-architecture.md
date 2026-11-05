# Ghost Branch architecture and official capability mapping

Installed Uliya catalog 2.0.0 and authoring references were checked. The parent issues self-contained delegations to the registered owner of each CLI; actual paths and completed results must be passed. Runtime field schemas and propagation are not guaranteed. The exact normalized action records and parameters are in [catalog](../research/ugreen-capabilities/02-operation-catalog.json).

| Capability / owner | Documented selected actions | Inputs and purpose | Unverified or excluded |
|---|---|---|---|
| `file-agent` / `ug-filesystem` | `find` (`path` required), `ls` (`path`), `stat` (`path`), `cat` (`path`), `sha256sum` (`path`) | Discover authorized candidates and read relevant source/logs; hash only if meaningful. `find`/`ls` support bounded limits. | Enumerating all paths, full code content, truncation signals and file-type handling. No shell, Git, compiler or tests. |
| `document-agent` / `ug-document` | `qa` (`query` required; optional `file`, `max-files` etc.), `reconcile` | Inspect selected returned docs, compare claims and versions. | Source-code formats, excerpts, citation fields and context truncation unverified. File-agent reading can be used when available. |
| `photo-agent` / `ug-photo` | `vision-vlm` and `vision-ocr` | Inspect an actual authorized screenshot for visible UI or text. | Result identity, screenshot path propagation and visual model quality unverified; screenshots do not prove functionality. |
| `knowledge-agent` / `ug-knowledge` | `collect-evidence` (`query` required), `audio-transcription`, `save-text` | Find actual supporting/contrary evidence, optionally transcribe an authorized recording, optionally request saving a reviewed packet. | Citation and return formats, audio support, save collision behavior and approval resumption unknown. |

`save-text` is a **workflow-approved state change**, not automatic saving: the user must request the exact authorized destination and review; if safe no-overwrite cannot be established, the Skill stays in preview. It never invents result fields or calls a GitHub/GitLab API. Private source content may be sent to a configured provider; the owner must check the actual model and data handling. The operation catalog is not an enforcement boundary and NAS ownership does not prove offline inference.

The local experiment directly reads disposable text/files and attaches an image to Codex as a research analogue. It does not simulate actual expert outputs or prove that expert calls will run. [Experiment](../experiments/ghost-branch/test-report.md).
