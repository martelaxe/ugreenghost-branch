# Twelve invention hypotheses

These are hypotheses, not prototypes. “UGREEN” means a documented expert operation exists, not that a parent can receive the right data or that a real device has executed it. Paths and permissions must come from the user. Details in [capability audit](ugreen-unexplored-capabilities.md). Inspiration and competitor links are concrete; user demand beyond the sources is speculative. We deliberately keep distinct outcomes rather than twelve versions of a document search.

## 1. Wild: The same minute, many cameras
- **Concept / request:** “Show me this birthday from every recording at the same instant,” without manually syncing clips.
- **Observable result:** a multi-angle view; switching camera preserves the shared moment. Sound alignment estimates offsets; source originals and uncertainty remain visible.
- **Mechanism / difference:** audio waveform or fingerprint alignment and synchronised playback, not semantic text generation. A shared household archive could discover potential takes, but generic AI with media tools could also do it.
- **Prior art / research:** [Final Cut audio sync](https://support.apple.com/en-ie/guide/final-cut-pro/ver8798d940/mac), [SyncSink](https://github.com/JorenSix/SyncSink), [US8111326B1](https://patents.google.com/patent/US8111326B1/en). The technical behavior already exists; no global novelty claim.
- **UGREEN fragment:** `media-agent` searches authorized media, `file-agent` retrieves metadata; actual playable formats and return values unknown. **Missing:** waveform extraction/correlation, simultaneous synchronized player, visual interface, cross-user access handling; cannot build central feature as documented Skill.
- **Disproof:** editors or an existing self-hosted app can ingest unsorted family clips, identify the event and switch angles with equal ease; or recordings lack common usable sound. Consumer need unvalidated.

## 2. Bridge: Hear the picture
- **Concept / request:** “Find the recording where my grandfather explains this handwritten recipe, and show the original card next to the relevant words.”
- **Observable result:** one selected audio source and a cited transcript excerpt paired with the actual selected picture; a confirmation or honest no-match, not a fabricated audio timecode.
- **Mechanism / difference:** link transcript passage and visual text using a corroborated shared marker (e.g., a recipe name and ingredient); examine misleading matches. If offered as a runnable playback-at-time experience, it needs a real timestamp and verified player, neither documented as guaranteed.
- **Prior art / research:** [OHMS](https://journal.code4lib.org/articles/10643), [Descript](https://www.descript.com/tools/audio-text), [EM²Mem](https://arxiv.org/abs/2609.00551); related to 18's photo curation and 07's conversation bridge, but the candidate specifically joins independently stored audio and a physical image. This may be just multimodal search.
- **UGREEN fragment:** `knowledge-agent` audio transcription, `photo-agent` OCR, `file-agent` bounded list; parent synthesizes only actually returned excerpt and photo source. **Missing:** guaranteed timestamps, sample-level verification, synchronized UI and proof audio or image matching is accurate. No actual UGREEN test.
- **Disproof:** generic Codex with same actual audio transcription and OCR returns the same verified pairing; or the recording does not identify the card, making a confident match unjustified. Demand is inspired by oral-history effort, not verified for this interaction.

## 3. Practical wildcard: Live Photo survival check
- **Concept / request:** “Before I stop using the old library, did these ten moving photos survive as moving photos?”
- **Observable result:** a side-by-side source/destination check of known still/motion components and relevant sidecars: evidenced present, missing from checked scope, or unknown. Do not claim app-level playback succeeded.
- **Mechanism / difference:** compare compound-object components and captured evidence, not file count or a generic summary. This tests *representation continuity* after migration, unlike 16's recovery of one file; hashing verifies bytes, not pair identity.
- **Prior art / research:** [Immich XMP](https://docs.immich.app/features/xmp-sidecars/), [Immich #22601](https://github.com/immich-app/immich/issues/22601), [PhotoPrism sidecars](https://docs.photoprism.app/getting-started/faq/); see [migration checker](https://photoproof.kitforma.com/) whose publication date and practical performance were not verified. Some migration verification already exists.
- **UGREEN fragment:** file listing, stat/hash, metadata lookup; **missing:** guaranteed EXIF pair identifiers, app database or export semantics, automatic Live Photo playback. Use only a user-provided explicit component mapping unless a returned metadata field establishes pairing.
- **Disproof:** source component association is unavailable or the actual destination app stores the media differently, so file-level comparison cannot answer the user's question. Narrow need evidenced by one bug and docs, not measured demand.

## 4. Event vs footage gap card
- **Concept / request:** “I got a camera alert at 3:10; what evidence is available around it?”
- **Observable result:** a bounded event list, available evidence references and a visibly unknown area when retention cannot be established.
- **Mechanism:** separately track detection and actual footage availability; no detection is not no event. **Prior art:** [Frigate history](https://docs.frigate.video/usage/history/) already does event-to-recording navigation; [issue](https://github.com/blakeblackshear/frigate/discussions/16823) shows confusion.
- **UGREEN:** authorized `security-monitor-agent` cameras, timeline and event-evidence; **missing:** complete recording inventory, actual playable references/retention/coverage. **Disproof:** ordinary UGREEN or Frigate UI already communicates the same evidence and gaps, or event-evidence does not surface useful references. Privacy and consent essential; no face identification needed.

## 5. Accessibility: subtitle handoff without silent download
- **Request/result:** “Find subtitles for this selected film and tell me which one I can inspect.” Returns available language/ID/source if actually provided; downloading only after explicit approval and gateway success.
- **Mechanism:** pair an accessible playback need with qualified matching and approval, avoiding unverified language/sync claims. **Prior art:** [Plex subtitle search](https://support.plex.tv/articles/subtitle-search/) already does this, so this is mostly existing functionality.
- **UGREEN:** `media-agent` subtitle-search/download, actual playback conditional. **Missing:** guaranteed match correctness, private/offline source and safe file semantics. **Disproof:** Plex/UGREEN built-in already handles it; likely ordinary. Need is plausible, not tested locally.

## 6. Sidecar naming translator
- **Request/result:** “Will my selected XMP files be recognized by this destination library?” For each user-selected pair, demonstrate the destination's documented naming rule and flag mismatches; no automatic rename.
- **Mechanism:** destination-specific import rule applied to actual paths, different from global organizer. **Prior art:** [Immich XMP docs](https://docs.immich.app/features/xmp-sidecars/) and existing import tools. **UGREEN:** file listing/read and optional document extraction; **missing:** reliable XML semantics, app index/state and universal mappings. **Disproof:** library already displays the same actionable import diagnostics, or the library version's rule differs. User need supported by metadata discussion, no market size.

## 7. Spoken-workshop cross-check
- **Request/result:** “While I repair this object, find the recorded explanation and the drawing for the same labeled component.” Present source audio excerpt, photo OCR label and uncertain correspondence; never claim safe repair.
- **Mechanism:** corroborate a task-specific item across speech and image, then direct attention to original sources. **Prior art:** [OHMS](https://journal.code4lib.org/articles/10643), [Nextcloud Assistant](https://docs.nextcloud.com/server/stable/user_manual/en/ai_assistant.html). **UGREEN:** transcription + photo OCR + file retrieval; **missing:** verified instructional correctness and video playback. **Disproof:** same tool-equipped generic model performs equivalently; no real repair users tested. Closely related to 2 but targets working with a physical procedure rather than memorial retrieval; competition between them should retain only one.

## 8. Where did the recording go?
- **Request/result:** “Why does this alert have no playable recording?” Show only returned references, searched time/camera, warnings, and clearly separate possibilities (retention/configuration/access), without diagnosing an unobserved cause.
- **Mechanism:** distinguish possible failure mechanisms from proof in event-linked sources. **Prior art:** [Frigate troubleshooting](https://docs.frigate.video/troubleshooting/recordings/). **UGREEN:** event-timeline/evidence; **missing:** retention, config, segment inventory and system logs. **Disproof:** no additional facts are available beyond an empty reference or built-in UI already explains it. One user report, not verified demand.

## 9. Listening-room language rehearsal
- **Request/result:** “Find short samples in my authorized recordings containing this phrase, then help me listen and practice.” It returns real excerpts with sources; playback only upon explicit action if a playable media identifier is returned.
- **Mechanism:** oral practice with primary recordings, not merely transcription; personally owned dialect recordings are a plausible NAS-specific collection. **Prior art:** [Descript synchronized transcript](https://www.descript.com/tools/audio-text). **UGREEN:** audio transcription and media control; **missing:** verified timestamp linking, automatic phrase loop, speech assessment. **Disproof:** parent cannot connect transcript to playable track, or generic transcription players already give same experience. User interest speculative.

## 10. Soundtrack with a stop rule
- **Request/result:** “Play the family playlist for 20 minutes, then stop.” Observable event is playback and the scheduled stop, only after user explicitly requests action.
- **Mechanism:** native stateful media control (`stop-after-minutes`), not an invented file analysis. **Prior art:** ordinary sleep timers and music apps; almost certainly already implemented. **UGREEN:** music search/control; **missing:** verified library IDs, semantics, playback state and actual stop. **Disproof:** built-in music player already does it. Clearly useful action but unlikely competition differentiator; demand speculative.

## 11. Temporary event evidence bundle
- **Request/result:** “For my selected camera and two-hour interval, collect the available event references for my own review.” List actual event IDs and time-limited evidence references with expiration only if returned.
- **Mechanism:** scoped ephemeral references plus explicit authorized purpose; not a permanent identity graph. **Prior art:** [Frigate event review](https://docs.frigate.video/usage/history/) and mainstream NVRs. **UGREEN:** cameras/timeline/evidence `ttl-sec`; **missing:** verified TTL enforcement, export, link usability and consent semantics. **Disproof:** references are unusable in parent response or the existing UI already provides the bundle. No facial identity required; user need not measured.

## 12. Verified procedural checkpoints
- **Request/result:** “Help me run this recurring archival intake, and show which checkpoint remains unverified.” After each selected step, present an actual observation and the next action; no silent continuation after failure.
- **Mechanism:** explicit state transitions with validation, inspired by [SKILL.state](https://arxiv.org/abs/2608.26263) and [HASP](https://arxiv.org/abs/2605.17734). Closest project ancestor is 14 Task Handoff; its actual new claim requires machine-enforced transitions rather than a handoff document.
- **UGREEN:** can request expert results and report completion; **missing:** validated durable state store and runtime interception; Markdown is advisory. **Disproof:** failure injection bypasses the checkpoint or generic agent follows same process. Not a realistic autonomous Skill claim and no new user demand shown.
