#!/usr/bin/env python3
"""Replay immutable publication evidence; exact, reporting, and exploratory roles stay separate.

No network access. Every mode validates SHA-256 hashes. Full mode additionally
repeats legacy numerical checks and the instrumented reporting experiments.
"""
from __future__ import annotations
import argparse,hashlib,json,os,shutil,subprocess,sys,tempfile,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def package_files():
    # Git checkout administration and Python bytecode are not release payload.
    # Every other file (including untracked files) must be in SHA256SUMS.
    return {str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file()
            and p != ROOT/'SHA256SUMS'
            and not any(part in ('.git', '__pycache__') for part in p.relative_to(ROOT).parts)}
def manifest():
    path=ROOT/'SHA256SUMS'
    if not path.is_file():raise RuntimeError('Missing SHA256SUMS')
    seen=set()
    for line in path.read_text().splitlines():
        digest,name=line.split('  ',1);p=(ROOT/name).resolve()
        if name in seen or not p.is_relative_to(ROOT) or not p.is_file():raise RuntimeError('Invalid manifest entry: '+name)
        if sha(p)!=digest:raise RuntimeError('Checksum mismatch: '+name)
        seen.add(name)
    # Internal predecessor manifests themselves must be included; only the root manifest is self-excluded.
    actual=package_files()
    if actual!=seen:raise RuntimeError('Manifest coverage mismatch: '+str(sorted(actual^seen)))
    return len(seen)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--mode',choices=('integrity','exact','full'),default='exact')
    ap.add_argument('--output',type=Path);ap.add_argument('--timeout',type=int,default=900);a=ap.parse_args()
    if sys.flags.optimize:raise RuntimeError('Do not run with -O: original checks use assertions.')
    count=manifest();out=a.output.resolve() if a.output else Path(tempfile.mkdtemp(prefix='ptolemaic-publication-'))
    if out.is_relative_to(ROOT):raise RuntimeError('Output must be outside the immutable bundle.')
    out.mkdir(parents=True,exist_ok=True)
    report={'version':'1.0','mode':a.mode,'manifest_files_verified':count,'jobs':[],
            'scope':'Specified algebraic checks, report integrity and bounded numerical corroboration; not universal proof validation.',
            'formal_proof_assistant_used':False}
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONHASHSEED='0',
             PYTHONDONTWRITEBYTECODE='1',PYTHONOPTIMIZE='0')
    def run(name,cmd,cwd,outputs):
        print('Running '+name,flush=True);start=time.monotonic()
        p=subprocess.run(cmd,cwd=cwd,env=env,capture_output=True,text=True,timeout=a.timeout)
        (out/(name+'.log')).write_text(p.stdout+'\n--- STDERR ---\n'+p.stderr)
        entry={'job':name,'exit_code':p.returncode,'elapsed_seconds':round(time.monotonic()-start,3),'reports':{}}
        report['jobs'].append(entry)
        if p.returncode:raise RuntimeError(name+' failed; see its log')
        for generated,reference,exact in outputs:
            if not generated.is_file():raise RuntimeError('Missing output '+str(generated))
            shutil.copy2(generated,out/(name+'__'+generated.name))
            equal=generated.read_bytes()==reference.read_bytes()
            entry['reports'][generated.name]={'sha256':sha(generated),'matches_shipped_bytes':equal,'exact_byte_match_required':exact}
            if exact and not equal:raise RuntimeError('Exact output mismatch: '+name+'/'+generated.name)
    try:
        if a.mode!='integrity':
            with tempfile.TemporaryDirectory(prefix='ptolemaic-replay-work-') as temp:
                work=Path(temp);core=work/'core';supplied=work/'supplied';nu=work/'numerics'
                shutil.copytree(ROOT/'evidence/core',core);shutil.copytree(ROOT/'evidence/supplied',supplied)
                if a.mode=='full':
                    run('core_replay',[sys.executable,'replay.py'],core,[(core/'checks'/x,ROOT/'evidence/core/checks'/x,x!='numerical_results.json') for x in ('exact_results.json','symbolic_results.json','numerical_results.json')])
                else:
                    for name in ('exact','symbolic'):
                        fn=name+'_results.json';run('core_'+name,[sys.executable,'verify_'+name+'.py'],core,[(core/'checks'/fn,ROOT/'evidence/core/checks'/fn,True)])
                for name,script,ref in [('manuscript','verify_manuscript.py','manuscript_checks.json'),('revision','verify_revision.py','revision_checks.json')]:
                    target=work/ref
                    run(name+'_checks',[sys.executable,str(ROOT/'scripts'/script),'--output',str(target)],work,[(target,ROOT/'evidence/current'/ref,True)])
                if a.mode=='full':
                    for job in ('audit_allsize','near_extremal','adversarial_lemma4'):
                        run('legacy_'+job,[sys.executable,job+'.py'],supplied,[(supplied/(job+'.json'),ROOT/'evidence/supplied'/(job+'.json'),False)])
                    run('current_numerics',[sys.executable,str(ROOT/'scripts/current_numerics.py'),'--output',str(nu)],work,
                       [(nu/x,ROOT/'evidence/current/numerics'/x,False) for x in ('near_extremal_current.json','near_extremal_trials.jsonl','adversarial_current.json','adversarial_trials.jsonl')])
                    summary=work/'CURRENT_NUMERICAL_SUMMARY.json'
                    run('current_summary',[sys.executable,str(ROOT/'scripts/build_current_summary.py'),'--numerical-dir',str(nu),'--output',str(summary)],work,[(summary,ROOT/'evidence/current/CURRENT_NUMERICAL_SUMMARY.json',False)])
                else:nu=ROOT/'evidence/current/numerics';summary=ROOT/'evidence/current/CURRENT_NUMERICAL_SUMMARY.json'
                target=work/'reporting_checks.json'
                run('reporting_checks',[sys.executable,str(ROOT/'scripts/verify_reporting.py'),'--data',str(nu),'--summary',str(summary),'--output',str(target)],work,[(target,ROOT/'evidence/current/reporting_checks.json',True)])
        report['status']='PASS';report['manifest_files_verified_after_replay']=manifest()
    except Exception as e:
        report['status']='FAIL';report['error']=str(e)
        (out/'REPLAY_REPORT.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');raise
    (out/'REPLAY_REPORT.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(f"PASS: {count} manifest files; {len(report['jobs'])} jobs. Reports: {out}")
    print('PASS denotes completion of the specified checks, not proof-assistant verification.')
if __name__=='__main__':
    try:main()
    except Exception as e:print('ERROR: '+str(e),file=sys.stderr);raise SystemExit(1)
