// Research-only interaction logic. These checks are necessary but not sufficient.
const FIELDS = ['mic','position','gain','sampleRate','duration'];
function assess(left,right) {
  const issues=[];
  for (const k of FIELDS) {
    if (left[k] === null || left[k] === undefined || left[k] === '' || right[k] === null || right[k] === undefined || right[k] === '') issues.push(`${k}: missing or unknown`);
    else if (left[k] !== right[k]) issues.push(`${k}: values differ`);
  }
  return {ready:issues.length===0, issues};
}
function makeTrial(pair, swap) {
  if (!Array.isArray(pair) || pair.length!==2) throw Error('two samples required');
  const assessment=assess(pair[0],pair[1]);
  if (!assessment.ready) return {state:'blocked', issues:assessment.issues};
  return {state:'listening', items:swap?[pair[1],pair[0]]:pair.slice()};
}
function decide(trial, choice) {
  if (trial.state !== 'listening') throw Error('comparison not available');
  if (![0,1,'unsure'].includes(choice)) throw Error('invalid choice');
  return {state:'revealed', choice, items:trial.items};
}
if (typeof module !== 'undefined') module.exports={assess,makeTrial,decide};
