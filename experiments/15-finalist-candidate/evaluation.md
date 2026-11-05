# Evidence-based comparison and failure audit

## What was executed

The [preregistered plan](preregistered-design.md) froze the exact Skill SHA-256 `f1551c265082f62358019a42512c6937a7135054c40c1a1f52fc1691f2c7e152` before testing. Thirty independent local Codex processes ran: 5 cases × generic G and exact Skill S × three separately preserved waves; the latter two were explicitly **post-observation fixture repairs**, not prospective replications. Two extra fresh G/S processes compared the actual saved v3 base-S output with the current critical case. All requested the same `gpt-6.1-sol`, low effort; local direct read-only filesystem tools stood in for documented expert delegation. No actual NAS, UGREEN expert return, save or platform approval was tested. Prompts, event streams, raw answers, user scopes and input manifests are preserved under `runs/`, `runs-v2/`, `runs-v3/`, `runs-delta/` and corresponding `workspaces*`. Answer keys are outside these workspaces.

The first launcher failed before any model process because a temporary bubblewrap binary was missing; its replacement and hashes are documented in `environment-notes.md`. The model sandboxes hide the project and known history folders but allow configured Codex runtime and other host paths; no chat was intentionally passed, but absolute isolation is not proved. Scope in restricted cases is also enforced physically by omitting `rights/`, as well as by prompt. Read-only input hashes were unchanged. Eight deterministic checks pass in `test-integrity.log`; they verify inputs, source hashes, frozen prompts and link mechanics, not the models' semantic reliability.

## Preserved original observations

- **v1 baseline ambiguity:** The event schedule listed open/close but did not document named volunteer shifts. Baseline S gave volunteer coverage UNKNOWN; baseline G gave PASS, while G on the *irrelevant* decoration mutation gave UNKNOWN. Either interpretation exposes the fixture's ambiguous word “coverage”; it is not defensible to call the v1 baseline an unambiguous three-PASS case. The same generic method yielded differing overall results on one pair whose only changed file was irrelevant; one pair does not establish cause or a population failure rate. S stayed UNKNOWN across that pair. Critical permission was correctly FAIL; restricted permission UNKNOWN.
- **v1/v2 business date defect:** The purportedly completed workshop was dated April 2027, future relative to the actual October 2026 review, and the payment confirmation lacked a date. Both v1 methods marked relevant checks UNKNOWN; that was a defensible response to flawed data. v2 added volunteer shifts but still did not establish the fictional evaluation date or dated payment. These outputs are preserved, not relabeled as model failures.
- **v3 repair:** All event cases gained an explicit continuous roster, the fictional as-of date was set to 25 April 2027 for both conditions, and the business payment was dated 24 April 2027. v3 was initiated after observing v1 and partial v2 results. Its comparisons are valid within that wave, but they cannot be treated as an independently preregistered holdout or mixed with earlier prompts.

## Corrected v3 same-input results

| Test | G: generic Codex | S: frozen Skill | Interpretation |
|---|---|---|---|
| Event baseline | Three documented checks PASS, qualified as stored evidence | Same three PASS | Both supported the three explicit conditions; neither established general publication safety or authentication. |
| Relevant permission mutation | Permission FAIL; other two PASS | Same | Both identified the public-use restriction and requested an appropriate permission. |
| Irrelevant décor mutation | Three PASS | Three PASS | For these one-shot cases neither changed the explicit checks because stripe color changed. |
| Restricted rights | Permission UNKNOWN; other two PASS | Same | Both distinguished inaccessible evidence from proof of prohibition or permission. |
| Business packet | Three PASS | Three PASS | Both reconciled 800-unit final invoice/payment, 12 attendees and superseded 1,000-unit draft. **Qualification:** the report itself labels 800 as an invoice amount, not explicitly as “revenue”; both noticed this but still passed the revenue requirement. Treat that semantic equivalence as questionable and requiring user clarification, not as proven generalization or an unequivocal PASS. |

The important outcome is **parity on the obvious decisive evidence**. The Skill did not demonstrate superiority over generic analysis on these cases. The v3 source data were deliberately structured and small; no actual user, real photo understanding, external authority verification or real hardware was tested. The text-shaped SVG was read as local file data; no UGREEN photo-agent analysis or rendered visual placement was demonstrated.

## Controlled mutation and rerun

`audit.json` verifies that each v3 mutation changed **exactly one path** relative to v3 baseline:

- `rights/art17.txt`: permission text changed from “public use allowed for the Cedar Repair Cafe invitation” to “public use restricted to internal review only.” SHA-256 changed `c2e05c46…` → `d570a027…`; all other paths' hashes match. The file remains readable; this is an intentional semantic change, not evidence of disk corruption.
- `other/decor.txt`: “blue stripes” changed to “green stripes.” SHA-256 changed `6d71afae…` → `10ede849…`; all other paths' hashes match. Nothing makes décor a documented requirement.

The user-supplied previous-review test copied the **actual** v3 baseline S output unchanged into two new critical-case workspaces. Generic and S each independently compared that actual review with current sources and described the relevant status as PASS → FAIL while holding other checks PASS. Both correctly said the record/current discrepancy does not prove when or why the file changed; no automatic history is claimed. Exact raw results: `runs-delta/G/response.md`, `runs-delta/S/response.md`. This two-run comparison was added after inspecting v3 baseline output and is post-hoc, not part of the initial preregistration.

## Source navigation and actual work

`audit.py` found **82 Markdown links in v3 outputs**: **43 resolve from the saved reports, 39 do not**. All 82 map to existing paths in the corresponding frozen fixture after normalization, which checks file identity only, not whether a citation semantically entails a claim. The 43 resolving links appear in G outputs; all 39 S Markdown links are unportable. One S report and one G report used plain path identifiers rather than Markdown links, so their zero link counts are not successful link-resolution evidence. Both G and S delta outputs contain only broken raw links from the saved result locations: G 0/9, S 0/10. Paths refer to temporary workspaces or unadjusted filenames/line suffixes; no claim that UGREEN citations will work is justified.

S sometimes mentioned that the Skill's disclosure reference was absent from the **fictional data workspace**; the linked reference does exist in the actual Skill package. That is workflow/meta noise, not a static validation error. Restricted-S and business-S each used 12 local shell commands; their logs show, respectively, an unavailable `python` command and a failed malformed `rg` invocation followed by recovery. This is a real local-test behavior, not an official NAS expert result, and illustrates why command counts do not straightforwardly measure user effort. One-shot runtime, concurrency and different token caching preclude claims of general speed or cost savings.

Static checker: `static-pass`, exit 0, zero errors/warnings; exact hash above. It verifies structural compliance, not execution, provenance, platform approval or legal correctness. The final-user-facing status is advisory and limited to specified requirements, not a platform-level release gate.
