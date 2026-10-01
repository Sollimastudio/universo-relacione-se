"""Validate canonical content, pin source, synchronize generated app content. No deploy."""
import json, pathlib, hashlib, argparse, shutil
ROOT=pathlib.Path(__file__).resolve().parents[1]
def read(p): return json.loads(p.read_text())
def run():
 ap=argparse.ArgumentParser();ap.add_argument('--app');ap.add_argument('--write-lock',action='store_true');a=ap.parse_args()
 days=[read(p) for p in sorted((ROOT/'days').glob('d*.json'))]
 assert [x['day'] for x in days]==list(range(1,31)),'Need all 30 days'
 claims={x['claim_id'] for x in read(ROOT/'research/claims-evidence.json')['claims']}
 fs=[];bs=[];counts={}
 sections=[read(ROOT/'prebook.json')]+days+[read(ROOT/'postbook.json')]
 for d in sections:
  counts[d['id']]=sum(len(' '.join(b['content']).split()) for b in d['blocks'])
  for b in d['blocks']:
   assert isinstance(b['content'],list) and all(isinstance(x,str) for x in b['content'])
   assert set(b['claim_basis'])<=claims,(d['id'],b['claim_basis'])
   assert b['source_refs'],b['id'];bs.append(b['id'])
   for f in b['fields']:
    fs.append(f['id']);assert f['kind'] in ['textarea','select','number']
    assert not (f.get('opt_in') and f['required']),'Sensitive fields cannot be required'
  if d.get('day'):
   local={f['id'] for b in d['blocks'] for f in b['fields']}
   assert set(d['completion']['required_field_ids'])<=local
   assert counts[d['id']]>=600,(d['id'],counts[d['id']])
 assert len(set(fs))==len(fs),'duplicate field ID';assert len(set(bs))==len(bs),'duplicate block ID'
 manifest={'product_id':'mindsetmagro_30d','version':'2.0.0-review.1','status':'editorial_review_and_runtime_homologation','author':'Sol Lima','language':'pt-BR','days':[{'day':d['day'],'id':d['id'],'title':d['title'],'traversal':d['traversal']} for d in days],'progression':{'interval_hours':24,'clock':'server','requires_entitlement':True,'requires_completion':True,'not_neuroscience':True},'entry':'prebook.json','postbook':'postbook.json','commercial_release':False}
 (ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 files=[p for p in sorted(ROOT.rglob('*')) if p.is_file() and p.suffix in ['.json','.md','.py','.html','.svg'] and p.name!='source-lock.json' and 'qa' not in p.relative_to(ROOT).parts and '__pycache__' not in p.parts]
 hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
 lock={'algorithm':'sha256','files':hashes,'source_hash':hashlib.sha256(json.dumps(hashes,sort_keys=True).encode()).hexdigest()}
 lp=ROOT/'source-lock.json'
 if a.write_lock:lp.write_text(json.dumps(lock,indent=2)+'\n')
 elif lp.exists():assert read(lp)==lock,'Source changed; review then --write-lock'
 else:raise AssertionError('Missing source-lock; use --write-lock once after review')
 if a.app:
  dst=pathlib.Path(a.app)/'content/mindsetmagro';dst.mkdir(parents=True,exist_ok=True)
  for name in ['manifest.json','prebook.json','postbook.json','source-lock.json','visual-assets.json'] :shutil.copy2(ROOT/name,dst/name)
  shutil.copytree(ROOT/'days',dst/'days',dirs_exist_ok=True)
  for p in [dst/'prebook.json',dst/'postbook.json']+list((dst/'days').glob('*.json')):assert p.read_bytes()==(ROOT/p.relative_to(dst)).read_bytes()
  # Diagram assets contain no paid manuscript or personal data.
  shutil.copytree(ROOT/'assets',pathlib.Path(a.app)/'public/mindsetmagro',dirs_exist_ok=True)
 report={'days':30,'blocks':len(bs),'fields':len(fs),'words':counts,'total_words':sum(counts.values()),'unique_ids':True,'claims_resolve':True,'sensitive_fields_optional':True,'source_hash':lock['source_hash'],'app_synced':bool(a.app)}
 (ROOT/'qa').mkdir(exist_ok=True);(ROOT/'qa/content-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':run()
