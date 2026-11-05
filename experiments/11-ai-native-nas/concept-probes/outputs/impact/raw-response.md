The proposed move could affect **two projects**. The archive labels `assets/shared/cover.txt:3` an “active source asset,” so filing it under `unused` would conflict with the recorded usage.

| Work | Observed evidence | Likely impact if moved without updating references |
|---|---|---|
| Autumn Walk program | `projects/autumn/program.md:1–2` references `../../assets/shared/cover.txt` and says the layout uses this source. | The recorded path would stop resolving; layout or republication work could be affected. |
| Winter guide | `projects/winter/readme.md:1` references the same file. `projects/winter/status.md:1` says design handoff is pending. | The draft’s cover reference would stop resolving, potentially affecting handoff. |

The Summer guide and 2022 brochure reference the separate `assets/shared/cover_old.txt` (`projects/summer/readme.md:1`, `projects/old/record.md:1`). Those recorded references would remain valid.

**Coverage limits:** I inspected all 12 files present in the workspace. Autumn’s exported PDF is absent according to `projects/autumn/program.md:2`; its production note mentions sponsor notes that I could not locate (`projects/autumn/production.md:1`). External partner files are explicitly unchecked (`admin/vendor-note.txt:1`), and the inventory is incomplete for applications and external copies (`admin/inventory.txt:1`). Actual application behavior and external dependencies remain unknown.

**Practical next step:** keep the asset in place for now. Treat any later move as a coordinated migration: update both project references to `../../archive/unused/cover.txt` and verify the Autumn layout and Winter handoff against the relocated asset before calling it unused.

No files were changed.