import json,sys
from pathlib import Path
from adapter_core import Adapter
args=sys.argv[1:];a=Adapter('/tmp/work',json.loads(Path('/tmp/faults/config.json').read_text()),'/tmp/out/adapter-events.jsonl')
print(json.dumps(a.call(args[0],args[1],args[2],args[3] if len(args)>3 else None)))
