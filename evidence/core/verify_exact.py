#!/usr/bin/env python3
"""Dependency-free rational checks. These check identities, not the universal proof."""
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import hashlib, json, random

HERE = Path(__file__).resolve().parent

def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]
def tr(A):
    return [list(x) for x in zip(*A)]
def mm(A,B):
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
def mv(A,x):
    return [sum((a*b for a,b in zip(row,x)),F(0)) for row in A]
def dot(x,y):
    return sum((a*b for a,b in zip(x,y)),F(0))
def inv(A):
    n=len(A); M=[list(map(F,row))+e for row,e in zip(A,eye(n))]
    for j in range(n):
        p=next(i for i in range(j,n) if M[i][j])
        M[p],M[j]=M[j],M[p]
        s=M[j][j]; M[j]=[a/s for a in M[j]]
        for i in range(n):
            if i!=j:
                s=M[i][j]
                M[i]=[a-s*b for a,b in zip(M[i],M[j])]
    return [row[n:] for row in M]
def sub(A,I):
    return [[A[i][j] for j in I] for i in I]
def aug(C):
    n=len(C);r=[C[i][i] for i in range(n)]
    E=[[F(0)]*(n+1) for _ in range(n+1)]
    for i in range(n):
        E[0][i+1]=E[i+1][0]=r[i]
        for j in range(n): E[i+1][j+1]=r[i]+r[j]-2*C[i][j]
    A=[[F(0)]+[F(1)]*(n+1)]+[[F(1)]+row for row in E]
    return A,E

def witness(a,r,T):
    m=a+r
    raw=[[F(0) if i==j else F(2 if i>=a and j>=a else 1) for j in range(m)] for i in range(m)]
    E=[[F(0) if i==j else T if i>=a and j>=a else F(1) for j in range(m)] for i in range(m)]
    return raw,E

def metric_checks(d):
    n=len(d); tc=pc=0
    for i,j,k in permutations(range(n),3):
        assert d[i][j]<=d[i][k]+d[k][j];tc+=1
    for i,j,k,l in combinations(range(n),4):
        p=[d[i][j]*d[k][l],d[i][k]*d[j][l],d[i][l]*d[j][k]]
        for h in range(3):
            assert 2*p[h]<=sum(p);pc+=1
    return tc,pc

