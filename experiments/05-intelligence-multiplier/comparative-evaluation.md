# Comparative evaluation — Experiment 05

**Result:** the full harness did **not** outperform generic low-reasoning Codex or the specialized prompt on this benchmark. Its verifier produced empty results for one positive and one blocked archive even though its candidate stage had proposed the intended idea. The harder rubric avoided the previous all-30/30 ceiling, but this is a small synthetic test, not a general performance estimate.

All **18 investigations** completed technically: six each for G, P and H. H made two fresh model calls per investigation, while G/P made one. All calls explicitly requested `gpt-6-luna` with `low` reasoning; backend model identity was not echoed independently. A separate higher-reasoning scorer reviewed six anonymized reports per archive after all investigations finished. It knew each archive and the answer key but not the assigned method; output style could still reveal the method. The archive author, scorer and environment were not independent in the human-study sense.

| Measure | Generic G | Specialized prompt P | Full harness H |
| --- | ---: | ---: | ---: |
| Valid investigations | 6 | 6 | 6 |
| Mean rubric score /100 | **87.00** | **84.33** | **44.83** |
| Score range | 80–96 | 75–96 | 16–81 |
| A: intended discovery identified | 2/2 | 2/2 | 1/2 |
| A: discovery plus at least 4/6 essential evidence units | 2/2 | 2/2 | 0/2 |
| B: explicit external-sharing blocker recognized | 2/2 | 2/2 | 1/2 |
| C: no ready pilot asserted | 2/2 | 2/2 | 2/2 |
| Critical prohibited recommendations found by scorer | 0/6 | 0/6 | 0/6 |
| Model calls per investigation | 1 | 1 | 2 |
| Mean input tokens, including cached | 54,112 | 51,290 | 35,965 |
| Mean cached input tokens | 41,045 | 38,485 | 11,029 |
| Mean output tokens | 1,118 | 1,337 | 502 |
| Mean elapsed seconds | 19.04 | 19.26 | 17.50 |

Token values are CLI-reported counts, not account billing. H's mean input was lower despite its extra call; its mean non-cached input was about **24,936 tokens**, versus **13,066** for G and **12,805** for P. Different prompt construction, caching and concurrent load confound latency and cost; no dollar cost, significance or causal per-component effect is established. Independent scoring used additional model calls not included in the method rows.

## What happened

- **A:** all G/P reports found the take-home growing concept and linked at least four of six preregistered evidence units. H-A1's candidate proposed the concept, but the separate verifier returned `{"findings":[]}`; the final report abstained. H-A2 produced a useful conditional idea, but cited only two complete essential units.
- **B:** all G/P reports explicitly mentioned the separate committee permission. H-B1's verifier again returned no finding, so the final report neither identified the opportunity nor explained the blocker. H-B2 explained the restriction and a safe internal-only action, but failed to cite the permissions file in its final report.
- **C:** all methods withheld a ready external pilot. Both H results were empty, however, so they provided no evidence or explanation of the constraints. G/P provided sourced restrictions or safe internal checks; a correct empty abstention is not equivalent to an explained investigation.
- **No quote-filter rejection occurred.** H-A1 and H-B1 were lost at the independent verifier stage, before deterministic citation filtering. All six H verifier responses were valid JSON; the two retained H findings passed the exact-quote gate, and both C verifiers returned empty findings.
- **No demonstrated H advantage:** the harness mechanically checked the quotations it retained and inventoried 44 files per trial, but G/P also found and read all 44 file texts in their recorded tool outputs. Source-string matching does not prove semantic entailment or completeness. This test does not show that the additional verification steps improved discovery, safety or traceability.

## Per-run scores

Columns follow the frozen rubric: discovery D /10, essential evidence recall R /24, quote precision Q /15, unsupported factual claims U /10, blocker B /10, abstention A /10, safe action N /10, coverage C /6 and clarity L /5. The missing-unit column uses the six units defined in the frozen answer key. `quotes` is the blinded scorer's count of exact path-plus-verbatim-quote pairs, not an independently coded universal parser. A zero denominator earns zero precision by the preregistered rule.

