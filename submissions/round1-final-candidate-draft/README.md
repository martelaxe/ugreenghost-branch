# Round 1 draft — human review required

- [Proposal PDF](proposal-draft.pdf), [editable source](proposal-source.md), [extracted text](proposal-extracted.txt).
- [Skill ZIP](skill-draft.zip): only `SKILL.md` and three directly linked `references/*.md` files; no fixture, code, binary, secret or separate manifest.
- [Verification](package-verification.json): 282 substantive words across ten answers; PDF 3,851 bytes; ZIP 6,903 bytes; 13,903 bytes uncompressed, four files, each <1 MB. PDF text extracts all ten headings. ZIP CRC check passed.
- [Official checker](../../experiments/final-flagship-tests/static-check.json): `static-pass`, zero errors/warnings, catalog 2.0.0, on `prototype/final-flagship/`. The identical file hashes were checked against the ZIP. This is not runtime validation.
- AI assistance and third-party platform dependency are disclosed in the package and proposal. ReportLab and pypdf were used only to produce/check the PDF, not added to the Skill. PDF is for review and the entrant must verify all content and links.
- The ordinary and Skill prompts found the main normal-case evidence; Skill caught one ambiguous detail on an authored restricted fixture. No comparative general advantage or actual UGREEN execution is established.
- **Eligibility/newness**: the [rules](https://ugreenhackathon.devpost.com/rules) permit pre-existing ideas but require the submitted Skill and core workflow to be newly developed during the hackathon. This new package was authored during the session and uses earlier design ideas; the entrant must verify dates, substantial workflow originality, ownership and compliance. Do not assume a rewritten file alone proves eligibility.
- Finalist testing must validate real expert results, scoped access, source propagation, bounded discovery, hash mapping and permission behavior. The read-only Skill never executes a file change.

Not uploaded, published, submitted, committed or pushed. These are review drafts, not a representation of submission readiness or hardware success.
