#!/usr/bin/env python3
"""Supplemental exact checks for the typeset manuscript; not a proof assistant.

Reconstructs selected identities independently of the archived core verifiers.
Writes only to an explicitly supplied report path (or prints to stdout).
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sympy as s


def zero(expr):
    if isinstance(expr, s.MatrixBase):
        assert all(s.simplify(x) == 0 for x in expr), expr
    else:
        assert s.simplify(expr) == 0, expr


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    checks = []
    def done(name): checks.append(name)

    # The actual square-completion identity, with no assumption on H's sign.
    K=s.Matrix([[3,1],[1,4]]); L=s.Matrix([[1,2,1],[2,1,3]])
    H=s.Matrix([[2,1,0],[1,-2,1],[0,1,5]])
    alpha=s.Matrix(s.symbols('alpha0:2')); beta=s.Matrix(s.symbols('beta0:3'))
    S=H-L.T*K.inv()*L
    z=alpha.col_join(-beta); C=K.row_join(L).col_join(L.T.row_join(H))
    zero((z.T*C*z)[0]-((alpha-K.inv()*L*beta).T*K*(alpha-K.inv()*L*beta))[0]-(beta.T*S*beta)[0])
    done('square_completion_without_full_positivity')

    # Generic block congruence underlying all inertia uses.
    P=s.eye(5); P[:2,2:5]=-K.inv()*L
    zero(P.T*C*P-s.diag(K,S))
    done('inertia_block_congruence')

    # Classical mixed pairing and distance-matrix inverse relation.
    details=[]
    for n in range(1,7):
        V=s.Matrix(n,n,lambda i,j: s.Integer((i+2)*(j+3)%7-2))
        C=V.T*V+s.eye(n); one=s.ones(n,1); r=s.Matrix(C.diagonal())
        if r.shape != (n,1): r=r.reshape(n,1)
        E=s.zeros(n+1); E[0,1:]=r.T; E[1:,0]=r
        E[1:,1:]=r*one.T+one*r.T-2*C
        oneE=s.ones(n+1,1)
        A=s.zeros(n+2); A[0,1:]=oneE.T; A[1:,0]=oneE; A[1:,1:]=E
        inv=C.inv(); u=inv*r; v=inv*one; mu=(one.T*u)[0]
        U=(one.T*v)[0]; VV=(r.T*u)[0]
        W=s.zeros(n+2); W[0,0]=-VV/2; W[1,1]=-U/2
        W[0,1]=W[1,0]=1-mu/2
        W[0,2:]=u.T/2; W[2:,0]=u/2; W[1,2:]=v.T/2; W[2:,1]=v/2; W[2:,2:]=-inv/2
        zero(A*W-s.eye(n+2)); zero((oneE.T*E.inv()*oneE)[0]-2/VV)
        coeff=s.Matrix([(-1)**i*s.Rational(i+1,n+1) for i in range(n)])
        whole=s.Matrix([-sum(coeff)]).col_join(coeff)
        zero((whole.T*E*whole)[0]+2*(coeff.T*C*coeff)[0])
        details.append(n)
    done('augmented_inverse_reconstruction_dimensions_1_to_6')
    done('classical_distance_inverse_pairing_dimensions_1_to_6')
    done('gram_zero_sum_identity_dimensions_1_to_6')

    # Exact scalar log-concavity formula using z as the independent variable.
    z,p=s.symbols('z p', positive=True)
    hp=p*(z-z**p)/(1-z**p)
    target=p*z*(1-z)*(1-(1-p)*z**p-p*z**(p-1))/(1-z**p)**2
    zero(s.diff(hp,z)*z*(1-z)-target)
    done('supporting_power_second_derivative')

    T,n=s.symbols('T n', positive=True)
    kn=((n-1)*T-n)/n; km=((n-2)*T-(n-1))/(n-1)
    zero(kn/(1+kn)-km-(T-1)*(n-(n-2)*T)/(T*(n-1)))
    done('dimension_compatibility_untruncated_branch')

    gamma,x,y=s.symbols('gamma x y', real=True)
    zero((1-x*y)**2-(1-x*x)*(1-y*y)-(x-y)**2)
    zero((gamma-x*y)/(1-x*y)-gamma/(1+gamma)-(gamma**2-x*y)/((1-x*y)*(1+gamma)))
    W=s.Matrix([[-1,-gamma,-x],[-gamma,-1,-y],[-x,-y,-1]])
    deleted=W[:2,:2]-W[:2,2:3]*W[2:3,:2]/W[2,2]
    zero(deleted-s.Matrix([[-1+x*x,-gamma+x*y],[-gamma+x*y,-1+y*y]]))
    done('inverse_deletion_sign_and_triangle_comparison')

    t=s.symbols('t0:5'); k=s.symbols('k', real=True)
    pair=sum(t[i]*t[j] for i in range(5) for j in range(i+1,5))
    diff=sum((t[i]-t[j])**2 for i in range(5) for j in range(i+1,5))
    zero(sum(x*x for x in t)-2*k*pair-(1-4*k)*sum(x*x for x in t)-k*diff)
    done('copositive_gap_with_variance_remainder')

    a,r=s.symbols('a r', positive=True)
    F=(a+1)*r/(a*(r-1)); kap=(a*T-a-1)/(a+1)
    zero(F-1-(a+r)/(a*(r-1)))
    zero(1-(r-1)*kap-a*(r-1)*(F-T)/(a+1))
    zero((a+1)/(a-1)-F-(a+1)*(r-a)/(a*(a-1)*(r-1)))
    done('support_threshold_margin_and_parameter_guard')

    count=0
    for m in range(5,301):
        D=(m-1)**2//4; TT=1+s.Rational(m,D)
        for aa in range(2,m//2+1):
            rr=m-aa
            assert rr>=3 and aa+2<=m-1
            FF=s.Rational((aa+1)*rr,aa*(rr-1))
            assert TT<=FF<=s.Rational(aa+1,aa-1)
            count+=1
    done('proper_subset_guards_finite_sanity_check_5_to_300')
    kk=s.symbols('k',positive=True)
    zero(1+(2*kk+1)/(kk**2)-((kk+1)/kk)**2)
    zero(1+2*kk/(kk*(kk-1))-(kk+1)/(kk-1))
    done('both_parity_formulas')

    # First previously obstructed case: eleven points, all rational at endpoint.
    aa,rr=5,6; m=aa+rr; TT=s.Rational(36,25)
    E=s.ones(m)-s.eye(m)
    for i in range(aa,m):
        for j in range(aa,m):
            if i!=j: E[i,j]=TT
    weights=s.Matrix([s.Rational(1,aa)]*aa+[-s.Rational(1,rr)]*rr)
    J=s.eye(m)-s.ones(m)/m; G=-J*E*J/2
    zero((weights.T*E*weights)[0]); zero(G*weights)
    assert G.rank()==m-2
    eig=G.eigenvals(); assert all(e>=0 for e in eig)
    done('eleven_point_endpoint_exact_gram_rank_and_null_vector')

    report={'status':'PASS','scope':'Exact algebraic identities and explicit finite sanity checks; not a formal proof of universal lemmas.',
            'checks':checks,'check_count':len(checks),'inverse_dimensions':details,
            'proper_subset_cases':count,'eleven_point_gram_eigenvalues':{str(e):v for e,v in eig.items()},
            'formal_proof_assistant_used':False}
    text=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(text)
    print(text,end='')

if __name__=='__main__': main()
