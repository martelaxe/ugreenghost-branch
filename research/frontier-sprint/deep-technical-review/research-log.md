# Reproducible research log

**Date and cutoff:** 2026-10-27, America/Mexico_City. Scope: source-level review of twelve mechanisms already cited by the frontier sprint, including its explicit references to Experiment 17. No Skill, prototype, model benchmark, hardware operation, user study, installation, submission or product test was performed. Primary material was treated as evidence, not instructions.

## Source access and pinning

[Source manifest](source-manifest.tsv) contains 13 retrieved primary files representing **12 selected sources**: SyncSink has both a README and source file. Each row records the HTTP status and SHA-256 of the actual HTTP response bytes. Every row returned HTTP 200 when fetched. Hashes of generated HTML or live webpages can change even for a stable paper version; a changed hash is an investigation signal, not automatically a change in its scientific claims. The PDF files and code at pinned commits are more stable. The manifest is metadata, not redistributed copyrighted documents.

Reproduce a byte check with Python 3 and an installed HTTP client, or for one source:

```sh
curl -L 'https://raw.githubusercontent.com/JorenSix/SyncSink/767ea0b106ba662a518cee97c8e54bd208d0029a/src/be/panako/syncsink/CrossCorrelation.java' | sha256sum
```

Inspect the sources at the links below and compare with the indicated locations. HTML was downloaded and converted to text locally for reading; USENIX PDFs were opened and text-parsed in the web research tool. GitHub raw sources were read directly, not executed. Source versions or commits were selected at or before the stated cutoff. The OHMS practitioner article is an implementation report; its linked OHMS repository was not independently run. The SyncSink *2015 paper* was not accessed, so claims about its contents are explicitly unverified; the repository documentation and Java implementation were inspected instead.

