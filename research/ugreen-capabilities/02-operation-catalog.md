# Full operation catalog — 78 documented Actions

Source: `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json`, catalog 2.0.0 (2026-09-01); [machine-readable catalog](02-operation-catalog.json). See [source inventory](01-source-inventory.md).

One row is a documented (CLI, Action) pair. **The parent does not run child CLI examples.** Types, defaults, repeatability, descriptions, enum values and conflicting or malformed entries are preserved exactly in the JSON `verbatim_catalog_record`. `*` denotes required. All outputs are catalog summaries, not a guaranteed or complete return schema. Generic placeholders are retained as evidence of unknowns. Every row needs user-authorized scope; `none` is a catalog platform-approval label, not consent. All runtime behavior and exact errors are unverified on hardware.

Follow-on consumers are candidate handoffs, not verified parent-visible contracts; where absent, no exact mapping is documented. Approval `gateway`/`workflow` is platform-labeled, `conditional` is operation-specific and not resolved here. The operation descriptions are concise interpretations of action names; consult raw record for constraints.

## ug-music → media-agent

### `ug-music:search`

- **Result / purpose:** Search music library and optionally play a result.
- **Owner:** `media-agent`; **effect / approval:** `mixed` / `none`.
- **Required:** `type` (string).
- **Optional:** `keyword` (string), `play` (boolean), `singer-name` (string), `album-name` (string), `songlist-id` (integer), `start-year` (integer), `end-year` (integer), `page` (integer), `playindex` (integer).
- **Catalog return summary (verbatim):** Music/// scene  `items`；PlayPlayresult.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** Same action can optionally play a search result; exact item identifier and play resolution unspecified. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/0/actions/0`; **real NAS:** not verified.

### `ug-music:control`

- **Result / purpose:** Control current music playback.
- **Owner:** `media-agent`; **effect / approval:** `state-change` / `none`.
- **Required:** `operation` (string).
- **Optional:** `seek-type` (string), `position-ms` (integer), `volume` (string), `speed` (string), `playback-mode` (string), `stop-after-minutes` (integer).
- **Catalog return summary (verbatim):** /failure.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/0/actions/1`; **real NAS:** not verified.

## ug-video → media-agent

### `ug-video:search`

- **Result / purpose:** Search media library and possibly play a result.
- **Owner:** `media-agent`; **effect / approval:** `mixed` / `none`.
- **Required:** `type` (string).
- **Optional:** `keyword` (string), `play` (string), `classification` (string), `video-type` (string), `ug-video-info-id` (string), `collection-id` (string), `episode` (string), `media-lib-id` (string), `limit` (string), `offset` (string), `ug-style-id` (string), `ug-country-id` (string), `release-start` (string), `release-end` (string), `prefer` (string), `identify-status` (string), `watch-status` (string), `ug-video-info-ids` (string), `order-type` (string), `create-time-order` (string), `sort-type` (string), `page` (string), `page-size` (string), `video-ids` (string), `with-all` (string), `all-limit` (string), `recently-limit` (string), `favorites-limit` (string).
- **Catalog return summary (verbatim):** Media、、、PlayPlayresult；PlayRequiresreal ID/path.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/1/actions/0`; **real NAS:** not verified.

### `ug-video:control`

- **Result / purpose:** Control video playback.
- **Owner:** `media-agent`; **effect / approval:** `state-change` / `none`.
- **Required:** `operation` (string).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** English returnSummary text..
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/1/actions/1`; **real NAS:** not verified.

### `ug-video:subtitle-search`

- **Result / purpose:** Search for subtitles.
- **Owner:** `media-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `video-path` (string), `query` (string), `season-number` (integer), `episode-number` (integer).
- **Catalog return summary (verbatim):** Subtitles、`file-id`、/.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** Possible returned file-id → subtitle-download file-id, with video-path, if compatible integer and confirmed selection. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/1/actions/2`; **real NAS:** not verified.

### `ug-video:subtitle-download`

- **Result / purpose:** Download a selected subtitle.
- **Owner:** `media-agent`; **effect / approval:** `state-change` / `gateway`.
- **Required:** `video-path` (string), `file-id` (integer).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** `status`Downloadresult；.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/1/actions/3`; **real NAS:** not verified.

