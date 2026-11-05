# Ghost Branch — Round 1 draft

**Decision: SUBMIT WITH RESERVATIONS** if the entrant chooses to participate. This is a draft for human review, not a submitted entry.

## Submission files

- [Proposal PDF](ghost-branch-proposal.pdf): 297 English words across the ten substantive answers, one page, 3,945 bytes.
- [Skill ZIP](ghost-branch-skill.zip): 8,286 bytes; one `SKILL.md` and four directly linked Markdown references, 16,437 bytes uncompressed. No executable scripts, binary assets, fixtures or separate manifests.
- [Editable proposal](proposal-source.md), [extracted PDF text](proposal-extracted.txt), [package and hash verification](package-verification.json).

## Checks and important limitations

- [Official static checker](../../experiments/ghost-branch/static-check.json): `static-pass`, zero errors/warnings; checked hashes match the ZIP. Static checking is not NAS runtime validation.
- The synthetic local comparison found the useful CSV prototype, an explicitly rejected authentication experiment, and a title filter already represented in current files. Generic and detailed Codex also found the central results. [Test report](../../experiments/ghost-branch/test-report.md).
- Actual UGREEN expert outputs, code support, source-reference propagation, image inspection, complete search coverage and optional save/approval behavior remain unknown. Several local Skill-generated citations were not portable from the saved reports. The Skill does not run code, Git, tests or external services and does not create a branch.
- One local canary probe showed the short generic condition read a **synthetic** credential value into its tool trace while the detailed and Skill conditions did not. It was not included in any final response. This is one test, not a security guarantee.
- The entrant must verify personal eligibility, ownership, whether the submitted Skill and core workflow were newly developed during the competition, and complete AI and third-party disclosures. No such determination can be made from a static check.

## Next steps for the entrant

Review the two files, complete the project form on [Devpost](https://ugreenhackathon.devpost.com/) and choose a suitable track such as Open Innovation. The [official rules](https://ugreenhackathon.devpost.com/rules) set the Round 1 deadline at **November 15, 2026, 11:45 p.m. Pacific**. Round 1 does not require a NAS or demo video. Finalists receive one assigned remote testing day and must submit a working Skill and actual demo video for the same project.

Nothing has been uploaded, published, submitted, committed or pushed.
