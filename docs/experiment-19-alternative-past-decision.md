# Experiment 19 — Alternative Past Room

**Verdict: WEAK.** The local prototype makes a meaningful evidentiary change visible, and the separated THEN agent did not reveal the later correction. But a competent generic Codex agent, given the same full archive, reconstructed the same essential distinction. The reveal is an effective presentation of conventional point-in-time evidence analysis—not a demonstrated new storage mechanism or a proven advantage over existing temporal systems.

## The actual scenario and cutoff

This is an **author-created fictional archive**, not a real historical incident. At **2024-09-12 23:59 UTC**, the community board's shared archive contained an official order naming Harbor Reading Room at **27 Alder Street** and describing a blocked exit. A receipt showed the order entered the archive; board minutes recorded that the chair read its location and exit concern. Before the decision, someone had questioned whether it concerned the Reading Room or Harbor Annex, and the city desk said to follow the order pending clarification. The board temporarily moved children's reading sessions to a school hall, with longer walks and transport costs unresolved. Eleven records and a fictional snapshot attestation establish what this test supplies as available; they do not show what every person read or believed.

A fresh [THEN agent](../experiments/19-alternative-past/runs/THEN/response.md) saw only that separated snapshot. It described a precautionary temporary relocation under an unresolved location question, along with the costs and alternative actions. It did not suggest a permanent closure or claim to know the room's actual physical condition. It was not told the later outcome.

## The reveal and revised interpretation

On September 20–23, new records entered the fictional archive: the inspector's fieldbook and photo ledger identified the inspected location as **72 Alder Street, Harbor Annex**; a city correction said the original order had transposed the address. A fresh [NOW agent](../experiments/19-alternative-past/runs/NOW-P/response.md) concluded that the order had misidentified the Reading Room. That changes the factual explanation for the move: the official inspection on which the order was based concerned the other building.

It does **not** make the earlier archive contain the correction, prove that the board knew the address was wrong, or establish that the Reading Room was safe on September 12. An October 4 inspection found its exit clear only on that later date. The most surprising reveal is that a decision which could look foolish in hindsight followed a formal notice whose location had already been questioned but not yet clarified. The [interactive view](../experiments/19-alternative-past/visual-review/index.html) presents the order, correction and revised account in three steps; the [overview](../experiments/19-alternative-past/visual-review/overview.png) shows all three at once.

## Temporal adversarial checks

1. **Hindsight leakage:** the THEN workspace contained 11 attested cutoff records plus its snapshot inventory, with later fixture files physically absent. Its response contained no 72 Alder address, transposition, fieldbook or correction; manual review found no material future fact. Known project and temporary paths were masked, but other host paths and network isolation were not fully verified, so this is not a formal proof of complete isolation.
2. **Backdated document:** both retrospective agents correctly said an August-heading account was written and entered on **October 18**. It was not admitted as September evidence.
3. **Uncertain availability:** both identified the handwritten September 10 carbon as having unknown authorship and receipt. Finding it in October does not prove it existed in the board archive on September 12 or was created after that date.
4. **Irrelevant later evidence:** a separate fresh P run received the same full archive plus a single October poster. It called the poster irrelevant and retained the same central interpretation and safety uncertainty. This is one controlled case, not a general robustness guarantee.

[Execution and evaluation](../experiments/19-alternative-past/evaluation.md) includes the exact prompts, raw outputs and limitations; [mechanical audit](../experiments/19-alternative-past/tests.json) verifies hashes and selected markers. Keyword checks supplement rather than replace the manual interpretation. Four fresh read-only processes completed; G and P received identical full input bytes. The snapshot and receipt attestations were authored for this fictional fixture and are not independently verified real archival history.

## Generic AI and prior art

The [generic retrospective](../experiments/19-alternative-past/runs/NOW-G/response.md) identified the same wrong building, contemporary uncertainty, backdated memo, unknown carbon and limit of the later inspection. The specialized procedure provided a more explicit record-by-record table, but one response per method cannot demonstrate an intelligence advantage. The HTML control reveals the evidence progressively and helps the user experience the change; it does not demonstrate a new database or agent capability. A historical documentary or a temporal query plus a normal assistant could present the same story. The dramatic address error was intentionally authored into the fixture, so the reveal does not demonstrate that comparable surprises are common in personal archives.

The closest prior mechanisms include [XTDB](https://docs.xtdb.com/about/time-in-xtdb.html), which distinguishes valid and system time; [ForeSci](https://arxiv.org/abs/2606.00644), which restricts agent access to cutoff-aligned evidence; and [VersionRAG](https://arxiv.org/abs/2510.08109), which routes retrieval across document versions. These overlap the proposed mechanism substantially. Their existence does not automatically determine product usefulness, but no defensible claim of a novel temporal primitive follows. [Focused prior art](../research/19-alternative-past/prior-art.md).

A person might value this on a NAS because their own dated records, notes and snapshots are stored together, especially for understanding a decision without assuming the participants knew the outcome. That value remains hypothetical: there was no real-user test. A real archive may lack reliable receipt dates, historical versions or access logs; an old document's subject date or file modification time is not proof it was available to the decision-maker.

## UGREEN and decision

A limited faithful version is conceptually possible **if the user provides two authorized, trustworthy dated snapshots and the relevant provenance**: the previously documented file and document experts could inspect them, with clear uncertainty. The installed toolkit has not been shown to provide an authenticated historical-access boundary, bitemporal database, reactive timeline or actual NAS execution. The interactive HTML/Pillow code here is local research software and cannot be included as a Markdown-only Skill. Since the novelty test did not pass, no new Skill was created.

**Recommendation:** end the invention search for this hackathon. The remaining deliberate choice is whether to submit the existing practical Project Rescue candidate, with its unverified NAS copy and approval risks clearly disclosed, or pursue genuinely new storage-system research outside the competition. Do not start Experiment 20 automatically. No submission or publication was made.