## ug-surveillance → security-monitor-agent

### `ug-surveillance:cameras`

- **Result / purpose:** List cameras.
- **Owner:** `security-monitor-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `status` (integer), `include-deleted` (boolean).
- **Catalog return summary (verbatim):** real `camera_id`/`device_id`、、.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** Possible returned camera_id → event-timeline camera-id; identifier spelling/type equivalence is plausible, not contractually guaranteed. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/2/actions/0`; **real NAS:** not verified.

### `ug-surveillance:event-timeline`

- **Result / purpose:** Query bounded event timeline.
- **Owner:** `security-monitor-agent`; **effect / approval:** `read` / `none`.
- **Required:** `start-time` (string), `end-time` (string).
- **Optional:** `timezone` (string), `request-id` (string), `device-id` (string), `camera-id` (string ×), `location` (string ×), `floor` (string ×), `room` (string ×), `topic` (string ×), `identity-type` (string), `person-name` (string), `limit` (integer).
- **Catalog return summary (verbatim):** events `items`、summary、warnings、events/evidence； scene monitoringevents.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** Possible returned event identifier → event-evidence event-id; output schema/identifier spelling unspecified. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/2/actions/1`; **real NAS:** not verified.

### `ug-surveillance:identity-resolve`

- **Result / purpose:** Resolve an identity for specified inputs.
- **Owner:** `security-monitor-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `event-id` (string ×), `face-id` (string ×), `plate-id` (string ×), `start-time` (string), `end-time` (string), `timezone` (string), `include-explanation` (boolean), `request-id` (string).
- **Catalog return summary (verbatim):** /identity、.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/2/actions/2`; **real NAS:** not verified.

### `ug-surveillance:event-evidence`

- **Result / purpose:** Retrieve event evidence references.
- **Owner:** `security-monitor-agent`; **effect / approval:** `read` / `none`.
- **Required:** `event-id` (string ×).
- **Optional:** `evidence-type` (string ×), `max-items` (string), `ttl-sec` (string), `purpose` (string), `request-id` (string).
- **Catalog return summary (verbatim):** events、Playevidence.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/2/actions/3`; **real NAS:** not verified.

### `ug-surveillance:faces`

- **Result / purpose:** List face-related records.
- **Owner:** `security-monitor-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `camera-id` (string), `identity-type` (string), `page` (string), `page-size` (string), `request-id` (string).
- **Catalog return summary (verbatim):** Requires `face-id`.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/2/actions/4`; **real NAS:** not verified.

### `ug-surveillance:face-detail`

- **Result / purpose:** Inspect one face record.
- **Owner:** `security-monitor-agent`; **effect / approval:** `read` / `none`.
- **Required:** `face-id` (string).
- **Optional:** `request-id` (string).
- **Catalog return summary (verbatim):** English returnSummary text..
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/2/actions/5`; **real NAS:** not verified.

### `ug-surveillance:vehicle-plates`

- **Result / purpose:** List vehicle plate records.
- **Owner:** `security-monitor-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `camera-id` (string ×), `identity-type` (string), `query` (string), `page` (string), `page-size` (string), `request-id` (string).
- **Catalog return summary (verbatim):** Requires `plate-id`.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/2/actions/6`; **real NAS:** not verified.

### `ug-surveillance:vehicle-plate-detail`

- **Result / purpose:** Inspect a plate record.
- **Owner:** `security-monitor-agent`; **effect / approval:** `read` / `none`.
- **Required:** `plate-id` (string).
- **Optional:** `request-id` (string).
- **Catalog return summary (verbatim):** English returnSummary text..
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/2/actions/7`; **real NAS:** not verified.

## ug-filesystem → file-agent

### `ug-filesystem:cat`

