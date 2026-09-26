#!/usr/bin/env python3
"""Independent SymPy reconstruction of the load-bearing algebraic identities."""
from pathlib import Path
import json
import sympy as s

HERE=Path(__file__).resolve().parent
checks=[]
def zero(expr,name):
    assert s.factor(s.cancel(s.simplify(expr)))==0, (name,expr)
    checks.append(name)

def main():
    z,q=s.symbols('z q',positive=True)
    hp=q*(z-z**q)/(1-z**q)
    hpp=q*z*(1-z)*(1-(1-q)*z**q-q*z**(q-1))/(1-z**q)**2
    zero(s.diff(hp,z)*z*(1-z)-hpp,'logarithmic_second_derivative')
    # Direct first derivative of log K, using t=z/(1-z).
    t=s.symbols('t',positive=True)
    K=(1+t)**q-t**q
    direct=t*s.diff(K,t)/K
    transformed=q*(t/(1+t)-(t/(1+t))**q)/(1-(t/(1+t))**q)
    assert s.simplify(s.powsimp(direct-transformed,force=True))==0
    checks.append('logarithmic_first_derivative')
    T,n=s.symbols('T n',positive=True)
    zero(q*(s.Rational(1,2)-1/T)/(1-1/T)+q*(1-T/2)/(T-1),'supporting_tangent_slope')
    kn=(n-1)*T/n-1;kh=(n-2)*T/(n-1)-1
    zero(kn/(1+kn)-kh-(T-1)*(n-(n-2)*T)/(T*(n-1)),'dimension_compatibility')
    Rn=2*n/(2*n-(n-1)*T)
    zero(1-2/Rn-kn,'mass_to_correlation_constant')
    zero(Rn-(2*n)/(n+1-(n-1)*(T-1)),'packing_constant_rearrangement')
    m,a=s.symbols('m a',positive=True)
    zero((a+1)*(m-a)/(a*(m-a-1))-1-m/(a*(m-1-a)),'threshold_minimisation_formula')
    r=s.symbols('r',positive=True)
    zero((a+1)/(a-1)-(a+1)*r/(a*(r-1))-(a+1)*(r-a)/(a*(a-1)*(r-1)),'parameter_condition')
    kap=(a*T-a-1)/(a+1)
    zero(1-(r-1)*kap-(a*(r-1)/(a+1))*((a+1)*r/(a*(r-1))-T),'copositive_margin')

    # General Gram matrix of dimension 3; reconstruct inverse from cofactors.
    d1,d2,d3,x,y,z0=s.symbols('d1 d2 d3 x y z0')
    C=s.Matrix([[d1,x,y],[x,d2,z0],[y,z0,d3]])
    det=C.det();I=C.adjugate()/det
    one=s.ones(3,1);diag=s.Matrix([d1,d2,d3]);u=I*diag;v=I*one
    M=(one.T*u)[0];P=(one.T*v)[0];Q=(diag.T*u)[0]
    A=s.Matrix.vstack(s.Matrix([[0,1,1,1,1]]),s.Matrix([[1,0,d1,d2,d3]]),s.Matrix.hstack(one,diag,diag*one.T+one*diag.T-2*C))
    V=s.Matrix.vstack(s.Matrix.hstack(s.Matrix([[-Q/2,1-M/2],[1-M/2,-P/2]]),s.Matrix.vstack(u.T,v.T)/2),s.Matrix.hstack(u/2,v/2,-I/2))
    residual=A*V-s.eye(5)
    assert all(s.factor(x)==0 for x in residual)
    checks.append('augmented_inverse_generic_dimension_three')

    # Delete a coordinate in a generic unit-negative-diagonal inverse matrix.
    rr,ss,tt=s.symbols('r s t',real=True)
    V3=s.Matrix([[-1,-rr,-ss],[-rr,-1,-tt],[-ss,-tt,-1]])
    A3=V3.inv(); deleted=A3[:2,:2].inv()
    wanted=s.Matrix([[-(1-ss**2),-rr+ss*tt],[-rr+ss*tt,-(1-tt**2)]])
    assert all(s.factor(x)==0 for x in deleted-wanted)
    checks.append('normalised_inverse_deletion')
    zero((1-ss*tt)**2-(1-ss**2)*(1-tt**2)-(ss-tt)**2,'denominator_comparison')
    zero((rr-ss*tt)/(1-ss*tt)-rr/(1+rr)-(rr**2-ss*tt)/((1-ss*tt)*(1+rr)),'triangle_magnitude_lower_bound')

    # Gram-to-residual correlation: squared identity plus off-diagonal sign factor.
    S=C[1:,1:]-(C[1:,:1]*C[:1,1:])/d1
    Sinv=S.inv()
    assert all(s.factor(x)==0 for x in I[1:,1:]-Sinv)
    zero((I[1,2]**2)/(I[1,1]*I[2,2])-S[0,1]**2/(S[0,0]*S[1,1]),'residual_correlation_squared')
    zero(-I[1,2]-S[0,1]/S.det(),'residual_correlation_sign')

    # Chebyshev identity from direct expansion, independent of the ordered argument.
    w=s.symbols('w0:5');v0=s.symbols('v0:5')
    expr=sum(w)*sum(v0)-5*sum(wi*vi for wi,vi in zip(w,v0))
    zero(expr+sum((w[i]-w[j])*(v0[i]-v0[j]) for i in range(5) for j in range(i+1,5)),'opposite_order_chebyshev')

    # Four-point cut decomposition.
    zz=s.symbols('zz')
    vec=[s.Matrix(b) for b in [(1,1,1),(1,1,0),(1,0,1),(0,1,1),(1,0,0),(0,1,0),(0,0,1)]]
    weight=[zz,x-zz,y-zz,z0-zz,d1-x-y+zz,d2-x-z0+zz,d3-y-z0+zz]
    D=s.zeros(3)
    for c0,b in zip(weight,vec):D+=c0*b*b.T
    assert s.expand(D-C)==s.zeros(3)
    checks.append('strict_four_point_cut_decomposition')

    # M2 certificate.
    rr=s.symbols('rr');kk=(rr-1)/2
    zero(25*(2*rr-kk*(1+rr))-36*(rr-kk**2)+(7*rr**2+8*rr-43)/2,'star_mass_counterexample')
    result={"status":"PASS","implementation":"SymPy; independent reconstruction, not a proof assistant","checks":checks,"count":len(checks)}
    (HERE/'checks'/'symbolic_results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
