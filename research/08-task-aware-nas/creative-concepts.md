# 24 creative concepts

Research date 2026-10-26. F = file-agent; D = document-agent; K = knowledge-agent; P = photo-agent; mappings and limits are in [capability feasibility](capability-feasibility.md). All inputs are user-selected/authorized, outputs are text unless explicitly marked; no actual device, rendering, write, or automatic external action is implied. Natural-language triggers are proposed, not observed user demand. Related user evidence is in [new user evidence](new-user-evidence.md); the concept-specific solution and its value are hypotheses. Generic Codex can already perform each text interpretation if it has the same inputs; photo use also needs a model with suitable image access. Competitor names indicate nearest relevant class, not an exhaustive search.

## Grounded and useful

### 01. Missing Piece

**User / problem:** bookkeeper; monthly report can miss required invoice. **Trigger:** “Prepare my quarterly support-invoice report.” **Inputs:** contract, current invoices, authorized archive folders. **Output:** cited report, expected gaps and candidate. **Distinctive interaction / example:** find a matching invoice elsewhere and exclude wrong-year one.

**UGREEN candidates:** F D K. **Closest comparator:** invoice-agent. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** missing prerequisite inferred without evidence.

### 02. Change-Safe Report

**User / problem:** team analyst; multiple versions change report totals. **Trigger:** “Report totals and show what changes if this revision is accepted.” **Inputs:** draft invoice, revision, approval policy. **Output:** two conditional totals and decision request. **Distinctive interaction / example:** same invoice produces two clearly labeled outcomes.

**UGREEN candidates:** F D K. **Closest comparator:** Excel Copilot. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** a provisional scenario is presented as final.

### 03. Receipt Crosscheck

**User / problem:** small business; transaction has no supporting receipt. **Trigger:** “Prepare a receipt coverage list for these transactions.” **Inputs:** transactions, receipt files, expense policy. **Output:** matched and unresolved list with cited rationale. **Distinctive interaction / example:** a payment date matches a receipt for another merchant.

**UGREEN candidates:** F D K. **Closest comparator:** invoice-agent. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** false positive identity match.

### 04. Scan Page Completeness

**User / problem:** family archivist; digitized records can omit pages. **Trigger:** “Check whether these scanned documents meet their stated page counts.” **Inputs:** scan text/page count, user manifest or page references. **Output:** review list distinguishing known gaps and unknown totals. **Distinctive interaction / example:** page 3 is expected by an index but not located.

**UGREEN candidates:** F D K. **Closest comparator:** Paperless-ngx. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** no reliable original page-count evidence.

### 05. Release Checklist

**User / problem:** photographer; photo reuse requires permissions. **Trigger:** “List these assets and any documented limitations.” **Inputs:** asset manifest, releases, use brief. **Output:** source-linked use/hold/unknown checklist. **Distinctive interaction / example:** attractive image has an exclusion clause.

**UGREEN candidates:** F D K P. **Closest comparator:** Adobe Stock/DAM. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** confusing subject or overclaiming legal clearance.

### 06. Repair Prep

**User / problem:** homeowner; repair details are scattered. **Trigger:** “Prepare a technician handoff for my appliance.” **Inputs:** manual, purchase receipt, service notes. **Output:** model and service evidence with unknowns. **Distinctive interaction / example:** service note belongs to a different model.

**UGREEN candidates:** F D K. **Closest comparator:** HomeMemory. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** wrong model match or unsafe technical instructions.

### 07. Project Handoff

**User / problem:** freelancer; teammate cannot understand a project folder. **Trigger:** “Prepare a project handoff from this folder.” **Inputs:** brief, delivery list, status notes. **Output:** cited delivery map and unresolved responsibilities. **Distinctive interaction / example:** latest handoff still names a missing draft.

**UGREEN candidates:** F D K. **Closest comparator:** Nextcloud Assistant. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** stale task status mistaken as current.

### 08. Coverage Contract

