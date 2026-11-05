# Prior art: attack the central interactions

Search and review date 2026-10-27. These comparisons use public research, vendor documentation and repository descriptions. We did not install the competitors or perform a patent search; search results and undated living pages may not establish historical availability. “No exact match found” means only that this targeted search did not find one. None of these is a claim of global novelty.

## 1. Blind listening gated by source conditions — keep provisionally

**Functional searches:** `blind soundscape before after noise monitoring compare paired recordings ABX experiment ecology`; `bioacoustics audio annotation web blind randomized recordings metadata`; `soundscape metadata blind listening paired comparison`.

[ABX](https://github.com/jaakkopasanen/ABX) is an existing web AB/ABX listening test. [Audio ABX Comparator](https://github.com/kelvinlim/audio-compare) describes random blinded X trials with scoring, although its current repository is not verified as of the precise cutoff. Blind playback is not new. [Open Ecoacoustics](https://openecoacoustics.org/) offers ecological recordings and analysis; [bird survey guidelines](https://birdsurveyguidelines.org/acoustic-survey-methods/) explicitly call for recording time, place, microphone and settings; [a PLOS One study](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0253763) compares citizen-science and professional recorders and discusses device/metadata limits. Controlled before/after soundscape studies already exist ([example](https://www.sciencedirect.com/science/article/pii/S0006320725001533)).

**Verdict: strong partial overlap, possible combination; not a new scientific method.** We did not find, in this narrow search, a household-owned system that automatically **blocks a blind listening interaction when specifically required capture metadata are missing**, then reveals source qualifications. An ordinary experimenter can configure a blind test after manually checking metadata; that may eliminate any practical advantage. Matching metadata is not evidence of an experimental control, nor are synthetic sounds evidence of ecology. User usefulness and privacy remain untested.

## 2. Two people compare hearing and haptic interpretations — keep wild with low confidence

**Functional searches:** `sound to haptic touch audio frequency realtime tactile visualization open source deaf accessibility music haptic`; `interspecies communication haptic audio deaf paired listening cross sensory game rhythm`; `haptic rhythm game hearing deaf collaboration`.

[Google audio-to-tactile](https://github.com/google/audio-to-tactile) translates audio to wearable tactile signals; [Sonic Inclusion](https://github.com/indjoov/sonic-inclusion) describes visual/haptic feedback for musicians; [Stanford Haptic Drum-Hero](https://charm.stanford.edu/ME327/2023-Group2) describes a haptic rhythm game; [Seeing Music](https://comma.eecs.qmul.ac.uk/projects/crossmodal/) investigates cross-sensory associations using games. Exact publication timing of some live repository pages is unverified.

**Verdict: close underlying and experiential overlap, possible new combination, uncertain demand.** A specifically **paired, blind comparison in which one participant feels a private recording and another hears it before both commit** was not located in this short search. It may exist. Haptic translation is lossy, human hearing differences vary, and accessibility must be co-designed with disabled participants. Generic blind comparison plus existing haptic tooling may already be sufficient. UGREEN lacks the hardware, real-time processing and independent sessions. Retain only as an ambitious research hypothesis, not an accessible product claim.

## 3. Household/classroom coded physical experiment — keep as field insight, not unique core

**Functional searches:** `scientific self experiment crossover schedule blind controlled N of 1 individual app`; `blind randomized classroom experiment coded samples physical experiment app`; `community science experiment blind condition protocol missing measurement`.

[StudyU](https://pmc.ncbi.nlm.nih.gov/articles/PMC9297132/) implements digital N-of-1 trial design; [UK guidance](https://www.gov.uk/guidance/n-of-1-study-comparative-studies) describes experimental conditions and reversibility. Blinding, procedural randomization and physical experimental notebooks predate NAS AI. An adult-guided classroom exercise can also be performed with paper labels.

**Verdict: existing methodology and close generic software; speculative narrow interaction.** The system could make user-provided recording/measurement constraints active, but there is no evidence that this is better than a teacher and cards. It risks repeating Experiment 17's One-Bit Workshop and 14's task handoff. The concrete difference would have to be a reproducible double-blind physical test and enforceable commitment, neither available in UGREEN's documented Skill runtime. Do not pitch it as a new scientific method.

## 4. Hear your sound in a saved room — reject

**Functional searches:** `convolution reverb user recorded impulse response play audio sounds room`; `sonic museum hear your voice in historical space impulse response virtual acoustics interactive`.

[A university interactive auralization demo](https://mta.hmu.gr/en/research/in-brief-research/research-demos/auralisation/) accepts an uploaded sample and plays it from different positions in a measured auditorium. [Sonic Palimpsest](https://research.kent.ac.uk/sonic-palimpsest/impulse-responses/) provides historical-space impulse responses; [Stanford's Hagia Sophia work](https://arts.stanford.edu/excavating-an-echo/) described capturing and replaying a room's acoustic properties years ago.

**Verdict: central experience already implemented.** The audio effect is compelling but adding a NAS is insufficient differentiation. Reject rather than renaming it. Also, one recorded sound is not automatically an accurate impulse response.

## 5. Personal photo and voice communication board — reject

**Functional searches:** `cooperative accessibility image recorded audio board personal communication AAC photo create buttons`; `AAC personal recordings photos communication buttons`.

[MyTalkTools](https://www.mytalktools.com/dnn/prod/home.html) describes custom boards using a familiar recorded voice, and [Sanoo](https://sanoo.app/) describes photo-based speaking buttons. This is established augmentative and alternative communication.

**Verdict: central interaction already available.** A NAS-derived import may be convenient, but claiming a distinctive invention or accessibility outcome without disabled-user input would be unsupported. Reject as a hackathon direction.

## Other overlaps and reality checks

- Audio call-and-response is already a performance technique and [AudioTools](https://mashav.com/sha/praat/scripts/AudioTools_CallResponse.html) describes interactive co-improvisation. An archive-generated rhythm activity needs more than playing recordings in sequence.
- [TCFS group sharing](https://www.usenix.org/legacy/events/usenix01/freenix01/full_papers/cattaneo/cattaneo_html/node10.html) already describes threshold-encrypted access, and Experiment 17 explored consent-bearing objects. Threshold release has real limitations: unlocked audio can be retained and prior disclosures cannot be revoked.
- A multi-camera grid at a shared time already appears in [Frigate Review](https://docs.frigate.video/usage/review/). Avoid pitching synchronized timeline navigation as new.