- **Result / purpose:** Read file content.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** `path` (string).
- **Optional:** `offset` (integer), `length` (integer).
- **Catalog return summary (verbatim):** filecontent、/.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/0`; **real NAS:** not verified.

### `ug-filesystem:category`

- **Result / purpose:** Query file categories.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `root-type` (integer), `limit` (integer), `permission` (string).
- **Catalog return summary (verbatim):** file.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/1`; **real NAS:** not verified.

### `ug-filesystem:find`

- **Result / purpose:** Find files in a scope.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** `path` (string).
- **Optional:** `pattern` (string), `type` (string), `min-size` (string), `max-size` (string), `date-type` (string), `start-timestamp` (string), `end-timestamp` (string), `max-depth` (string), `limit` (string).
- **Catalog return summary (verbatim):** file、realpath `fileId`.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** Potential returned path → file-agent `cat`/`stat`/`sha256sum`; document-agent `extract` or knowledge-agent transcription if compatible. Path, format and parent transfer unverified. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/2`; **real NAS:** not verified.

### `ug-filesystem:getfattr`

- **Result / purpose:** Read file attributes.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** `path` (string).
- **Optional:** `field` (string).
- **Catalog return summary (verbatim):** file.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/3`; **real NAS:** not verified.

### `ug-filesystem:ls`

- **Result / purpose:** List files in a directory.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** `path` (string).
- **Optional:** `recursive` (boolean), `max-depth` (string), `limit` (string).
- **Catalog return summary (verbatim):** directory、real/path `fileId`.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** Potential returned path → file-agent reads or specialist source path; completeness and format unknown. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/4`; **real NAS:** not verified.

### `ug-filesystem:md5sum`

- **Result / purpose:** Compute MD5.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** `path` (string).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** MD5.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/5`; **real NAS:** not verified.

### `ug-filesystem:sha256sum`

- **Result / purpose:** Compute SHA-256.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** `path` (string).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** SHA-256.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/6`; **real NAS:** not verified.

### `ug-filesystem:stat`

- **Result / purpose:** Read file metadata.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** `path` (string).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** realpath、、time stat.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/7`; **real NAS:** not verified.

### `ug-filesystem:chtimes`

- **Result / purpose:** Change file times.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `gateway`.
- **Required:** `path` (string).
- **Optional:** `atime` (integer), `mtime` (integer).
- **Catalog return summary (verbatim):** timeresult.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/8`; **real NAS:** not verified.

### `ug-filesystem:cpmv`

- **Result / purpose:** Copy or move files.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `gateway`.
- **Required:** `src` (string), `dst` (string).
- **Optional:** `type` (string), `action-type` (string), `overwrite` (boolean).
- **Catalog return summary (verbatim):** /real.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/9`; **real NAS:** not verified.

### `ug-filesystem:del`

- **Result / purpose:** Delete an item.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `gateway`.
- **Required:** `path` (string).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** /， `final_path`.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/10`; **real NAS:** not verified.

### `ug-filesystem:echo`

- **Result / purpose:** Write content to a file.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `gateway`.
- **Required:** `path` (string).
- **Optional:** `content` (string), `write-mode` (string), `offset` (string).
- **Catalog return summary (verbatim):** fileresult.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/11`; **real NAS:** not verified.

### `ug-filesystem:mkdir`

- **Result / purpose:** Create a directory.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `gateway`.
- **Required:** `path` (string).
- **Optional:** `mode` (string), `parents` (boolean).
- **Catalog return summary (verbatim):** directorypath.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/12`; **real NAS:** not verified.

### `ug-filesystem:rename`

- **Result / purpose:** Rename an item.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `gateway`.
- **Required:** `path` (string), `old-name` (string), `new-name` (string).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** 、.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/13`; **real NAS:** not verified.

### `ug-filesystem:restore`

- **Result / purpose:** Restore an item (exact semantics unspecified).
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `gateway`.
- **Required:** `path` (string).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** English returnSummary text..
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/14`; **real NAS:** not verified.

### `ug-filesystem:share-mkdir`

- **Result / purpose:** Create a shared directory.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `gateway`.
- **Required:** `volume` (string), `folder-name` (string).
- **Optional:** `quota-bytes` (string), `quota-unit` (string), `network-places-hide` (string), `no-permission-hide` (string), `enable-recycle` (string), `allow-only-admin-recycle` (string).
- **Catalog return summary (verbatim):** directoryCreate.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/15`; **real NAS:** not verified.

