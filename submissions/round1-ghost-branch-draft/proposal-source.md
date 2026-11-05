# Ghost Branch — Round 1 proposal draft

Ten substantive answers: 297 words.

## 1. What does the Skill do?
Ghost Branch investigates potentially forgotten software work in authorized NAS project archives and prepares an evidence-backed recovery handoff.

## 2. Who is the target user and what is their problem?
Developers may have old experiments, source snapshots, screenshots and review notes scattered across backups, making useful unfinished work and reasons it was abandoned difficult to find together.

## 3. What is the solution?
The Skill proposes candidates, checks available current-project evidence, searches for objections or replacements, and classifies work as worth investigating, retired, uncertain or not established.

## 4. What is the main user flow?
The owner authorizes current and archived folders and asks for discovery, a specific feature investigation, or a recovery packet. The Skill requests bounded source analysis, presents evidence and gaps, and drafts a coding-agent handoff.

## 5. How does it differ from existing tools or common AI?
It focuses on artifacts outside a repository and combines positive evidence with reasons not to revive a feature. Git history and generic AI can overlap; local generic agents also found the central synthetic examples.

## 6. Which UGREEN AI NAS features does it use, and when?
File-agent discovers and reads authorized snapshots; document-agent compares selected notes and source evidence; photo-agent may inspect a screenshot; knowledge-agent may collect evidence or, with approval, save a reviewed packet.

## 7. What is the technical approach?
Markdown instructions direct registered experts to documented ug-filesystem, ug-document, ug-photo and ug-knowledge operations. The user authorizes scope. Saving is optional and approval-gated. Model provider and any external processing depend on device configuration.

## 8. What is built and what needs testing?
The Skill and linked references pass official static checking. Fresh local Codex trials on a fictional archive compare short, detailed and Skill-guided prompts. No UGREEN expert or NAS has run the workflow; source propagation and coverage remain unverified.

## 9. How will finalists test the Skill?
Test a potentially useful old export and a deliberately retired login experiment. Edge case: a decisive review note lies outside the authorized scope; report uncertainty and request access only if useful.

## 10. What are the known limitations?
Ghost Branch cannot execute Git or code, create branches, run tests, or prove repository-wide absence. Safe saving, expert output formats, large archives, screenshots, permissions and actual NAS behavior require validation.

## Disclosures
OpenAI Codex assisted with research, design, writing and local testing. The Skill ZIP includes no third-party libraries, executable code or service integration. UGREEN Uliya and its registered experts are platform dependencies. The entrant must verify ownership, competition eligibility, model/data handling and any other required AI or third-party disclosures.
ReportLab (BSD license, https://www.reportlab.com/) generated this PDF; pypdf (BSD-3-Clause, https://github.com/py-pdf/pypdf) checked its text. Neither is included in the Skill package.
