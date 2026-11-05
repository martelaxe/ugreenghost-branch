# Two concept probes — actual local Codex runs

On 2026-10-26 two fresh independent `codex exec` sessions, each requested as `gpt-6.1-sol` / medium and read-only, inspected separate **12-file fictional text archives**. They received only the respective [prompt and task](outputs/) and assigned workspace, not the [answer key](keys/answer-key.md). The project directory and key were hidden at their normal location by a separate bubblewrap mount namespace; other host paths and Codex runtime/auth remained accessible, so perfect isolation is not proven. Web was disabled in configuration. Input hashes and events are in [status](outputs/status.json) and each output folder. Both exited 0; no files changed. These are Codex runs, not UGREEN expert outputs or human feedback.

## 1. Impact Rehearsal

**Task:** “I am considering moving `assets/shared/cover.txt` to `archive/unused/cover.txt`. Before I touch anything, help me understand what work in this archive could be affected, and give me a practical next step.”

**Actual result:** [Raw response](outputs/impact/raw-response.md) found the Autumn program and Winter guide both contain direct relative references to the target. It identified a separate historical `cover_old.txt`, an unchecked external partner, and recommended keeping the file in place while checking both projects. This is a real actionable text preview; no application was opened and no move occurred. **Unexpected moment:** a seemingly routine file move may affect two projects.

**Source/semantic audit:** `projects/autumn/program.md` and `projects/winter/readme.md` actually contain `../../assets/shared/cover.txt` relative to their own directories; `projects/winter/status.md` says handoff is pending; `admin/vendor-note.txt` and `admin/inventory.txt` disclose external/incomplete context. `assets/shared/cover_old.txt` is distinct. The model's relative `:line` references identify actual fixture files, but are not portable clickable file links from its saved report. A real app break is an inference and was not verified. One scenario with deliberately inserted path references is not proof the concept is surprising to people, or that it can find opaque application links.

## 2. Rebuild Kit

**Task:** “I have an unfinished project in this archive. Help me turn the material into a small useful thing I can actually make within the documented constraints.”

**Actual result:** [Raw response](outputs/rebuild/raw-response.md) created a complete four-section River Walk handout and a preparation checklist. It named the absent image and public-use permission and unconfirmed venue/printing. The output is genuinely usable as text to review; no printable layout, photograph, production or venue booking occurred.

**Source/semantic audit:** `project/purpose.txt`, `materials/notes.txt`, `materials/fold.txt`, `rights/use.txt`, `planning/time.txt` and `planning/venue.txt` support the purpose, narrative, uncertain materials, limited grant, time/budget and unconfirmed venue. The three locations from `project/steps.txt` are not actually specified; the model correctly substitutes general prompts. Its quoted “Low water…” starts with uppercase whereas the source's phrase after the colon starts lowercase; meaning is preserved, but the punctuation/case is not byte-exact. Workspace-relative source references are not portable links. Creative and educational value was not independently assessed.

**Selection:** Impact Rehearsal's concrete planned change and cross-project map fit NAS ownership and give a stronger immediately understandable decision. Rebuild Kit is the fallback and produces the more complete creative artifact. A generic Codex produced both without a Skill, so neither proves a distinct technical mechanism. This is a pragmatic product choice, not evidence that either is exceptional or better than a generic assistant.
