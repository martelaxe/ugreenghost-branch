# Before and after: local simulation only

User request: “My old Cedar folder is missing something important. Can you find the intended asset and propose how to recover it without changing originals?” Authorized fictional search workspace and existing `projects/cedar/assets` destination. Full [prompt and frozen Skill](user-prompt-and-skill.md); actual [model response](raw-model-response.md).

**Before:** [snapshot](before.json) lists 25 existing files; `projects/cedar/assets/lantern-banner.svg` is absent. `layout.txt` points to that missing path; `review.md` selects Northwick revision C; `design-codes.txt` maps Northwick to L42; `production-register.csv` points L42/C to `shared/q7.svg`; the actual SVG title agrees; `projects/winter/board.md` actively references the source. The more obvious `shared/banner-final.svg` is rejected revision A. The printer's external copy is not inspected. All source material is under [creative fixture](../fixtures/creative/).

**Proposal returned by the actual Skill-guided Codex:** copy `shared/q7.svg` to `projects/cedar/assets/lantern-banner.svg`, preserving the source. The user did not give a hash or the original filename. A human can follow the same records, but filename-only search would be misleading; neither time saved nor user surprise was measured.

**Action:** local Python adapter used `os.O_CREAT | os.O_EXCL` on a disposable clone after [synthetic approval flags](approval-simulation.json), not real human or platform approval. The [copy record](copy-record.json) and [after manifest](after.json) show exactly one added file, every previous file unchanged, source before and after and destination SHA-256 all `b54b91bc33582c053fc0b0f81fa7b529089c2d586d14190afd03551d54b292e8`. This is a real local copy, not a NAS copy. It demonstrates byte equality and source preservation, not authenticity of a real-world asset or application-level recovery.

## 90-second storyboard (future NAS demo, conditional)

0–15s: Show Cedar's existing folder and the missing referenced banner. Ask the user's actual natural-language request and authorize only the appropriate folders.
15–35s: Show the old red file with the misleading `final` name and the review selecting revision C.
35–55s: Show design code → production register → opaque `q7.svg`, and Winter's existing use. The practical reveal: the apparently wrong-named source is needed elsewhere too.
55–70s: Show the exact proposed source-preserving copy, evidence and explicit permission. On real NAS, proceed only if its child/platform can establish atomic no-overwrite semantics and real platform approval. Otherwise honestly stop at the proposal.
70–90s: If a real supported copy completed, show source/destination hashes and unchanged original; otherwise show this clearly labeled local simulation and disclose that no UGREEN action occurred. Do not claim the application itself was repaired.
