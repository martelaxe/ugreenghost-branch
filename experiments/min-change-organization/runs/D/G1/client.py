import subprocess,json
paths=['historic/finance/2022/item_e8a64c651ef4.jpg','historic/finance/2023/item_27d41ab681d3.csv','historic/finance/2023/item_2afb34972841.jpg','historic/finance/2024/item_e0892293f376.txt','historic/finance/2025/item_39aeda2a0c65.csv','historic/finance/2025/item_4033e9b9392c.json','historic/personal/2022/item_1eb145a617ad.jpg','historic/personal/2023/item_87cfce419c97.jpg','historic/projects/2022/item_f07e0f0388e5.csv','historic/projects/2024/item_bd6436e2d0cc.md','historic/projects/2025/item_8a03518a7ed4.csv','sorted/finance/2022/item_b1269b43e7c3.json','sorted/finance/2022/item_e7baf0d4f618.jpg','sorted/finance/2023/item_e9148c1b76bf.csv','sorted/finance/2025/item_85c19e03a0ea.json','sorted/finance/2025/item_ad7861c75dd0.md','sorted/personal/2023/item_179127a3f057.json','sorted/personal/2024/item_6516b0c340ac.json','sorted/personal/2024/item_ef59807a9934.md','sorted/projects/2022/item_14ea39f15746.md','sorted/projects/2022/item_19430d056fe7.txt','sorted/projects/2022/item_6c11b801fd82.json','sorted/projects/2024/item_a180a92e997c.jpg','sorted/projects/2025/item_2df2466c250d.pdf']
results=[]
for p in paths:
 r=subprocess.run(['python3','/tmp/tools/adapter.py','read',p],capture_output=True,text=True)
 results.append({'path':p,'code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
json.dump(results,open('/tmp/out/reads.json','w'),indent=2)
for r in results: print(json.dumps(r))
