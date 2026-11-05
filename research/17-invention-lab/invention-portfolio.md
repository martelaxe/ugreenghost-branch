# Invention portfolio: first-pass conceptual ranking

Research checked 2026-10-27. Ranked by the author for surprise and distinctive behavior, **not** feasibility; these are hypotheses, not invented research findings or global novelty claims. Methods: A cross-domain collision; B inverted assumption; C missing primitive; D unusual request; E research tension. Sources are linked in [Skills frontier](agent-skills-frontier.md), [storage frontier](storage-frontier.md), and the six-concept [prior-art hunt](prior-art-red-team.md). Distinctions among categories overlap.

## 1. Consent-Bearing Object

- **Categories and invention method:** storage, A+C
- **Invention:** A file grants a narrow operation, then denies future calls when its owner withdraws permission.
- **User request:** Let my family hear this story for a month, but not download the recording.
- **Surprising result:** A previously working story request stops after a policy change.
- **Technical mechanism:** Policy-mediated object, revocable gateway, protected execution and leak-aware audit.
- **Research inspiration:** YoloFS; Tahoe; MFM
- **Closest known prior art:** Tahoe-LAFS capabilities, Solid access control, DRM
- **What might be new:** Combining selective AI operations with independently revocable household context; no novelty established.
- **Why it matters:** Families may share outcomes without distributing whole archives.
- **Failure condition:** A reader records the output; enforcement or keys fail; consent changes.
- **UGREEN fragment:** Beyond current catalog; local toy gate is bypassable.

## 2. What-If Exhibit

- **Categories and invention method:** storage, B+C
- **Invention:** A story keeps its beats while a user removes an input class and it selects backed alternatives or shows a gap.
- **User request:** Rebuild this three-moment exhibit without red artwork.
- **Surprising result:** A three-panel display swaps two panels while keeping the ending.
- **Technical mechanism:** Role-to-alternative constraints, provenance, explicit excluded sets, recompose or leave empty.
- **Research inspiration:** lakeFS; archival graph; SkillCAT
- **Closest known prior art:** photo book swaps, smart albums, Publish-Safe Photo Review, Script to Selects
- **What might be new:** Preserving an explicit sequence under counterfactual exclusions with visible gaps is the proposed combination.
- **Why it matters:** A creator needs to adapt a collection without manually rediscovering every alternative.
- **Failure condition:** Metadata is wrong, a substitute changes meaning, or no suitable alternative exists.
- **UGREEN fragment:** On-demand candidate selection and optional approved album are documented in outline; reactive rebuilding and ordering are not.

## 3. One-Bit Workshop

- **Categories and invention method:** skill, D
- **Invention:** Turn source-backed alternative procedures into a one-question-at-a-time physical decision interaction.
- **User request:** Help me make this sign; ask only what changes the next step.
- **Surprising result:** The NAS asks about available materials, then offers an actionable route.
- **Technical mechanism:** Build alternatives and missing preconditions; select a question that partitions feasible choices; wait for answer.
- **Research inspiration:** Skill-Use; SkillCAT
- **Closest known prior art:** ordinary AI tutors, decision trees, Nextcloud Assistant
- **What might be new:** A tested, source-grounded question-selection contract may improve an interaction; improvement not shown.
- **Why it matters:** Someone can turn scattered how-to notes into a usable live procedure.
- **Failure condition:** Wrong prerequisites, fabricated sources, irrelevant questions or unsafe advice.
- **UGREEN fragment:** File/document agents can provide evidence; interactive state and fidelity remain unverified.

## 4. Alternative Past Room

- **Categories and invention method:** storage, A+C
- **Invention:** Open an archive through a counterfactual branch where selected facts are explicitly unknown, not deleted.
- **User request:** Show what I could have concluded before I saw that email.
- **Surprising result:** A reconstructed reading view omits future evidence yet exposes a timestamp boundary.
- **Technical mechanism:** Bitemporal constraints, immutable versions, evidence-as-of access.
- **Research inspiration:** lakeFS; DataLad; archival graph
- **Closest known prior art:** Git time travel, bitemporal databases, LLM RAG filtering
- **What might be new:** Consumer-accessible evidence-bounded counterfactual without treating it as real history.
- **Why it matters:** Revisiting a decision needs the information available at the time.
- **Failure condition:** Timestamps are missing or do not indicate availability; hindsight contaminates model.
- **UGREEN fragment:** Only bounded simulations from explicit dates; no universal historic snapshot.

## 5. Evidence-Sensitive Keepsake

