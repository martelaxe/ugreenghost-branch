# Three documentation-grounded walkthroughs

These are **hypothetical workflows**, not transcripts or evidence of a UGREEN run. `delegate` requests below describe responsibilities rather than pretending a runtime response. `D` = documented action/parameter concept; `U` = necessary runtime unknown. No user paths, IDs, OCR results, approval signals or output values are invented. The [catalog](02-operation-catalog.md) contains exact types and effects. Any write or playback is allowed only for the actual authorized request; child experts, not the parent, invoke their registered specialist capabilities.

## A. Photo of a set list → a song plays

**Classification: DOCUMENTED WITH RUNTIME QUESTIONS.** It crosses photo and music and ends in a real player action, conditional on actual selection and playback.

1. **Trigger:** “Read this set list photo and play the song I choose from my library.” **Required data:** a user-selected authorized image containing a legible song; a matching accessible music-library item; consent to play. If the intended line is ambiguous, ask.
2. **First delegation:** photo-agent, restricted to the user's chosen image, extract visible text via **D** `ug-photo:vision-ocr` (`path` cataloged as optional string). **Expected type:** OCR text; exact text field, formatting, clipping, and parent delivery are **U**. No assumed highlight recognition or identity.
3. **Parent handoff:** quote only text actually returned, let the user choose the line and correct artist/title, then pass that actual confirmed wording to media-agent. This is parent interpretation of text, not an established identifier translation.
4. **Second delegation, discovery:** media-agent uses **D** `ug-music:search` with required `type` and optional `keyword`; request search without playing first. The catalog labels the whole operation `mixed`, and actual behavior without `play` is **U**. Return actual candidate details if provided. A title alone does not prove the intended recording.
5. **Confirmation and action:** identify the intended returned item with the user. **D** the catalog example for this specialist action includes `--type song --keyword ... --play`; **U** the schema has no explicit song-ID parameter, and `playindex` mapping to a prior search is not guaranteed. Only request playback if the child expert can identify the confirmed match and act on it; otherwise offer manual selection. `play` is state-changing despite `approval=none`.
6. **Observable outcome:** the player actually begins the confirmed track and child reports the actual result. Whether playback is visible/audible on the finalist interface, whether result details propagate and what constitutes success are **U**. No album/playlist is created.
7. **Failure:** inaccessible image, poor OCR, no title, no item or ambiguous result → ask or stop, reporting actual evidence. `waiting_user`/`waiting_approval` → pending; `failed`/`cancelled` → no claim of playback. Catalog has no claim that OCR and playback occur offline or that no data leaves the NAS.

**Closest ordinary behavior:** [BandsManager](https://bandsmanager.com/whats-new), [SongDeck](https://www.songdeck.studio/) and Uliya's own OCR/media commands overlap. The novel value must be demonstrated, not assumed.

## B. Voice memo → matching movie

**Classification: DOCUMENTED WITH RUNTIME QUESTIONS.** Crosses knowledge and media. This avoids claiming audiovisual signal matching.

1. **Trigger / inputs:** “Find and play the movie I mentioned in this memo.” User selects authorized audio and movie library and explicitly requests playback.
2. **First delegation:** knowledge-agent `ug-knowledge:audio-transcription`, catalog `path`, `language`, `speak-count` optional. The catalog describes `items[].transcriptText`, `transcriptRef`, `segments`, `sourcePath`, quality/coverage/warnings. These are described child result items, not a complete guaranteed parent schema. Supported audio codecs and timestamps are **U**.
3. **Handoff:** parent displays actual returned text, marks transcription uncertainty and obtains user confirmation of movie title. If result has no transcript, is incomplete, or contains multiple titles, do not guess.
4. **Second delegation:** media-agent `ug-video:search` with required `type`, optional `keyword`, `play`, optional real media IDs and path-related context as actually available. The listed `play` type is `string` (do not change it to the music boolean). Media search is `mixed`; actual confirmed match, returned identifier and play semantics are **U**.
5. **Confirmation / outcome:** user confirms actual search candidate and requests play. If the expert cannot safely target the same confirmed media, provide manual choice; do not invent a media ID. Actual player activity and child `completed` are required before claiming it played.
6. **Failure / privacy:** no matching accessible movie, failed recognition, partial results, denied scope, cancellation or waiting state stops dependent playback. No automatic seek to a word is documented. Video media may be local but inference/provider locality is **U**.

## C. Dated note → camera evidence

**Classification: DOCUMENTED WITH RUNTIME QUESTIONS, with the final evidence step BLOCKED unless an actual usable ID is returned.** This crosses document and surveillance.

1. **Trigger / scope:** “Use this training note to show my dog's camera event around that time.” User selects a note, time zone and own authorized camera; avoid face recognition and unnecessary other people.
2. **First delegation:** document-agent `ug-document:extract` with required `query` and optional actual `file`; parent gets returned date/time excerpt and asks the user to confirm interpretation and a bounded window. Unclear date or incomplete extraction → stop/clarify.
3. **Camera discovery:** security-monitor-agent `ug-surveillance:cameras` is a read action and return summary describes real `camera_id`/`device_id`. **U:** ID format, UI visibility and correspondence to `event-timeline camera-id`.
4. **Event query:** same expert `ug-surveillance:event-timeline` takes required `start-time`, `end-time`, optional `timezone`, `camera-id`, `topic=Pet` and `limit`; request a bounded list. Summary says `items`, summary, warnings and event/evidence, but a precise event-ID field and completeness are **U**.
5. **Evidence:** only if an actual usable event identifier returns, ask the same expert for `ug-surveillance:event-evidence` using required `event-id`, optional `evidence-type=clip`/`snapshot`/`playback_position`, purpose and TTL. Return summary describes event/play evidence; direct playable URL, clip bytes, duration and stability are **U**. If ID cannot be obtained, evidence step is **BLOCKED**, not guessed.
6. **Result and safety:** show only real returned references or metadata and the original note. A recorded pet event is not proof it was the same dog or the described activity. Empty event query, retention gaps and capped results cannot establish absence of activity. No modification, automatic monitoring or person identification is required.
7. **Failure:** preserve note and partial event results; stop on `failed`, `cancelled`, `waiting_user` or `waiting_approval`; do not claim a clip is available merely because the event query completed.

## Syntax boundaries and an official example

The installed catalog contains the child-side example `cli.invoke --cli ug-music --action search -- --type song --keyword "周杰伦 稻香" --play` with `outputStatus: unknown`. It is an **official catalog example for the specialist**, not a parent Skill command and not a tested playback. The parent invokes only documented `delegate --target ... --instruction ...` with actual user context. Parameter types and limits are available verbatim in [JSON](02-operation-catalog.json); suspicious reused type/enums are preserved, not repaired.
