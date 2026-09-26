#!/usr/bin/env python3
"""Instrumented numerical corroboration for publication; not a proof certificate.

Reuses the supplied near-extremal and adversarial designs/seeds, without editing
historical scripts. Stores every attempt, full-precision metrics, rejection and
solver diagnostics. Empty statistics are null, never initial sentinel values.
Outputs must be outside the immutable publication bundle.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
import os
from pathlib import Path
import sys
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ.setdefault(key,'1')
import numpy as np
from scipy.optimize import minimize

ROOT=Path(__file__).resolve().parents[1]

def dump(path:Path,obj:object)->None:
    path.write_text(json.dumps(obj,indent=2,sort_keys=True,allow_nan=False)+'\n')

def finite(x):
    if x is None:return None
    y=float(x)
    return y if math.isfinite(y) else None

def stat(values,op='min'):
    clean=[float(v) for v in values if v is not None and math.isfinite(float(v))]
    return {'accepted_samples':len(clean),'value':(min(clean) if op=='min' else max(clean)) if clean else None,
            'status':'observed' if clean else 'no_observations'}

def margins(d):
    tri=[]; pt=[]; n=len(d)
    for i,j,k in itertools.combinations(range(n),3):
        a,b,c=d[i,j],d[i,k],d[j,k];tri.extend((b+c-a,a+c-b,a+b-c))
    for i,j,k,l in itertools.combinations(range(n),4):
        a,b,c=d[i,j]*d[k,l],d[i,k]*d[j,l],d[i,l]*d[j,k]
        pt.extend((b+c-a,a+c-b,a+b-c))
    return np.array(tri),np.array(pt)

def minmargin(a):return float(a.min()) if len(a) else None

def helmert(m):
    """Orthonormal columns spanning 1-perp, constructed without an eigensolver."""
    Q=np.zeros((m,m-1))
    for k in range(1,m):
        Q[:k,k-1]=1/math.sqrt(k*(k+1)); Q[k,k-1]=-k/math.sqrt(k*(k+1))
    return Q

def near_extremal(out:Path):
    rng=np.random.default_rng(5); allrows=[]; groups=[]
    for m in (11,12,13,14):
        a=(m-1)//2;r=m-a;T=1+m/((m-1)**2//4);p=math.log2(T)
        Q=helmert(m);J=np.eye(m)-np.ones((m,m))/m;z=np.array([1/a]*a+[-1/r]*r)
        rows=[]
        for trial in range(600):
            eps=rng.uniform(0,.06);d=np.zeros((m,m))
            for i in range(m):
                for j in range(i+1,m):
                    if i<a and j<a:v=rng.uniform(1-eps,1)
                    elif i>=a and j>=a:v=rng.uniform(2-4*eps,2-2*eps)
                    else:v=rng.uniform(1-eps/2,1)
                    d[i,j]=d[j,i]=v
            tr,pt=margins(d);accepted=min(float(tr.min()),float(pt.min()))>=-1e-9
            row={'m':m,'trial':trial,'a':a,'r':r,'exponent':p,'epsilon':float(eps),
                 'triangle_min_slack':float(tr.min()),'ptolemy_min_slack':float(pt.min()),
                 'feasibility_tolerance':1e-9,'feasibility_accepted':bool(accepted),
                 'rejection_reason':None if accepted else 'metric_or_ptolemy_constraint',
                 'upper_triangle':d[np.triu_indices(m,1)].tolist(),
                 'centred_gram_min_eigenvalue':None,'zero_sum_gram_min_eigenvalue':None,
                 'split_vector_gap':None,'split_vector_rayleigh_quotient':None,'numerical_exception':None}
            if accepted:
                try:
                    E=d**p; G=-J@E@J/2;Z=-Q.T@E@Q/2
                    row.update(centred_gram_min_eigenvalue=float(np.linalg.eigvalsh(G).min()),
                               zero_sum_gram_min_eigenvalue=float(np.linalg.eigvalsh(Z).min()),
                               split_vector_gap=float(-z@E@z/2),
                               split_vector_rayleigh_quotient=float((-z@E@z/2)/(z@z)))
                except Exception as e:row['numerical_exception']=type(e).__name__+': '+str(e)
            rows.append(row);allrows.append(row)
        accepted=[x for x in rows if x['feasibility_accepted']]
        groups.append({'m':m,'T':T,'exponent':p,'attempted':len(rows),'accepted':len(accepted),
                       'rejected':len(rows)-len(accepted),'numerical_exceptions':sum(x['numerical_exception'] is not None for x in rows),
                       'statistics':{key:stat([x[key] for x in accepted]) for key in (
                         'centred_gram_min_eigenvalue','zero_sum_gram_min_eigenvalue',
                         'split_vector_gap','split_vector_rayleigh_quotient')}})
        print('near-extremal',m,len(accepted),'accepted',flush=True)
    (out/'near_extremal_trials.jsonl').write_text(''.join(json.dumps(x,sort_keys=True,allow_nan=False)+'\n' for x in allrows))
    report={'schema_version':'1.0','design':'supplied near_extremal.py with seed 5; separate measurements and full-precision samples',
            'seed':5,'scope':'numerical corroboration only; sampled unscaled metrics near split witnesses',
            'centred_eigenvalue_caveat':'The centred Gram matrix has an exact structural zero; its full minimum is not a positive stability margin.',
            'zero_sum_eigenvalue_definition':'lambda_min(-Q^T E Q/2), Q^T Q=I and Q^T 1=0; ordinary Euclidean orthonormal basis',
            'split_gap_definition':'-z^T E z/2 with z=(1/a,...,1/a,-1/r,...,-1/r); not an eigenvalue',
            'rayleigh_definition':'split_vector_gap/(z^T z); not substituted for a minimum eigenvalue',
            'certified_error_bounds':False,'groups':groups,'trials':'near_extremal_trials.jsonl'}
    dump(out/'near_extremal_current.json',report)

def constraints(d):
    # Same ordering and floating-point operations as the received optimiser.
    m=len(d);c=[]
    for i,j,k in itertools.permutations(range(m),3):
        if i<j:c.append(d[i,k]+d[k,j]-d[i,j])
    for i,j,k,l in itertools.combinations(range(m),4):
        a,b,cc=d[i,j]*d[k,l],d[i,k]*d[j,l],d[i,l]*d[j,k];c.extend((b+cc-a,a+cc-b,a+b-cc))
    return np.array(c)

def inverse_measure(d,p,n):
    m=len(d); E=d**p; A=np.zeros((m+1,m+1));A[0,1:]=1;A[1:,0]=1;A[1:,1:]=E
    try:V=np.linalg.inv(A)
    except np.linalg.LinAlgError:return {'valid':False,'reason':'singular_augmented_matrix','deficit':None}
    dg=np.diag(V)
    if not np.all(dg<0):return {'valid':False,'reason':'nonnegative_inverse_diagonal','deficit':None}
    N=V/np.sqrt(np.outer(dg,dg)); v=float(N[~np.eye(m+1,dtype=bool)].min())
    if not math.isfinite(v):return {'valid':False,'reason':'nonfinite_correlation','deficit':None}
    k=max(0.,((n-1)*2**p-n)/n)
    return {'valid':True,'reason':None,'deficit':float(-v-k),'minimum_normalised_inverse_entry':v}

def adversarial(out:Path):
    rng=np.random.default_rng(21);rows=[];groups=[]
    for n in (3,4,5,6):
        m=n+1;Tb=n/(n-2);p=min(.999,math.log2(Tb)-.001);iu=np.triu_indices(m,1)
        def unpack(v):d=np.zeros((m,m));d[iu]=np.exp(v);return d+d.T
        def objective(v):
            val=inverse_measure(unpack(v),p,n)
            # Original invalid-inverse penalty. Not counted as a measured deficit.
            return -val['deficit'] if val['valid'] else 1.
        for run in range(40):
            if run%2:
                P=rng.normal(0,1,(m,3));v0=np.log(np.linalg.norm(P[:,None]-P[None],axis=2)[iu]);kind='euclidean'
            else:
                a=m//2;d0=np.ones((m,m));d0[a:,a:]=2;np.fill_diagonal(d0,0)
                v0=np.log(d0[iu])+rng.normal(0,.15,len(iu[0]));kind='split_perturbation'
            row={'n':n,'m':m,'run':run,'exponent':p,'T':2**p,'k_n':max(0.,((n-1)*2**p-n)/n),
                 'start_kind':kind,'initial_log_distances':v0.tolist(),'exception':None,'solver_success':False,
                 'solver_status':None,'solver_message':None,'iterations':None,'function_evaluations':None,
                 'constraint_min_slack':None,'feasibility_accepted':False,'converged_and_feasible':False,
                 'measurement_accepted':False,'inverse_measurement':None,'upper_triangle':None,'root_gram_min_eigenvalue':None,
                 'augmented_condition_number':None,'feasibility_tolerance':1e-8}
            try:
                res=minimize(objective,v0,method='SLSQP',bounds=[(-4,4)]*len(v0),
                              constraints=[{'type':'ineq','fun':lambda v:constraints(unpack(v))}],
                              options={'maxiter':300,'ftol':1e-12})
                d=unpack(res.x); slack=float(constraints(d).min());measure=inverse_measure(d,p,n)
                feasible=bool(np.isfinite(res.x).all() and slack>=-1e-8)
                E=d**p;rr=E[0,1:];C=(rr[:,None]+rr[None,:]-E[1:,1:])/2
                A=np.zeros((m+1,m+1));A[0,1:]=1;A[1:,0]=1;A[1:,1:]=E
                row.update(solver_success=bool(res.success),solver_status=int(res.status),solver_message=str(res.message),
                           iterations=int(res.nit),function_evaluations=int(res.nfev),constraint_min_slack=slack,
                           feasibility_accepted=feasible,converged_and_feasible=bool(feasible and res.success),
                           measurement_accepted=bool(feasible and measure['valid']),inverse_measurement=measure,
                           upper_triangle=d[iu].tolist(),root_gram_min_eigenvalue=float(np.linalg.eigvalsh(C).min()),
                           augmented_condition_number=finite(np.linalg.cond(A)))
            except Exception as e:row['exception']=type(e).__name__+': '+str(e)
            rows.append(row)
        group=[x for x in rows if x['n']==n]
        measured=[x for x in group if x['measurement_accepted']]
        conv=[x for x in measured if x['converged_and_feasible']]
        counts={}
        for x in group:
            key=str(x['solver_status']) if x['exception'] is None else 'exception';counts[key]=counts.get(key,0)+1
        groups.append({'n':n,'m':m,'T':2**p,'exponent':p,'k_n':max(0.,((n-1)*2**p-n)/n),
                       'attempted':len(group),'feasibility_accepted':sum(x['feasibility_accepted'] for x in group),
                       'feasibility_rejected':sum(not x['feasibility_accepted'] and x['exception'] is None for x in group),
                       'exceptions':sum(x['exception'] is not None for x in group),'solver_successes':sum(x['solver_success'] for x in group),
                       'converged_and_feasible':sum(x['converged_and_feasible'] for x in group),
                       'invalid_measurements':sum(x['feasibility_accepted'] and not x['measurement_accepted'] for x in group),
                       'solver_status_counts':counts,
                       'maximum_deficit_feasible_valid':stat([x['inverse_measurement']['deficit'] for x in measured],'max'),
                       'maximum_deficit_converged_feasible_valid':stat([x['inverse_measurement']['deficit'] for x in conv],'max')})
        print('adversarial',n,groups[-1]['converged_and_feasible'],'converged and feasible',flush=True)
    (out/'adversarial_trials.jsonl').write_text(''.join(json.dumps(x,sort_keys=True,allow_nan=False)+'\n' for x in rows))
    dump(out/'adversarial_current.json',{'schema_version':'1.0','seed':21,
        'design':'supplied SLSQP design and random stream with per-attempt diagnostics; 40 starts per n',
        'log_distance_bounds':[-4,4],'max_iterations':300,'ftol':1e-12,'constraint_tolerance':1e-8,
        'scope':'bounded exploratory optimisation; local convergence and tolerance-feasibility do not certify global extrema or counterexamples',
        'conditional_hypotheses_note':'The universal strictness assumption of the inverse theorem is analytic; these tests do not verify that hypothesis over all metrics.',
        'positive_deficit_interpretation':'A floating-point positive deficit is not a validated counterexample. Constraint and numerical error require independent certification.',
        'groups':groups,'trials':'adversarial_trials.jsonl'})

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--part',choices=('all','near','adversarial'),default='all');a=p.parse_args()
    out=a.output.resolve()
    if out.is_relative_to(ROOT):p.error('Choose an output directory outside the immutable bundle.')
    out.mkdir(parents=True,exist_ok=True)
    if a.part in ('all','near'):near_extremal(out)
    if a.part in ('all','adversarial'):adversarial(out)
if __name__=='__main__':main()
