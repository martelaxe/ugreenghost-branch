# Twelve mechanisms: technical review and NAS implications

Research date and cutoff: **27 October 2026**. This review selects twelve sources linked or explicitly covered in the frontier sprint and prior-work audit. It reads paper methods/evaluation/limitations, implementation design or source code—not only abstracts. Pinned versions and what was actually inspected are in the [reproducible log](research-log.md). Examples below are labeled **paper example** or **illustration**: illustrations are thought experiments, not experiments performed here.

**How to read feasibility.** A consumer NAS may have snapshots, media search, playback and backups, depending on the product and configuration. Statements about missing features refer to a specific *documented end-to-end behavior*, not an assertion that no NAS has any similar function. A UGREEN fragment means only that the installed catalog documents a corresponding delegated expert capability; no NAS execution, output envelope, privacy guarantee or performance was verified. The parent orchestrator delegates to registered experts, rather than directly executing specialist commands. See [catalog audit](../ugreen-unexplored-capabilities.md). Research papers are experimental claims, not proofs that consumer use works.

## 1. SKILL.state — execution as a constrained state transition

**Source and verification:** [SKILL.state, version 3](https://arxiv.org/html/2608.26263v3), §3, Algorithm 1, §3.1–3.2, §5 and Limitations. Submitted 2026-08-26; revised 2026-09-02. Full methods and limitations inspected.

**Mechanism.** The runtime submits an immutable procedure `P`, a structured current state `Σ`, and the latest observation `O` to a model. The model proposes an action and a JSON state patch; the runtime deterministically validates and merges the patch, then executes the action. Its algorithm discards the intermediate reasoning trace, previous observations and previous actions from subsequent prompts. Domain-authored schemas are reused across tasks; validation constrains structure/updates, not the truth of every model inference. A bad omission can become irreversible if the relevant original observation was discarded.

**What is actually different.** Structured state, checkpoints and workflow engines are old. The specific research claim is to make a validated state projection the *primary reasoning substrate* instead of appending or compressing dialogue. Its bounded-prompt argument assumes bounded state/schema/observation sizes. The authors explicitly admit it fails when an initially overlooked observation later becomes relevant, the schema must be discovered, or the history itself is needed for audit.

**Paper example.** §3.1 reports one five-field CTF schema: `discovered_flags`, `tested_hypotheses`, `active_files`, `working_dir`, `cmd_summary`. §5 reports results across benchmark tasks; these do not test a NAS. A history-free design is especially risky for our evidence-heavy archive projects, where later interpretation can require discarded observations.

**Consumer gap / interaction.** Some NAS products offer tasks and logs, but the reviewed UGREEN catalog does not document an inspectable, validated agent-state runtime. Imagine an interrupted authorized restoration resuming with a compact map of pending approvals, source hashes and unknowns, while preserving an independent audit trail. This is **not** the same as merely saving a handoff note.

**Exact interaction check.** [LangGraph persistence](https://docs.langchain.com/oss/javascript/langgraph/thinking-in-langgraph) already checkpoints workflow state and supports pause/resume. That establishes significant prior art for the interaction; it does not prove LangGraph uses SKILL.state's exact history-discard method. The paper itself implements the algorithm; a user-facing NAS equivalent was not established in this search.

**UGREEN fragment.** An orchestrated Skill can tell experts to report what completed and what remains, and, with approval, `knowledge-agent` can request `ug-knowledge:save-text`. That is an advisory report, not deterministic patch validation, atomic durable transitions, automatic resumption or retained audit provenance. File format, approval, data integrity and parent-visible returns remain unverified.

## 2. Graph-of-Skills — recover prerequisites before executing

**Source and verification:** [Graph-of-Skills v4](https://arxiv.org/html/2604.05333v4), §3.1–3.3, §4, limitations and Appendix implementation. Revised 2026-09-11. The [source repository](https://github.com/davidliuk/graph-of-skills) exposes a retrieval implementation; its README was inspected, not executed.

**Mechanism.** Offline normalization extracts names, input/output descriptions, tools, source locations and other fields. Nodes are skills and edges represent dependency, workflow, semantic and alternative relations. Some dependency edges arise deterministically from I/O-schema overlap; a bounded candidate pool undergoes additional LLM validation. Online, lexical/dense queries seed a graph walk; reverse-aware personalized PageRank recovers upstream skills, then reranking and token-budgeted hydration return a bundle. Related I/O is evidence of plausible compatibility, not proof an edge is valid. Exact budgeted selection is formulated as a quadratic knapsack problem and approximated.

**What's different.** Simple vector search, DAGs and PageRank are old. The contribution is their particular composition for **prerequisite-complete, budgeted skill retrieval**. It does not discover guaranteed dependencies, execute skills, or ensure they are safe. Evaluation uses particular skill corpora and models.

**Illustration.** User says “produce a searchable transcript with the original audio link.” A transcription skill is a lexical hit, but an upstream scope/permission skill and a downstream source-link validation skill also need inclusion. A graph could surface them even if their wording does not resemble the user's request. If induced edges are incorrect, it might wrongly omit a required step.

**Consumer gap / interaction.** A normal NAS user selects a task rather than manually combining dozens of procedures; the system could present the *smallest dependency-complete procedure bundle* and identify missing prerequisites before starting. We did not find evidence this is a standard consumer NAS feature.

**Exact interaction check.** The authors' [GoS implementation](https://github.com/davidliuk/graph-of-skills) already retrieves skills with prerequisites, so the core interaction exists in developer tooling. Workflow DAG tools already encode explicit dependencies. We did not establish a household-NAS implementation, which is not proof of novelty.

**UGREEN fragment.** A static UGREEN Skill can explicitly sequence file, knowledge and photo experts and report an unavailable prerequisite. There is no documented dynamically built graph, embedding index, PageRank scheduler or ability to install this research code in the submitted Markdown-only Skill.

## 3. SkillAlign — control the exposure interface, not only the skill

**Source and verification:** [SkillAlign v1](https://arxiv.org/html/2609.07255v1), §3.1–3.3, §4, Limitations and Appendix B. Submitted 2026-09-07. Full method and evaluation design inspected.

**Mechanism.** The same candidate skill becomes a multi-view card: full text, short hint, compressed affordances/constraints/risks, and a workflow. An exposure policy picks `none`, `full`, `hint`, `compressed`, or `workflow`, and the selected rendering is inserted into the agent context. The original skill is not changed. Counterfactual experiments fix the task, agent and candidate set while varying exposure; a lightweight learned policy is compared with an oracle and remains below it.

**What's different.** Prompt compression and retrieval already exist. SkillAlign makes *presentation form conditional on context* an explicit experimental variable and uses multiple views of the same artifact. This does not establish that compressing a safety-critical instruction is safe: an omitted permission or failure rule can materially change behavior.

**Illustration.** During media inventory the agent receives a short hint; just before a proposed copy it receives the full safety/approval procedure. That is a proposed policy, **not** something established safe by the paper. It requires a trustworthy trigger and retention of mandatory rules.

**Consumer gap / interaction.** NAS assistants rarely expose which procedure and level of detail is active. One possible interaction is an adaptive help panel showing progressively detailed technical steps as a user moves from exploration to a potentially risky action.

**Exact interaction check.** The paper's fixed rendering and policy experiments already implement adaptive exposure for agents, not a consumer NAS help panel. [Progressive-disclosure UI](https://www.ibm.com/docs/en/technical-content?topic=practices-progressive-disclosure) is established; this search did not verify an identical adaptive NAS interaction. No evidence it improves user comprehension or device safety.

**UGREEN fragment.** A Markdown Skill can structure a short core and optional references, but there is no documented policy-learning/rendering hook or guarantee that loading changes at a specific action boundary. Mandatory scope and permissions must remain present; a prompt cannot enforce a policy.

## 4. HASP — executable interception at the agent loop

**Source and verification:** [HASP v2](https://arxiv.org/html/2605.17734v2), §2.1, §2.2, §3, limitations and Appendix examples. Revised 2026-09-28. Methods and evaluation inspected.

**Mechanism.** The base model proposes an action. A harness retrieves relevant program functions and invokes each `should_activate` on current state/action. A firing function's `intervene` can replace the action or supply corrective context; records of interventions can feed post-training/evolution. Candidate functions are checked for syntax, interface and mock execution; the paper also considers optional teacher assistance. The guardrail's reliability is only as good as its trigger, access to state and semantics.

**What's different.** Middleware, ACLs and input guardrails are existing mechanisms. HASP's contribution packages observed agent errors as reusable intervention functions and studies inference, training and evolution, not the invention of interception itself. Its test suites are web/math/coding, not NAS recoveries. A program function that fires on some modeled risks is not a complete security boundary.

**Illustration.** Before executing a copy, an external hook sees source, destination and proposed operation; if source scope is missing it blocks the call and requests authorization. The action is actually intercepted before execution. No such custom hook is documented for UGREEN Skills.

**Consumer gap / interaction.** A user could see *why a proposed action was stopped* and then approve an amended scoped action, rather than trusting that a model remembered an instruction. Most ordinary NAS permissions do not by themselves supply task-specific, model-proposal-aware intervention.

**Exact interaction check.** [OpenAI Agents SDK tool guardrails](https://github.com/openai/openai-agents-python/blob/main/docs/guardrails.md) already offers pre-tool checks that skip/replace a call or raise a tripwire; [YoloFS](https://arxiv.org/html/2604.13536) stages filesystem mutations for review. The general interaction is therefore existing, not a new product capability. Their enforcement scope and semantics differ.

**UGREEN fragment.** The documented gateway and workflow approval mechanisms apply to particular expert actions; a Skill may request consent and report `waiting_approval`. It cannot install HASP `should_activate` / `intervene` middleware or establish that its own prompt catches every unsafe call.

## 5. EM²Mem — event anchors bind multimodal evidence before search

**Source and verification:** [EM²Mem v1](https://arxiv.org/html/2609.00551v1), §3.2–3.4, §4, ablations and limitations. Submitted 2026-09-01. Full schema, construction and evaluation sections inspected.

**Mechanism.** The method partitions a video into base segments, e.g. 30 seconds, each with an anchor `(id, start, end)`. A cell binds a transcript/dialogue context, selected keyframes, visual captions, structured action/object/topic/scene/entity fields and multi-scale contextual summaries. An episodic graph links temporal/cross-event relations and a semantic graph links concepts; an evidence selector retrieves anchors with attached data. Alignment is performed during construction, not inferred anew from unrelated snippets for every query. Extraction errors and segment boundaries propagate to the index.

**What's different.** Video keyframe indexing, ASR and event graphs are established. The paper's technical combination joins heterogeneous observations and provenance into event cells with temporal context and linked graphs, then measures performance versus baselines. The reported benchmark benefits are not universal. Its limitations admit that textual conversion loses fine visual detail; an anchor does not by itself prove a causal or personal relationship.

**Paper example.** §3.2 describes a segment where someone discusses a flower craft while flowers and vases appear: spoken context, images and object/action fields share one anchor. A later query can retrieve that cell instead of assembling a caption and transcript independently. This is a published illustration, not a NAS test.

**Consumer gap / interaction.** Ask a library “show the moment the speaker points at the part they are describing”; display the actual video segment, transcript and image evidence together, or an explicit incomplete-coverage marker. To really find pointing, the system needs appropriate visual analysis, not just co-occurrence in the same 30-second window.

**Exact interaction check.** [Azure Video Indexer](https://learn.microsoft.com/en-us/azure/azure-video-indexer/video-indexer-search) already indexes and searches moments and synchronizes player/insights; [its insight documentation](https://learn.microsoft.com/en-us/azure/azure-video-indexer/insights-overview) covers transcript, shots and keyframes. [MomentSearch](https://github.com/traversaal-ai/momentsearch) also describes a matched keyframe with a timestamp for playback. The precise composite memory implementation and pointing query are not established there; comparable visible behavior substantially exists in a cloud product. No user-owned NAS advantage is established.

**UGREEN fragment.** `knowledge-agent` can request documented audio transcription and `photo-agent` can request OCR/vision on selected photos. Time-aligned video decoding, graph construction, keyframe extraction, timecoded provenance, source playback and cross-modal anchor identity are not guaranteed by the catalog. Do not promote the excerpt to a verified video moment without returned timing evidence.

## 6. SyncSink — coarse acoustic fingerprints then precise alignment

**Source and verification:** [SyncSink README at 2021 commit](https://github.com/JorenSix/SyncSink/blob/8dc83d72e2af909a5e9f24c1e20c613c4cf81464/README.textile), “How does SyncSink synchronize media files?”; [CrossCorrelation.java at 2021 commit](https://github.com/JorenSix/SyncSink/blob/767ea0b106ba662a518cee97c8e54bd208d0029a/src/be/panako/syncsink/CrossCorrelation.java). Both full files inspected; repository linked by the sprint. The related 2015 paper itself was not read here, so its claims beyond the implementation are unverified.

**Mechanism.** Extract fingerprints from a reference and other recordings to find a rough shared-audio offset; the README says roughly 8 ms. Then refine near that offset with cross-covariance. The inspected Java class decodes via an audio dispatcher at 4 kHz, compares ten audio blocks, computes a cyclic correlation maximum for each, retains offsets within 0.064 seconds of the coarse estimate, and averages accepted estimates. `ffmpeg` and Java are prerequisites. An empty set of accepted estimates can produce a non-useful numerical result; reliability and drift handling require further assessment, not assumption.

**What's different.** Audio fingerprints, correlation and synchronized media predate this system. The practical engineering choice is a two-stage search: robust/coarse identification followed by a smaller precise calculation, rather than expensive fine correlation across the whole recording. It is not an AI model and cannot establish that two people consented to sharing the recording.

**Illustration.** A friend's camera starts 12 seconds before another camera; both recorded the same applause. Fingerprints suggest the shift; local correlation refines the overlap. Quiet scenes, unrelated repeating music, time-varying drift or compression can invalidate a single-offset interpretation.

**Consumer gap / interaction.** On a household NAS, a person could select an event and switch viewing angles while staying at a matched instant, rather than manually arranging clips in an editor. This requires real synchronization and a multi-stream player; no conclusion about user demand follows from the algorithm.

**Exact interaction check.** [Final Cut Pro](https://support.apple.com/en-ie/guide/final-cut-pro/ver8798d940/mac) already uses audio waveforms for synchronization and multicam; SyncSink itself exposes offsets for the same recordings. The baseline feature exists. The proposed household archive discovery and consent workflow were not established in the reviewed source, not proven absent elsewhere.

**UGREEN fragment.** `media-agent` can request a catalog search, and `file-agent` can request media metadata. Neither waveform extraction/correlation nor synchronized playback is documented. A Skill cannot reproduce the central interaction using only those operations.

## 7. OHMS — timestamped oral-history index as a navigation layer

**Source and verification:** [Code4Lib Journal: Latah County OHMS implementation](https://journal.code4lib.org/articles/10643), 2015, sections “OHMS”, “OHMS Implementation”, and discussion of XML indices and jPlayer. This is a detailed practitioner report on an implemented open-source system, not an independent controlled study. The article and implementation details were read; we did not run OHMS.

**Mechanism.** Interview metadata, transcript, index sections and timestamps are encoded in XML; a PHP viewer and JavaScript media player link searchable text/segments to audio. For the Latah collection, administrators adapted existing metadata, edited XML, changed templates, and modified `Transcript.class.php` to multiply their index's minute values by 60 because the viewer/player expected seconds. Timestamp alignment and units are explicit engineering, not something implied by a transcript string.

**What's different.** Time-coded media annotation long predates OHMS. The practical contribution here is integrating human-authored, structured oral-history indices, transcript search and a player in a reusable archival workflow. The study documents customization and digitization work; it does not demonstrate automatic, accurate transcript alignment.

**Paper example.** A section indexed at minute 3 becomes point 180 seconds for playback after the local conversion. If minutes are silently treated as seconds, the link goes to the wrong location; if there is no timestamp, the exact moment is unknown.

**Consumer gap / interaction.** User selects a recorded voice note and sees each verified sentence as a tap-to-listen item, with a nearby photograph explicitly marked as linked by a human or as an uncertain inference. Typical NAS file listings are not an oral-history editor; whether a particular vendor offers this interaction requires product-specific checking.

**Exact interaction check.** OHMS already supports search-to-audio navigation; [Descript](https://www.descript.com/tools/audio-text) also synchronizes transcript and audio. Linking a specific separately stored photo automatically is a narrower unverified combination, and a generic multimodal agent might do it. This is close to the project's prior family-memory ideas.

**UGREEN fragment.** `knowledge-agent` may return a transcript and `segments`; catalog does not guarantee segment timestamps, supported playback identifiers, player links, or cross-file relationships. Return an exact excerpt and source if present; claim a tap-to-moment link only when actually produced and checked.

## 8. Frigate — interval joins between events and retained recording segments

**Source and verification:** [Frigate `storage.py` pinned to 2026-09-14](https://github.com/blakeblackshear/frigate/blob/3931ab74a8f676011437360859e52036d37cf5a8/frigate/storage.py), `check_storage_needs_cleanup` and `reduce_storage_consumption`; [recording/history docs](https://docs.frigate.video/usage/history/). The source code was read. This is one cleanup path, not a complete statement of all Frigate retention rules.

**Mechanism.** The inspected code estimates hourly recording consumption and checks available disk space. It traverses recording segments in start-time order and separately queries indefinitely retained events with clips. It compares event and recording time intervals to decide which segments can be deleted in this low-space cleanup path; when insufficient unretained data can be freed, it logs an error and proceeds into further cleanup handling. Event records, clips and raw recording segments are distinct data objects. A segment's presence, a recognized event, and successful video playback are separate facts.

**What's different.** Time-interval joins and NVR retention are long-established. The interesting reusable primitive is **reasoning over overlapping time intervals with different retention roles**, rather than treating event descriptions as a complete timeline of what a camera saw. The implementation is existing operational code, not a new AI algorithm.

**Illustration.** A detection record says 12:00:10–12:00:20; a retained segment spans 12:00:00–12:00:30. The interval overlaps, but an event result alone does not tell us whether that segment still exists, whether it can play or whether footage exists outside it. Low disk pressure can change the available segments.

**Consumer gap / interaction.** A camera owner asks “What can I actually review around this alert?” A view separates known event intervals, verified playable segment intervals and unobserved gaps, with an explicit scope/timezone. This is stronger than an empty search result, but requires a reliable segment inventory, not simply an event list.

**Exact interaction check.** [Frigate History](https://docs.frigate.video/usage/history/) already opens event-related recordings and documents why recordings may be absent. Its [review interface](https://docs.frigate.video/usage/review/) also documents a multi-camera grid at a shared point in time. It substantially overlaps the interaction. We did not find proof of a complete automatic gap explanation for arbitrary retention histories; no claim it does not exist. Camera data are sensitive and may involve other people.

**UGREEN fragment.** `security-monitor-agent` documents camera enumeration, `event-timeline` and `event-evidence`. The latter's references, actual lifetime, playable segments and parent propagation remain unknown. There is no documented complete recording-segment inventory or retention history, so a Skill must not draw a full coverage bar or claim no event occurred.

## 9. LESS — distribute recovery work across overlapping erasure-coded stripes

**Source and verification:** [LESS full FAST 2026 paper](https://www.usenix.org/system/files/fast26-cheng.pdf), §3.2, Figure 1, §3.3–3.4, §4.1–4.2. Paper pages 633–637; the full PDF was parsed via the browsing tool. The published results are for the authors' HDFS-based evaluations, not this NAS.

**Mechanism.** For an `(n,k,α)` layout, each of `n` blocks is split into `α` sub-blocks. LESS groups blocks and arranges overlapping extended sub-stripes, using Reed–Solomon/Vandermonde coding coefficients so each extended sub-stripe is recoverable. When one block fails, both of its sub-blocks are reconstructed using survivors from an appropriate extended sub-stripe. The design trades read volume and seek count against sub-packetization, while keeping RS-like MDS properties under the stated construction.

**What's different.** Erasure coding and repair-efficient codes are prior art. The new construction layers extended sub-stripes over widely used RS codes to reduce repair reads and seeks with configurable small α, and balances repair costs across block positions. It requires selecting an encoding when data are written; it cannot retrofit its guarantees onto arbitrary existing RAID blocks by prompting.

**Paper example.** In Figure 1, `(n,k,α)=(6,4,2)` has 12 sub-blocks arranged as three `(8,6)` extended sub-stripes. To repair the two missing sub-blocks of `B1`, the paper reads six surviving sub-blocks, equivalent to three whole blocks, versus four full blocks in conventional `(6,4)` RS repair: **25% less repair I/O** in that example. This is a layout example, not a user device measurement.

**Consumer gap / interaction.** A NAS owner could ask a storage system, before committing to a protection policy, “How much can I still access and how long might repair take when one disk fails?” The system would need actual coding layout, measured workload, device health and a repair model. Typical consumer UI's parity/rebuild progress does not imply this predictive explanation is available; no blanket vendor claim is made.

**Exact interaction check.** LESS's [authors' HDFS implementation](https://github.com/adslabcuhk/less) already implements its repair construction. RAID/ZFS systems already expose rebuild/resilver operations; we did not verify a consumer interface implementing this exact predictive question. Performance forecasting is speculative and not a consequence proved by LESS.

**UGREEN fragment.** There is no system health, encoding layout, disk repair or low-level block API in the inspected catalog. A Skill can explain user-supplied documentation, but cannot determine actual repair cost or implement LESS. Treat the interaction as infrastructure-dependent, not a hackathon Skill feature.

## 10. CORDS — inject a local fault and observe end-to-end consequences

**Source and verification:** [Redundancy Does Not Imply Fault Tolerance, FAST 2017](https://www.usenix.org/system/files/conference/fast17/fast17-ganesan.pdf), §3.1–3.2, §4.1.1 and limitations, pp. 151–153; full paper parsed via the browsing tool. Its 2017 system versions and cluster settings are not evidence of defects in current NAS products.

**Mechanism.** CORDS wraps storage via `errfs`, a FUSE filesystem, and uses `errbench` workloads and behavior-inference scripts. It initializes replicated/persisted data, injects one filesystem-block error or corruption per run, and compares client-visible behavior/logs to expected durability, integrity and availability. Faults include zero/junk corruption, read/write EIO and space-related ENOSPC/EDQUOT. It distinguishes a local node's reaction from global system outcomes.

**What's different.** Fault injection and replication were established long before 2017. The paper's contribution is a systematic *cross-system empirical study* of how local filesystem errors propagate through distributed storage protocols, including carefully selected fault types and system-specific observations. Tests covered simple workloads and a subset of possible faults; the authors state these limits.

**Paper example.** For the tested Redis v3.0.4 configuration, §4.1.1 describes leader append-only-file user-data corruption remaining undetected and later propagating during follower resynchronization. This is a historical finding for that setup, not a general claim that Redis or all replication systems currently behave this way.

**Consumer gap / interaction.** Instead of “backup complete,” imagine a user-authorized isolated rehearsal that removes access to one selected copy, then tries to restore and open a disposable target, reporting which exact step failed. This tests a recovery path, not merely redundancy; successful rehearsal still cannot guarantee future restore under other failures. Do not inject faults into real user storage.

**Exact interaction check.** [Restic `check --read-data`](https://restic.readthedocs.io/en/v0.17.0/047_tuning_backup_parameters.html) verifies repository data and existing tools routinely perform test restores. Those are closely related but are not the CORDS block-fault experiment or a guarantee that an application opens correctly. No complete consumer-NAS equivalent to the specific isolated rehearsal was established.

**UGREEN fragment.** `file-agent` can list, read and calculate SHA-256 for authorized paths, and compare two *actually read* files. It cannot inject block errors, create isolation, mount backups, access snapshot state or prove restorability with the documented catalog. Copying also requires real approval and verified no-overwrite behavior.

## 11. YoloFS — staged, mediated filesystem changes and command-level travel

**Source and verification:** [YoloFS full paper v5](https://arxiv.org/html/2604.13536v5), §5.1–5.4, Figures 7–8, evaluation and limitations. This was already researched in [Experiment 17](../../17-invention-lab/storage-frontier.md); it is included to correct any impression that we missed it. A paper system is not a UGREEN feature.

**Mechanism.** A kernel filesystem interposes between an agent's commands and the base filesystem. Staged content lives in a flat file store; an in-memory override tree maps each path to a staged file, a base-file source or absence. A journal records stage, delete and rename operations; snapshots/travel give the agent intermediate views and permission rules gate sensitive accesses. For a rename whose contents do not change, the path can refer to the base backing rather than copying a large file into a mirrored upper tree. Changes remain staged for user review and commit/abort under the described model.

**What's different.** Copy-on-write, overlays, journaling and snapshots predate YoloFS. Its contribution combines a storage-efficient staged representation, command-level travel and progressive access rules for agents. Security depends on complete mediation and correctness of the actual implementation; a natural-language promise to stage changes provides neither.

**Illustration.** Agent renames a 10 GB video: update the override mapping to the original base backing rather than copy all bytes merely to represent a new path; the user reviews the proposed staged view. Editing the contents would still require appropriate staged storage. This is based on §5.2, not a measurement we ran.

**Consumer gap / interaction.** A user says “try organizing these assets, then let me inspect every change before it reaches my files.” They can roll back a specific failed command while keeping earlier safe staged work. Generic previews and recycle bins are weaker than enforcing all filesystem mutations through a staging layer, though some NAS products offer snapshots and previews.

**Exact interaction check.** YoloFS itself already implements this agent-facing staging and review interaction in a research filesystem; git branches and snapshot-enabled systems supply related previews. Our Experiment 12/16 recovered files and locally simulated approval, but did not install or reproduce YoloFS. No novelty claim remains for the basic idea.

**UGREEN fragment.** Gateway approvals and `cpmv` with `overwrite` exist as documented expert operations, and a Skill can propose a plan. No catalog operation creates YoloFS's kernel overlay, universal command interception, staged views, command snapshots or atomic rollback. A user-approved copy is not equivalent to an overlay.

## 12. lakeFS — immutable commit metadata plus mutable branch/staging state

**Source and verification:** [lakeFS accepted KV design pinned 2022-07-11](https://github.com/treeverse/lakeFS/blob/9949f65f7841f07294a6b49e24ff3d40441e36e0/design/accepted/metadata_kv/index.md), especially “Semantics”, “Consistency non-guarantees” and “Committer flow”. This is an **accepted design proposal**, not proof every implementation detail remains identical in current releases. lakeFS was already covered in Experiment 17 and related temporal concepts in Experiment 19.

**Mechanism.** Committed entries are immutable metadata stored as ranges and metaranges; branch pointers, uncommitted entries and related metadata are mutable. A branch maintains a staging token and sealed tokens. A commit rotates/seals the token with conditional `SetIf` (compare-and-swap), applies sealed staged entries against the prior commit and conditionally advances the branch; the design describes retry/overlap cases for concurrent commits. These operations create a versioned object-store namespace, not a magical reconstruction of every physical or human action.

**What's different.** Git-like commits, copy-on-write, compare-and-swap and content versioning already existed. This design adapts them to object-store metadata with a defined key-value abstraction and concurrency behavior. Its explicit non-guarantees are as important as its commit mechanism: it says the model does **not** supply linearizability of all operations and failed mutations might still be visible.

**Source example.** In the design's “1-3-2 problem,” concurrent unsafe increment operations can lead an observer to commit values `1`, then `3`, then `2`. A perfectly preserved commit sequence is therefore not necessarily a causally correct story about what users intended or knew. This directly challenges simplistic chronological reconstructions.

**Consumer gap / interaction.** A user asks “show me what the archive presented while two devices were editing, and identify conflicts or uncertain order.” Actual transaction IDs, write provenance and a trustworthy capture boundary would be required; snapshots alone cannot reveal unseen concurrent operations or who knew what.

**Exact interaction check.** [lakeFS](https://docs.lakefs.io/) already provides object-store commits, branches and version navigation; our own [Experiment 19](../../../docs/experiment-19-alternative-past-decision.md) explored past-versus-present evidence, although its time boundary was authored and attested in a fixture. The new technical question is concurrent-write consistency and provenance, not another retrospective report. No consumer NAS system was proven to lack all such controls.

**UGREEN fragment.** Documented file metadata and hashes can compare selected accessible copies; `knowledge-agent` can help report evidence. No documented snapshot/branch/read-at-commit API, trusted transaction log or atomic history capture appears in the installed catalog. Do not infer historical access time from file timestamps.

## Five technical mechanisms worth taking forward

These are **mechanisms**, not named product concepts. “Not already tried” means the precise mechanism and falsification condition are absent from the reviewed 01–19 work, not that nobody has ever built them.

1. **Construction-time multimodal event binding with inspectable uncertainty.** Bind each audio/text/image observation to a source interval *before* retrieval, retain native evidence and competing alignments, then navigate to it. Unlike 18's static photo story and 19's document cutoff, this requires a reproducible cross-modal time model. EM²Mem and Azure overlap strongly; a decisive test is whether linking an ambiguous phrase to the wrong moment is detected. UGREEN lacks guaranteed segment timecodes/video extraction.
2. **Coarse-to-fine acoustic alignment of independent recordings.** Audio fingerprints propose offsets and correlation refines them; retain rejected matches and confidence, model clock drift separately. This creates a playable shared moment rather than an AI-generated description. SyncSink and Final Cut already do the core; the project has not tested it. It needs signal processing and a player unavailable as documented UGREEN Skill primitives.
3. **Interval-based event-versus-recording coverage.** Join camera event windows with independently verified retained media intervals and explicitly mark unknown spans. This asks what can actually be reviewed—not whether a text report mentions an event—and is meaningfully distinct from 19's human-authored record cutoff. Frigate already does much of the underlying event review; a meaningful distinction needs actual segment and retention evidence, which UGREEN's catalog does not guarantee.
4. **Enforced staging with evidence-preserving state transitions.** Combine a filesystem overlay that mediates writes with deterministic state validation and an independently retained audit log; simulate failure before any actual commit. Project 16 used an isolated local exclusive copy and 14 tested a static handoff, but neither achieved runtime mediation plus state/audit integrity. YoloFS, SKILL.state, LangGraph and tool guardrails are strong existing prior art. The combination needs real platform primitives; Markdown rules alone cannot enforce it.
5. **Causal/consistency-qualified history.** Preserve commit identity, per-write observations and concurrency relationships alongside versioned file data, and display where ordering or access is unknowable. Project 19 already handled attested snapshots and historical evidence; it did not establish concurrent-write consistency. lakeFS's 1-3-2 example illustrates why timestamps and snapshots cannot prove causality. Distributed tracing, event logs and existing versioned storage overlap; true causality needs trusted instrumentation unavailable in the UGREEN catalog.

These five span two useful frontiers: **media becomes an interactive source**, and **storage becomes a truthful execution/history boundary**. The second frontier is more technically differentiated but mostly outside today's documented Skill interface. None has been implemented, tested with users or verified on a NAS during this review.