**User / problem:** researcher; report hides what was not read. **Trigger:** “Summarize this topic and show what was actually reviewed.” **Inputs:** selected documents, explicit scope, extraction results. **Output:** cited summary with supported and unresolved claims. **Distinctive interaction / example:** one inaccessible source changes the confidence in a conclusion.

**UGREEN candidates:** F D K. **Closest comparator:** Open WebUI. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** real experts omit source or coverage signals.

## Surprising combinations

### 09. Creative Salvage

**User / problem:** independent filmmaker; abandoned projects contain unused material but rights and context are scattered. **Trigger:** “Use my old work to suggest a feasible new pitch.” **Inputs:** project notes, asset list, release terms, new brief. **Output:** two creative pitch options with evidence and hold states. **Distinctive interaction / example:** a rejected scene becomes a new premise but its featured image is restricted.

**UGREEN candidates:** F D K optionally P. **Closest comparator:** MemoryJam / creative DAM. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** unverifiable rights or generic ideas without creator value.

### 10. Fork & Finish

**User / problem:** analyst; a contested record prevents a useful output. **Trigger:** “Create a report for either plausible interpretation.” **Inputs:** two source versions, criteria and user decision. **Output:** conditional outputs with exact source differences. **Distinctive interaction / example:** a $40 revision changes the total and remains unapproved.

**UGREEN candidates:** F D K. **Closest comparator:** Excel Copilot and generic Codex. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** chat state does not persist or users cannot distinguish branches.

### 11. Lost Media Handoff

**User / problem:** film editor; an old project references media in different folders. **Trigger:** “Prepare a relinking checklist for this project manifest.” **Inputs:** human-readable project manifest, file inventory, editor notes. **Output:** possible path matches and unresolved assets. **Distinctive interaction / example:** the clip exists under an old delivery name.

**UGREEN candidates:** F D. **Closest comparator:** Premiere relink media. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** proprietary project parsing or actual relinking unsupported.

### 12. Time Travel Interview

**User / problem:** family historian; a photo date conflicts with a dated note. **Trigger:** “Help me ask my family about this photo.” **Inputs:** photo, metadata, dated letter. **Output:** open question with alternative dates and sources. **Distinctive interaction / example:** two sources disagree so a relative becomes the missing witness.

**UGREEN candidates:** P D K. **Closest comparator:** MemoryJam. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** same-person or event link is wrong.

### 13. Exception or Error

**User / problem:** admin; absence can be legitimate rather than a missing document. **Trigger:** “Prepare a monthly compliance checklist.” **Inputs:** schedule, exception note, reports. **Output:** each period with required/not required/unknown status. **Distinctive interaction / example:** missing February is an explicit planned shutdown.

**UGREEN candidates:** F D K. **Closest comparator:** invoice-agent. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** policy exceptions are incomplete or out of date.

### 14. Rehearsed Recovery

**User / problem:** home server owner; another person cannot follow recovery notes. **Trigger:** “Give my successor a recovery practice question.” **Inputs:** recovery notes, contact instructions, selected scope. **Output:** exercise card with evidence and unresolved steps. **Distinctive interaction / example:** a supposedly complete handoff lacks the location of a key.

**UGREEN candidates:** F D K. **Closest comparator:** Microsoft digital legacy. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** exercise falsely certifies real recoverability.

### 15. Contextual Duplicate

**User / problem:** archivist; exact copies have different roles. **Trigger:** “Why are these copies kept?.” **Inputs:** candidate hashes, path inventory, human role notes. **Output:** copy relationships and unresolved intent. **Distinctive interaction / example:** the same file is a project dependency in one location.

**UGREEN candidates:** F D K. **Closest comparator:** Immich duplicates. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** hash fails to establish intended role.

### 16. Research Crossroads

**User / problem:** genealogy researcher; two plausible identities fit incomplete documents. **Trigger:** “Show what would distinguish these two ancestors.” **Inputs:** two certificates, place notes, research question. **Output:** comparison and next evidence request. **Distinctive interaction / example:** same name belongs to two separate people.

