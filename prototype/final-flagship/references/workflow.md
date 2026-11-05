# Workflow and decision rules

All steps are read-only. User-supplied paths and scope are necessary inputs, not permission to search elsewhere. Ask the owner to resolve ambiguous target identity before evaluating that target. Do not read the contents of excluded files even when their names appear in authorized records.

## 1. Focus the investigation

Record the selected item, change, actual destination/new name if relevant, authorized search roots and constraints. Check the target with `file-agent` using documented `ug-filesystem` operations and ask it to return observed paths, limits, failures and potential reference-bearing candidates. If target is missing or inaccessible, report the uncertainty; do not state that the intended change will or will not break anything. For a folder, name the scope of returned contents rather than assuming every descendant was examined.

## 2. Find and resolve references

Ask `file-agent` for a bounded candidate inventory based on target path, filename and user-supplied contextual clues. Ask `document-agent` to read actual selected candidates and distinguish:

- **Exact or path-resolved reference:** evidence explicitly points to the target, subject to supported path context.
- **Ambiguous match:** a matching filename or phrase does not identify the target uniquely.
- **Historical/context-only:** source discusses an item or old project without establishing current use.
- **Contrary evidence:** source qualifies, replaces, or rules out an apparent dependency.
- **Unknown:** document not read, result unavailable, incomplete scope or live application behavior not observable.

Request exact source paths and excerpts where returned, preserve the raw substance of the evidence, and distinguish a quoted reference from its interpretation. Do not equate a real quote with proof that an application will fail. Only describe a consequence as observed when an actual returned record supports it; otherwise label it conditional or unknown. Seek a narrow contrary check via `knowledge-agent` only when it may change the proposed action. Do not falsely claim all references or applications have been examined.

## 3. When comparing copies

On user request, check explicitly identified authorized copies. If child results provide hashes for each, compare those hashes as observations at that time. Equal SHA-256 is strong evidence of matching bytes, not proof of same role. Different hashes do not establish which version is newer or correct. Inspect returned records for each copy's role; absence of a reference in the bounded scan does not prove no role. If a source indicates the same content is used by two projects, explain the specific source-backed relationship rather than treating either path as redundant. Do not assume inaccessible or unselected copies are covered.

## 4. Prepare the decision

Rank actual directly supported possible consequences above name-only matches; put unknowns beside the relevant claim. Present an appropriate next action, such as verifying an ambiguous reference or asking an application owner. If the desired change conflicts with an observed reference, advise preserving the item until the user resolves the conflict. If no supporting evidence is returned, report the limited search and ask for a more useful authorized scope only if justified. Never execute a change. A repeat request starts a fresh check: do not assume old results remain current, a persistent cache exists, or a previous result proves today's state.
