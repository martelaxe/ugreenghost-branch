import subprocess,json,concurrent.futures,collections
POOL=concurrent.futures.ThreadPoolExecutor(max_workers=12)
def call(op,w,s,p=None):
    args=['python3','/tmp/tools/adapter.py',op,w,s]+([p] if p is not None else [])
    try:
        r=subprocess.run(args,capture_output=True,text=True)
        d=json.loads(r.stdout)
        if r.returncode or 'error' in d: return None,str(d)
        return d,None
    except Exception as e: return None,str(e)
def pair(op,w,p):
    fs=[POOL.submit(call,op,w,s,p) for s in ['source','destination']]
    return [f.result() for f in fs]
result={'workloads':[]}
for w in ['small','large','matching','different','incomplete']:
    ls=[call('list',w,s) for s in ['source','destination']]
    sets=[set(d.get('paths',[])) if d else set() for d,e in ls]
    complete=[bool(d and d.get('complete') is True) for d,e in ls]
    rows=[]; meta=0; hashes=0; errors=[]
    for p in sorted(sets[0]|sets[1]):
        if p not in sets[0]: status='destination_only' if complete[0] else 'unverified'
        elif p not in sets[1]: status='source_only' if complete[1] else 'unverified'
        else:
            st=pair('stat',w,p)
            if all(d is not None and isinstance(d.get('size'),int) for d,e in st):
                meta+=1
                if st[0][0]['size']!=st[1][0]['size']: status='different'
                else:
                    hs=pair('sha256',w,p)
                    if all(d is not None and isinstance(d.get('sha256'),str) and len(d['sha256'])==64 for d,e in hs):
                        hashes+=1
                        status='identical' if hs[0][0]['sha256']==hs[1][0]['sha256'] else 'different'
                    else:
                        status='unverified'; errors.append(p+': hash operation failed '+str(hs))
            else:
                status='unverified'; errors.append(p+': metadata operation failed '+str(st))
        rows.append({'path':p,'status':status})
    counts={s:sum(r['status']==s for r in rows) for s in ['identical','different','source_only','destination_only','unverified']}
    notes=[]
    for s,c,(d,e) in zip(['source','destination'],complete,ls):
        if not c: notes.append(s+' listing incomplete; unlisted paths remain unknown and absence on this side is not proven.'+((' Listing error: '+e) if e else ''))
    notes+=errors
    if not notes: notes=['Both listings are complete; all listed paths have conclusive results.']
    item={'name':w,'paths':rows,'counts':counts,'source_complete':complete[0],'destination_complete':complete[1],'both_metadata_count':meta,'both_hash_count':hashes,'explanation':' '.join(notes),'next_action':'Obtain complete listings and retry failed operations before making archive coverage claims.' if not all(complete) or errors else ('Review differing and one-sided files before any synchronization.' if counts['different']+counts['source_only']+counts['destination_only'] else 'Retain this verified comparison as a baseline.'),'strategy':'Compare exact listing paths; stat common paths on both sides, classify unequal sizes as different, otherwise compare actual SHA-256 values. Failed checks remain unverified.'}
    result['workloads'].append(item)
    print(w,json.dumps(counts),'metadata',meta,'hashes',hashes,flush=True)
    with open('/tmp/out/response.json','w') as f: json.dump(result,f,indent=2)
