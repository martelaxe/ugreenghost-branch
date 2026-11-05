# Expert handoffs and boundaries

The parent constructs self-contained delegations with actual user-authorized source paths, dish clues, limits and completed earlier results. The example delegations in the entry point are syntax examples, not complete calls. No placeholder path, guessed file ID, shell call, third-party API, arbitrary executable or fabricated tool response belongs in a request.

| Stage | Owner and documented capability | What to request | Limit / gate |
|---|---|---|---|
| Inventory | `file-agent`: `ug-filesystem:find`, `cat` | Search actual authorized paths for clues; return candidate paths and any errors/limits. | A capped or unproven listing is not the entire archive. Only pass candidates actually returned. |
| Text | `document-agent`: `ug-document:qa`, `extract`, `reconcile` | Read actual selected documents and return relevant evidence for ingredients, steps, disagreements and missing context. | Exact source excerpt, type coverage, handwriting and result schemas are not guaranteed. |
| Card/photo | `photo-agent`: `ug-photo:vision-ocr`, `vision-vlm`, optionally `search-picture` | OCR a specific authorized returned card; inspect chosen related photos when the user wants them. | OCR/visual observations may be wrong; availability of paths/IDs and handoff formats is unverified. |
| Audio | `knowledge-agent`: `ug-knowledge:audio-transcription` | Transcribe a specific authorized recording with language if actually known. | Formats, timestamp precision, speaker identity, source attribution and privacy depend on runtime. Never create a transcript that was not returned. |
| Optional save | `knowledge-agent`: `ug-knowledge:save-text`, catalog effect state-change/approval workflow | Only owner-reviewed text, actual allowed destination and explicit request; send a self-contained instruction and let the child conduct platform approval. | Overwrite/collision and destination semantics are unverified. If safe non-overwrite cannot be established, stop. Report only completed evidence, never a request as a saved file. |
| Optional album | `photo-agent`: `ug-photo:create-album`, catalog effect state-change/approval workflow; `album-detail` for real returned identity if supported | Only user-selected actual photo identities and name after explicit request. | `add-item` encoding and ID correspondence, selected membership, ordering and album visibility are unverified. Require expert confirmation and user/platform approval; stop if unsupported. |

Handle `completed`, `failed`, `cancelled`, `waiting_user` and `waiting_approval` exactly as described in the entry point. Preserve partial results without claiming complete coverage. A pending save or album cannot be described as successful. Do not reuse approval for another operation. A later session requires a fresh request and evidence; no durable state or automatic watcher is documented.

## Disclosures

OpenAI Codex assisted in research, workflow design, writing and local illustrative tests for this Skill. The package includes no third-party scripts, libraries or services. UGREEN Uliya and its registered experts are platform dependencies; model provider and possible external processing depend on the configured device. The user must authorize sensitive material and the selected provider. Ownership, AI disclosures and hackathon eligibility are for the entrant to verify.