def main():
    out={"status":"PASS","scope":"exact identities and finite witnesses; analytic proof in RESEARCH_NOTE.md"}
    rng=random.Random(260925)
    blocks=deletions=gauges=0
    for n in range(2,8):
        for trial in range(4):
            X=[[F(rng.randint(-3,3),rng.randint(1,3)) for _ in range(n)] for _ in range(n)]
            C=mm(tr(X),X)
            for i in range(n): C[i][i]+=1
            I=inv(C);r=[C[i][i] for i in range(n)];ones=[F(1)]*n
            u=mv(I,r);v=mv(I,ones);M=sum(u);P=sum(v);Q=dot(r,u)
            predicted=[[-Q/2,1-M/2]+[x/2 for x in u], [1-M/2,-P/2]+[x/2 for x in v]]
            predicted += [[u[i]/2,v[i]/2]+[-x/2 for x in I[i]] for i in range(n)]
            A,E=aug(C);V=inv(A)
            assert V==predicted; assert mm(A,V)==eye(n+2);blocks+=1
            for k in range(n+2):
                keep=[i for i in range(n+2) if i!=k]
                assert V[k][k]!=0
                small=inv(sub(A,keep))
                calc=[[V[i][j]-V[i][k]*V[k][j]/V[k][k] for j in keep] for i in keep]
                assert small==calc;deletions+=1
            scales=[F(rng.randint(1,6),rng.randint(1,5)) for _ in range(n+2)]
            scaled=[[A[i][j]*scales[i]*scales[j] for j in range(n+2)] for i in range(n+2)]
            Vi=inv(scaled)
            assert Vi==[[V[i][j]/scales[i]/scales[j] for j in range(n+2)] for i in range(n+2)]
            for i,j in combinations(range(n+2),2):
                assert Vi[i][j]**2/(Vi[i][i]*Vi[j][j])==V[i][j]**2/(V[i][i]*V[j][j])
            gauges+=1
    out["augmented_inverse_cases"]=blocks;out["deletion_cases"]=deletions;out["diagonal_congruence_cases"]=gauges

    # Rational checks of the two elementary inequalities in the inverse-triangle step.
    tri=0
    for R in range(1,19):
        r=F(R,20)
        for S in range(1,R+1):
            s=F(S,20)
            for U in range(1,R+1):
                t=F(U,20)
                assert (1-s*t)**2-(1-s*s)*(1-t*t)==(s-t)**2
                assert (r-s*t)/(1-s*t)>=r/(1+r)
                tri+=1
    out["normalised_triangle_rational_cases"]=tri

    # Exact constant compatibility with zero truncation.
    constants=0
    for n in range(3,150):
        upper=min(F(199,100),F(n,n-2))
        for j in range(1,40):
            T=1+(upper-1)*F(j,40)
            k=max(F(0),F(n-1,n)*T-1)
            h=max(F(0),F(n-2,n-1)*T-1)
            assert h<=k/(1+k)
            constants+=1
    out["compatibility_rational_cases"]=constants

    # Uniform exact-star packing is attained whenever the untruncated bound is >=2.
    packing=0
    for n in range(1,30):
        for T in [F(5,4),F(4,3),F(3,2),F(16,9),F(19,10)]:
            c=1-T/2; w=1/(1+(n-1)*c)
            assert w+(n-1)*c*w==1
            assert n*w==F(2*n)/(2*n-(n-1)*T)
            assert n*w<=max(F(2),F(2*n)/(2*n-(n-1)*T))
            packing+=1
    out["uniform_star_cases"]=packing

    # Threshold minimisation and every support condition below it.
    thresholds=[];patterns=0
    for m in range(3,301):
        T=1+F(m,((m-1)**2)//4)
        vals=[F((a+1)*(m-a),a*(m-a-1)) for a in range(1,m//2+1)]
        assert min(vals)==T
        if m%2: assert T==F((m+1)**2,(m-1)**2)
        else: assert T==F(m+2,m-2)
        if m>=6:
            for a in range(2,m//2+1):
                r=m-a;n=a+1
                assert a+2<m
                assert T<=F(n,n-2)
                k=max(F(0),F(a*T-a-1,a+1))
                assert (r-1)*k<=1
                patterns+=1
        if m in [6,7,8,9,10,11,12,13,14,20,50,100,300]:
            thresholds.append({"m":m,"T":str(T)})
    out["thresholds"]=thresholds;out["support_pattern_cases"]=patterns

    # Endpoint witnesses: exact all-pair distance decomposition into two simplex Gram blocks.
    records=[]
    for m in [3,4,5,6,7,8,9,10,11,12,13,14,20]:
        a=(m-1)//2;r=m-a;T=1+F(m,((m-1)**2)//4)
        d,E=witness(a,r,T);tc,pc=metric_checks(d)
        z=[F(1,a)]*a+[-F(1,r)]*r
        assert dot(z,mv(E,z))==0
        J=[[F(i==j)-F(1,m) for j in range(m)] for i in range(m)]
        G=mm(mm(J,E),J);G=[[-x/2 for x in row] for row in G]
        target=[[F(0) for _ in range(m)] for _ in range(m)]
        for i in range(a):
            for j in range(a):target[i][j]=(F(i==j)-F(1,a))/2
        for i in range(a,m):
            for j in range(a,m):target[i][j]=T*(F(i==j)-F(1,r))/2
        assert G==target
        # The positive-eigenvalue multiplicities are a-1 and r-1, rank m-2.
        records.append({"m":m,"a":a,"r":r,"T":str(T),"triangles":tc,"ptolemy":pc,"rank":m-2})
    out["endpoint_witnesses"]=records

    # M1: both raw seven-point metrics satisfy all inequalities exactly.
    lengths=[1,1,1,1,99,99]
    d=[[F(0) for _ in range(7)] for _ in range(7)]
    for i in range(6):
        d[0][i+1]=d[i+1][0]=F(lengths[i])
        for j in range(i+1,6):d[i+1][j+1]=d[j+1][i+1]=F(lengths[i]+lengths[j])
    mc1=metric_checks(d);d[5][6]=d[6][5]=F(197);mc2=metric_checks(d)
    assert F(185,132)**2<2
    out["M1_counterexample"]={"star_checks":mc1,"shortened_checks":mc2,"sign_certificate":"sqrt(2)>185/132, plus inequalities in note"}
    # M2: intervals and rational threshold separating the two masses.
    ru=F(246,125);Tu=F(119,100)
    assert ru**4>15 and Tu**4>2
    assert 7*ru*ru+8*ru<43
    assert F(400,281)<F(36,25)
    out["M2_counterexample"]={"r_upper":str(ru),"T_upper":str(Tu),"M_lower":"36/25","uniform_upper":"400/281"}

    # Positive strict-four-point cut decomposition, full rational examples.
    binary=[[int((j>>k)&1) for k in range(3)] for j in range(1,8)]
    cuts=0
    for trial in range(50):
        weights=[F(rng.randint(1,30),rng.randint(1,20)) for _ in binary]
        C=[[sum((w*b[i]*b[j] for w,b in zip(weights,binary)),F(0)) for j in range(3)] for i in range(3)]
        s1,s2,s3=[C[i][i] for i in range(3)];p,q0,t=C[0][1],C[0][2],C[1][2]
        lo=max(F(0),p+q0-s1,p+t-s2,q0+t-s3);hi=min(p,q0,t)
        assert lo<hi;zz=(lo+hi)/2
        bb=[[1,1,1],[1,1,0],[1,0,1],[0,1,1],[1,0,0],[0,1,0],[0,0,1]]
        ww=[zz,p-zz,q0-zz,t-zz,s1-p-q0+zz,s2-p-t+zz,s3-q0-t+zz]
        assert min(ww)>0
        reconstructed=[[sum((w*b[i]*b[j] for w,b in zip(ww,bb)),F(0)) for j in range(3)] for i in range(3)]
        assert C==reconstructed;cuts+=1
    out["strict_cut_decompositions"]=cuts
    dest=HERE/'checks'/'exact_results.json';dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
