# Three creative Uliya workflows — decision

**Verdict: NO STRONG CANDIDATE.** The most promising interaction is a one-time camera-evidence check that can pause the current film, but it is closely related to existing smart-home automation. The other two are substantially covered by existing products and are constrained by unverified media handoffs. They are worth understanding as candidates; none has shown a compelling advantage over generic Uliya or warrants a submission claim yet.

Reviewed 2026-10-27: the [machine catalog](../research/ugreen-capabilities/02-operation-catalog.json), [composition graph](../research/ugreen-capabilities/04-composition-graph.md), [prior originality check](../research/ugreen-capabilities/09-originality-check.md), [previous walkthroughs](../research/ugreen-capabilities/10-end-to-end-walkthroughs.md) and installed `uliya-skill-kit` capability/orchestration references. Live searches checked the user outcomes, not invented names. Each sequence below is a **hypothetical, one-time user-requested interaction**, not a NAS transcript or successful deployment. The parent delegates to the named owning experts, and only actual returned data can be passed onward. For every sequence: `waiting_user` and `waiting_approval` are pending, not success; `failed` and `cancelled` stop dependent actions; incomplete or inaccessible results are disclosed. Platform permissions and real results are unverified.

## 1. A film pauses when a recent package event matters

**Exact user request:** “I'm watching a film. Check my front-door camera for package events in the last ten minutes. If you find one, pause the film and show me the available event evidence. If the result is unclear, leave the film alone and tell me what you could check.”

**Execution path.**

1. The user authorizes the particular camera, time range and player and explicitly requests the conditional pause. The parent sends a self-contained instruction to **`security-monitor-agent`**, which can use `ug-surveillance:cameras` to resolve a real authorized camera and `ug-surveillance:event-timeline` with required `start-time` and `end-time` and the optional `topic=Package`, camera and limit filters. These actions are cataloged `read/none`.
2. The parent acts only on a successfully returned event relevant to that requested scope. If a usable actual event identifier is returned, the same expert may request `ug-surveillance:event-evidence` with that `event-id` and an available `evidence-type` such as `snapshot` or `clip`. The catalog describes evidence references, not a guaranteed viewable image or video.
3. If the event result meets the user's condition, the parent delegates to **`media-agent`** for `ug-video:control`, `operation=pause`. It is cataloged `state-change/none`: the initial user request authorizes this specific conditional pause, but `none` is not general permission to control a player. If the camera query is ambiguous, failed, capped without a usable matching event, or returns no usable evidence, do not infer that a package is present. An absent event does not establish that no package arrived.
4. Only report a pause after the media expert actually returns completion. Present the actual event reference if usable; otherwise say that the pause and the requested visual evidence have different statuses.

**Observable result and surprise.** A film that is already playing could actually pause after a one-time evidence query. The surprising part is that one NAS domain changes another in response to a user-specified condition. It is more than returning a camera search result, but does not change the camera or schedule future monitoring.

**Uncertain handoffs and runtime.** The catalog does not guarantee `cameras` identifier compatibility with `event-timeline`, an event-ID field or its mapping into `event-evidence`, playable clips, freshness or full coverage, parent-visible confidence/metadata, current player targeting, actual `pause` feedback, or resumption after interruption. The catalog does not expose a trigger that continuously watches the camera. Detection can be a false positive; the presence of an event is not proof that the package is still there. If the result is unclear, no pause should be asserted or initiated under the stated request.

