# UGREEN contract gaps

| Assumption | Classification | Evidence / consequence |
| --- | --- | --- |
| `find`, `cat`, `qa`, `extract`, `reconcile`, `collect-evidence` are mapped to the listed experts | **Documented** | Catalog action records and agent mappings; not a runtime success claim. |
| Generic CLI `{ok,data}` / `{ok,error}` envelopes | **Documented** | Catalog `invocation.resultEnvelope`; empty example object does not define actual per-action fields. |
| `completed`, `failed`, `cancelled`, `waiting_user`, `waiting_approval` must be handled | **Documented** | Kit `completion-and-errors.md`; exact serialized representation remains unconfirmed. |
| `save-text` has `workflow` approval, read actions are cataloged `none` | **Documented** | Generation-time catalog flags; actual permissions and approval handling are unknown. |
| A completed result can always be passed with exact source citations to the next agent | **Unconfirmed** | Orchestration requires passing verified results, but availability, identity and retention of citations are not specified. |
| `find` path/`fileId`, QA `answer`, coverage, evidence, save `verified`/`outputFile` are present on every successful call | **Unconfirmed** | Mentioned in `returnSummary`, without required per-action schema. |
| `full` always means all source content; every cap/truncation is detectable | **Unconfirmed** | Input options are documented; output/completeness semantics are not. |
| `status` and `result` are nested as in Experiment 04 | **Unconfirmed** | Mock construction only; no such expert envelope was established. |
| `paths`, `documents`, `text`, `coverage.complete`, citation `role/path/quote`, `blocker` match real outputs | **Unconfirmed** | Experiment 04 inventions; possible collisions with summary terminology do not prove shape or semantics. |
| Parent can output a rich multi-source investigation reliably | **Inferred** | Markdown orchestration can request it; behavior and response channel have not been tested. |
| The parent directly executes `cli.invoke` or includes a Python harness in the Skill | **Contradicted** | Official kit requires parent delegation and prohibits scripts in the Skill package. |
| A static checker pass proves NAS runtime compatibility or evidence completeness | **Contradicted** | Kit checker and Experiment 04 explicitly limit static validation. |