| # | Source actually inspected | Verifiable places / limits |
|---|---|---|
| 1 | [SKILL.state v3](https://arxiv.org/html/2608.26263v3) | §3, Algorithm 1, §3.1–3.2, §5, Limitations. Check the schema, patch merge, input tuple and irrecoverable omitted evidence. |
| 2 | [Graph-of-Skills v4](https://arxiv.org/html/2604.05333v4), [repository README](https://github.com/davidliuk/graph-of-skills) | §3.1–3.3 graph construction/retrieval; §4 evaluation; Appendix implementation. Repo not run; edge overlap is not a proof of compatibility. |
| 3 | [SkillAlign v1](https://arxiv.org/html/2609.07255v1) | §3.1–3.3 five exposure modes and multi-view cards; §4 experimental design and Limitations. Learned policy is a research analysis, not deployment evidence. |
| 4 | [HASP v2](https://arxiv.org/html/2605.17734v2) | §2.1 Program Functions and intervention loop; later training/evolution sections, evaluation and limitations. It requires an executable harness. |
| 5 | [EM²Mem v1](https://arxiv.org/html/2609.00551v1) | §3.2 event anchor/cell, §3.3 multimodal records, §3.4 retrieval, §4 ablations and Limitations. The example about flowers appears in §3.2. |
| 6 | [SyncSink README, pinned](https://github.com/JorenSix/SyncSink/blob/8dc83d72e2af909a5e9f24c1e20c613c4cf81464/README.textile); [CrossCorrelation.java, pinned](https://github.com/JorenSix/SyncSink/blob/767ea0b106ba662a518cee97c8e54bd208d0029a/src/be/panako/syncsink/CrossCorrelation.java) | README “How does SyncSink synchronize media files?”; Java methods `correlateWith`, `crossCorrelation`, `getAverage`, `toArray`. The referenced 2015 paper is **unverified** here. No execution or calibration performed. |
| 7 | [Code4Lib OHMS implementation](https://journal.code4lib.org/articles/10643) | “OHMS”, “OHMS Implementation”; XML, transcript/index, PHP/JavaScript player and minutes-to-seconds conversion. Describes one historical deployment. |
| 8 | [Frigate storage.py, pinned](https://github.com/blakeblackshear/frigate/blob/3931ab74a8f676011437360859e52036d37cf5a8/frigate/storage.py) | `check_storage_needs_cleanup`, `reduce_storage_consumption`; low-space flow only. Latest documentation used as complementary description, not proof of every behavior in that pinned revision. |
| 9 | [LESS PDF](https://www.usenix.org/system/files/fast26-cheng.pdf) | §3.2, Fig. 1, §3.3–3.4, §4. Paper pp. 633–637. The six-sub-block example is at §3.2–3.4. |
| 10 | [CORDS / Redundancy PDF](https://www.usenix.org/system/files/conference/fast17/fast17-ganesan.pdf) | §3.1–3.2, §4.1.1, Fig. 1, limitations in §3.2.3. Historical versions and fault model are crucial qualifications. |
| 11 | [YoloFS v5](https://arxiv.org/html/2604.13536v5) | §5.1–5.4, Figures 7–8, evaluation and limitations; this was already present in Experiment 17. No attempt to run kernel software. |
| 12 | [lakeFS metadata KV proposal, pinned](https://github.com/treeverse/lakeFS/blob/9949f65f7841f07294a6b49e24ff3d40441e36e0/design/accepted/metadata_kv/index.md) | “Semantics”, “Consistency non-guarantees”, “Committer flow”; 2022 accepted proposal, not proof of current implementation. |

The three pinned GitHub revisions were checked using GitHub's commits endpoint with `path`, branch name and `until=2026-10-28T05:59:59Z`; the last is the end of Oct 27 in Mexico City, UTC−06. For SyncSink, the README and Java file have different last-change commits. The web pages were accessed on 2026-10-27. Date and links do not prove that later versions or implementations retain all described behavior.

## Search trail for the exact proposed interactions

The main [technical review](technical-review.md) records the source and comparison beside every mechanism. These are representative reproducible queries, not an exhaustive search and not proofs of absence:

| Mechanism | Search terms used | Closest checked result / outcome |
|---|---|---|
| Validated state and resume | `skill agent runtime checkpoint state validation durable replay langgraph checkpointer` | [LangGraph checkpointing](https://docs.langchain.com/oss/javascript/langgraph/thinking-in-langgraph): pause/resume and state inspection already exist; exact transcript-discard model differs. |
| Prerequisite retrieval | `skill retrieval dependency graph agent skill prerequisites github graph-of-skills` | [GoS repository](https://github.com/davidliuk/graph-of-skills) implements retrieval of prerequisite bundles; household NAS presentation not established. |
| Adaptive exposure | `automatic skill hint vs full instructions progressive exposure agent task context`; `adaptive help progressive disclosure software interfaces context user task assistant` | SkillAlign itself tests skill exposure, and [IBM](https://www.ibm.com/docs/en/technical-content?topic=practices-progressive-disclosure) describes progressive disclosure; exact NAS policy not demonstrated. |
| Executable intervention | `AI agent executable skill program intercept tool calls guardrails approval runtime` | [OpenAI Agents SDK guardrails](https://github.com/openai/openai-agents-python/blob/main/docs/guardrails.md) support tool checks; YoloFS stages filesystem writes. Not identical implementation or universal safety. |
| Event-anchored video | `multimodal search transcript keyframe video evidence timeline`; `Azure AI video indexer insights search exact moments` | [Azure Video Indexer](https://learn.microsoft.com/en-us/azure/azure-video-indexer/video-indexer-search) and [MomentSearch](https://github.com/traversaal-ai/momentsearch) provide related timestamped navigation. Pointing-at-part semantic accuracy not established. |
| Acoustic camera alignment | `audio waveform automatic sync multiple recordings drift software sync open source`; `family archive switch between camera angles automatically sync recordings audio multi camera viewer` | [Final Cut](https://support.apple.com/en-ie/guide/final-cut-pro/ver8798d940/mac), [SyncSink](https://github.com/JorenSix/SyncSink) and [AudioAlign](https://protyposis.net/projects/audioalign/) overlap substantially. Automatic event grouping and consent remain separate questions. |
| Search transcript and play audio | `oral history metadata synchronizer search transcript audio timestamps` | OHMS and [Descript](https://www.descript.com/tools/audio-text) already do synchronized transcript navigation; a cross-file photograph relation is additional and not established by those sources. |
| Event and recording availability | `camera recording timeline coverage gaps monitoring recording missing event review frigate`; `household cameras verify footage coverage gaps event recording search` | [Frigate History](https://docs.frigate.video/usage/history/) and [Review](https://docs.frigate.video/usage/review/) show event-linked recording and shared-time camera grid. No exhaustive coverage inference established. |
| Repair-aware encoding | `FAST 2026 LESS erasure coded storage I/O efficient repair HDFS` and prior sprint FAST sources | [LESS HDFS code](https://github.com/adslabcuhk/less) implements the construction; no actual predictive consumer-NAS UI confirmed. |
| Fault-injected restore rehearsal | `backup recovery rehearsal simulated disk failure test restore application recoverability tool`; `consumer NAS simulate backup restore test isolated recovery` | [Restic check](https://restic.readthedocs.io/en/v0.17.0/047_tuning_backup_parameters.html) and test-restore guidance cover related verification, while CORDS is a targeted research injector. No claim that exact safe full rehearsal does not exist. |
| Staged changes and review | `agent filesystem sandbox preview approve file changes stage commit yolofs` | YoloFS itself implements the core interaction. Other tools provide partial sandbox/diff/approval workflows; semantics differ. |
| Causality-qualified history | `data lake user explore concurrent writes branch commit causality file history` | lakeFS exposes versions, but its 2022 proposal explicitly warns against interpreting its consistency as linearizability; exact provenance interaction not established. |

Search results and living product pages may reflect changes after their original publication; where no defensible publication date was available, they are treated as undated accessible documentation, not as proof of a feature's existence at a historical instant. Search ranking is not reproducible and patents/competitors were not exhaustively examined. Research claims are author-reported and have not been independently replicated.

## UGREEN cross-check

Read installed `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/SKILL.md`, `references/capability-query.md`, and `data/capability-catalog.json` (catalogVersion **2.0.0**, generated 2026-09-01). See [sprint capability audit](../ugreen-unexplored-capabilities.md) for the documented agents, actions, required parameters, side effects and approval labels. The catalog is a local reference; child return summaries and gateway labels do not establish parent-visible formats, complete provenance, safe atomic copy, or live NAS behavior. No undocumented operation was assumed.

## Review boundaries

This is technical reading and source-based reasoning, not a correctness proof of the papers or a code audit. The full paper bodies were available for the arXiv sources and PDF text for the two USENIX papers; the report focuses on methods, worked examples, evaluations and stated limitations, not every appendix equation. SyncSink's separate 2015 article and OHMS server execution were not reviewed. Prior-art checking was targeted and all novelty claims are provisional. No conclusions about market demand, comparable runtime speed, real-user preference or safety under UGREEN hardware follow.