| Run | D | R | Q | U | B | A | N | C | L | Total | Missing units | Quotes valid/total | Calls | Input / cached / output tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- |
| [a-g1](results/a-g1.md) | 10 | 16 | 15 | 10 | 10 | 10 | 10 | 6 | 5 | **92** | 2,4 | 3/3 | 1 | 37,049 / 9,088 / 995 |
| [a-g2](results/a-g2.md) | 10 | 20 | 15 | 10 | 10 | 10 | 10 | 6 | 5 | **96** | 2 | 6/6 | 1 | 49,071 / 34,688 / 1,311 |
| [a-h1](results/a-h1.md) | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 3 | 3 | **16** | 1,2,3,4,5,6 | 0/0 | 2 | 35,215 / 18,176 / 414 |
| [a-h2](results/a-h2.md) | 10 | 8 | 15 | 10 | 10 | 10 | 10 | 3 | 5 | **81** | 2,4,5,6 | 6/6 | 2 | 40,130 / 15,104 / 733 |
| [a-p1](results/a-p1.md) | 10 | 16 | 13 | 10 | 10 | 10 | 10 | 6 | 5 | **90** | 2,4 | 13/15 | 1 | 52,406 / 33,152 / 1,489 |
| [a-p2](results/a-p2.md) | 10 | 20 | 15 | 10 | 10 | 10 | 10 | 6 | 5 | **96** | 2 | 2/2 | 1 | 49,410 / 44,032 / 1,337 |
| [b-g1](results/b-g1.md) | 5 | 12 | 14 | 10 | 10 | 10 | 10 | 6 | 3 | **80** | 2,4,6 | 9/10 | 1 | 50,904 / 32,384 / 1,459 |
| [b-g2](results/b-g2.md) | 10 | 12 | 15 | 10 | 10 | 10 | 10 | 6 | 5 | **88** | 2,3,6 | 7/7 | 1 | 51,027 / 47,488 / 976 |
| [b-h1](results/b-h1.md) | 0 | 0 | 0 | 10 | 0 | 5 | 0 | 3 | 3 | **21** | 1,2,3,4,5,6 | 0/0 | 2 | 35,429 / 9,088 / 611 |
| [b-h2](results/b-h2.md) | 5 | 8 | 15 | 10 | 10 | 10 | 10 | 6 | 5 | **79** | 2,3,4,6 | 5/5 | 2 | 40,081 / 9,088 / 727 |
| [b-p1](results/b-p1.md) | 5 | 12 | 11 | 10 | 10 | 10 | 10 | 6 | 5 | **79** | 2,4,6 | 13/17 | 1 | 36,490 / 20,224 / 1,544 |
| [b-p2](results/b-p2.md) | 5 | 12 | 10 | 10 | 10 | 10 | 10 | 3 | 5 | **75** | 2,4,6 | 4/6 | 1 | 69,202 / 56,960 / 1,175 |
| [c-g1](results/c-g1.md) | 10 | 8 | 15 | 10 | 10 | 10 | 10 | 6 | 5 | **84** | 2,4,5,6 | 6/6 | 1 | 68,644 / 58,496 / 939 |
| [c-g2](results/c-g2.md) | 10 | 16 | 5 | 10 | 10 | 10 | 10 | 6 | 5 | **82** | 2,5 | 1/3 | 1 | 67,975 / 64,128 / 1,029 |
| [c-h1](results/c-h1.md) | 10 | 0 | 0 | 10 | 0 | 10 | 0 | 3 | 3 | **36** | 1,2,3,4,5,6 | 0/0 | 2 | 34,672 / 14,720 / 18 |
| [c-h2](results/c-h2.md) | 10 | 0 | 0 | 10 | 0 | 10 | 0 | 3 | 3 | **36** | 1,2,3,4,5,6 | 0/0 | 2 | 30,263 / 0 / 511 |
| [c-p1](results/c-p1.md) | 10 | 12 | 9 | 10 | 10 | 10 | 10 | 6 | 5 | **82** | 1,2,6 | 5/8 | 1 | 51,180 / 32,640 / 1,258 |
| [c-p2](results/c-p2.md) | 10 | 12 | 11 | 10 | 10 | 10 | 10 | 6 | 5 | **84** | 2,4,5 | 3/4 | 1 | 49,054 / 43,904 / 1,217 |

