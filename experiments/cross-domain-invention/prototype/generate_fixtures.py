"""Create fictional audio stimuli; no real environmental recording is involved."""
import math, random, struct, wave, json, hashlib
from pathlib import Path
p=Path(__file__).resolve().parent
rate=16000; duration=4; count=rate*duration

def make(name, calls):
    rng=random.Random(3241)
    frames=[]
    for i in range(count):
        t=i/rate
        bg=.022*rng.uniform(-1,1)+.018*math.sin(2*math.pi*180*t)
        signal=0.0
        for start in calls:
            d=t-start
            if 0 <= d < .18:
                env=math.sin(math.pi*d/.18)**2
                signal+=.14*env*math.sin(2*math.pi*(1050*d+390*d*d))
        v=max(-1,min(1,bg+signal))
        frames.append(struct.pack('<h',int(v*32767)))
    target=p/'audio'/name
    with wave.open(str(target),'wb') as out:
        out.setnchannels(1);out.setsampwidth(2);out.setframerate(rate);out.writeframes(b''.join(frames))
    return hashlib.sha256(target.read_bytes()).hexdigest()
hashes={'sample-a.wav':make('sample-a.wav',[.65,2.30]), 'sample-b.wav':make('sample-b.wav',[.65,1.4,2.3,3.15]), 'sample-c.wav':make('sample-c.wav',[.85,2.7])}
(p/'audio'/'sha256.json').write_text(json.dumps(hashes,indent=2)+'\n')
print(json.dumps({'sample_rate':rate,'duration_seconds':duration,'files':hashes},indent=2))
