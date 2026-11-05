# Three finalists and skeptical review

These are three meaningfully different user experiences, not three generic discovery skins. Ranking and descriptions are hypotheses; no real user or real NAS has validated them. Full evidence, score rationale, and technical mappings: [user needs](user-pain-points.md), [landscape](competitive-landscape.md), [ranking](idea-ranking.md), and [top-five analysis](top-five-analysis.md).

## 1. Knowledge Succession Rehearsal — best balance and safest delivery

**Concept:** A selected-archive practice session: “If I were unavailable, could someone else carry out this specific task using the notes we already have?” Output a short task card, source-backed facts, contradictions, and explicit questions for the owner. A real person rehearses; the assistant does not certify readiness.

**Demand:** Self-hosters describe family access and disaster handoff worries in multiple discussions ([critical data access](https://www.reddit.com/r/selfhosted/comments/1ppne5l/how_do_you_handle_access_to_critical_data_for/), [disaster plan](https://www.reddit.com/r/selfhosted/comments/1i2x3bc)). The proposed rehearsal is unvalidated.

**Originality:** The central output is a challenge designed for a second person, not a file list. Legacy products such as [OneDrive](https://support.microsoft.com/en-gb/onedrive/preserve-your-digital-legacy-with-onedrive) address access; an AI assistant can already generate exercises. We did not find a close match for the exact role-play in our limited scan, which does not establish global novelty.

**NAS / technical:** File discovery (`file-agent`), reading (`document-agent`), evidence (`knowledge-agent`) draw on an authorized archive the owner maintains. Actual citations, scope and privacy are unverified; a mounted NAS folder may give generic Codex equivalent access. The core needs no writes or custom backend.

**Three-minute demo:** A fictional small handoff folder; a second person tries to locate a spare and identify the correct contact; sources appear; a referenced recovery note is not retrieved and is explicitly marked unknown; owner identifies the next question. A text artifact can be shown without NAS but is not runtime proof.

**Risk / next test:** Wrong steps could create dangerous overconfidence. Test with actual people, unambiguous fictional records, conflicting instructions, missing records and a generic-agent baseline; enforce critical-error failure criteria. Separately test expert returns on a real NAS.

## 2. Consent Before Reuse — strongest unexpected practical twist

**Concept:** A creator asks what stored assets might fit a new brief. The Skill proposes at most a few grounded candidates and places each relevant rights restriction or unresolved release beside it; the safe next action is human review, not publication.

**Demand:** Photographers describe difficult image/release matching ([event photography](https://www.reddit.com/r/photography/comments/1t1m32l/event_photography_your_workflow_re_releases_for/), [museum workflow](https://www.reddit.com/r/MuseumPros/comments/1w4pc27/photo_releases/)). Adobe Stock already imposes [release documentation requirements](https://helpx.adobe.com/in/stock/contributor/content-policies-guidelines/model-property-releases/model-release-requirements.html), and rights-aware DAM workflows exist.

**Originality:** The memorable change is an enticing reuse idea visibly blocked by a source. This is a combination and a presentation choice, not a novel rights system. Automatic legal clearance is excluded.

**NAS / technical:** `photo-agent` metadata/search, `document-agent` extraction and `knowledge-agent` evidence; photo-to-rights matching, per-file source provenance and permissions remain unverified. Text output only, with human-confirmed asset identity. A generic multimodal assistant can compare the same files.

**Demo:** Show a fictional image, a relevant proposed use, a matching clause forbidding it, and a hold card asking the creator to check alternative permissions.

**Risk / next test:** A missed restriction can mislead a user, and false identity matching may produce a wrong release. Test a same-name/different-person conflict and an absent release; no “cleared” status without direct support and human review. Compare with a DAM and generic assistant.

## 3. Conversation Bridge — creative and emotionally memorable, but crowded

**Concept:** Use an image and a related family note to generate a specific open question for an actual relative, foregrounding alternative interpretations and sources. No fabricated answer, identity, voice or date.

**Demand:** [Unlabeled photo discussions](https://www.reddit.com/r/Genealogy/comments/1wbr7gq/anyone_else_inherit_a_box_of_family_photos_with/) and [lost photo context](https://www.reddit.com/r/Genealogy/comments/1ubnb7n/how_do_you_keep_the_story_attached_to_scanned/) illustrate the problem.

**Originality:** [MemoryJam](https://memoryjam.com/) already offers AI questions from photo/context and source-grounded archive exploration. Thus the central idea is **nearly identical**; using a household's existing UGREEN archive may reduce setup but is unproven and not exclusive. This is a serious reason not to select it without a sharper differentiator.

**NAS / technical:** `photo-agent` vision/metadata, `document-agent` extraction and `knowledge-agent` evidence; audio is optional and not part of the minimum. UGREEN image formats, IDs and cross-expert references require a real test.

**Demo:** Show a fictional photo and contemporaneous note with a possible date conflict, then ask a relative an open question with both sources visible. The meaningful result is the person's response, not synthetic history.

**Risk / next test:** Avoid false person identification, emotional assumptions and unauthorized disclosure. Test unrelated same-date items, photo/note mismatches and family feedback; compare directly with MemoryJam and generic multimodal AI.

## Skeptical judge's review

| Question | Succession rehearsal | Consent before reuse | Conversation bridge |
|---|---|---|---|
| Why interesting / who uses it? | A family member or successor discovers a concrete knowledge gap before a handoff. | A creator finds a tempting resource but also the constraint that changes the decision. | A relative sees a specific prompt for a conversation they might otherwise miss. |
| Why not normal AI? | It can do it; hypothesized advantage is low-friction authorized NAS scope and a reusable safety contract. | It can do it; native photo and document integration may reduce preparation. | It can do it; potential convenience is existing library access, subject to MemoryJam overlap. |
| Wrong inference? | Wrong contact or procedure could create false readiness; show exact sources, contradictions, and no credential handling. | False clearance could cause unauthorized use; hold unclear assets and require human review. | Wrong identity/date could distort a memory; phrase as a question and identify uncertainty. |
| Is this already a feature renamed? | Access products and generic AI are established; specific role-play differentiation is a hypothesis. | Rights management and creative search are established; side-by-side opportunity and blocker need proof of value. | MemoryJam's marketed workflow is nearly identical; ordinary prompt wording is not defensible novelty. |
| One-day NAS test risk? | Lowest of the three: document-only, but real source returns still unknown. | Higher: cross-modal asset/contract identity and return details. | Higher: photo vision, image context and source handoff. |
| Memorable moment / likely rejection? | Novice hits a missing instruction; rejection if it is just a generic checklist. | A desirable image becomes a hold; rejection if it overstates clearance or duplicates DAM. | A real relative answers a photo question; rejection because MemoryJam already does it. |
| Deadline / improvement | Small Skill plausible for Round 1; test a novice and compare generic baseline. | Round 1 plausible; limit to a small fictional dataset and a conservative gate. | Round 1 plausible but higher runtime risk; directly compare with existing products before commitment. |

**Recommendations:** Safest and best balance: **Knowledge Succession Rehearsal**. Most creatively ambitious plausible direction: **Consent Before Reuse**, because it combines creation with a source-grounded obstacle and a clear decision; its originality is not established. Conversation Bridge is the most immediately emotional demo, but MemoryJam's near-identical product makes its competitive claim weak. **Substantially redesign Surprise Me** into a specific user-facing exercise or decision; preserve its evidence, uncertainty, bounded scope and approval safeguards as reusable methods. Do not discard the existing prototype until a new concept outperforms the baseline on a meaningful test.
