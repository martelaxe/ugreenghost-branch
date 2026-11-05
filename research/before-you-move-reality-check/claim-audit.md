# Claim and instruction audit

Reviewed 27 October 2026 against the installed v2.0.0 catalog and orchestration/completion references, [previous implementation map](../ugreen-ecosystem-deep-dive/05-real-skill-feasibility.md), previous package and this test. This is a claim-level assessment of the entire entry point, all linked references and ten proposal answers; “documented” means the installed catalog describes an action, not that actual NAS behavior is proven.

| Skill claim or instruction | Assessment / correction |
|---|---|
| Read-only pre-change preview and user goal | A proposed instruction workflow; local agents produced reports, but UGREEN outcome is unverified. It is not a new runtime enforcement layer. |
| Trigger, target, action, destination and authorization | Appropriate required inputs. Asking for authorization is an instruction to the model, not proof of platform authorization enforcement. |
| `ug-filesystem` → `file-agent`: `find`, `ls`, `stat`, `cat`, `sha256sum` | Action names/owner exist in installed catalog. How complete results are and whether they return every required field/format on a device remain unknown. |
| `ug-document` → `document-agent`: `qa`, `reconcile`; `ug-knowledge` → `knowledge-agent`: `collect-evidence` | Correct catalog ownership; actual child-to-parent provenance and data schemas are unspecified. These are requests, not proof of successful source attribution. |
| `delegate --target` illustrations and parent/child boundary | Syntax examples use registered targets; body expressly requires actual scope, limits and completed results. The short examples are not valid complete production requests by themselves. |
| 50-path/20-document defaults | Requested limits only; explicitly not a guaranteed budget, number of examined documents, complete scan or enforced limit. |
| Direct references vs ambiguous, historical, contrary and runtime use | A reasoning policy, not a verified dependency graph or assurance that all reference formats can be read. Actual passages must be returned. |
| Hash comparison | Same SHA-256 is strong evidence for same bytes at check time, not identity of role, provenance, authorization or backup protection; it is not a mathematical or future-state guarantee. Actual hash mapping on device unknown. |
| Expert status/failure instructions | `completed`, `failed`, `cancelled`, `waiting_user`, `waiting_approval` are official vocabulary; propagation, partial data and resume semantics are unverified. Only completed results can support dependent work. |
| Scope completeness, counts and citations | Requests exact paths and real excerpts; no fabricated counts, no pagination assumption and no no-dependency claim from absence. Link renderability remains unverified. Output limit on primary items must not be represented as complete coverage. |
| Write/approval and atomicity | Core says no writes, and this remains true of the documented intended workflow; it does not independently enforce a security boundary or perform an approval. No safe-copy or rollback guarantee. |
| Privacy/model processing | Does not promise offline or on-device AI. Provider and processing depend on runtime configuration and user consent. |
| Output improvement | In the initial limited-scope test, the Skill named the outside area but failed to explicitly request targeted authorization; revised references make that next action concrete. First post-change run did so. This is post-observation and not independent validation. |
| Disclosures | Describes UGREEN platform and AI assistance, no bundled third-party libraries/executables. Entry ownership, eligibility and dates/newness must be verified by entrant, not inferred from this package. |

## Ten proposal answers

The original is preserved at `submissions/round1-final-candidate-draft/`. The revised PDF/source is in `submissions/round1-before-you-move-reality-check/`.

| Question | Audit and revision |
|---|---|
| 1. What it does | Changed “previews” to “is designed to preview” to distinguish desired function from verified UGREEN execution. |
| 2. User/problem | Clear intended user and plausible problem; no claim of frequency, measured demand or validated user benefit. |
| 3. Solution | Changed “distinguishes” to “aims to distinguish”; it is an instruction, not measured guaranteed behavior. |
| 4. User flow | Changed declarative search/analysis to “requests” operations and reports returned evidence. |
| 5. Difference | Explicitly says detailed generic prompting produced similar local findings and superiority was not established. Reusable packaging is a convenience hypothesis, not novel model capability. |
| 6. UGREEN features | Changed definitive expert actions to requests conditional on returned results. |
| 7. Architecture/data | Changed definite delegation to instructions directing delegation. Scope and no-write are intended policy, with provider and processing dependent on device configuration. |
| 8. Built vs unbuilt | Reports static check and three-condition local Codex tests; explicitly says no UGREEN agents and hardware behavior unknown. |
| 9. Test plan | Prospective finalist tests, not claims already conducted on hardware. |
| 10. Limitations | Explicitly says the Skill is not designed for complete application visibility, safe-delete proof, moving, backup restore or a maintained graph; formats, completeness and model behavior remain unknown. |

The PDF describes prospective performance, not product guarantees. Neither static pass nor local model results establish UGREEN safety, coverage, accuracy, privacy or a competitive advantage. It contains 282 substantive answer words. PDF generation uses ReportLab and pypdf outside the Skill ZIP, and these tools are disclosed in the draft.
