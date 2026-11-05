# Underused domains: concrete user goals

All outcomes are conditional on actual expert returns, configured services and user authorization. See catalog pointers in [02](02-operation-catalog.md).

## Video

`ug-video` → `media-agent`: search uses cataloged `type` categories and `keyword`, library/IDs, release ranges etc.; result is a media library result, not documented semantic analysis of video frames, scene retrieval, arbitrary video transcription or timestamps. `control` supports pause/continue/next/previous; subtitle search takes optional video-path/query/season/episode and describes candidate `file-id`; download needs video-path and integer file-id and is `gateway`. Provider origin and match correctness are UNKNOWN.

1. **“Play the film whose title is on this photo.”** photo-agent OCR reads a chosen picture → parent identifies actual candidate and asks if unclear → media-agent searches authorized library and plays requested selection. Photo text and title extraction are interpretations; exact search result-to-play mapping and device playback are UNKNOWN. No visual video-content understanding is required.
2. **“Find subtitles for the film that my note names, then add the selected one.”** document-agent extracts a real title → media-agent finds actual matching video and `subtitle-search`; present candidate; user confirms → `subtitle-download` gateway. Needs real returned path/file-id, network/source policy, timing and safe overwrite behavior; otherwise stop. Closest existing [Plex subtitle search](https://support.plex.tv/articles/subtitle-search/).

## Audio and music

knowledge-agent `audio-transcription` accepts optional path/language/speaker count and describes text/ref/segments/coverage; no exhaustive codec list or timecoded segment schema. media-agent `ug-music:search` covers search types including song, album, singer and songlist and can play; `control` supports seek, speed, volume, mode and stop timer. There is no documented audio fingerprinting, waveform processing, beat alignment or sound classification.

1. **“My voice note names a tune; play my copy of it.”** User authorizes a voice note → knowledge-agent transcribes → parent cites actual text and asks for clarification if artist/title uncertain → media-agent searches music library and plays the confirmed candidate. No guarantee transcription, library result or end-to-end playback works, and a generic assistant may do the same.
2. **“Read this handwritten set list and play the song I point to, then stop after 10 minutes.”** photo-agent OCR → user confirms exact text → media-agent search with play → `control set-stop-timer` with `stop-after-minutes` if supported at runtime. A timer command is a state-change and no guarantee of actual stop is documented. No automatically constructed playlist is promised.

## Surveillance

security-monitor-agent has `cameras`, `event-timeline` with required start/end and optional topic enums `Human`, `HumanFace`, `Vehicle`, `Pet`, `Package`, and `event-evidence` with `snapshot`, `clip`, `playback_position`. It also exposes identity-resolution, face and vehicle-plate operations. Avoid using biometric functions without strong explicit scope. Camera setup and retention, event IDs, reference usability and clip access are unverified. No event ≠ no activity or no recording.

1. **“Show me the event evidence for packages at my own door yesterday, together with my delivery note.”** Parent gets the permitted time/camera; event timeline → actual event ID → event-evidence; document-agent reads the user's note to contextualize, not prove a match. User may see actual returned evidence references if accessible; correlation and playback are conditional.
2. **“Review my pet's activity around the time noted in my training log.”** Read selected log → derive a narrow time range with user confirmation → query consented camera topic `Pet` → return actual event evidence if provided. Does not prove pet identity, behavior, welfare or continuous footage. No background monitoring.

## System

No `system-agent`, `ug-system` or system health CLI is listed. `ug-photo:health` checks the photo CLI, not disks. Under the catalog, system topics are read indirectly only through user-authorized files or individual metadata and cannot be made into SMART/RAID diagnosis.

1. **“Check whether my backups are healthy.”** No documented backup status, scrub, snapshot, restore-test or SMART tool. `sha256sum` can compare two actual authorized files but not certify backup health. Answer **unsupported** for the broader goal.
2. **“How much space is left and can you schedule cleanup?”** No cataloged capacity API, scheduler or watcher; cannot do this. `scan-dedupe` may identify duplicate candidates, but `state-change` deletion needs exact approval and is not equivalent to a storage-health plan.