**Closest prior art.** [Frigate's Home Assistant guide](https://docs.frigate.video/guides/ha_notifications/) documents event-driven notifications and access to event evidence; [Home Assistant](https://www.home-assistant.io/actions/media_player.media_pause/) documents pausing media in response to automations and includes a doorbell example. Together these already enable closely related cross-device behavior, and can perform ongoing automation that the documented UGREEN Skill cannot. This is a composition of existing behavior, not a new technique.

**Faithful 60-second Uliya demonstration.** A real film is already playing; the user issues the exact one-time request with an authorized camera and actual bounded time range. Show the actual returned camera result, then the actual player pause only if the query supports the condition. If a real event-evidence reference opens, show it; otherwise explicitly show the limitation. On an empty or indeterminate result, show that Uliya leaves playback alone. No fabricated clip, continuous monitoring or custom interface.

**Generic Uliya vs Skill.** [Uliya's user guide](https://support.ugnas.com/detail/article/en-US/850) already describes multi-step tasks and surveillance queries; generic Uliya might perform the same sequence from the same request. A Skill would package camera scope, the uncertain/empty-result branch and the conditional pause as a reusable procedure. It would not add a trigger, a verified event schema or enforcement, and no comparison has shown that it improves reliability.

**Assessment:** Most action-oriented of the three, but ordinary in smart-home terms and **DOCUMENTED WITH RUNTIME QUESTIONS**, with the evidence-to-player experience conditional on actual outputs. Not selected as a strong winner.

## 2. A family voice recording becomes a slow listening exercise

**Exact user request:** “Help me practice a phrase from my grandmother's recording. Transcribe this recording, let me choose a phrase, then play the same recording slowly. I'll tell you where to seek if I know the time.”

**Execution path.**

1. The user selects an authorized recording and expressly requests transcription and playback. **`knowledge-agent`** may use `ug-knowledge:audio-transcription` with its cataloged `path`, `language` and `speak-count` inputs. The catalog describes transcript text, segments, source information and warnings, but does not guarantee timestamped words or supported codecs.
2. The parent shows actual returned words and uncertainties. The user chooses the phrase. No start time is invented from a transcript or an unspecified segment.
3. If that same recording exists as an identifiable, authorized music-library item, **`media-agent`** may search using `ug-music:search` and request playback of the **user-confirmed actual item**. The search is cataloged `mixed/none`, and the exact mapping from an audio `path` or search result to the confirmed item is not documented. Stop at manual selection if identity cannot be confirmed.
4. Once playback is actually running, the media expert may request `ug-music:control` with `operation=set-speed` and a requested supported `speed`. If the user supplies an actual time, `operation=seek`, `seek-type` and `position-ms` may be requested. These are `state-change/none` and require the user's instruction. If no usable timestamp exists, play the whole recording; do not claim automatic navigation to the phrase.

**Observable result and surprise.** The user could hear a familiar person's actual recording more slowly while practicing; an actual returned transcript provides a reading aid. The human activity and playback are the experience, not simply a saved transcript. The user might appreciate hearing a family voice as the teacher, but that value is untested.

**Uncertain handoffs and runtime.** Transcription and music playback may accept different formats or indexes; an audio path or transcript reference is not a documented music ID. Search may expose or play the wrong result; first locate and confirm the item. Word timestamps, reliable automatic seek, segment loops, playback-rate support for that recording, accuracy of dialect transcription, player output, parent result propagation and user consent from other speakers are all unverified. The Skill cannot promise privacy or offline inference from NAS ownership alone.

**Closest prior art.** [FamilyTongue](https://familytongue.com/how-it-works) describes learning heritage languages from family recordings with transcription and practice; [InterpreterPro](https://app.interpreterpro.ai/) describes loading audio, reading a transcript and adjusting playback speed. These vendor descriptions were not independently tested, but the central experience already substantially exists. This proposal has less proven functionality.

**Faithful 60-second Uliya demonstration.** The user selects a real authorized voice recording; show an actual transcript passage and its correction or uncertainty. The user identifies the real matching playable item and requests slower playback; demonstrate only if the player really supports it. The user supplies a seek time if available. If the recording cannot be resolved or the player cannot slow it, stop and show that specific failure. No generated voice, inferred timestamp, synchronized text highlighting or automatic phrase loop.

**Generic Uliya vs Skill.** Generic Uliya may already be able to follow the request using speech and music experts. A Skill could retain a repeatable pattern of checking source identity, requesting corrections and avoiding invented timestamps. It does not provide the missing path-to-music-ID mapping, pronunciation assessment or synchronized player. No evidence shows it adds intelligence or beats an existing language tool.

**Assessment:** **DOCUMENTED WITH RUNTIME QUESTIONS**, and potentially **BLOCKED** at the audio-to-playable-item handoff. Strong existing prior art makes it an ordinary candidate rather than a creative finalist.

## 3. Pause a film to compare a scene with its source text

**Exact user request:** “Pause the film. In the book I selected, find the part where the character returns the letter, and show me what differs from the scene I just described. Resume only when I ask.”

**Execution path.**

1. The user explicitly asks to pause the current player and authorizes one source document. **`media-agent`** can request `ug-video:control` with `operation=pause`, cataloged `state-change/none`; actual current-player targeting and completion remain unverified.
2. The user names the scene and describes what happened in the film. The parent passes that actual user description and selected document to **`document-agent`**, which may use `ug-document:qa` or `ug-document:extract`; `qa` requires `query`, while `extract` requires `query` and accepts `file`. Ask for excerpts or references actually returned. The catalog describes evidence and coverage but not guaranteed page-level citations or an exhaustive search.
3. The parent compares the **user's description** with actual returned book evidence and flags gaps. The system must not imply it watched or understood the film. If the passage is not returned or the scene identification is unclear, say so. On a later explicit user request, the media expert may request `ug-video:control` with `operation=continue`; do not automatically resume.

**Observable result and surprise.** The film pauses for a short, source-linked comparison and later resumes at the user's request, if actual player control works. It creates an interactive intermission tied to the viewer's own book. The source comparison itself is conventional document reasoning.

**Uncertain handoffs and runtime.** The catalog has no general scene recognition, video transcript analysis, player position, automatic timestamp or access to the current frame. Passage extraction and evidence references may be incomplete. The user description may be wrong, and no comparison can establish what was in the video. Player state and pause/continue results may not propagate. All of those are disclosed rather than filled in.

**Closest prior art.** The [Book vs. Film xRay listing](https://socket.dev/chrome/package/jiifnkgjhpfebeohilnhloaiiamcphkf) describes pausing a Netflix/HBO scene and comparing it with the book using subtitles; the official Chrome Web Store page was inaccessible in this check, so this is an indexed listing rather than hands-on verification. [Amazon X-Ray](https://www.aboutamazon.co.uk/news/retail/behind-the-scenes-with-x-ray) provides content tied to points in a film. These are substantially overlapping interactions and can offer more automatic context than the documented UGREEN path.

**Faithful 60-second Uliya demonstration.** With an actual local film already playing and an authorized book available, ask Uliya to pause. User supplies the actual scene description; show only the actual returned book excerpt and a clearly labeled comparison. Ask Uliya to continue and show the real player state if supported. If pausing or extraction fails, stop and say so. No inferred current scene, automatic overlay, custom UI, or synthetic playback result.

**Generic Uliya vs Skill.** Generic Uliya is already documented as supporting document Q&A and multi-step requests and may perform this sequence. A reusable Skill could consistently distinguish user-described movie details from evidence in the book and prevent unrequested resume; it does not introduce frame understanding or automatic synchronization. No observed benefit over generic Uliya exists.

**Assessment:** **DOCUMENTED WITH RUNTIME QUESTIONS**, but substantially overlapping prior art and limited to user-supplied scene context. This is not a strong creative contender.

## Why no winner

All three are plausible arrangements of documented operations, not fully documented end-to-end paths; they may fail at actual expert return, playback or permission handoffs. They also have close existing alternatives and no proven benefit over a capable generic Uliya request. The first is the best next **runtime question** if testing becomes available: can actual camera evidence safely cause the currently playing media to pause on an explicit one-time request? A useful result would answer that technical question, not establish originality or justify starting a Skill. No hardware call, custom executable, simulated NAS run or submission artifact was created in this assessment.