### `ug-filesystem:touch`

- **Result / purpose:** Touch or create a file.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `gateway`.
- **Required:** `path` (string).
- **Optional:** `mode` (string), `content` (string).
- **Catalog return summary (verbatim):** file.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/3/actions/16`; **real NAS:** not verified.

## ug-filemgr → file-agent

### `ug-filemgr:mediainfo`

- **Result / purpose:** Read media information.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** `path` (string).
- **Optional:** `intranet-share-id` (string).
- **Catalog return summary (verbatim):** data.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/4/actions/0`; **real NAS:** not verified.

### `ug-filemgr:scan-dedupe`

- **Result / purpose:** Scan for duplicates.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** `path` (string ×).
- **Optional:** `scope` (string).
- **Catalog return summary (verbatim):** English returnSummary text..
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/4/actions/1`; **real NAS:** not verified.

### `ug-filemgr:tag-filter`

- **Result / purpose:** Filter files by tag.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** `tag-id` (string ×).
- **Optional:** `path` (string ×), `recursive` (boolean).
- **Catalog return summary (verbatim):** file.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/4/actions/2`; **real NAS:** not verified.

### `ug-filemgr:tag-get`

- **Result / purpose:** Get a tag.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** `tag-id` (integer).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** tag.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/4/actions/3`; **real NAS:** not verified.

### `ug-filemgr:tag-get-by-name`

- **Result / purpose:** Get a tag by name.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** `name` (string).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** tag.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/4/actions/4`; **real NAS:** not verified.

### `ug-filemgr:tag-get-file`

- **Result / purpose:** Get tags of a file.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** `path` (string ×).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** filetag.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/4/actions/5`; **real NAS:** not verified.

### `ug-filemgr:tag-list`

- **Result / purpose:** List tags.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** none declared.
- **Catalog return summary (verbatim):** tag.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/4/actions/6`; **real NAS:** not verified.

### `ug-filemgr:tag-list-file`

- **Result / purpose:** List files by tag.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** `tag-id` (integer).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** tagfile.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/4/actions/7`; **real NAS:** not verified.

### `ug-filemgr:tag-add`

- **Result / purpose:** Add a tag.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `gateway`.
- **Required:** `tag-id` (string).
- **Optional:** `colour` (string).
- **Catalog return summary (verbatim):** tag-add result。.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/4/actions/8`; **real NAS:** not verified.

### `ug-filemgr:tag-add-file`

- **Result / purpose:** Add a tag to a file.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `conditional`.
- **Required:** `path` (string ×), `tag-id` (string).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** tag-add-file result。.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/4/actions/9`; **real NAS:** not verified.

### `ug-filemgr:tag-delete`

- **Result / purpose:** Delete a tag.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `gateway`.
- **Required:** `tag-id` (string).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** tag-delete result。.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/4/actions/10`; **real NAS:** not verified.

### `ug-filemgr:tag-delete-file`

- **Result / purpose:** Remove a tag from a file.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `conditional`.
- **Required:** `path` (string ×), `tag-id` (string).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** tag-delete-file result。.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/4/actions/11`; **real NAS:** not verified.

### `ug-filemgr:tag-set`

- **Result / purpose:** Set a tag.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `gateway`.
- **Required:** `tag-id` (integer).
- **Optional:** `name` (string), `colour` (string).
- **Catalog return summary (verbatim):** tag-set result。.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/4/actions/12`; **real NAS:** not verified.

## file-workflow → file-agent

### `file-workflow:get-user-dir`

