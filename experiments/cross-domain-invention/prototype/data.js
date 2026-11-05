// Entire dataset is fictional. It is visible in browser tools: masking is not secure.
const FIXTURE = {
  samples: {
    a: {id:'A', path:'audio/sample-a.wav', calls:2, mic:'fixture-mic-1', position:'fictional garden marker', gain:'fixed-1', sampleRate:16000, duration:4, notes:'Synthetic fixture, 2 generated tones. Not a field recording.'},
    b: {id:'B', path:'audio/sample-b.wav', calls:4, mic:'fixture-mic-1', position:'fictional garden marker', gain:'fixed-1', sampleRate:16000, duration:4, notes:'Synthetic fixture, 4 generated tones. Not a field recording.'},
    c: {id:'C', path:'audio/sample-c.wav', calls:2, mic:null, position:'fictional garden marker', gain:'fixed-1', sampleRate:16000, duration:4, notes:'Synthetic fixture: microphone identity deliberately missing.'}
  },
  pairs: {ready:['a','b'], incomplete:['a','c']}
};
if (typeof module !== 'undefined') module.exports = FIXTURE;
