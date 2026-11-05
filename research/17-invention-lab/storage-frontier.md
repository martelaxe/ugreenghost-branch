# Storage frontier — checked 27 October 2026

## Agent-native filesystem

**Don't Let AI Agents YOLO Your Files**, Shawn Zhong, Junxuan Liao, Jing Liu, Mai Zheng, Andrea C. Arpaci-Dusseau and Remzi H. Arpaci-Dusseau, April 2026, [Microsoft Research](https://www.microsoft.com/en-us/research/publication/dont-let-ai-agents-yolo-your-files-shifting-information-and-control-to-filesystems-for-agent-safety-and-autonomy/), [system and reported experiments](https://yolofs.github.io/). YoloFS is an implemented Linux filesystem that stages changes, snapshots, and gates sensitive access; authors report correction in 8 of 11 hidden-side-effect tasks. A future personal NAS could represent an agent's attempted action as a reviewable branch. The mechanism is a filesystem plus control infrastructure, not an LLM promise or a UGREEN capability.

## One store as memories and procedures

**Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability**, Sizhe Zhou et al., 29 July 2026, [arXiv](https://arxiv.org/abs/2607.26637). Authors evaluate management/search/execution agents on growing stores. Organized memory roughly halves search cost in large stores but did not itself improve answer quality in their tested conditions; most managers' organization degraded. A useful interaction would expose *which memory is safe to reuse* rather than quietly trusting a folder hierarchy. This requires memory management/tool infrastructure for their experiments; a static instruction alone does not reproduce them.

**Multimodal Filesystem Memory For Long-Horizon Embodied Agents**, Chloe Su et al., 15 October 2026, [arXiv](https://arxiv.org/abs/2610.22686). MFM stores episodic, spatial, semantic and procedural memories linked back to original observations. Authors report improved Minecraft and KiCad outcomes across three models. It implements an agent architecture and multimodal storage, not merely summaries. A household artifact could let a person replay a procedure while revisiting the original visual evidence; the model's interpretation could still be wrong.

## Archival provenance and redaction

**From File Systems to Knowledge Graphs: A Multi-Phase Workflow for the Description of Born-Digital Literary Archives**, Lucia Giagnolini and Paolo Bonora, 15 September 2026, [Semantic Web](https://journals.sagepub.com/doi/10.3233/SSW260020). Their implemented archival pipeline combines metadata, hashes, RDF, provenance, curation and selective redaction; it reports 61 million triples for a 78,211-file archive. It establishes that file layout and provenance can become queryable archival evidence, not that current consumer NAS automatically knows relationships. NAS idea: a story whose individual beats retain sources and become unavailable when an input changes; enforcement and accurate provenance require new infrastructure.

## Branches, versions and recomputation

[lakeFS documentation](https://docs.lakefs.io/) describes isolated branches, commits and atomic merges over object storage; [DataLad](https://www.datalad.org/index.html) documents versioning data using Git and git-annex; [Snakemake rules](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html) describe dependency-driven workflows and data-dependent checkpoints. These are implemented systems with their own runtimes. A personal archive could offer a **what-if projection**: declare one input ineligible and recompute an artifact without changing source bytes. Git/lakeFS branches and build systems already exist, so the speculative novelty would be a consumer semantic request, verified substitutions and graceful gaps—not branching or recomputation itself.

## Content capabilities and user-controlled sharing

[Tahoe-LAFS capability architecture](https://github.com/tahoe-lafs/tahoe-lafs/blob/master/docs/architecture.rst) defines read, write and verify capabilities with cryptographic properties; recipients of transferred secrets may retain access, and prior disclosure cannot be recalled. These are real systems, not claims of revocable plaintext. A more ambitious NAS object might expose only approved *operations* on data, with revocation for future interactions, mediated by a trusted boundary. This needs real identity, enforcement, isolation, audit and leak protection; no prompt or local toy broker provides them.

## Existing AI context

[Nextcloud Assistant](https://docs.nextcloud.com/server/stable/user_manual/en/ai_assistant.html) already chains tools and supports Skills. [UGREEN Model Manager](https://ai-ca.ugreen.com/pages/notice-on-model-manager) describes local semantic document indexes and summaries. Do not claim a semantic folder, agent memory, search or file-aware chat is unprecedented. Evidence for each product is documentation rather than a hands-on comparison.
