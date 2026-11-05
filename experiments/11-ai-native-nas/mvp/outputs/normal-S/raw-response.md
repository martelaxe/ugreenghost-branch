Proposed change: `assets/shared/cover.txt` → `archive/unused/cover.txt`. The source exists and describes itself as an “active source asset” ([cover.txt](/tmp/work/assets/shared/cover.txt:3)). The destination folder is absent.

| Work | Direct evidence | Inferred impact |
|---|---|---|
| Autumn Walk program | [program.md](/tmp/work/projects/autumn/program.md:1) references `../../assets/shared/cover.txt` and says the layout refers to this source. [production.md](/tmp/work/projects/autumn/production.md:1) calls for inspecting the referenced cover before publication. | Moving the file would leave the documented path unresolved unless updated. Actual layout behavior is unverified. |
| Winter guide draft | [readme.md](/tmp/work/projects/winter/readme.md:1) uses the same exact relative path as a cover illustration. [status.md](/tmp/work/projects/winter/status.md:1) says design handoff is pending. | The draft and handoff could be affected by a stale cover reference. No application failure was demonstrated. |

**Historical and contrary evidence:** Summer and the closed 2022 brochure reference `cover_old.txt`, a different asset ([summer/readme.md](/tmp/work/projects/summer/readme.md:1), [old/record.md](/tmp/work/projects/old/record.md:1)). That asset explicitly has “distinct content”; it is not an established replacement ([cover_old.txt](/tmp/work/assets/shared/cover_old.txt:2)).

**Coverage:** Investigated the full authorized `/tmp/work` workspace: 12 files discovered, selected and read, within the Skill’s 50-path/20-document limits. No inaccessible files or truncated output were encountered. Dependency coverage remains incomplete: the Autumn exported PDF is absent, the inventory does not cover every application or external copy, and print-partner references are unchecked ([program.md](/tmp/work/projects/autumn/program.md:2), [inventory.txt](/tmp/work/admin/inventory.txt:1), [vendor-note.txt](/tmp/work/admin/vendor-note.txt:1)).

**Safe next step:** Keep the file in place while reviewing the Autumn layout and Winter handoff against these references. Prepare corresponding reference updates and verify those workflows before moving it. Nothing was modified.