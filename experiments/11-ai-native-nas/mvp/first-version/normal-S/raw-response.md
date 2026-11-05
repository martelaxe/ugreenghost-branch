The move could affect the Autumn Walk program and the Winter guide draft. Keep the file in place while reviewing those references.

**Proposed change:** `assets/shared/cover.txt` → `archive/unused/cover.txt`. The source exists; the destination directory does not currently exist.

**Direct evidence**

- `assets/shared/cover.txt:3` describes it as an “active source asset.”
- `projects/autumn/program.md:1–2` references `../../assets/shared/cover.txt` and says the program layout refers to this source. Its exported final PDF is absent from that folder.
- `projects/autumn/production.md:1` requires inspecting the cover referenced in `program.md` before publishing.
- `projects/winter/readme.md:1` references the same relative path as a cover illustration and says the release remains a draft.
- `projects/winter/status.md:1` records pending design handoff and a cover reference in the README.

Both relative paths resolve to the proposed source from their respective project folders.

**Inference and contrary evidence**

Moving the asset could leave those references stale and affect Autumn’s publishing review or Winter’s design handoff. The archive does not establish that an application will break.

`projects/summer/readme.md:1` and `projects/old/record.md:1` reference `cover_old.txt` instead. `assets/shared/cover_old.txt:2` identifies that file as a retired version with distinct content; it is not established as a replacement.

**Coverage and limits**

Scope: the full `/tmp/work` workspace. Discovered, selected and read: 12 files, within the skill’s limits of 50 paths and 20 documents. No output truncation, inaccessible files or symlinks were reported; `.git` internals were excluded.

Application and external-copy coverage remains unknown. `admin/inventory.txt:1` says the inventory does not cover every application or external copy. `admin/vendor-note.txt:1` says the print partner may hold separate, unchecked files.

**Safe next step:** Before moving anything, review Autumn’s layout and Winter’s pending design handoff to determine how their source links would be updated and verified. The current evidence supports treating this as an active shared asset, not confirmed unused material.

No files were modified or moved; no external services were accessed.