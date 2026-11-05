# Lightweight concept tests

Executed 2026-10-26 in the project workspace. No NAS, official expert, AI model or independent users were invoked. These deliberately narrow tests can disprove certain assumptions; they cannot establish real product performance, usefulness, delight or differentiation. Research code is outside any Skill package.

## Test 1: Can a succession exercise preserve actual references and unknowns?

- **Hypothesis:** A simple human-curated text rehearsal can give an actionable question and exact supporting text while reporting a referenced record as unreviewed, rather than asserting that it does not exist.
- **Inputs:** Two fictional text files, `checks/fixtures/maintenance.txt` and `checks/fixtures/handoff.txt`; hand-authored excerpts and questions; an expected but absent `recovery.txt`; inventory completeness unknown.
- **Expected:** An actual Markdown question card with each supplied excerpt and filename; the missing record described only as not among reviewed records; an explicit incomplete-coverage statement. Reject a fabricated quote or inaccessible cited file.
- **Failure condition:** A missing file is described as nonexistent, an invented quote passes, an evidence path disappears, or the artifact claims verified recovery.
- **Actual:** `python3 research/07-idea-discovery/checks/checks.py` produced [a readable simulated rehearsal](checks/simulated-rehearsal.md); `python3 -m unittest discover -s research/07-idea-discovery/checks -p 'test_*.py' -v` passed the relevant three tests, including nonexistent source and fabricated quote checks. Five tests passed overall; exit code 0.
- **Limitations:** Questions and excerpts were manually written. The test checks exact strings, not whether the wording logically supports the exercise. It does not test generation, expert returns, user cognition, user safety, backup recoverability, or a meaningful comparison against generic AI. Relative fixture paths are local test references, not UGREEN output.
- **Effect:** A concise useful-looking artifact is possible with curated data; the differentiating claim that an AI can autonomously create a correct exercise remains untested.

## Test 2: Do three finalists have cataloged building blocks?

- **Hypothesis:** The documented catalog contains assigned agent/action pairs needed for a minimal read-only textual version of each finalist.
- **Inputs:** Project copy of official catalog 2.0.0; nine explicit pairs across succession (file find, document extract, knowledge collect-evidence), consent/reuse (photo meta, document extract, evidence), and conversation bridge (photo vision-vlm, document extract, evidence).
- **Expected:** Each action exists under the designated owner; a deliberately fabricated `ug-video:render-montage` must not be credited as documented.
- **Failure condition:** Any required identifier/owner is missing, or the fabricated action is accepted as cataloged.
- **Actual:** All nine requested identifier/owner checks returned true; the fabricated montage action returned false. Tests passed. See [checks.py](checks/checks.py).
- **Limitations:** Presence/agent name only. This does not exercise API parameters, access, image parsing, a meaningful transformation, source identifiers, completion states or cross-expert handoffs. A false catalog match only shows that exact name is absent; it does not prove that video creation is impossible elsewhere. The full text workflow may use other documented actions and needs separate checking. Catalog read/approval labels are analyzed in [technical boundary](technical-boundary.md).
- **Effect:** These concepts remain plausible for a read-only textual Skill; no complete workflow is validated. Drop any promise of a generated video or slideshow unless official support is separately established.

## Test 3: Can we establish creative or human value today?

- **Hypothesis:** A real user finds the rehearsal more useful than an ordinary AI answer and can identify a consequential missing step.
- **Inputs / design:** The current fictional files and expected but unavailable record. Present comparable, equally authorized source files to a generic agent and to an eventual Skill; counterbalance and mask the source of the output. Have real intended users independently answer predetermined questions and inspect cited sources. Record task completion, unsupported facts, false claims of absence, time, and preferred output, including negative feedback.
- **Expected:** A successor completes the task and identifies the gap without unsafe claims; the hypothesized improvement would require a predeclared meaningful edge over the generic baseline.
- **Failure condition:** Wrong or fabricated instructions, a false claim that absence was proven, or users cannot reliably distinguish unknown from complete. For competitive value, no practically meaningful improvement over the baseline is also a failure to demonstrate the differentiator.
- **Actual:** **Not run.** There are no independent participants or real NAS agent outputs here. A planned test is not an experimental result.
- **Effect:** User value, surprise, and superiority remain unknown. Do not use synthetic AI personas as validation.

## Next falsifiable test

As soon as representative people and a runnable candidate are available, use a small fictitious NAS handoff archive containing an explicit contact, a conflicting instruction, an intentionally omitted expected record, and one inaccessible/limited listing. Ask a second person to answer three questions and identify what they cannot establish. Compare the candidate with a generic assistant given the same available files, model access and task; blind presentation, counterbalance ordering with distinct archives, and pre-register failure conditions above. For an initial feasibility pilot, treat any invented citation, wrong critical instruction, false absence or undisclosed incomplete scope as a failure, regardless of user preference. Record actual source access and do not interpret a handful of users as population estimates. If official agents are unavailable before finalist access, run the generic-plus-human half and state that the UGREEN comparison is pending. A real-device provenance/state-transition check remains separately essential.