- **Result / purpose:** Get a user directory.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** none declared.
- **Catalog return summary (verbatim):** `fileId`、realdirectory `path`.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/5/actions/0`; **real NAS:** not verified.

### `file-workflow:start`

- **Result / purpose:** Create a planned workflow.
- **Owner:** `file-agent`; **effect / approval:** `read` / `none`.
- **Required:** `kind` (string), `target` (string).
- **Optional:** `lang` (string), `destination` (string), `by` (string), `filter` (string), `type-rule` (string), `scope` (string), `keep-by` (string).
- **Catalog return summary (verbatim):** `id`、`status=planned`、`plan`.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** `id` potentially → file-workflow:run `id`/`start.data.id`; runtime wiring and approval semantics unknown. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/5/actions/1`; **real NAS:** not verified.

### `file-workflow:run`

- **Result / purpose:** Run a planned workflow.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `workflow`.
- **Required:** `id` (string).
- **Optional:** `start.data.id` (string).
- **Catalog return summary (verbatim):** `id`、`status`、`total`、`succeeded`、`failed`.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/5/actions/2`; **real NAS:** not verified.

### `file-workflow:batch-del`

- **Result / purpose:** Batch delete.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `workflow`.
- **Required:** `paths` (string).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** `status`、`total`、`succeeded`、`failed`.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/5/actions/3`; **real NAS:** not verified.

### `file-workflow:batch-move`

- **Result / purpose:** Batch move.
- **Owner:** `file-agent`; **effect / approval:** `state-change` / `workflow`.
- **Required:** none declared.
- **Optional:** `data` (string), `actionType` (string), `root` (string), `renameBy` (string), `dateField` (string), `sourceDir` (string), `destination` (string).
- **Catalog return summary (verbatim):** `status`、`total`、`succeeded`、`failed`、`renamedFiles`、`hasMore`.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/5/actions/4`; **real NAS:** not verified.

## ug-document → document-agent

### `ug-document:page-count`

- **Result / purpose:** Count document pages.
- **Owner:** `document-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `file` (string ×).
- **Catalog return summary (verbatim):** `items[].file`、`items[].page_count`.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/6/actions/0`; **real NAS:** not verified.

### `ug-document:metadata`

- **Result / purpose:** Read document metadata.
- **Owner:** `document-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `file` (string ×), `include-pages` (boolean), `directory-limit` (string).
- **Catalog return summary (verbatim):** file/directorydata、.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/6/actions/1`; **real NAS:** not verified.

### `ug-document:qa`

- **Result / purpose:** Answer questions about document content.
- **Owner:** `document-agent`; **effect / approval:** `read` / `none`.
- **Required:** `query` (string).
- **Optional:** `file` (string ×), `intent` (string), `content-scope` (string), `top-k` (string), `entities` (string ×), `answer-mode` (string), `evidence-mode` (string), `max-files` (string), `body-cap` (string).
- **Catalog return summary (verbatim):** `answer`、/evidence、coverage、Read.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** Returned answer/evidence → parent synthesis or content for save-text if actually returned; provenance schema incomplete. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/6/actions/2`; **real NAS:** not verified.

### `ug-document:extract`

- **Result / purpose:** Extract document data.
- **Owner:** `document-agent`; **effect / approval:** `read` / `none`.
- **Required:** `query` (string).
- **Optional:** `file` (string ×), `schema` (string), `content-scope` (string), `max-files` (string), `body-cap` (string), `dedupe` (boolean).
- **Catalog return summary (verbatim):** data、、coverage、failures.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** Returned content → parent reasoning, possibly knowledge-agent save-text via content if actual text is returned; transfer/semantics unverified. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/6/actions/3`; **real NAS:** not verified.

### `ug-document:translate`

- **Result / purpose:** Translate document/text.
- **Owner:** `document-agent`; **effect / approval:** `mixed` / `gateway`.
- **Required:** none declared.
- **Optional:** `query` (string), `file` (string ×), `target-lang` (string), `style` (string), `body-cap` (string), `max-files` (string), `extract-only` (boolean), `content` (string), `source-title` (string).
- **Catalog return summary (verbatim):** `mode`、`translation`、`output_file`、`target_lang`、coverage、sources、safety.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/6/actions/4`; **real NAS:** not verified.

### `ug-document:writing`

