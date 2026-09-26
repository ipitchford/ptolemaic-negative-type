#!/usr/bin/env python3
"""Deterministic exploratory checks. None is a premise of the analytic proof."""
from pathlib import Path
import json
import math
import numpy as np
import mpmath as mp
from scipy.optimize import linprog

HERE=Path(__file__).resolve().parent

def stable_b(x,q):
    x=np.asarray(x,dtype=float);out=np.empty_like(x)
    pos=x>=0
    out[pos]=(1-np.exp(q*x[pos])*np.expm1(q*np.log1p(np.exp(-x[pos]))))/2
    out[~pos]=(np.exp(q*x[~pos])-np.expm1(q*np.log1p(np.exp(x[~pos]))))/2
    return out

def rooted_gram(d,q):
    E=d**q;r=E[0,1:]
    return (r[:,None]+r[None,:]-E[1:,1:])/2

def invert_metric(d,p):
    n=len(d);ids=[i for i in range(n) if i!=p]
    # New root is old infinity, then the surviving old points.
    D=np.zeros_like(d)
    R=d[p,ids]
    D[0,1:]=D[1:,0]=1/R
    D[1:,1:]=d[np.ix_(ids,ids)]/np.outer(R,R)
    return D

def main():
    rng=np.random.default_rng(9260925)
    out={"status":"PASS","scope":"bounded numerical corroboration only; no global search or formal proof","seed":9260925}
    lp=[]
    for n in [2,3,4,8,16,32]:
        for q in [.03,.2,.5,.85]:
            T=2**q;bound=max(2,2*n/(2*n-(n-1)*T))
            largest=-math.inf;max_violation=0.0;success=0
            for _ in range(10):
                logL=rng.uniform(-18,18,n)
                B=stable_b(logL[:,None]-logL[None,:],q);np.fill_diagonal(B,1)
                res=linprog(-np.ones(n),A_ub=B,b_ub=np.ones(n),bounds=(0,None),method='highs')
                assert res.success,res.message
                violation=max(0.0,float(np.max(B@res.x-1)),float(-np.min(res.x)))
                assert violation<1e-7
                largest=max(largest,float(-res.fun));max_violation=max(max_violation,violation);success+=1
            assert largest<=bound+1e-7
            lp.append({"n":n,"q":q,"bound":bound,"maximum":largest,"constraint_violation":max_violation,"successful_runs":success})
    out['packing_tests']=lp

    # Scalar supporting-power inequality checked at high precision across wide ratios.
    mp.mp.dps=80;scalar=0;min_log_slack=mp.inf
    for q0 in ['0.01','0.05','0.2','0.5','0.83','0.99']:
        q=mp.mpf(q0);T=2**q;de=T-1;beta=q*(1-T/2)/de
        for x in range(-60,61,3):
            t=mp.exp(x);K=(1+t)**q-t**q
            slack=mp.log(de)-beta*x-mp.log(K)
            assert slack>-mp.mpf('1e-45')
            min_log_slack=min(min_log_slack,slack);scalar+=1
    out['scalar_tests']={"count":scalar,"precision_digits":80,"smallest_log_slack":str(min_log_slack)}

    # Correlation test: stars, Euclidean metrics, split metrics, and their inversions.
    tests=0;skip=0;worst=1.0;max_cond=0.;max_inverse_residual=0.
    for n in [2,3,4,6,10,16]:
        upper=1.0 if n<=3 else min(1.0,math.log2(n/(n-2)))
        for frac in [.2,.75,.98]:
            q=frac*upper;T=2**q;k=max(0,(n-1)*T/n-1)
            for typ in ['star','euclidean','split']:
                for trial in range(6):
                    m=n+1
                    if typ=='star':
                        l=np.exp(rng.uniform(-5,5,n));d=np.zeros((m,m));d[0,1:]=d[1:,0]=l
                        d[1:,1:]=l[:,None]+l[None,:];np.fill_diagonal(d,0)
                    elif typ=='euclidean':
                        pts=rng.normal(size=(m,3));d=np.sqrt(np.sum((pts[:,None]-pts[None,:])**2,axis=2))
                    else:
                        d=np.ones((m,m));d[n-1:,n-1:]=2;np.fill_diagonal(d,0)
                    if trial%2:d=invert_metric(d,int(rng.integers(m)))
                    C=rooted_gram(d,q);cond=float(np.linalg.cond(C))
                    if cond>1e10:skip+=1;continue
                    assert np.linalg.eigvalsh(C).min()>0
                    r=np.diag(C);I=np.linalg.inv(C);u=I@r;v=I@np.ones(n);M=u.sum();P=v.sum();Q=r@u
                    V=np.block([[np.array([[-Q/2,1-M/2],[1-M/2,-P/2]]),np.vstack([u,v])/2],[np.vstack([u,v]).T/2,-I/2]])
                    assert np.diag(V).max()<0
                    corr=V/np.sqrt(np.outer(np.diag(V),np.diag(V)));np.fill_diagonal(corr,1)
                    gap=float(corr.min()+k);worst=min(worst,gap)
                    assert gap>=-1e-7,(n,q,typ,gap)
                    E=d**q;A=np.ones((m+1,m+1));A[0,0]=0;A[1:,1:]=E
                    err=float(np.max(np.abs(A@V-np.eye(m+1))))
                    max_inverse_residual=max(max_inverse_residual,err);max_cond=max(max_cond,cond);tests+=1
    out['inverse_correlation_tests']={"count":tests,"skipped_ill_conditioned":skip,"minimum_bound_slack":worst,"largest_gram_condition_number":max_cond,"largest_inverse_identity_residual":max_inverse_residual,"tolerance":1e-7}

    # High-precision counterexample masses, separate from exact sign proofs.
    mp.mp.dps=80
    def mass(d,q):
        n=len(d)-1;r=mp.matrix([mp.mpf(d[0][i+1])**q for i in range(n)])
        C=mp.matrix(n)
        for i in range(n):
            for j in range(n):C[i,j]=(r[i]+r[j]-mp.mpf(d[i+1][j+1])**q)/2
        return sum(mp.lu_solve(C,r))
    ls=[1,1,1,1,99,99];d=[[0]*7 for _ in range(7)]
    for i in range(6):
        d[0][i+1]=d[i+1][0]=ls[i]
        for j in range(i+1,6):d[i+1][j+1]=d[j+1][i+1]=ls[i]+ls[j]
    M0=mass(d,mp.mpf('.5'));d[5][6]=d[6][5]=197;M1=mass(d,mp.mpf('.5'))
    assert M1>M0
    d2=[[0,1,15],[1,0,16],[15,16,0]];M2=mass(d2,mp.mpf('.25'));R2=4/(4-2**mp.mpf('.25'))
    assert M2>R2
    out['counterexample_masses']={"M1_star":str(M0),"M1_shortened":str(M1),"M1_difference":str(M1-M0),"M2_star":str(M2),"M2_claimed_bound":str(R2)}
    out['no_numerical_step_is_used_as_a_proof_premise']=True
    (HERE/'checks'/'numerical_results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':main()
