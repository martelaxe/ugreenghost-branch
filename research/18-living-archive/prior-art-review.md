# Prior-art review: narrative adaptation under missing sources

Research date: 27 October 2026. Search terms covered visual-storytelling image replacement, narrative coherence, adaptive digital archives, photo curation, rights-aware asset selection and dynamic storyboards. The three strongest comparable systems below are sources we could inspect, not hands-on evaluations. This is a focused search, not an exhaustive patent or market survey; absence of a match does not establish novelty.

## 1. Monet — semantic photo selection and story remix

Yue Wu and colleagues' [Monet (IEEE Transactions on Multimedia, October 2016)](https://www.microsoft.com/en-us/research/publication/monet-system-reliving-memories-theme-based-photo-storytelling/) groups photos into events, selects representative, diverse images and turns them into a themed edited video. **Overlap:** existing photo collections are automatically selected and made into a visual narrative, so slideshow creation and theme-based selection are not new. **Difference not established:** its public description does not claim a source-evidence ledger that deliberately leaves a historical claim blank after a specific source disappears. We did not test the product or rule out other versions.

## 2. Collaposer — story-driven preparation of visual source material

[Collaposer, CHI 2026](https://doi.org/10.1145/3772318.3791160) reports a pipeline combining detection, segmentation and LLM-based association/grouping to prepare visual assets for collage storytelling, with a user study. **Overlap:** selects and organizes elements from photo collections for narrative use, rather than a generic photo sorter. **Possible residual:** our proposed change-of-eligibility interaction asks whether a changed visual story remains historically justified; the reviewed account does not establish that precise operation. The publisher page was accessible via indexed search but direct DOI open returned 403; we rely on its indexed primary abstract, not a full independent replication.

## 3. Publish-Safe Photo Review — the same NAS event

[Publish-Safe Photo Review](https://devpost.com/software/publish-safe-photo-review) is a public Round 1 UGREEN entry that proposes sorting event photos by documented publishing constraints and creating an approved album. Its author says it has not run on NAS. **Overlap:** user-selected photo collections, possible exclusion for use, NAS photo agent and an approved output. **Possible residual:** this experiment asks how an explicitly recorded narrative changes when a source becomes ineligible, including weakening a claim or showing a gap. We found no claim that the entry performs this precise source-to-narrative version comparison, but lack of a documented claim is not proof it cannot.

## Other relevant competitors and limits

[Runway Story Panels](https://help.runwayml.com/hc/en-us/articles/50985233945747-Story-Panels) produces additional generated visual shots from a source image and prompt. It is an adjacent visual storytelling product rather than evidence-preserving selection from unchanged archive photographs. [Story-oriented Image Selection and Placement](https://pure.mpg.de/rest/items/item_3187969_1/component/file_3187970/content) already studies choosing and placing images for a story. [Script to Selects](https://devpost.com/software/script-to-selects) describes a UGREEN scene-based album workflow. A conventional curator or generic AI can also perform these adaptations.

**Verdict:** source-specific narrative state, visible gaps and explicit change tracking may improve the interaction, but those properties are not proven unique; our few synthetic constraints, preformatted results and lack of user testing do not establish novelty or user benefit. We did not identify any source proving that this exact combination is globally absent.
