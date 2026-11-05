# Failure analysis

## H unnecessarily abstained on A and B

In A-H1, candidate generation produced a relevant growing-activity hypothesis, but the independent verifier returned `{"findings":[]}`. B-H1 similarly produced two candidate hypotheses and identified the sharing restriction, but its verifier returned no findings. These were technically successful model calls and valid JSON; they are **substantive false-negative outcomes**, not transport failures. The harness's deterministic quote filter rejected no candidates in these runs because the verifier returned none. No retry was attempted. The reason the verifier discarded them is not observable in the final response; attributing it to excessive caution is a hypothesis, not a proven causal explanation.

C-H1 and C-H2 also returned no findings; that matches the negative-control disposition, but the empty reports provide no source-grounded explanation of the barriers. The harness can therefore make the right binary choice while failing the product's evidence-grounded reporting objective.

## H can miss a citation for a key claim

B-H2 correctly stated that BX19 cannot be shared externally without committee approval but did not cite `04-rights/lot-disposition.txt`. The verifier's JSON supplied five valid quotations from other sources; the mechanical gate checked those quotes, not whether every material assertion was supported. Thus exact quote matching is necessary but not sufficient for grounded conclusions. A genuine improvement would require claim-level mapping and semantic review, itself unproven and potentially more expensive.

## Coverage-reporting mistakes

Every G/P event log contains all 44 archive file texts, yet seven reports asserted incorrect file counts (36, 39, 40 or 43). These are mistakes in self-reported coverage, not proof that the input was absent. The blinded scorer treated them as non-material to the domain claims and did not deduct unsupported-fact points; this is a weakness in both output quality and the score's interpretation. H recorded the 44 visible files mechanically but did not flag the referenced, missing sleeve-size PDF solely from inventory.

## Missing provenance and evaluation limits

All methods frequently omitted the `Phaseolus vulgaris` / common bean lookup pair when naming the lot. The rubric correctly deducts the essential-source unit; a plausible fact inferred by a language model is not equivalent to citing the provided source. B-G2 and B-H2 were initially credited by the scorer for an uncited rights source; those two scores were corrected mechanically and raw scorer outputs preserved.

The independent scorer was anonymized by case name, not fully blind: report style and its knowledge of archive condition could expose treatment. The designer authored both data and rubric; no human independently reviewed all claims. Some precision deductions reflect strict punctuation rather than substantive misrepresentation. C is not proof of impossibility and shares many background records with A/B. The test used 44 short text files, no unreadable actual PDF and no NAS. No conclusions about significant differences or real-world safety follow.
