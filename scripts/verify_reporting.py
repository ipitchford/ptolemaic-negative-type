#!/usr/bin/env python3
"""Validate current reporting, recompute every saved measurement, and test missingness controls.

This is data/report integrity validation, not proof-assistant verification.
"""
from __future__ import annotations
import argparse,json,math,os
from pathlib import Path
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ.setdefault(k,'1')
import numpy as np
from current_numerics import margins,helmert,inverse_measure,stat,constraints
ROOT=Path(__file__).resolve().parents[1]
def load(p):return json.loads(p.read_text(),parse_constant=lambda s:(_ for _ in ()).throw(ValueError(s)))
def lines(p):return [json.loads(x,parse_constant=lambda s:(_ for _ in ()).throw(ValueError(s))) for x in p.read_text().splitlines()]
def require(c,msg):
    if not c:raise ValueError(msg)
def close(a,b):
    if a is None or b is None:require(a is None and b is None,'null mismatch');return
    require(math.isfinite(a) and math.isfinite(b),'nonfinite metric')
    require(abs(a-b)<=5e-11*(1+abs(a)+abs(b)),'numerical measurement mismatch')
def restore(row):
    m=row['m'];D=np.zeros((m,m));D[np.triu_indices(m,1)]=row['upper_triangle'];return D+D.T
def check_stat(observed,values,op='min'):
    expected=stat(values,op);require(observed['accepted_samples']==expected['accepted_samples'],'count mismatch')
    require(observed['status']==expected['status'],'status mismatch');close(observed['value'],expected['value'])
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--data',type=Path,default=ROOT/'evidence/current/numerics')
    ap.add_argument('--summary',type=Path,default=ROOT/'evidence/current/CURRENT_NUMERICAL_SUMMARY.json')
    ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();checks=[]
    n=load(a.data/'near_extremal_current.json');rows=lines(a.data/'near_extremal_trials.jsonl')
    for row in rows:
        D=restore(row);tr,pt=margins(D);close(float(tr.min()),row['triangle_min_slack']);close(float(pt.min()),row['ptolemy_min_slack'])
        feasible=min(tr.min(),pt.min())>=-row['feasibility_tolerance']
        require(bool(feasible)==row['feasibility_accepted'],'near feasibility mismatch')
        if row['feasibility_accepted'] and row['numerical_exception'] is None:
            m=row['m'];E=D**row['exponent'];J=np.eye(m)-np.ones((m,m))/m;Q=helmert(m)
            require(np.max(abs(Q.T@Q-np.eye(m-1)))<1e-12,'basis not orthonormal')
            require(np.max(abs(Q.T@np.ones(m)))<1e-12,'basis not zero-sum')
            z=np.array([1/row['a']]*row['a']+[-1/row['r']]*row['r'])
            gap=float(-z@E@z/2)
            close(float(np.linalg.eigvalsh(-J@E@J/2).min()),row['centred_gram_min_eigenvalue'])
            close(float(np.linalg.eigvalsh(-Q.T@E@Q/2).min()),row['zero_sum_gram_min_eigenvalue'])
            close(gap,row['split_vector_gap']);close(gap/float(z@z),row['split_vector_rayleigh_quotient'])
    for g in n['groups']:
        group=[r for r in rows if r['m']==g['m']];accept=[r for r in group if r['feasibility_accepted']]
        require(g['attempted']==len(group) and g['accepted']==len(accept),'near counts wrong')
        require(g['rejected']==len(group)-len(accept),'near rejected count wrong')
        for k,v in g['statistics'].items():check_stat(v,[r[k] for r in accept])
    checks.append('all_saved_near_extremal_arrays_recomputed_with_separate_statistics')
    adv=load(a.data/'adversarial_current.json');arows=lines(a.data/'adversarial_trials.jsonl')
    for r in arows:
        if r['exception'] is None:
            D=restore(r);slack=float(constraints(D).min());close(slack,r['constraint_min_slack'])
            require(r['feasibility_accepted']==(slack>=-1e-8),'optimisation feasibility mismatch')
            require(r['converged_and_feasible']==(r['feasibility_accepted'] and r['solver_success']),'convergence/feasibility conflation')
            v=inverse_measure(D,r['exponent'],r['n']);require(v['valid']==r['inverse_measurement']['valid'],'invalid inverse status')
            if v['valid']:close(v['deficit'],r['inverse_measurement']['deficit'])
    for g in adv['groups']:
        group=[r for r in arows if r['n']==g['n']];m=[r for r in group if r['measurement_accepted']];c=[r for r in m if r['converged_and_feasible']]
        require(g['attempted']==len(group),'optimisation count mismatch')
        require(g['solver_successes']==sum(r['solver_success'] for r in group),'solver successes wrong')
        require(g['converged_and_feasible']==sum(r['converged_and_feasible'] for r in group),'converged counts wrong')
        require(g['feasibility_accepted']==sum(r['feasibility_accepted'] for r in group),'feasible count wrong')
        require(g['exceptions']+g['feasibility_rejected']+g['feasibility_accepted']==len(group),'attempt partition wrong')
        check_stat(g['maximum_deficit_feasible_valid'],[r['inverse_measurement']['deficit'] for r in m],'max')
        check_stat(g['maximum_deficit_converged_feasible_valid'],[r['inverse_measurement']['deficit'] for r in c],'max')
    checks.append('all_saved_optimisation_attempts_recomputed_and_statuses_reconciled')
    summary=load(a.summary)
    for g in summary['historical_empty_near_extremal_experiment']:
        if g['accepted']==0:
            require(g['minimum_centred_gram_eigenvalue']['value'] is None,'empty minimum must be null')
            require(g['minimum_centred_gram_eigenvalue']['accepted_samples']==0,'empty count must be zero')
    for g in summary['historical_mixed_followup']:
        require(g['minimum_centred_gram_eigenvalue']['value'] is None and g['minimum_split_vector_gap']['value'] is None,'historical mixed statistic cannot be unmixed')
    require(summary['fresh_near_extremal']['groups']==n['groups'],'near current summary differs')
    require(summary['fresh_adversarial_optimisation']['groups']==adv['groups'],'optimisation summary differs')
    checks.append('summary_preserves_missingness_and_does_not_recover_unrecorded_historical_statistics')
    # Negative controls demonstrate that an initial sentinel/count error is rejected.
    rejected=0
    for mutant in ({'accepted_samples':0,'status':'no_observations','value':1e9},
                   {'accepted_samples':1,'status':'observed','value':None},
                   {'accepted_samples':2,'status':'observed','value':1.0}):
        try:check_stat(mutant,[])
        except ValueError:rejected+=1
    require(rejected==3,'missingness negative control failed')
    checks.append('three_missingness_and_count_mutations_rejected')
    report={'status':'PASS','scope':'report integrity and finite numerical recomputation; no universal theorem validation',
            'checks':checks,'near_extremal_arrays':len(rows),'optimisation_attempts':len(arows),
            'negative_controls_rejected':rejected,'numerical_recomputation_tolerance':'5e-11*(1+abs(a)+abs(b))',
            'formal_proof_assistant_used':False}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