- **Result / purpose:** Generate written content.
- **Owner:** `document-agent`; **effect / approval:** `mixed` / `gateway`.
- **Required:** none declared.
- **Optional:** `query` (string), `file` (string ×), `task` (string), `style` (string), `template` (string), `content-scope` (string), `max-length` (string), `body-cap` (string), `max-files` (string), `extract-only` (boolean), `content` (string), `source-title` (string).
- **Catalog return summary (verbatim):** `mode`、`draft`、`output_file`、`task`、`processing_mode`、coverage、sources、safety.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/6/actions/5`; **real NAS:** not verified.

### `ug-document:reconcile`

- **Result / purpose:** Reconcile document information.
- **Owner:** `document-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `query` (string), `file` (string ×), `max-files` (string).
- **Catalog return summary (verbatim):** result、、 coverage.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/6/actions/6`; **real NAS:** not verified.

## ug-knowledge → knowledge-agent

### `ug-knowledge:answer-official`

- **Result / purpose:** Answer using official knowledge.
- **Owner:** `knowledge-agent`; **effect / approval:** `read` / `none`.
- **Required:** `query` (string).
- **Optional:** none declared.
- **Catalog return summary (verbatim):** Knowledge.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/7/actions/0`; **real NAS:** not verified.

### `ug-knowledge:audio-transcription`

- **Result / purpose:** Transcribe audio.
- **Owner:** `knowledge-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `path` (string ×), `language` (string), `speak-count` (integer).
- **Catalog return summary (verbatim):** `items[].transcriptText`、`transcriptRef`、`segments`、`sourceKind`、`sourcePath`、coverage、summary、failures、quality、warnings.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** Actual transcriptText/sourcePath → parent can formulate media keyword, evidence query, or text save; timestamps and segment structure unknown. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/7/actions/1`; **real NAS:** not verified.

### `ug-knowledge:collect-evidence`

- **Result / purpose:** Collect evidence.
- **Owner:** `knowledge-agent`; **effect / approval:** `read` / `none`.
- **Required:** `query` (string).
- **Optional:** `path` (string ×), `extension` (string ×), `full` (boolean).
- **Catalog return summary (verbatim):** `evidence`、sources、coverage、failures/warnings.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** Actual evidence → parent synthesis; save-text accepts content/content-ref but reference compatibility unknown. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/7/actions/2`; **real NAS:** not verified.

### `ug-knowledge:save-text`

- **Result / purpose:** Save text.
- **Owner:** `knowledge-agent`; **effect / approval:** `state-change` / `workflow`.
- **Required:** none declared.
- **Optional:** `path` (string), `content` (string), `content-ref` (string), `filename-hint` (string).
- **Catalog return summary (verbatim):** real `verified=true`、`outputFile`、`contentBytes`.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/7/actions/3`; **real NAS:** not verified.

## ug-photo → photo-agent

### `ug-photo:albums`

- **Result / purpose:** List albums.
- **Owner:** `photo-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `keyword` (string), `album-select` (string), `album-perm` (string), `album-type` (object ×), `share-select` (string ×), `page` (string), `page-size` (string), `sort-by` (string), `asc` (string), `raw` (string).
- **Catalog return summary (verbatim):** Album、real `album_uuid`、photos.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/0`; **real NAS:** not verified.

### `ug-photo:album-detail`

- **Result / purpose:** Inspect album details.
- **Owner:** `photo-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `album-uuid` (string), `get-type` (string), `raw` (string).
- **Catalog return summary (verbatim):** Albumpeople.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/1`; **real NAS:** not verified.

### `ug-photo:figure-albums`

- **Result / purpose:** List person-related albums.
- **Owner:** `photo-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `album-name` (string), `album-uuid` (string), `show-hidden` (string), `show-name` (string), `page` (string), `page-size` (string), `sort-by` (string), `asc` (string), `raw` (string).
- **Catalog return summary (verbatim):** people/Album UUID.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/2`; **real NAS:** not verified.

### `ug-photo:object-albums`

