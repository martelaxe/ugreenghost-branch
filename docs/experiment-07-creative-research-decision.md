# Experiment 07 — creative research decision

Research date: October 26, 2026. **Decision: explore a focused “Knowledge Succession Rehearsal” as the leading candidate, while keeping two alternatives and the existing prototype available.** This is a product hypothesis, not a declaration of a final winner. The proposed exercise asks whether a second person can use the owner's selected NAS notes to complete a specific task and reveals what they still need to ask. If it cannot beat a generic assistant on a useful real-person test, do not force the pivot.

## What the research found

The [user-needs review](../research/07-idea-discovery/user-pain-points.md) records **30 observations** with 40 direct source links, principally independent Reddit threads and GitHub discussions. The [competitive review](../research/07-idea-discovery/competitive-landscape.md) records 41 additional distinct links, including product documentation, vendors, contest materials and a public project page: **81 distinct linked sources across those two core reviews**. Counts are URLs, not independent studies or statistically representative respondents; some accounts rely on search-result excerpts and vendor claims rather than hands-on tests. Additional idea-specific links appear in the detailed reports. Research spans home servers, family photographs, archivists, creators, information management, NAS products and AI tools; English-language technical communities are overrepresented.

The most compelling repeated problems are difficult archive handoffs to less technical family members, scattered aging media and missing photo context, creator assets disconnected from rights or production notes, and fear of unsafe duplicate cleanup. A particularly useful insight: access to a pile of records is not the same thing as knowing how to use it. That is our interpretation of the discussions, not a measured market gap. The [user-needs report](../research/07-idea-discovery/user-pain-points.md) labels repeated reports, isolated anecdotes, workarounds and uncertainties.

## Competition changes the brief

