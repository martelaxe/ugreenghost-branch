# Boundaries: package, documented platform and outside applications

The installed `references/skill-format.md` permits root Markdown with directly linked Markdown references and says not to add scripts, binaries, manifests or sidecars. The question is not whether a NAS running Linux *could* support a tool: the question is whether this Skill may rely on it in the documented environment. “Not documented” is not proof it is impossible for all external software.

| Capability | A. In this Skill package | B. Documented experts | C. Independent external application | Status |
|---|---|---|---|---|
| Arbitrary Python, ffmpeg, code or custom processor | **Not permitted** executable Skill files | No arbitrary process/shell/ffmpeg action | May exist outside Skill, subject to separate environment and contest rules; no integration contract established | Hard package constraint; device availability UNKNOWN |
| Custom HTML, web server or interactive UI | No HTML/JS package under this standard | No host/open/custom UI action | An external application may host one separately; not evidence it is finalist-compatible | Unsupported as native Skill feature |
| Install services, persistent database, watchers, schedules | No executables/services | No service install, database, timer or watcher operation | Other software may support them independently | Unsupported through catalog |
| Filesystem overlay, snapshots, RAID repair, low-level state | No implementation in Markdown | No cataloged primitive | System or other software may support it; no Skill API claimed | Unsupported in catalog, hardware/product may have unrelated features |
| Audio/video waveform sync, clips or generated audiovisual media | No custom processor | Media search/control, subtitle search/download, transcription and media info only; no waveform sync/render | External apps may do these, e.g. editors | Unsupported through catalog |
| Content generation and persistence | Markdown may request an expert | `writing`/`translate` mixed gateway; `save-text` workflow; album creation workflow | External editors also possible | DOCUMENTED WITH CONDITIONS; returned outputs/runtime unknown |
| Atomic no-overwrite | Instructions can demand it, not enforce | `cpmv overwrite` parameter, not atomic semantics; other writes likewise lack guarantees | Some filesystems offer exclusive create but not documented through these agents | UNKNOWN; stop if required safety cannot be established |
| Platform approval | Cannot pre-grant in Skill | gateway/workflow/conditional labels; `waiting_approval` state | User/platform actually decides | DOCUMENTED process label; resume/approval UI unknown |
| Verified successful write | Can instruct verification | Child completion and some summary fields; optional readback/hashes if exposed | Independent check possible | CONDITIONAL; never claim before actual completed evidence |
| External AI/model, network and local-only privacy | No implicit provider guarantee | Catalog does not specify all provider/network/data flow | Depends on environment | UNKNOWN; do not claim offline/private solely because storage is on NAS |

No hard ban on every external app in the general universe is implied; this audit only establishes the installed Skill format and documented expert boundary. Actual finalist device access may resolve unverified results, but it does not create a new cataloged API automatically.
