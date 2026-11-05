# Family Recipe Detective — local proof

## Actual test

The fixture contains a **synthetic image** of a printed card, a gathering note, a fictional owner-provided transcript supplied as text, and an unrelated tea note. The attached card says one cup milk; the supplied transcript says one cup water. The gathering note supplies two eggs. No source gives baking time or temperature. The original audio is deliberately unavailable; no AI transcription of audio occurred.

Two fresh local `codex exec` processes were given the same fiction, user request, files and **actual attached image**, requested model `gpt-6.1-terra` and low reasoning effort. One received the complete frozen Skill and references; one received only the ordinary request and common safety instructions. Full source: [local runner](run_local_test.py); [Skill hashes](skill-hashes.json); [generic prompt/response/logs](results/generic/); [Skill prompt/response/logs](results/skill/). Each exited 0, returned a response and left fixture hashes unchanged.

The runs used disposable copies and read-only instructions with `danger-full-access` because the local read-only shell sandbox was unavailable. That is not OS-enforced isolation or proven network isolation. The real image was attached directly to Codex; this is not evidence that UGREEN's `vision-ocr`, photo-agent, knowledge-agent or a NAS processed it. File paths in raw output use temporary locations and are not established as permanent or clickable UGREEN citations.

### What happened

- **Skill-guided:** produced an incomplete recipe draft, attributed flour/apples to the card and note, kept eggs tied to the gathering note, displayed **milk versus water** with source identifiers, explicitly said the source transcript was supplied as text and the original audio was missing, and asked for the missing full method, pan, time and temperature. It rejected the unrelated tea's ginger.
- **Generic:** also identified milk versus water, the missing temperature/time and the unrelated tea, and asked the user to check additional ingredients and steps. It did not establish that the Skill discovered the main conflict uniquely.
- **Assessment:** the Skill offers a reusable procedure and a clear conflict/coverage presentation. These two small runs do not establish reliability, user preference, better reasoning, greater convenience, real creative novelty or usefulness compared with recipe-specific apps.

The [illustrative preview image](illustrative-recipe-preview.png) was made separately from these fixture facts with [local research code](render_example.py). It is **not** a Skill-generated visual, an album, a saved NAS document, or a real family recipe. It exists to make the proposed user experience easy to inspect. The recipe is incomplete and must not be treated as cooking instructions.

## Official static check

Command: `node /mnt/c/Users/RkLop/.codex/skills/uliya-skill-kit/scripts/check-skill.mjs prototype/family-recipe-detective`. [Final result](static-check.json): **static-pass, zero errors, zero warnings**. Earlier warning-bearing checks are preserved. This is structural validation only.

## Not tested

No real audio, UGREEN OCR, image expert handoff, valid UGREEN photo identity, album creation, album membership/order, saved recipe, no-overwrite semantics, platform approval, permission resumption, or physical device was tested. The optional write/album flows must stop if the required safety behavior and real result are not established. No final contest ZIP, proposal, or publication was created.