- [Nextcloud Assistant](https://docs.nextcloud.com/server/stable/user_manual/en/ai_assistant.html) documents tool chaining and custom Skills; [Open WebUI](https://docs.openwebui.com/features/workspace/knowledge/) documents source-aware synthesis; [QNAP Qsirch](https://www.qnap.com/en/solution/qsirch-ai-mode) markets semantic NAS retrieval. A generic “AI discovers connections in your files” is not a compelling standalone differentiator.
- [MemoryJam](https://memoryjam.com/) already advertises personalized questions from photos and context, interview transcription and source-grounded archive exploration. Our Conversation Bridge is **nearly identical in its core interaction**, notwithstanding possible NAS integration differences.
- [HomeMemory](https://homememory.ai/) describes a home-maintenance archive combining receipts, manuals, photos and repair history. A generic Repair Memory concept has substantial overlap. These are vendor statements, not independently verified performance.
- [ClaimReady Home Inventory](https://devpost.com/software/claimready-home-inventory) is an individually public UGREEN hackathon entry claiming an evidence-linked inventory across photos, receipts, warranties and insurance records; its page says NAS execution remains unverified. The [official gallery](https://ugreenhackathon.devpost.com/project-gallery) was unpublished during this research, so public entries and existing Skills could not be comprehensively surveyed. It is not evidence that no other entries exist.

## Ideas and shortlist

The [idea universe](../research/07-idea-discovery/idea-universe.md) contains **30 distinct concepts** across practical, unexpected and experimental tiers, plus **10 additional combinations** in the [second wave](../research/07-idea-discovery/unexpected-combinations.md). Some are close neighbors or established concepts in new contexts; counts are not a claim that all are original. The most useful combination is archival records + an actual successor's task: it shifts from “what files do I have?” to “could someone act on them?” Other notable combinations join an attractive reuse opportunity with an explicit rights blocker, and a photo with conflicting contextual notes to prompt a human conversation.

Our five subjective [ranking](../research/07-idea-discovery/idea-ranking.md) candidates, equally weighted across user value, differentiation, NAS fit, UGREEN feasibility and demo impact, are:

1. **Knowledge Succession Rehearsal — 80/100.** Practice a handoff from evidence-backed instructions and expose an unresolved question.
2. **Consent Before Reuse — 76/100.** Pair a creative reuse opportunity with verified restrictions or a clear unknown.
3. **Conversation Bridge — 72/100.** Turn a photo and note into a tentative question for a relative. Its main interaction closely resembles MemoryJam.
4. **Repair Memory — 64/100.** Prepare a grounded appliance handoff; HomeMemory is a close competitor.
5. **Surprise Me — 64/100.** General unexpected findings remain useful but difficult to distinguish from generic agents.

Scores are subjective estimates, with at least ±1 point uncertainty per 1–5 dimension; the small gaps are not statistically meaningful. A closer competitor or a failed NAS return could change the order. [Top-five analysis](../research/07-idea-discovery/top-five-analysis.md) maps each concept to evidence, a concrete demo, a failure case, official agents and the generic-AI baseline.

The three finalists are succession rehearsal, consent before reuse and conversation bridge. The **most surprising plausible demo** may be consent before reuse: the system finds an exciting idea, then the source evidence changes the decision to “hold.” The **most technically realistic** is a text-only succession rehearsal, because it avoids relying on photo-to-document identity matching. Both are judgments, not runtime findings. Full finalist descriptions and skeptical judge critiques are in [finalists](../research/07-idea-discovery/finalists.md).

## What the checks actually establish

The installed catalog names the file, document, knowledge and photo actions used by the finalists and assigns them to experts. A research-only script verified nine action/agent pairs and a negative control: a made-up `ug-video:render-montage` name was not in the catalog. Five local unit tests passed. The local script also generated a [fictional question card](../research/07-idea-discovery/checks/simulated-rehearsal.md) with human-curated source quotes and a carefully worded missing-record limitation.

This checks catalog presence and deterministic artifact handling only. It does **not** test AI generation, logical support, UGREEN expert return envelopes, photo matching, system permissions, real NAS operation, or human usefulness. The full procedures and failure criteria are in [concept tests](../research/07-idea-discovery/concept-tests.md). The prior Surprise Me Skill's static validation remains separate and does not prove that the new concepts run.

The [technical boundary](../research/07-idea-discovery/technical-boundary.md) records official action owners, approval constraints and contest rules. The most important technical unknown is whether real UGREEN expert handoffs provide traceable source identities, usable excerpts, omission signals and consistent completion states across a bounded archive. A NAS device is not itself proof of privacy, complete coverage or a working backup; local versus remote inference depends on actual model configuration.

## Pivot and next experiment

**Substantially redesign the product pitch rather than commit to broad Surprise Me.** Retain its evidence preservation, explicit uncertainty and approval discipline as reusable design work. The existing prototype should remain intact until a replacement is independently tested. The succession rehearsal is a leading hypothesis, not yet a stronger proven product.

Run one **blind human handoff challenge** with a small fictional archive, contradictory note, expected missing record and limited search scope. Give a generic assistant and the future candidate equal access and identical goals; blind the outputs and counterbalance ordering with distinct archives. Ask real potential successors to perform tasks and identify what is unknown. Record completion, source correctness, unsupported assertions, time and preference. Any invented citation, false claim that a missing file does not exist, wrong critical instruction or undisclosed incomplete scope is a failure. Do not claim a competitive improvement if results do not show one. If UGREEN hardware is not available before finalist selection, run the human/generic half now and explicitly leave the UGREEN comparison pending; when access exists, verify actual expert source propagation and state handling.

Round 1 is due November 15, 2026 at 11:45 p.m. Pacific. The documented remote test window gives finalists one assigned day between November 22–28, with the final package and video due November 30 at 11:45 p.m. Pacific. See the [official rules](https://ugreenhackathon.devpost.com/rules) and recheck them before submitting. This research did not produce a proposal PDF, submission ZIP or device demonstration.