- **Result / purpose:** List object-related albums.
- **Owner:** `photo-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `album-name` (string), `album-uuid` (string), `page` (string), `page-size` (string), `sort-by` (string), `asc` (string), `raw` (string).
- **Catalog return summary (verbatim):** Album UUID.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/3`; **real NAS:** not verified.

### `ug-photo:search-picture`

- **Result / purpose:** Search pictures.
- **Owner:** `photo-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `album-uuid` (string ×), `album-name` (string ×), `album-type` (string ×), `figure-uuid` (string ×), `figure-name` (string ×), `pet-uuid` (string ×), `pet-name` (string ×), `figure-pet-method` (string), `ai-object-index` (object ×), `ai-object-uuid` (object ×), `ai-object-name` (object ×), `location` (object ×), `dir` (object ×), `file-name-contains` (object ×), `ocr-contains` (object ×), `start-time` (string), `end-time` (string), `total-judge` (string), `file-type` (string ×), `range-personal` (string), `range-share` (string), `camera-model` (string ×), `lens-model` (string ×), `focal` (string ×), `exposure` (string ×), `aperture` (string ×), `iso` (string ×), `page` (string), `page-size` (string), `sort-by` (string), `asc` (string), `raw` (string).
- **Catalog return summary (verbatim):** photos/、fileidentity.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** Possible file identity/path → vision-ocr/meta or album add-item; identity encoding and parent delivery unverified. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/4`; **real NAS:** not verified.

### `ug-photo:search-screen`

- **Result / purpose:** Search screen.
- **Owner:** `photo-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `category` (string), `keyword` (string), `album-type` (string), `album-uuid` (string), `figure-uuid` (string), `pet-uuid` (string), `storage-type` (string), `common-album-type` (string), `index-id` (string), `class-index` (string), `range-personal` (string), `range-share` (string), `location-level` (string), `folder-id` (string), `path` (string), `file-type` (string ×), `camera-model` (string ×), `lens-model` (string ×), `focal` (string ×), `exposure` (string ×), `aperture` (string ×), `iso` (string ×), `page` (string), `page-size` (string), `sort-by` (string), `asc` (string), `total-judge` (string), `raw` (string).
- **Catalog return summary (verbatim):** Search、 UUID/ID.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/5`; **real NAS:** not verified.

### `ug-photo:search-classify`

- **Result / purpose:** Search classifications.
- **Owner:** `photo-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `keyword` (string), `category` (string), `page` (string), `page-size` (string), `raw` (string).
- **Catalog return summary (verbatim):** people/.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/6`; **real NAS:** not verified.

### `ug-photo:search-hint`

- **Result / purpose:** Search hints.
- **Owner:** `photo-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `keyword` (string), `cover-total` (string), `record` (string), `page` (string), `page-size` (string), `raw` (string).
- **Catalog return summary (verbatim):** Search/.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/7`; **real NAS:** not verified.

### `ug-photo:meta`

- **Result / purpose:** Read photo metadata.
- **Owner:** `photo-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `path` (string ×), `raw` (string).
- **Catalog return summary (verbatim):** EXIF/data、failure/.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/8`; **real NAS:** not verified.

### `ug-photo:vision-ocr`

- **Result / purpose:** OCR photo text.
- **Owner:** `photo-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `path` (string).
- **Catalog return summary (verbatim):** OCR text AI.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** Actual OCR text → parent synthesizes media search keyword or document-agent content, conditional on supported result and task context. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/9`; **real NAS:** not verified.

### `ug-photo:vision-vlm`

- **Result / purpose:** Analyze image with a vision-language prompt.
- **Owner:** `photo-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `path` (string), `prompt` (string), `model` (string), `max-tokens` (string), `temperature` (string), `top-p` (string).
- **Catalog return summary (verbatim):** result.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/10`; **real NAS:** not verified.

### `ug-photo:health`

