# Local verification results

Date: 2026-10-27. Commands run from the project root:

```
node experiments/cross-domain-invention/prototype/test.js
PASS: 11 state, missing metadata, mismatch, order, reveal and rejection checks

node experiments/cross-domain-invention/prototype/test-ui.js
PASS: simulated UI state transition, early answer blocked, missing metadata blocked, reveal after both play promises

node --check experiments/cross-domain-invention/prototype/engine.js
node --check experiments/cross-domain-invention/prototype/app.js
```

Both syntax checks completed with exit code 0 and no output. The interface test uses a mocked DOM and `Audio` whose play promise resolves; it does not decode or play audio and does not prove a user listened. State permits reveal after both playback **starts**, not after confirmed completion or attention. `Math.random()` gives casual order masking, not an audited randomization protocol. Source filenames and fixture mapping are visible in local developer tools.

Python `wave` inspected all three files: mono, 16-bit PCM, 16 kHz and 64,000 frames (4 seconds); their SHA-256 digests matched `audio/sha256.json`. All inputs are generated: no field recording, real microphone, plant or bird was used. No scientist, NAS, UGREEN agent or participant supplied an outcome. The HTML was queued to open in the Codex browser, but actual browser playback was not verified; if it fails, the UI reports playback error.
