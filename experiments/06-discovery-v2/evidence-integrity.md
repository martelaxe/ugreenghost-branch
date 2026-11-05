# Evidence integrity

## What V2 actually does

The local engine retains an unchanged copy of every candidate, including its original citations, blocker text and proposed action, in its internal result. The public report is built separately and does **not** promote the original unreviewed action. A missing/empty/malformed review produces a labeled unverified candidate, not a false rejection or silent deletion. A candidate without at least two retrieved matching source paths is `INSUFFICIENT EVIDENCE` in this research prototype; two paths are a conservative local heuristic, not an official UGREEN requirement or a guarantee of independent facts.

Each illustrative evidence record carries a source path, excerpt, retrieval indicator, exact-match result, asserted relation to a claim and a semantic-assessment label. A blocker can be `BLOCKED` only when its source and quote were retrieved and a supplied reviewer explicitly assesses that quote as supporting the blocker. An uncited restriction stays unverified and prevents `SUPPORTED`. A reviewed contradiction can yield `REJECTED` only with a matching retrieved source; the original candidate remains internal.

A later mocked review can attach an additional source: the H-B1 regression attaches the actual archived rights passage and produces a sourced `BLOCKED` result while preserving the original candidate. This review is supplied by the test; the engine did not autonomously discover or semantically verify that source.

The engine records inventory paths and counts from the local filesystem, selected/read paths, skipped/failed items, byte limit, truncation and PDF-basename references not found in the observed inventory. It always states that coverage outside the observed local scope is unknown. The missing-reference scan is intentionally narrow: it can miss references, cannot inspect a missing file, and a basename match does not establish identity or access.

## What it does not verify

An exact substring check establishes only correspondence with returned local text. The semantic assessments in the tests and examples are supplied fixtures; no actual semantic verifier, model or independent expert runs in V2. A false semantic judgment, omitted blocker or misleading source can still lead to an incorrect state. `SUPPORTED` means the specified *mock checks* passed for a qualified, non-executing next step; it does not prove truth, source authenticity, usefulness, exhaustive blocker search or permission for an external action. A real deployment must surface these limitations.

The simulated expert handoff uses illustrative `status`, `paths`, `documents`, `complete`, and `reviews` fields. Those are research fixtures, **not UGREEN response contracts**. The actual kit's contract gaps are documented in [Experiment 05's audit](/home/martelaxe/ugreen-hackathon/experiments/05-intelligence-multiplier/ugreen-contract-audit.md:1). In particular, it is unknown whether real experts return retrievable quotes, reliable completeness/truncation indicators, or source IDs that survive handoff.

The local path checks reject obvious traversal and symlinks but do not provide a security boundary against filesystem races, hard links or permissions changes. They are not a substitute for NAS access controls. No modification, sharing or outreach is performed by the engine.
