import numpy as np, itertools, math, json
rng=np.random.default_rng(5)
def ptolemaic(d):
    n=len(d)
    for i,j,k in itertools.combinations(range(n),3):
        if d[i,j]>d[i,k]+d[k,j]+1e-9 or d[i,k]>d[i,j]+d[j,k]+1e-9 or d[j,k]>d[i,j]+d[i,k]+1e-9: return False
    for i,j,k,l in itertools.combinations(range(n),4):
        x=[d[i,j]*d[k,l],d[i,k]*d[j,l],d[i,l]*d[j,k]]
        if max(x)>sum(x)-max(x)+1e-9: return False
    return True
def T_m(m): return 1+m/((m-1)**2//4)
out={}
for m in [11,12,13,14]:
    a=(m-1)//2; r=m-a; q=math.log2(T_m(m)); worst=1e9; cnt=0; best_z=None
    for trial in range(600):
        eps=rng.uniform(0.0,0.06)
        d=np.zeros((m,m))
        for i in range(m):
            for j in range(i+1,m):
                if i<a and j<a: v=rng.uniform(1-eps,1)
                elif i>=a and j>=a: v=rng.uniform(2-4*eps,2-2*eps)
                else: v=rng.uniform(1-eps/2,1)
                d[i,j]=d[j,i]=v
        if not ptolemaic(d): continue
        cnt+=1; E=d**q; J=np.eye(m)-np.ones((m,m))/m; G=-J@E@J/2
        lam=float(np.linalg.eigvalsh(G).min()); worst=min(worst,lam)
        z=np.array([1/a]*a+[-1/r]*r); worst=min(worst,-(z@E@z)/2)
    out[f'm={m}']={'T_m':T_m(m),'(a,r)':(a,r),'metrics':cnt,'min_eig_centred_Gram':worst}
    print(out[f'm={m}'])
json.dump(out,open('near_extremal.json','w'),indent=1,default=str)
