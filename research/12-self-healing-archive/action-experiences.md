# Seven action experiences

These are concepts and planned demos, not device results. Parent delegates, user and gateway/workflow approval precede writes, all source and destination paths must be authorized, actual outputs decide feasibility. Failure to establish safe no-overwrite behavior stops all copy/move examples.

## 1. Project Rescue — selected
- **User/request:** creator: “Find the missing Harbor cover; restore one matching file without disrupting the other project.” Inputs: two project manifests, a missing destination, multiple shared candidate versions, checksum.
- **Before/investigate:** Harbor manifest points to an absent path; document-agent extracts the requirement; file-agent lists and hashes candidates, sees Meadow reference.
- **Propose/approval/after:** user approves one non-overwriting `ug-filesystem:cpmv` copy of exact matching bytes into an existing authorized folder; shared original remains. Platform gateway approval required. The destination path now has a copied asset; no application repair is inferred.
- **Verify/risk:** `ls`/`stat`/`sha256sum` source and destination, if actually returned. Wrong version, collision or inaccessible dependencies block the change; no documented automatic undo.
- **Competitor/NAS/demo:** Premiere Link Media already finds/relinks missing footage inside Premiere. Our unverified differentiator is cross-folder evidence plus a retained shared path on the NAS. Demo 60–90s: missing manifest → independent hash match → Meadow dependency → approval → added file → equal hashes. MVP is one copy, not universal project repair.

## 2. Safe Migration
- **User/request/input:** small team: “Move this one briefing to its approved new location without losing a known reference”; documents and folder tree.
- **Before/investigate:** find and extract exact references with file/document agents; preserve uncertain coverage. **Propose:** one `cpmv` move only if dependencies and no-overwrite can actually be verified. User + gateway approval. **After/verification:** old location absent and target present/hash matches. **Risk:** app references and retry/undo unknown. **Competitor:** VS Code refactoring preview; ordinary file moves lack semantic cross-document analysis. **NAS:** shared context and native action. **Demo:** show reference blocking move; minimal deliverable is a preview if checks fail.

## 3. Context Rescue
- **User/request/input:** freelancer: “Recover one misfiled document to its evidenced project without removing the original.” Selected notes and existing project folder.
- **Before/investigate:** misplaced generic filename; document `extract`, file `find`/`stat`. **Propose:** non-overwriting `cpmv` copy, user + gateway approval. **After/verification:** project gets an additional identical copy, source stays; `sha256sum`. **Risk:** ambiguous affiliation and private scope; false attribution stops action. **Competitor:** Paperless-ngx automated tagging; opportunity is evidence-backed recovery across ordinary files. **NAS/demo:** local project destination; before orphan → source-supported association → user-approved copy → file appears. MVP one document.

## 4. Archive Health Fix
- **User/request/input:** family administrator: “Fix the clearest recoverable broken reference in this folder.” Bounded manifest and source archive.
- **Before/investigate:** file list and content comparisons by file/document experts. **Propose:** one copy only when identity and destination are established; explicit/gateway approval. **After/verification:** source preserved, missing path restored, stat/hash. **Risk:** choosing the “most important” problem is subjective; missing coverage. **Competitor:** application-specific relink; ordinary file manager cannot interpret why a path matters. **NAS/demo:** local health → one verified path fix; MVP is one selected problem, not monitoring.

## 5. Duplicate Review with Protected Context
- **User/request/input:** NAS owner: “Review one duplicate without losing a version still used by a project.” Duplicate scan, two references.
- **Before/investigate:** file-agent `ug-filemgr:scan-dedupe` and hashes; document-agent finds actual references. **Propose:** preserve referenced path; if safe and desired, add an owner-approved tag using `tag-add-file` only if exact conditional approval semantics are established. **After/verify:** tag can be inspected with tag-get-file; do not claim storage freed. **Risk:** tag permissions/semantics unknown. **Competitor:** Immich duplicate review and folder-priority tools; AI could surface project context. **NAS/demo:** duplicate pair → link protects one → tag another for manual review; MVP may be read-only if tagging cannot be verified.

## 6. Family Memory Album Assembly
- **User/request/input:** family owner: “Create an album of actual selected celebration photos.” Photos with known IDs, permitted library.
- **Before/investigate:** photo-agent `search-picture`, `meta`, possibly `vision-vlm`; identity/privacy and source returned IDs checked. **Propose/approval/after:** user approves exact set and `ug-photo:create-album` workflow approval; new album exists if verified. **Verify/risk:** `album-detail` if actually returns members; unknown album semantics and faces. **Competitor:** Immich / NAS photo albums; no proven novelty. **NAS/demo:** one approval creates visible album without editing originals. **MVP:** small explicit selection; no hallucinated people.

## 7. Subtitle Rescue (unexpected)
- **User/request/input:** media collector: “Find a subtitle for this actual episode and add it after I confirm.” Existing video path and actual subtitle search result.
- **Before/investigate:** media-agent `ug-video:subtitle-search` on actual selected video. **Propose/approval/after:** one returned file-id with gateway `subtitle-download`; user approves. **Verify/risk:** inspect actual output and file if returned; language, source and download rights unknown. **Competitor:** Bazarr and built-in subtitle search/download already close; no novelty claim. **NAS/demo:** missing subtitle → actual match → approved download → playback check, if supported. **MVP:** one episode; fallback if download unavailable.
