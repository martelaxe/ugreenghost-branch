# 90-second primary storyboard

**Prepared fictional files:** `projects/harbor/project-manifest.txt` cites `projects/harbor/assets/launch-cover.txt` and a SHA-256; `shared/copy_17.txt` and `shared/review_17.txt` match; `shared/old_cover.txt` is a different red draft; `projects/meadow/project.txt` references `shared/review_17.txt`. Full 26-file fixture and hashes are in the experiment directory. Confirm whether actual UGREEN document and file experts can read text and return paths/checksums.

- 0–15s: show Harbor’s documented missing path and say: “Find the missing Harbor cover and restore one matching copy without disturbing the other project. You may inspect this fixture archive and propose a copy into Harbor assets.” Show the authorized folder and absence.
- 15–35s: file-agent discovers real paths and hashes; document-agent provides manifest and Meadow reference. Show exact returned evidence, not mocked UI. Explain the two similar names and why the referenced shared file remains.
- 35–55s: user sees exact copy source/destination and no-overwrite condition; grants explicit approval. Show the platform gateway approval if actually presented. If unclear whether collision protection is enforceable, stop.
- 55–75s: `file-agent` executes a copy only after actual approvals. Show real file listing; use independent post-action stat/hash against pre-action source; visually show source still exists. Label unverified results honestly.
- 75–90s: show `Meadow` reference unchanged, hashes equal, and external/printer dependencies unknown; no claim of app launch or complete restoration.

Failure path: owner rejects or platform pauses → show no copy; if readback fails, show “copy reported; verification unavailable,” not success. Local Python has performed an analogous safe exclusive copy and comparison; Codex trials are read-only. No device, actual platform UI/approvals or expert responses have been tested. No custom interface or automatic rollback is assumed.
