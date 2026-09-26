"""Independent checks of the all-size proof: scalar inequality (2)/concavity, counterexamples to (M1),(M2),
compatibility (6), deletion formula (5), star-packing LP, Lemma 4 on random Ptolemaic metrics, and the final theorem
near the extremal split metrics for m=11..14."""
import numpy as np, sympy as sp, itertools, math, json
from scipy.optimize import linprog
out={}; rng=np.random.default_rng(12)
# (a) scalar inequality and concavity
p_=sp.symbols('p',positive=True); s_=sp.symbols('s',real=True)
K=lambda t,p: (1+t)**p-t**p
h=sp.log(K(sp.exp(s_),p_)); h2=sp.diff(h,s_,2)
z=sp.symbols('z',positive=True)
claim=p_*z*(1-z)*(1-(1-p_)*z**p_-p_*z**(p_-1))/(1-z**p_)**2
diff_expr=sp.simplify((h2-claim.subs(z,sp.exp(s_)/(1+sp.exp(s_)))).subs({p_:sp.Rational(3,7),s_:sp.Rational(2,5)}))
out['h_second_derivative_formula_residual_at_sample']=float(diff_expr)
worst=-1e9; worst2=-1e9
for p in np.linspace(0.02,0.98,25):
    T=2**p; delta=T-1; c=1-T/2; beta=p*c/delta
    t=np.exp(np.linspace(-12,12,4001))
    worst=max(worst,float(np.max(K(t,p)-delta*t**(-beta))))
    zz=np.linspace(1e-4,1-1e-4,2001); worst2=max(worst2,float(np.max(1-(1-p)*zz**p-p*zz**(p-1))))
out['max(K - delta t^-beta) over grid']=worst; out['max(1-(1-p)z^p-p z^(p-1))']=worst2
# (b) counterexamples
def schoen(e,root):
    idx=[i for i in range(len(e)) if i!=root]; r=e[root,idx]; return (r[:,None]+r[None,:]-e[np.ix_(idx,idx)])/2, r
def mass(e,root=0):
    C,r=schoen(e,root); return float(np.ones(len(r))@np.linalg.solve(C,r))
def ptolemaic(d):
    n=len(d)
    for i,j,k in itertools.combinations(range(n),3):
        if d[i,j]>d[i,k]+d[k,j]+1e-9 or d[i,k]>d[i,j]+d[j,k]+1e-9 or d[j,k]>d[i,j]+d[i,k]+1e-9: return False
    for i,j,k,l in itertools.combinations(range(n),4):
        x=[d[i,j]*d[k,l],d[i,k]*d[j,l],d[i,l]*d[j,k]]
        if max(x)>sum(x)-max(x)+1e-9: return False
    return True
L=np.array([1,1,1,1,99,99.0]); d=np.zeros((7,7))
for i in range(6):
    d[0,i+1]=d[i+1,0]=L[i]
    for j in range(6):
        if i!=j: d[i+1,j+1]=L[i]+L[j]
d2=d.copy(); d2[5,6]=d2[6,5]=197
out['M1_counterexample']={'star_ptolemaic':ptolemaic(d),'shortened_ptolemaic':ptolemaic(d2),'M_star':mass(d**0.5),'M_short':mass(d2**0.5),'violates_M1':mass(d2**0.5)>mass(d**0.5)}
d3=np.array([[0,1,15],[1,0,16],[15,16,0.0]]); T=2**0.25
out['M2_counterexample']={'M_star':mass(d3**0.25),'untruncated_R_2':4/(4-T),'exceeds':mass(d3**0.25)>4/(4-T),'truncated_bound_2_holds':mass(d3**0.25)<=2}
# (c) compatibility (6)
n_,T_=sp.symbols('n T',positive=True)
kn=((n_-1)*T_-n_)/n_; knm=((n_-2)*T_-(n_-1))/(n_-1)
out['(6)_residual']=str(sp.simplify(kn/(1+kn)-knm-(T_-1)*(n_-(n_-2)*T_)/(T_*(n_-1))))
# (d)/(e) Lemma 4 and packing on random Ptolemaic metrics
def augmented_normalised(e):
    m=len(e); A=np.zeros((m+1,m+1)); A[0,1:]=1; A[1:,0]=1; A[1:,1:]=e; V=np.linalg.inv(A)
    dg=np.diag(V); assert np.all(dg<0) or None
    N=V/np.sqrt(np.outer(dg,dg)); return A,V,N