**UGREEN candidates:** F D K. **Closest comparator:** genealogy platforms. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** unwarranted identity merge.

## Experimental and unconventional

### 17. Counterfactual Exhibition

**User / problem:** museum volunteer; a planned exhibition lacks permission for one item. **Trigger:** “Give me two exhibition outlines from approved records.” **Inputs:** catalog notes, item descriptions, restriction. **Output:** two text outlines, each labeled by allowed assets. **Distinctive interaction / example:** the exclusion changes the exhibition theme.

**UGREEN candidates:** F D K P. **Closest comparator:** museum DAM. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** rights uncertainty or missing assets.

### 18. Unwritten Chapter

**User / problem:** oral-history researcher; archive cannot answer a meaningful question. **Trigger:** “What should I ask while building this life timeline?.” **Inputs:** timeline notes, known photo metadata, interview transcript. **Output:** prioritized open questions linked to unexplained evidence. **Distinctive interaction / example:** a long gap between dated jobs invites a human question.

**UGREEN candidates:** F D K P. **Closest comparator:** MemoryJam. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** question implies unsupported private story.

### 19. Claim Versus Counterclaim

**User / problem:** educator; teaching sources disagree. **Trigger:** “Build a debate handout from these sources.” **Inputs:** two historical accounts, source notes, curriculum brief. **Output:** evidence-linked positions plus unresolved factual dispute. **Distinctive interaction / example:** each source dates the same event differently.

**UGREEN candidates:** F D K. **Closest comparator:** NotebookLM. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** fabricated equivalence or misleading quotation.

### 20. Abandoned Prototype Remix

**User / problem:** maker; unused project notes hide a build idea. **Trigger:** “Suggest a safe project using these abandoned notes.” **Inputs:** design notes, parts list, safety limitations. **Output:** textual concept and missing prerequisites. **Distinctive interaction / example:** two unrelated spare parts fit a low-risk display concept.

**UGREEN candidates:** F D K. **Closest comparator:** generic Codex. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** invention impossible or unsafe without technical verification.

### 21. Personal Archive Challenge

**User / problem:** household; owner overestimates what someone else can find. **Trigger:** “Test whether my notes answer a simple handoff task.” **Inputs:** owner task, household notes, optional explicit expected records. **Output:** question-and-evidence exercise for a second person. **Distinctive interaction / example:** successor realizes an emergency contact is only a nickname.

**UGREEN candidates:** F D K. **Closest comparator:** digital legacy services. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** generated task lacks real user usefulness.

### 22. Archive Triage Route

**User / problem:** conservator; old file formats need future access plans. **Trigger:** “Which selected files deserve access review first?.” **Inputs:** file list/extensions, known format note, user priorities. **Output:** review priorities with unknown openability. **Distinctive interaction / example:** a small old project file is the only record of a family event.

**UGREEN candidates:** F D K. **Closest comparator:** digital preservation tools. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** filename extension is mistaken for proof of failure.

### 23. What Would Change My Mind?

**User / problem:** researcher; an ambiguous decision has multiple possible resolutions. **Trigger:** “What evidence would distinguish these interpretations?.” **Inputs:** conflicting records, decision criteria, authorized collection. **Output:** two hypotheses and the next discriminating source or question. **Distinctive interaction / example:** one short missing field would separate lookalike cases.

**UGREEN candidates:** F D K. **Closest comparator:** Open Deep Research. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** invented evidence requirement or inaccessible source.

### 24. Permitted Creative Detour

**User / problem:** designer; one resource has an explicit reuse blocker. **Trigger:** “Find an alternative way to meet this brief.” **Inputs:** brief, asset notes, restriction and independent asset list. **Output:** two proposed routes with sources and uncertainty. **Distinctive interaction / example:** a blocked photograph leads to a different source-backed concept.

**UGREEN candidates:** F D K P. **Closest comparator:** creative DAM. **Generic Codex:** could attempt the same task from supplied sources; any NAS convenience or quality gain is untested. **Failure assumption:** alternate also lacks permission or proposal is generic.