- **Categories and invention method:** storage, A+E
- **Invention:** A keepsake becomes visibly incomplete when one evidentiary source is unavailable.
- **User request:** Let me show this family story only while its sources remain available.
- **Surprising result:** A story tile turns into a marked gap instead of silently retaining a claim.
- **Technical mechanism:** Dependency-tracked source references and on-demand revalidation.
- **Research inspiration:** archival graph; SkillCAT
- **Closest known prior art:** data lineage, reactive notebooks, provenance systems
- **What might be new:** Family-facing view of evidence degradation; building blocks established.
- **Why it matters:** It prevents mistaken confidence as sources disappear.
- **Failure condition:** Revoked source cannot be unread; a stale exported copy persists.
- **UGREEN fragment:** Manual rerun and explanation only; no automatic invalidation established.

## 6. Memory Compost

- **Categories and invention method:** storage, B
- **Invention:** Preserve the lesson while quarantining personal episodes under separately granted rules.
- **User request:** Keep the repair lesson but hide my family photos.
- **Surprising result:** A new reusable procedure points to a restricted witness without copying it.
- **Technical mechanism:** Data minimization, provenance and capability-separated views.
- **Research inspiration:** MFM; Tahoe
- **Closest known prior art:** privacy-preserving summaries, knowledge distillation
- **What might be new:** Explicitly separable proof and operational lesson, not assured by summarization.
- **Why it matters:** Useful learning without indiscriminate distribution of raw memories.
- **Failure condition:** Derived text leaks sensitive information or bypasses permission.
- **UGREEN fragment:** Proposal only; no isolation or controlled declassification guaranteed.

## 7. Archive Weather

- **Categories and invention method:** storage, A
- **Invention:** An archive exposes a forecast of which collections are likely to become unreadable.
- **User request:** Which keepsakes are becoming impossible to open?
- **Surprising result:** A risk view changes when a file format, app or dependency becomes unavailable.
- **Technical mechanism:** Preservation-format identification and dependency/availability observations.
- **Research inspiration:** born-digital archival workflow
- **Closest known prior art:** PRONOM, digital preservation monitoring
- **What might be new:** Personal-facing dependency forecast plus actionable uncertainty.
- **Why it matters:** Owners can preserve files before their software disappears.
- **Failure condition:** Format signatures do not prove readability; false urgency.
- **UGREEN fragment:** Manual evidence review plausible; actual format registry/runtime support unverified.

## 8. Trial Branch

- **Categories and invention method:** storage, C
- **Invention:** A requested operation runs in a staged private filesystem branch, then the user inspects its effects.
- **User request:** Try reorganizing this but keep the real archive untouched.
- **Surprising result:** A preview shows file changes; discard or commit.
- **Technical mechanism:** Copy-on-write filesystem staging and effect log.
- **Research inspiration:** YoloFS; lakeFS
- **Closest known prior art:** YoloFS directly, git branches, snapshots
- **What might be new:** Household-specific semantics may improve UX; base mechanism already exists.
- **Why it matters:** Owner can safely see consequences before a risky action.
- **Failure condition:** Untracked external effects and leakage cannot be undone.
- **UGREEN fragment:** No documented branch/commit primitive; proposal/mock only.

## 9. Personal Receipt Compiler

- **Categories and invention method:** skill, A
- **Invention:** Compile a household practice into a procedure with preconditions and a source-backed test.
- **User request:** Turn my old notes into an energy-saving setup I can try safely.
- **Surprising result:** A runnable-by-human procedure branches on explicit observations.
- **Technical mechanism:** Extract candidates, map prerequisite to source, exercise against synthetic negative cases.
- **Research inspiration:** SkillFoundry; SkillCAT
- **Closest known prior art:** how-to AI, knowledge bases, instruction-generation skills
- **What might be new:** Joint traceable derivation and attempted falsification; generic assistants can already do much.
- **Why it matters:** A neglected archive becomes a reusable practice.
- **Failure condition:** Old notes omit hazards and unknown facts appear certain.
- **UGREEN fragment:** Read-only documented file/document experts; writing optional and approval-gated.

## 10. Skill Quarantine

- **Categories and invention method:** skill, C+E
- **Invention:** A proposed new Skill remains inert until it survives challenge cases.
- **User request:** Teach the NAS my way, but test it before adopting it.
- **Surprising result:** A candidate procedure and failed test remain visibly separate from approved instructions.
- **Technical mechanism:** Contrast trajectories, regression tests, scoped admission and human approval.
- **Research inspiration:** SkillCAT; dynamic skill survey
- **Closest known prior art:** SkillFoundry, CI, skill registries
- **What might be new:** Personal NAS governance interface, not new self-evolution.
- **Why it matters:** Bad learned routines should not silently become authority.
- **Failure condition:** Prompt-only quarantine is not runtime access control.
- **UGREEN fragment:** Can draft and critique text; auto-admission, sandbox tests and persistent isolation not documented.

## 11. Witness Relay