def kfun(n,T): return max(0.0,((n-1)*T-n)/n)
lemma_worst={}; del_err=0; pack_worst=-1e9
for m in [4,5,6,7,8]:
    n=m-1; worst=1e9; cnt=0
    for trial in range(1500):
        P=rng.normal(0,1,(m,rng.integers(2,5))); dd=np.linalg.norm(P[:,None]-P[None],axis=2)
        if trial%2: dd=dd*np.exp(rng.normal(0,0.2,(m,m))); dd=np.triu(dd,1); dd=dd+dd.T
        if not ptolemaic(dd): continue
        Tmax=n/(n-2) if n>=3 else 1.99; q=rng.uniform(0.05,min(0.99,math.log2(Tmax))); T=2**q
        e=dd**q
        try: A,V,N=augmented_normalised(e)
        except Exception: continue
        cnt+=1
        off=N[~np.eye(m+1,dtype=bool)]; worst=min(worst,float(off.min()+kfun(n,T)))
        # deletion formula (5) for a random triple
        pq=rng.choice(m+1,3,replace=False); pp,qq,jj=pq
        keep=[i for i in range(m+1) if i!=jj]; Vd=np.linalg.inv(A[np.ix_(keep,keep)]); dgd=np.diag(Vd)
        Nd=Vd/np.sqrt(np.outer(dgd,dgd)); ip,iq=keep.index(pp),keep.index(qq)
        r=-N[pp,qq]; s=-N[pp,jj]; t=-N[qq,jj]
        del_err=max(del_err,abs(-Nd[ip,iq]-(r-s*t)/math.sqrt((1-s*s)*(1-t*t))))
        # packing LP with the star of root 0
        Lr=dd[0,1:]; rr=Lr**q; B=np.zeros((n,n))
        for i in range(n):
            for j in range(n): B[i,j]=1.0 if i==j else (rr[i]+rr[j]-(Lr[i]+Lr[j])**q)/(2*rr[j])
        res=linprog(-np.ones(n),A_ub=B,b_ub=np.ones(n),bounds=[(0,None)]*n,method='highs')
        Ln=max(2.0,2*n/(2*n-(n-1)*T)); pack_worst=max(pack_worst,-res.fun-Ln)
    lemma_worst[f'm={m}']={'metrics':cnt,'min(normalised entry + k_n)':worst}
out['lemma4_random_test']=lemma_worst; out['deletion_formula_max_error']=del_err; out['packing_LP_max(sum w - L_n)']=pack_worst
# (f) final theorem near extremal CS(a,r), m=11..14, and sharpness
def T_m(m): return 1+m/((m-1)**2//4)
final={}
for m in [11,12,13,14]:
    a=(m-1)//2; r=m-a; q=math.log2(T_m(m)); worst=1e9; cnt=0
    base=np.ones((m,m)); base[a:,a:]=2; np.fill_diagonal(base,0)
    for trial in range(400):
        dd=base*np.exp(rng.normal(0,0.05,(m,m))); dd=np.triu(dd,1); dd=dd+dd.T
        if not ptolemaic(dd): continue
        cnt+=1; E=dd**q; J=np.eye(m)-np.ones((m,m))/m; G=-J@E@J/2
        worst=min(worst,float(np.linalg.eigvalsh(G).min()))
    # sharpness: CS(a,r) at q+1e-3 fails
    Eb=base**(q+1e-3); zc=np.array([1/a]*a+[-1/r]*r); fail=float(zc@Eb@zc)
    final[f'm={m}']={'T_m':T_m(m),'a,r':(a,r),'perturbed_Ptolemaic_metrics':cnt,'min_eig_centred_Gram_at_P(m)':worst,'CS_form_at_q+0.001 (should be >0)':fail}
out['final_theorem_near_extremal']=final
json.dump(out,open('audit_allsize.json','w'),indent=1,default=str); print(json.dumps(out,indent=1,default=str))
