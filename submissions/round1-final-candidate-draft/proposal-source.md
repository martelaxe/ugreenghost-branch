# Before You Move — Round 1 proposal draft

Exactly ten substantive answers; word count: 282

## 1. What does the Skill do?
Before You Move previews evidence of what a proposed file change might affect.

## 2. Who is the target user and problem?
NAS owners consolidate or reorganize long-lived files but may not know which projects use a particular copy.

## 3. What is the solution?
A read-only investigation distinguishes direct references, ambiguous matches, different copy roles and unknown dependencies before the owner decides.

## 4. What is the core user flow?
The owner identifies the target, proposed change and authorized folders. The Skill searches within those bounds, examines relevant references, optionally compares chosen copies, and presents evidence, limitations and a safe next step.

## 5. How does it differ from existing tools or common AI?
It packages a focused pre-change procedure: a byte-identical copy is not assumed to have the same role, and unsearched or unverified dependencies remain visible. Generic AI can perform similar reasoning; we have not established superiority.

## 6. Which UGREEN AI NAS capabilities does it use?
The file expert discovers and reads selected paths and optionally hashes copies. The document expert examines references. The knowledge expert may seek supporting and contrary evidence.

## 7. What is the technical approach?
The Markdown Skill delegates only to registered experts using documented filesystem, document and knowledge operations. The owner authorizes the scope. The core makes no changes. Model and any external processing depend on device configuration.

## 8. What is built and what needs testing?
The Skill instructions pass the official static checker. Independent local Codex tests on fictional files compared ordinary and Skill-guided requests; neither used UGREEN agents. Actual device execution, source propagation and coverage remain unverified.

## 9. What will finalists test?
First, inspect an asset before a proposed move when two documents reference it. Second, compare identical copies with one referenced role and one unknown role. Edge case: an essential reference lies outside the authorized scope; request authorization and report uncertainty.

## 10. What are the limitations and dependencies?
The Skill cannot observe all applications or prove a deletion safe. It does not move files, restore backups or maintain a dependency graph. Expert result formats, completeness and configured model behavior require hardware testing.

## Disclosures
OpenAI Codex assisted with research, drafting, design and local testing. The Skill package contains no external libraries or executable components. It depends on the UGREEN Uliya platform and its registered experts; applicable UGREEN terms apply. The configured AI model/provider is not fixed by the Skill and may process authorized content externally.
ReportLab (BSD license; https://www.reportlab.com/) was used solely to generate this PDF, and pypdf (BSD-3-Clause; https://github.com/py-pdf/pypdf) to check its extracted text; neither is included in the Skill package. Entrant must review ownership, eligibility, development timing and disclosures before submission.