- **Result / purpose:** Check photo CLI health.
- **Owner:** `photo-agent`; **effect / approval:** `read` / `none`.
- **Required:** none declared.
- **Optional:** `domain` (string).
- **Catalog return summary (verbatim):** photos CLI.
- **Completion evidence (catalog text):** result ok=true， data realresult。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/11`; **real NAS:** not verified.

### `ug-photo:create-album`

- **Result / purpose:** Create an album.
- **Owner:** `photo-agent`; **effect / approval:** `state-change` / `workflow`.
- **Required:** none declared.
- **Optional:** `album-name` (string), `add-item` (string ×), `sub-type` (string), `query` (string).
- **Catalog return summary (verbatim):** real `album_uuid` scene；/ blocked.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/12`; **real NAS:** not verified.

### `ug-photo:create-album-condition`

- **Result / purpose:** Create condition-based album.
- **Owner:** `photo-agent`; **effect / approval:** `state-change` / `workflow`.
- **Required:** none declared.
- **Optional:** `album-name` (string), `file-type` (object ×), `location` (object ×), `dir` (object ×), `figure-uuid` (object ×), `figure-name` (object ×), `pet-uuid` (object ×), `pet-name` (object ×), `camera-model` (object ×), `lens-model` (object ×), `focal` (object ×), `exposure` (object ×), `aperture` (object ×), `iso` (object ×), `file-name-contains` (object ×), `ocr-contains` (object ×), `start-time` (string), `end-time` (string).
- **Catalog return summary (verbatim):** Albumreal UUID.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/13`; **real NAS:** not verified.

### `ug-photo:create-album-anniversary`

- **Result / purpose:** Create anniversary album.
- **Owner:** `photo-agent`; **effect / approval:** `state-change` / `workflow`.
- **Required:** none declared.
- **Optional:** `album-name` (string), `commemorate-method` (string), `commemorate-month` (string), `commemorate-day` (string ×), `commemorate-range` (string), `start-time` (string), `end-time` (string).
- **Catalog return summary (verbatim):** Albumreal UUID.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/14`; **real NAS:** not verified.

### `ug-photo:create-album-baby`

- **Result / purpose:** Create baby album.
- **Owner:** `photo-agent`; **effect / approval:** `state-change` / `workflow`.
- **Required:** none declared.
- **Optional:** `album-name` (string), `add-item` (string ×), `baby-name` (string), `person-name` (string), `gender` (string), `birthday` (string), `blood-type` (string), `height` (string), `weight` (string), `figure-uuid` (string ×), `query` (string).
- **Catalog return summary (verbatim):** Albumreal UUID people.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/15`; **real NAS:** not verified.

### `ug-photo:create-album-custom`

- **Result / purpose:** Create custom album.
- **Owner:** `photo-agent`; **effect / approval:** `state-change` / `workflow`.
- **Required:** none declared.
- **Optional:** `album-name` (string).
- **Catalog return summary (verbatim):** Albumreal UUID.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/16`; **real NAS:** not verified.

### `ug-photo:timeline`

- **Result / purpose:** Create timeline grouping.
- **Owner:** `photo-agent`; **effect / approval:** `state-change` / `workflow`.
- **Required:** none declared.
- **Optional:** `figure-uuid` (string ×), `figure-name` (string ×), `pet-uuid` (string ×), `pet-name` (string ×), `figure-pet-method` (string), `location` (object ×), `dir` (object ×), `album-uuid` (object ×), `album-name` (object ×), `album-type` (object ×), `ai-object-index` (object ×), `ai-object-uuid` (object ×), `ai-object-name` (object ×), `file-name-contains` (object ×), `ocr-contains` (object ×), `start-time` (string), `end-time` (string), `camera-model` (string ×), `lens-model` (string ×), `focal` (string ×), `exposure` (string ×), `aperture` (string ×), `iso` (string ×), `file-type` (string ×), `group-by` (string).
- **Catalog return summary (verbatim):** `status=completed|submitted|partial|blocked`、、directory ID、/failure.
- **Completion evidence (catalog text):** result ok=true， data operation；Approval、failure。.
- **Consumer / limits:** UNKNOWN: no exact downstream field mapping established; check returned values, scope, failures and partial results. **Errors, precise permission conditions and schema:** UNKNOWN where the source says unknown.
- **Source:** `/mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/data/capability-catalog.json#/clis/8/actions/17`; **real NAS:** not verified.
