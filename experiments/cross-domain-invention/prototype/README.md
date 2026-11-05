# Local prototype: blind listening with capture-evidence gate

Open `index.html` locally in a modern browser. Choose the pair with known settings, listen to both four-second clips, then vote. Choose the pair with a missing microphone identifier to see the gate refuse that comparison. The first pair's left/right assignment is randomized in JavaScript; choose “I'm unsure” if preferred. This is a research interaction, not an experiment with valid scientific conclusions.

## What is actually present

- `audio/sample-a.wav`, `sample-b.wav`, `sample-c.wav`: **synthetic**, deterministic tone/noise signals, not garden, bird, human, equipment or field recordings. A has two generated tones and B four; C has two, with a deliberately missing fixture microphone ID.
- `generate_fixtures.py`: standard-library-only generator. It uses a fixed random seed and writes WAV files; `audio/sha256.json` records hashes. The source is at `data.js`: the capture metadata are fictional labels written by the author, not measured facts.
- `engine.js`: equality checks for microphone, position, gain, sample rate and duration; random-order state is assembled separately. `app.js` gates the controls on that result, tracks the user's play requests and shows the mapping only after both simulated play promises have succeeded and the user chooses. Browser metadata, source URLs and scripts remain inspectable: this is **casual masking, not secure blinding**.
- `test.js`: deterministic tests of incomplete/mismatched fields, order, status and invalid choice. `test-ui.js`: exercises interface code against a mocked DOM and audio object; it does not play sound in a real browser. The WAV headers and SHA-256 hashes were checked with Python. No actual user listened, and no ecological or causal conclusion was generated.

## The designed intervention

The experiment is not sound recognition. It forces one useful decision: when a comparison's essential capture condition is unknown, the workflow stops instead of allowing an apparently scientific before/after claim. When listed fields match, a blind listening exercise becomes available, followed by provenance and explicit caveats. Even then, it is **not proof of a controlled comparison**. The checker does not inspect actual environment, calibration, weather, distance, noise, sampling strategy, recording quality, metadata truthfulness or file validity at runtime. It cannot establish cause, biodiversity, trends or statistical significance. It currently assumes valid local fixture paths; playback errors are displayed.

Try:

1. Pair with known settings → listen to both → choose → inspect the revealed mapping.
2. Pair with missing microphone → observe that the listen and answer controls are unavailable.

This is a local HTML/JavaScript/Python implementation, not a UGREEN Skill, NAS execution, AI system, real-world dataset or user validation. It randomizes display order but is not a validated randomized trial, level-matched test, tamper-proof blind or secure privacy system. Samples are generated with different tone content and are deliberately easy to tell apart; loudness may reveal conditions.

## Verification performed

From this directory run `node test.js` and `node test-ui.js`, and `node --check engine.js && node --check app.js`. On 2026-10-27 the state tests and mocked interface test passed. Python's `wave` module confirmed all three WAVs are mono, 16-bit, 16 kHz, four seconds and match `audio/sha256.json`. Actual browser audio rendering and real-user experience were not verified in this environment. A mocked `Audio.play()` resolving is not proof of playback on the user's device.

Sources and competitor analysis: [prior art](../../../research/cross-domain-invention/prior-art.md); [decision](../../../docs/cross-domain-invention-decision.md).