- **Categories and invention method:** skill, A
- **Invention:** Separate an extractor, a skeptic and a narrator so every narrative line survives a challenge.
- **User request:** Tell our story but let the archive challenge you first.
- **Surprising result:** A usable story card omits unsupported claims and shows missing beats.
- **Technical mechanism:** Role separation, challenge requests and evidence-backed admission.
- **Research inspiration:** SkillsBench; archival graph
- **Closest known prior art:** multi-agent debate, RAG verification
- **What might be new:** Explicit challenge-driven content admission, but common multi-agent pattern.
- **Why it matters:** Family stories can be shared with visible uncertainty.
- **Failure condition:** All agents share the same biases or references fail.
- **UGREEN fragment:** File/document experts and parent reasoning plausible; truly independent agents not promised.

## 12. Procedure With Expiry

- **Categories and invention method:** skill, C
- **Invention:** A stored procedure carries explicit conditions that must still hold before its next step.
- **User request:** Walk me through the repair, but stop if the equipment changed.
- **Surprising result:** A live guidance session pauses at an unresolved precondition.
- **Technical mechanism:** State-machine contracts, user observations and source-linked instructions.
- **Research inspiration:** Skill-Use; PAE
- **Closest known prior art:** workflow engines, SOP software, assistants
- **What might be new:** Portable source-linked checks, not the idea of a checklist itself.
- **Why it matters:** Old personal instructions become less dangerous to follow.
- **Failure condition:** No live sensors, missing safety details, generic advice.
- **UGREEN fragment:** Read-only expert retrieval and interactive states plausibly documented.

## 13. Disagreement Dial

- **Categories and invention method:** skill, B
- **Invention:** The user adjusts how much contradictory source evidence an answer must survive.
- **User request:** Show only steps that work under either version of the notes.
- **Surprising result:** A practical decision narrows or stops when assumptions change.
- **Technical mechanism:** Robust optimization across source-supported hypotheses.
- **Research inspiration:** SkillCAT; temporal datasets
- **Closest known prior art:** robust decision analysis, RAG comparisons
- **What might be new:** A user-visible robustness control over personal procedures.
- **Why it matters:** People can see when they rely on an uncertain assumption.
- **Failure condition:** An invented alternative or incomplete coverage misleads.
- **UGREEN fragment:** Document-agent analysis and parent branching; no guaranteed semantic verifier.

## 14. Proof-Carrying Recipe

- **Categories and invention method:** skill, A
- **Invention:** Each procedure step carries its provenance and the smallest test that could invalidate it.
- **User request:** Can I really reproduce Dad’s lamp setup?
- **Surprising result:** A step-by-step instruction pauses when a required part is absent.
- **Technical mechanism:** Proof obligations and step preconditions, not mathematical proofs.
- **Research inspiration:** SkillFoundry; archival graph
- **Closest known prior art:** workflow contracts, proof-carrying code, AI instructions
- **What might be new:** User-facing household recipe with original evidence and invalidation.
- **Why it matters:** Shows gaps before following an old method.
- **Failure condition:** Proof terminology overstates informal evidence or safety.
- **UGREEN fragment:** Read-only procedure proposed; no hardware control.

## 15. Collective Amnesia Negotiator

- **Categories and invention method:** cross-domain, A+D
- **Invention:** Household members privately express what may be used; a broker returns a shared artifact under their constraints.
- **User request:** Make a family story everyone permits, without showing me the hidden material.
- **Surprising result:** A shared view includes only jointly approved material.
- **Technical mechanism:** Access policies, provenance and constrained recomposition.
- **Research inspiration:** Tahoe; YoloFS; archival redaction
- **Closest known prior art:** Solid pods, permissioned collaboration, privacy-preserving computation
- **What might be new:** Negotiating a multi-owner story with a view-level capability is a hypothesis.
- **Why it matters:** Shared archives have multiple owners and conflicting consent.
- **Failure condition:** Prompted filtering leaks data; consent not automatically enforceable.
- **UGREEN fragment:** Beyond documented security model; mock only.

## 16. Museum of Alternate Uses

- **Categories and invention method:** cross-domain, A
- **Invention:** Turn archived instructions into a hands-on exploration of other uses, with every suggested combination tested for conflicts.
- **User request:** What can we build with what is already here?
- **Surprising result:** A source-grounded assembly plan and an explicit missing piece.
- **Technical mechanism:** Resource allocation plus constraint satisfaction, physical-world verification.
- **Research inspiration:** SkillFoundry; provenance
- **Closest known prior art:** maker-project generators, AI brainstorming
- **What might be new:** A resource-backed, testable action rather than generic idea.
- **Why it matters:** Old tools and material can be put to new use.
- **Failure condition:** Permissions, missing supplies, physical safety.
- **UGREEN fragment:** Documents can be read; physical state and safety require humans.

## 17. Forgetting That Leaves a Hole

