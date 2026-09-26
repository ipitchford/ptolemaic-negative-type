#!/usr/bin/env python3
"""Check the packaged hashes, replay checks, compare generated reports."""
import hashlib,json,os,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parent
bad=[];count=0
for line in (root/'SHA256SUMS').read_text().splitlines():
    digest,name=line.split('  ',1)
    if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest:bad.append(name)
    count+=1
if bad:raise SystemExit('Checksum mismatch: '+', '.join(bad))
reports=['exact_results.json','symbolic_results.json','numerical_results.json']
before={x:(root/'checks'/x).read_bytes() for x in reports}
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
for script in ['verify_exact.py','verify_symbolic.py','verify_numerical.py']:
    done=subprocess.run([sys.executable,str(root/script)],cwd=root,env=env,capture_output=True,text=True)
    if done.returncode:
        print(done.stdout);print(done.stderr,file=sys.stderr);raise SystemExit(done.returncode)
match={x:before[x]==(root/'checks'/x).read_bytes() for x in reports}
result={'input_hashes_verified':count,'scripts_returned_success':3,'reports_byte_identical':match,'formal_proof_assistant_used':False}
(root/'checks'/'replay_results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
if not all(match.values()):print('Numerical/library differences may affect byte identity; inspect the regenerated report.')
