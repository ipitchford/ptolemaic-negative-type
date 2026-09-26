"""Adversarial test of Lemma 4 at its parameter boundary: maximise (-min normalised augmented-inverse entry) - k_n(T)
over Ptolemaic metrics on n+1 points, with T just below n/(n-2). A positive value would refute the lemma."""
import numpy as np, itertools, math, json, sys
from scipy.optimize import minimize
rng=np.random.default_rng(21); out={}
def cons(d):
    m=len(d); c=[]
    for i,j,k in itertools.permutations(range(m),3):
        if i<j: c.append(d[i,k]+d[k,j]-d[i,j])
    for i,j,k,l in itertools.combinations(range(m),4):
        a,b,cc=d[i,j]*d[k,l],d[i,k]*d[j,l],d[i,l]*d[j,k]; c+=[b+cc-a,a+cc-b,a+b-cc]
    return np.array(c)
def deficit(d,q,n):
    m=len(d); e=d**q; A=np.zeros((m+1,m+1)); A[0,1:]=1; A[1:,0]=1; A[1:,1:]=e
    try: V=np.linalg.inv(A)
    except Exception: return -1.0
    dg=np.diag(V)
    if np.any(dg>=0): return -1.0
    N=V/np.sqrt(np.outer(dg,dg)); off=N[~np.eye(m+1,dtype=bool)]
    T=2**q; k=max(0.0,((n-1)*T-n)/n); return float(-off.min()-k)
for n in [3,4,5,6]:
    m=n+1; Tb=n/(n-2); q=min(0.999,math.log2(Tb)-1e-3); iu=np.triu_indices(m,1)
    def unpack(v): d=np.zeros((m,m)); d[iu]=np.exp(v); return d+d.T
    best=-1e9; feas=0
    for s in range(40):
        if s%2: P=rng.normal(0,1,(m,3)); v0=np.log(np.linalg.norm(P[:,None]-P[None],axis=2)[iu])
        else:
            a=m//2; d0=np.ones((m,m)); d0[a:,a:]=2; np.fill_diagonal(d0,0); v0=np.log(d0[iu])+rng.normal(0,0.15,len(iu[0]))
        try:
            r=minimize(lambda v: -deficit(unpack(v),q,n), v0, method='SLSQP', bounds=[(-4,4)]*len(v0),
                       constraints=[{'type':'ineq','fun':lambda v: cons(unpack(v))}], options={'maxiter':300,'ftol':1e-12})
            if cons(unpack(r.x)).min()>=-1e-8: feas+=1; best=max(best,deficit(unpack(r.x),q,n))
        except Exception: pass
    out[f'n={n}']={'points':m,'T':2**q,'k_n':max(0.0,((n-1)*2**q-n)/n),'feasible_runs':feas,'max deficit (>0 would refute)':best}
    print(out[f'n={n}'],flush=True)
json.dump(out,open('adversarial_lemma4.json','w'),indent=1)
