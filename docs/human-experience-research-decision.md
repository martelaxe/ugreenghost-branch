# Finding the experience, not the tool combination

Research date: 2026-10-27. **Recommended direction: let someone continue an unfinished physical creation while distinguishing the original maker's documented choices from the new maker's own decisions.** This is a proposal to investigate, not a proven novel product or an established hackathon winner. It came from people already doing this for family members, not from a UGREEN API list.

The clearest example is a [quilter who wants to finish her grandmother's unfinished quilt for her father](https://www.reddit.com/r/quilting/comments/1wihcv7/last_quilt_of_my_grandma/). She says the quilt has **no written plan for the center**. Another [inheritor is unsure whether to frame or continue older quilt blocks](https://www.reddit.com/r/quilting/comments/1uvipkn/help_wanted_on_inherited_unfinished_quilt/) without changing original work. A different [quilter describes actually finding a handwritten finishing note](https://www.aquiltinglife.com/grandmas-quilts/). These are separate cases: we must not pretend that the first person's grandmother left instructions.

**Biggest unresolved obstacle:** the interesting experience depends on the system reliably distinguishing an actual, relevant source from an inference—and on a person finding that distinction useful while working on a real physical object. UGREEN's visual interpretation, evidence references and multi-agent handoffs are unverified. If no authentic note or relevant image exists, the only honest result is to ask the person to decide. Generic Uliya may already do that as well. A missing source cannot be turned into a deceased person's intention.

## What the research actually found

The [ten situations](../research/human-experiences/01-human-situations.md) include family quilters, genealogy researchers, people who keep field recordings, family-video editors, songwriters, educators and amateur-radio operators. The strongest patterns are people wanting to **continue someone else's work**, hear an original voice, enjoy recordings instead of endlessly organizing them, and bring personal history into a present-day human activity. These are mostly self-selected individual accounts, not proof of widespread demand or willingness to use an AI product.

Our strongest counterexamples matter just as much:

- [Queens Memory](https://www.queensmemory.org/memories-of-migration-making-a-talking-family-story-quilt/) actually ran a workshop where people made quilts with buttons playing recorded stories. A talking quilt is **already an implemented experience**.
- [CSUN's oral-history exhibit](https://libary.csun.edu/virtual-exhibit/PP/differing-perspectives) presents paired clips and transcripts of different witnesses to the same event. A two-voice comparison already exists.
- [Porter une marche](https://walklistencreate.org/walkingpiece/porter-une-marche/) describes a participatory artwork where people listen to another person's recorded walk while walking. A recorded-walk exchange is not new merely because it uses a NAS.

Those complete interactions were rejected as new flagship ideas. We did not reject the remaining possibilities merely because they use existing OCR, audio or human conversation; the remaining question is whether their **whole experience** materially differs from what people already do. Full prior-art and competitor qualifications are in the [five hypotheses](../research/human-experiences/02-experience-hypotheses.md).

## The three strongest experiences

### 1. Continue a maker's unfinished work

**Experience:** A person brings an actual partly made quilt to the table. They choose a related photo and note in Uliya. The assistant quotes what the note really says, then asks the person to choose how to handle a part where the maker's intent is unknown. The person places a fabric piece or decides to leave it untouched. The observable result is a **human action on a physical work**, with an explicit boundary between supported original choices and new choices.

**Prior art:** [Loose Ends](https://looseends.org/faqs) already matches human volunteers to finish projects and helps identify patterns; its [community case reports](https://egausa.org/community-spotlight-the-loose-ends-project-preserving-crafters-legacies/) demonstrate the human outcome. A volunteer may already achieve the same thoughtful handoff. The proposed difference is a reusable, user-controlled interaction that keeps the source of each design decision visible *while the person works*. We did not establish that this complete interaction is absent elsewhere or that it is more useful than a person and the original note.

**UGREEN approximation:** `photo-agent` can be asked for `ug-photo:vision-vlm` or `ug-photo:vision-ocr` on a selected image; `document-agent` can be asked for `ug-document:qa` or `ug-document:extract` on an authorized document. The parent can quote actual returned evidence, request clarification and present the user’s options. Exact visual interpretation, source references, handoff and display are **unverified**; a photo is not sufficient to establish craftsmanship or intention. There is no documented live camera, physical-work tracking, overlay, guarantee of step accuracy or automatic file save. The user remains responsible for the physical decision.

**60-second Uliya demonstration:** A person holds an unfinished sample and selects a photo plus a note. They ask, “What did the maker actually specify, and where do I get to choose?” Show a real returned note excerpt. The person chooses their own material for an unspecified section and places it beside the original. If the note does not specify a choice, Uliya says **unknown** instead of inventing an answer. No completed quilt or NAS execution is implied by this storyboard.

**Previous experiments:** Experiment 09's Creative Salvage proposed new uses from fictional notes; Experiment 17's One-Bit Workshop asked for a user response to guide a physical step; Experiment 16 recovered one missing file. This hypothesis's proposed difference is a real existing physical object, a provenance boundary between two makers, and an observable human choice. That is a narrower interaction, not evidence that it is a new capability or that those prior ideas failed to anticipate it.

### 2. Carry a radio tradition into a new conversation

**Experience:** A radio enthusiast chooses an old QSL card and an authorized station log, checks what they genuinely say about a previous call-sign holder, then chooses what—if anything—to say in a present-day conversation. The user can listen to a confirmed original recording if available; the NAS never invents the former operator's voice or transmits.

**Prior art:** The [ARRL's call-sign-history and memorial archive](https://www.arrl.org/news/national-silent-key-archive-lives-on), [Smithsonian QSL collection](https://americanhistory.si.edu/collections/archival-collection/sova-nmah-ac-1669) and [ARRL commemorative activities](https://www.arrl.org/arrl-heritage-museum) already support or demonstrate remembrance, record use and live tribute. [QSOrder Search](https://qsorder.hamradiomap.com/) describes search/playback of call-sign recordings, but its current implementation was not verified. Radio operators can perform the entire human practice without AI. The possible difference is scoped help connecting *this person's own* card, log and voluntary next conversation, with visible uncertainty. The actual [operator who found an older message](https://www.reddit.com/r/amateurradio/comments/1vzcbei/final_message_from_the_guy_who_had_my_callsign/) did not ask for this product; its desirability and distinctiveness are speculative.

**UGREEN approximation:** `photo-agent` `ug-photo:vision-ocr` on a chosen card; `document-agent` `ug-document:qa` or `extract` on an authorized log; optional `media-agent` `ug-music:search` for a user-confirmed indexed recording. Same call sign does **not** establish the same person or time; playback of an arbitrary audio path and source-ID handoff are not guaranteed. A human chooses any later radio interaction; no radio-transmit action or automatic communication is documented.

**60-second Uliya demonstration:** Show a real or clearly labeled fictional card and selected log, ask what can responsibly be said about the past holder, and show actual returned dated evidence plus an uncertainty. If a confirmed original recording plays, hear it; otherwise show the failure. The hobbyist decides their own words for a later conversation. Do not stage an on-air call as a NAS operation.

**Previous experiments:** Unlike Experiment 19's reconstruction of a past decision, the intended endpoint is a new, voluntary social interaction. The evidence matching is still ordinary archive reasoning, and the radio context does not itself make it original.

### 3. Answer an old creative fragment with a new performance

**Experience:** A person selects one unfinished voice memo and an associated note. They listen to the original, then sing, tap or play a response and decide if they want to continue. The NAS does not generate a song or record them. A [songwriter discussion](https://www.reddit.com/r/Songwriting/comments/1kmq3l0/whats_the_most_amount_of_unfinished_songs_youve/) and a [field-recording discussion](https://www.reddit.com/r/fieldrecording/comments/1kw7kc7/how_do_you_store_your_recordings_that_make_it/) support the existence of unused recordings, not demand for this specific exercise.

**Prior art:** [Splice Bridge](https://support.splice.com/en/articles/8652855-what-is-splice-bridge) documents auditioning samples in a DAW; musicians already play in response to recordings. [AudioTools](https://mashav.com/sha/praat/scripts/AudioTools_CallResponse.html) describes interactive co-improvisation, and [UnStrander](https://www.unstrander.com/) advertises helping musicians revisit voice memos. We did not run those products; the latter descriptions are claims, not proof. A personal-context prompt may be a different combination, but this could be indistinguishable from pressing play in an audio workstation.

**UGREEN approximation:** `document-agent` `ug-document:qa`/`extract` reads a selected note; `media-agent` `ug-music:search` can request a confirmed music-library item and `ug-music:control` can pause or stop it. No documented instrument recording, adaptive response, signal analysis, tempo synchronization or generated audio. Path-to-playable-item mapping is unverified. Without actual playback, the experience is only a suggestion to open a file.

**60-second Uliya demonstration:** Select the original sketch and note, show a real returned instruction or limitation, confirm the playable item, and let the user play or sing a response after hearing it. If playback fails, say so; do not substitute edited audio. The performance is not captured by UGREEN.

**Previous experiments:** Experiment 09 already tried to repurpose abandoned creative work, with generic AI finding comparable ideas. This proposal changes the endpoint to **listening and personally performing**, rather than an AI-generated creative plan; its superiority and surprise have not been tested.

## Recommendation and the test that matters

Explore **continuing an unfinished physical work**, but do not build or submit a Skill yet. It best connects a NAS archive to an action a person cares about in the present. The close human alternative is also its hardest test: give a willing maker a real unfinished item and whichever genuine notes they authorize. Ask them first to decide the next step with the original materials alone, then with a source-qualified assistant, varying order across people if feasible. Ask whether the assistant exposed an overlooked **specific** choice, preserved uncertainty and changed a decision; compare it with a knowledgeable human helper. If it only restates the note or invents the maker's wishes, stop. Separately, on actual UGREEN hardware, verify the real photo/document returns and whether citations can be carried between experts.

This is a recommended *research direction*, not evidence that a personal NAS has a unique new interaction. No prototype, Skill, PDF, ZIP, user contact or NAS run was made during this research.
