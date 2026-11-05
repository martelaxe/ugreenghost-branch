# Limitations and open questions

1. The real expert-result schemas, semantics of completeness/truncation, and source-reference granularity are not established by the catalog. All mock inner fields and delegation-envelope nesting are illustrative, not confirmed contracts.
2. No model or actual NAS expert was used. The candidate is hard-coded and scenario-specific; the simulation demonstrates guarded reporting, not unexpected discovery or generalized decision making.
3. The scope check is only lexical in the mock. Real server-side authorization, symlinks, permission-denied records, partial listings and race conditions are untested.
4. Exact mock text matching verifies consistency with supplied strings, not the truth of underlying documents, semantic entailment, the completeness of findings, or authority to act.
5. With no documented machine-readable proof of complete inventory and read coverage, a real implementation may need to report coverage as unknown even when calls return success. A missing relevant source may be undiscoverable without external knowledge.
6. The parent response method, actual model capability, runtime delegation substitutions, evidence context limits, CSV/PDF handling and multi-expert provenance are unverified. The static checker cannot validate these.
7. The pending-approval case is defensive. Cataloged read actions list `approval: none`; actual user/approval states and permissions may differ. No persistence, filesystem action, notification or outreach is included.
8. A static-pass draft is not a ready-to-submit package, runtime compatibility proof, install proof, or evidence of meaningful discovery. No ZIP was created.