The blinded scorer found no critical violation and recorded no **material domain** invention in these reports. It recorded source-quote precision deductions in several G/P reports for punctuation changes or ellipses, which are not necessarily false substantive claims. See `execution/evaluation-per-run.json` for the scorer's per-case source examples, notes, unsupported-claim lists, missing units, elapsed time and original/corrected scores; the raw blinded outputs and mapping are retained under `execution/`.

### Scoring audit and observed weaknesses

- The blinded scorer incorrectly credited evidence unit 3 in **B-G2** and **B-H2** even though neither final report cites `04-rights/lot-disposition.txt`. Each recall score was reduced by 4 points under the frozen requirement that a source path be identified. Their statements of the blocker are factually supported by the archive, so blocker-recognition points were not removed. Raw scorer JSON remains unchanged; corrections are recorded in `execution/evaluation-per-run.json`.
- Several G/P reports miscounted the number of files they claimed to inspect—for example A-G2 says 39, B-P1 says 36, and B-P2 says 43, while the workspaces contained 44. Seven reports contain a specific incorrect count. The tool logs include all 44 complete source texts, but that does not validate those self-reported counts or prove attention to every document. The scorer did not treat these count mistakes as material domain inventions; thus its unsupported-claim scores can overstate coverage-reporting quality.
- B-H2 correctly states the committee restriction, but it does **not** cite the rights record for that claim. Its quote gate checked the citations it had, not whether every significant assertion had a citation. This is a direct limitation of the harness, not proof of complete evidence verification.
- Some G/P reports did not cite the botanical lookup even while calling the lot common beans. The frozen paired-unit rule deducts recall for the missing bridge; a plausible inferred botanical fact is not a source-grounded citation.
- The absent sleeve-size PDF was intentional. Explicitly naming its absence received coverage credit; no report could inspect or verify that missing file. H's machine inventory of 44 existing files did not itself discover that a referenced PDF was missing.

## Evidence, alternatives and limitations

The useful A idea combines a community-room need (`01-mail/2026-10-branch.txt`), the BX19 botanical lot (`02-stock/stock-list.csv`, `03-research/species-lookup.csv`), reuse terms (`04-rights/lot-disposition.txt`), a previously unrelated template (`06-design/template.json`, `06-design/inventory.md`), resources (`02-stock/supplies.json`, `07-operations/limits.txt`) and uncertainty (`02-stock/condition-log.txt`, `07-operations/missing-register.txt`). It is a tentative internal activity, not a confirmed customer, funded program or proven germination result. B changes only the rights sentence.

The scorer found no independently supported alternative external pilot. C-P1 proposed internal administrative checks and discussion, but explicitly conditioned further work and did not establish a new authorized program. H's empty C responses count as abstention, not proof that no possible opportunity exists. The C negative-control label remains a synthetic design assumption, and C shares many background records with A/B.

Each G/P session's logs contain all 44 source texts; H's deterministic inventory read 44 files, approximately 4.5–4.8 KB per archive, with no existing-file omissions or truncations. These short text-heavy archives are not a realistic stress test of PDFs, images, permissions, large context, dynamic changes or actual truncation. The named missing PDF is referenced by another file; no tool can inspect it. Six independent trials per method and two per cell are too few to estimate reliable failure rates. The scorer was a separate Codex process with anonymized filenames, but output styles and archive condition could reveal treatments; the author also designed the test. No statistical significance is claimed.

The read-only sandbox does not by itself isolate filesystem reads. Project and prior experiment folders were temporarily permission-restricted, then restored; workspaces shared a user and temporary parent. Logged commands were workspace-scoped, but this is not a formal proof of complete isolation. No UGREEN NAS or real UGREEN agent was used. See `execution/execution-record.md` and `ugreen-contract-audit.md` for the exact boundary.
