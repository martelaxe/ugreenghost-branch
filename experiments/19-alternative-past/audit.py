from pathlib import Path
import hashlib,json,re
R=Path(__file__).parent; T=R/'workspaces/THEN';P=R/'workspaces/NOW-P';G=R/'workspaces/NOW-G';X=R/'workspaces/NOW-P-IRRELEVANT'
def digest(p):return {str(x.relative_to(p)):hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(p.rglob('*')) if x.is_file()}
a,b,c,d=map(digest,[T,P,G,X]);assert b==c
expected_names=set(re.findall(r'^- `([^`]+)`: `([a-f0-9]+)`', (T/'SNAPSHOT.md').read_text(),flags=re.M));assert all(a[name]==h for name,h in expected_names);assert set(a)=={n for n,h in expected_names}|{'SNAPSHOT.md'}
assert set(d)-set(b)=={'99_art_poster.md'} and all(d[k]==v for k,v in b.items())
then=(R/'runs/THEN/response.md').read_text();p=(R/'runs/NOW-P/response.md').read_text();g=(R/'runs/NOW-G/response.md').read_text();v=(R/'runs/NOW-P-IRRELEVANT/response.md').read_text()
for name in ['THEN','NOW-P','NOW-G','NOW-P-IRRELEVANT']:
 ex=json.loads((R/'runs'/name/'execution.json').read_text());assert ex['exit']==0 and ex['has_final'] and ex['inputs_unchanged']
leaks=[term for term in ['72 Alder','transposed','transposition','September 23','Sept 23','October 4','October 18','fieldbook','inspector_original_fieldbook'] if term.lower() in then.lower()]
result={'then_attested_files':len(expected_names),'then_including_snapshot':len(a),'then_names_and_hashes_match_attested_snapshot':True,'later_documents_absent_from_then':not any(int(n[:2]) in range(11,20) for n in a if n[:2].isdigit()),'now_generic_and_procedure_input_hashes_identical':True,'mutation_exactly_one_irrelevant_file':True,'then_output_future_marker_hits':leaks,'then_output_mentions_72_or_transposition':any(s.lower() in then.lower() for s in ['72 Alder','transposed','transposition']),'procedure_mentions_backdated_memo_and_oct_18':('17_backdated_memo' in p and 'Oct 18' in p),'procedure_marks_uncertain_carbon_unknown':('18_uncertain_carbon' in p and 'unknown availability' in p.lower()),'poster_run_marks_poster_irrelevant':('99_art_poster' in v and 'irrelevant' in v.lower()),'original_p_and_poster_run_both_state_wrong_building':all('misidentified the Reading Room' in s for s in [p,v]),'model_runs_exit_zero_and_inputs_unchanged':True,'limitations':'String checks are not semantic audits, complete isolation, external document authentication, or proof of human knowledge.'}
(R/'tests.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
