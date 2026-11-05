**Proposed change:** `assets/shared/cover.txt` → `archive/unused/cover.txt`.

**Direct evidence**
- [projects/autumn/program.md:1](/tmp/work/projects/autumn/program.md:1) lists `Cover file: ../../assets/shared/cover.txt`. Resolved relative to that document, this matches the proposed target path. The target remains **unverified** because it is outside scope.
- [projects/autumn/program.md:2](/tmp/work/projects/autumn/program.md:2) states that the program layout refers to this source file and that the exported final PDF is absent from the folder.

**Inferred impact**
- The Autumn Walk program may need its cover reference updated before a future layout edit or export. The document supports a potential dependency; it does not establish that moving the file would break an application.

**Coverage limitations**
- Investigated only `projects/autumn/`: one file discovered, selected and read, within limits of 50 paths and 20 documents.
- The file listing may exclude ignored files; completeness is not established. Neither the target nor destination was inspected. Layout behavior, external copies and dependencies outside scope remain unknown.

**Safe next step:** Leave the move pending. Obtain explicit, narrowly scoped authorization to inspect the target and verify the layout’s reference before deciding whether to move it. No files were modified.