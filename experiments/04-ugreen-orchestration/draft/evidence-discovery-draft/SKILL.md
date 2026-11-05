---
name: evidence-discovery-draft
description: An evidence-grounded discovery with source references and constraints when a user asks to investigate an authorized folder.
---

# Goal

Investigate a user-authorized folder on demand for one potentially useful, unexpected cross-file possibility. Explain the supporting sources, uncertainty, coverage limitations, decisive blockers and a safe next step. Treat the result as a hypothesis, not verified usefulness or permission to act. The response is shown to the user; this workflow does not write, share, move or delete files.

# Required input

Request the authorized folder and any user-provided objective or limits. Use only the explicitly authorized scope. If the user does not supply scope, wait for the user. Do not expand scope or request credentials.

# Generation-time capability evidence

- `ug-filesystem` → `file-agent`
- `ug-document` → `document-agent`
- `ug-knowledge` → `knowledge-agent`

# Orchestration

1. Delegate the scoped inventory to the file expert. Include the user's actual authorized scope and limits in the final instruction; request actual matching paths, coverage and any access failures. Never infer paths or treat an empty result as evidence of absence outside the scope.

`delegate --target file-agent --instruction 'Find files in the user-authorized folder for a bounded evidence investigation and report real paths, scope coverage and access failures.'`

2. Only after `completed` and a real nonempty inventory, pass verified business results from the inventory to the document expert. Include the actual returned paths, user scope, objective and limits in the assembled instruction. Ask it to read and compare relevant content, including contrary facts, and return source-grounded facts, excerpts, document coverage and any inaccessible, unsupported or truncated material. Do not assert that all content was read when coverage is unknown.

`delegate --target document-agent --instruction 'Read and compare the real files returned by the scoped inventory, identify useful and conflicting evidence, and report source references, coverage and read failures.'`

3. Only after `completed` with sufficient real document results, pass verified business results from that step to the knowledge expert. Include actual paths and the candidate investigation objective in the assembled instruction. Ask for evidence and counterevidence within the same authorized scope, identifying real sources, coverage and failures. Never manufacture citations or replace a missing source with a similar one.

`delegate --target knowledge-agent --instruction 'Collect supporting and contrary evidence for the scoped investigation from the real returned files and report sources, coverage, missing evidence and failures.'`

4. Synthesize at most one useful cross-file hypothesis from completed, source-grounded expert results. Provide exact source references and the supporting details, scope and coverage limits, what is uncertain, any critical blocker, and a safe next action. If evidence does not support a discovery, say so; if a blocker exists, do not recommend the blocked action. If meaningful coverage or provenance is missing, explicitly say the result is provisional or cannot be established. Do not claim the experts performed an action they did not report.

# Completion and failure

Treat `completed` as eligible for the next step only when its required actual business results are present; an empty result ends the investigation without broadening scope. For `failed` or `cancelled`, stop dependent steps and report the state and any verified partial evidence. For `waiting_user`, stop and ask only for the information needed to continue. For `waiting_approval`, stop and surface the pending approval without proceeding or bypassing the platform. If a result is incomplete, retain its verified evidence and report the limitation; never promote it into a confident discovery. Do not save reports or modify files as part of this workflow.