- **Categories and invention method:** cross-domain, B+C
- **Invention:** Revoke access to one episode while leaving a non-identifying warning that continuity is incomplete.
- **User request:** Hide that memory but warn me when it is needed for context.
- **Surprising result:** A story shows an intentional gap instead of inventing continuity.
- **Technical mechanism:** Redaction tombstones, provenance edges and controlled views.
- **Research inspiration:** archival redaction; temporal databases
- **Closest known prior art:** redacted archives, tombstones, access control
- **What might be new:** Consumer-facing contextual gap across generated views.
- **Why it matters:** Supports changing personal boundaries without rewriting every artifact.
- **Failure condition:** A tombstone itself leaks existence; old exports cannot be recalled.
- **UGREEN fragment:** Textual gap in an on-demand answer only; enforcement unsupported.

## 18. Future Curator Simulator

- **Categories and invention method:** cross-domain, D
- **Invention:** A future recipient attempts to use a preserved collection and reveals which meaning or equipment is missing.
- **User request:** Will my grandchildren know how to play this recording?
- **Surprising result:** A simulated playback attempt yields a missing format/tool clue.
- **Technical mechanism:** Digital preservation dependencies plus role-constrained simulation.
- **Research inspiration:** born-digital archival workflow; MFM
- **Closest known prior art:** digital preservation planning, succession rehearsal
- **What might be new:** Operational preservation test rather than an imagined emotional letter.
- **Why it matters:** A file is useless if no future reader can interpret it.
- **Failure condition:** Simulation is not proof a future app or human can recover content.
- **UGREEN fragment:** Can reason from documented evidence, but cannot test hypothetical future software.

## 19. Household Data Treaty

- **Categories and invention method:** cross-domain, A+C
- **Invention:** Several NAS owners grant narrow temporary uses through machine-checkable policies.
- **User request:** Let our neighbors use our garden photos only for the shared seed guide.
- **Surprising result:** An operation returns approved references while full stores stay separate.
- **Technical mechanism:** Federated policy enforcement and capability negotiation.
- **Research inspiration:** Tahoe; distributed systems
- **Closest known prior art:** Solid pods, federated identity, access control
- **What might be new:** Cross-household purpose restriction plus generated artifacts.
- **Why it matters:** Shared knowledge without uncontrolled full archive copies.
- **Failure condition:** Purpose limitation cannot stop a recipient remembering information.
- **UGREEN fragment:** No documented remote federation or trusted policy enforcement.

## 20. Decision Fossil

- **Categories and invention method:** cross-domain, A
- **Invention:** Store not only the chosen result but what information and options were available at that moment.
- **User request:** What did we reasonably know when we booked the venue?
- **Surprising result:** A versioned decision replays available alternatives without hindsight.
- **Technical mechanism:** Bitemporal records, explicit observation cutoffs, decision provenance.
- **Research inspiration:** lakeFS; archival graph
- **Closest known prior art:** temporal databases, decision logs, Git
- **What might be new:** Personal evidence-bounded replay with clear unknowns.
- **Why it matters:** Explains decisions without judging them by information learned later.
- **Failure condition:** Archive timestamps do not prove knowledge or access.
- **UGREEN fragment:** Only a bounded manual reproduction if explicit records exist.

## 21. Uncertainty Budget

- **Categories and invention method:** cross-domain, C
- **Invention:** Assign each generated artifact a maximum acceptable number of unsupported beats.
- **User request:** Give me a 3-panel exhibit, but never invent a missing moment.
- **Surprising result:** A visible blank panel replaces unsupported content.
- **Technical mechanism:** Constrained generation, source eligibility and unknown-state propagation.
- **Research inspiration:** SkillCAT; archival provenance
- **Closest known prior art:** RAG citations, proof obligations, structured generation
- **What might be new:** A visible artifact with explicit holes under a specified coverage policy.
- **Why it matters:** People can choose incomplete honesty over fluent fiction.
- **Failure condition:** Model hides uncertainty or source coverage is incomplete.
- **UGREEN fragment:** Parent can request and expose gaps; no guaranteed verifier.

## 22. A File That Interviews Its Future Reader

- **Categories and invention method:** cross-domain, D
- **Invention:** A preserved object asks the minimum questions needed to become usable by an unknown future reader.
- **User request:** My parents left an old craft pattern. Help me follow it with what I have.
- **Surprising result:** The reader is asked a branching question and receives only the next evidence-backed action.
- **Technical mechanism:** Active learning, constraint-based procedural compilation, reader feedback.
- **Research inspiration:** Skill-Use; MFM
- **Closest known prior art:** interactive AI tutoring, choose-your-path instructions
- **What might be new:** An archive-bound decision protocol, not a novel conversational UI.
- **Why it matters:** It turns static material into activity for an inexperienced person.
- **Failure condition:** Outdated guidance can be unsafe; the AI invents conditions.
- **UGREEN fragment:** File/document agents plus parent interaction plausibly support a bounded version.

