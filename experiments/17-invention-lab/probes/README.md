# Three small invention probes

These probes explore interaction mechanisms, not product performance. All data are fictional and under this experiment. No UGREEN expert, NAS hardware, user trial or independent preference evaluation occurred. Source-only local Codex runs retain prompts, event logs, responses and input hashes. The filesystem sandbox masks known project/history paths, but other host and runtime paths remain visible and network isolation was not independently proved.

## W: Consent-Bearing Object — toy mediation, not security

**Hypothesis:** A stored object might allow an interaction now and deny a later one when its owner changes a policy. **Request:** allow a fictional family story, then withdraw the right to use the broker. **Input:** [probe.py](wild/probe.py) creates [memory.txt](wild/disposable/memory.txt) inside a disposable fixture and uses an in-memory boolean. **Observed:** the broker returned the story, then `DENIED BY TOY BROKER`; a direct read immediately returned the same private text. See [raw output](wild/output.json). The direct bypass decisively disproves any claim that this toy protects the file. It cannot recall what a prior recipient saw. **Needed:** real identity, kernel/enclave/gateway enforcement, output controls, auditable policy and a threat model; none is in the submitted-Skill format.

## B: What-If Exhibit — a tangible projection

**User request:** “Show three stages of our event. Rebuild the exhibit without red artwork, and don't invent a substitute if no eligible artwork exists.” **Input:** [five actual fictional SVG drawings](bridge/fictional-assets/) and [manually authored role/color manifest](bridge/fixture-manifest.json). **Actual local execution:** [probe.py](bridge/probe.py), a deterministic research-only Python program, selects the first eligible drawing for each named beat and writes three real SVG exhibits plus selection records. It does not use AI or UGREEN. It renders a gap if neither red nor blue is allowed; this tests the abstention rule. [Raw observations](bridge/observations.json) include before/after hashes showing original SVGs unchanged.

- [Baseline exhibit](bridge/outputs/baseline.svg): arrival-red, workshop-red, ending-green.
- [No-red exhibit](bridge/outputs/no-red.svg): arrival-blue, workshop-blue, ending-green.
- [No-red-or-blue exhibit](bridge/outputs/no-red-or-blue.svg): arrival and workshop are marked missing, ending survives.

This changes a visible artifact, not the underlying filesystem view, albums, photos, or a live website. All scene labels and suitability are planted fixture facts; the geometric icons are not real photos and semantic equivalence is not independently checked. A meaningful system would infer/verify roles and exclusions, support access and ordering, and handle changed source evidence. On UGREEN, a conversational preview plus optional album creation is only **plausible** through documented experts, with actual album item format, ordering, creation and membership verification unknown.

## S: One-Bit Workshop — two actual local Codex calls

**Hypothesis:** An archive-backed procedure can use a user answer to select the next useful action rather than merely report the archive. **Inputs:** [plan.txt](skill-native/fixture/plan.txt) contains two ways to make a sign; [stock.txt](skill-native/fixture/stock.txt) is an unverified inventory. **Request and mechanism:** the first exact [prompt](skill-native/run-first/prompt.md) tells a local assistant to extract routes, ask one discriminating question and not act. The [actual first response](skill-native/run-first/response.md) asked a single four-option question about printer/paper versus marker/card. A second fresh process received that prior response and the explicitly fictional user answer “Yes, the marker and blank card are both here”; its [actual response](skill-native/run-followup/response.md) directed the user to the handwritten route. Both processes exited 0, issued 2 local read commands, and source hashes were unchanged; actual [execution records](skill-native/run-first/execution.json). They did not physically make a sign or call NAS experts.

This is conversational branching, not a calculated optimum or an implementation of REVOIR. The second result is a directive, not evidence an action occurred. There is no matched generic baseline, real user or benefit comparison; a generic agent could likely do the same. A UGREEN implementation could delegate scoped reading to file/document experts in principle, but real state retention, triggering and evidence propagation are unknown.
