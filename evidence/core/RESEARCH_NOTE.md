# Sharp negative type of finite Ptolemaic metrics: an all-size proof draft

Date: 25 September 2026.

## Status

This note gives an analytic proof of the conjectured universal negative-type exponent for every number of points at least six. Together with the established three-, four- and five-point results, it gives the all-size formula in Baker–Huh–Kummer–Lorscheid, Conjecture 6.4, via their Proposition 7.5.

The new proof uses a linear packing inequality for exact snowflaked stars and a normalised inverse-correlation induction. It does not assume either of the two global mass inequalities proposed in the incoming audit: both are false as stated. Explicit counterexamples are included.

The argument has been checked by mathematical derivation and by separate exact and symbolic implementations of its algebraic identities. These programs do not formally verify the universal analytic proof. Independent expert review, proof-assistant formalisation and historical-priority verification remain outstanding. This is a research proof draft, not a claim of peer-reviewed acceptance.

The new result for m >= 6 is independent of Ercan's computer-assisted five-point theorem, his scalar-defect certificate and his balanced coefficient transport. The known value P(5), when quoting the complete all-size formula including the small cases, remains an external preprint result.

## 1. Statement and notation

A metric d on a finite set X is Ptolemaic if

\[
d(x,y)d(z,w)\le d(x,z)d(y,w)+d(x,w)d(y,z)
\]

for every four points. It has q-negative type when

\[
\sum_{x,y\in X}z_xz_y d(x,y)^q\le0
\quad\text{whenever}\quad\sum_xz_x=0.
\]

Strict q-negative type means strict inequality for every nonzero such vector.

Let P(m) be the largest universal negative-type exponent for Ptolemaic metrics on m points. Put

\[
T_m=1+\frac{m}{\lfloor(m-1)^2/4\rfloor}\qquad(m\ge3).
\]

**Theorem 1 (new all-size range).** Every Ptolemaic metric on m >= 6 points has log_2(T_m)-negative type. It has strict q-negative type for every 0 < q < log_2(T_m). Complete split metrics show that this exponent is sharp.

In fact the proof establishes strict q-negative type for every m >= 2 whenever

\[
0<q<\min\{1,\log_2T_m\},
\]

with the evident convention for m=2. Endpoint passage is then by continuity for m >= 6, where T_m <= 2.

Consequently, using the established small cases,

\[
\boxed{
P(m)=\begin{cases}
2\log_2\!\dfrac{k+1}{k},&m=2k+1,\ k\ge1,\\
\log_2\!\dfrac{k+1}{k-1},&m=2k,\ k\ge2.
\end{cases}}
\]

Baker–Huh–Kummer–Lorscheid's identification q(n)=P(n-1) gives

\[
\boxed{
q(n)=\begin{cases}
2\log_2\!\dfrac{n}{n-2},&n\ge4\text{ even},\\
\log_2\!\dfrac{n+1}{n-3},&n\ge5\text{ odd}.
\end{cases}}
\]

Throughout the new proof, fix 0 < q < 1, T=2^q, delta=T-1, a=T/2 and c=1-T/2. A superscript on d denotes entrywise powers, not a matrix power.

For n >= 1 define

\[
R_n(T)=\frac{2n}{2n-(n-1)T},\qquad
L_n(T)=\max\{2,R_n(T)\},
\]

and

\[
k_n(T)=1-\frac2{L_n(T)}
=\max\left\{0,\frac{(n-1)T-n}{n}\right\}.
\]

The truncation at zero is important. A mass bound below 2 does not give a positive lower correlation bound through Cauchy–Schwarz.

## 2. Exact-star packing in every dimension

Let l_1,...,l_n > 0 be lengths and put r_i=l_i^q. Define the exact snowflaked-star Gram matrix R by

\[
R_{ii}=r_i,\qquad
R_{ij}=\frac{r_i+r_j-(l_i+l_j)^q}{2}\quad(i\ne j).
\]

Let D=diag(r) and B=RD^{-1}. Thus B_ii=1 and

\[
B_{ij}=b(l_i/l_j),\qquad
b(t)=\frac{1+t^q-(1+t)^q}{2}\quad(i\ne j).
\]

The function b is positive and strictly increasing on (0,infinity). Its value at 1 is c. This follows directly from concavity of t^q and

\[
b'(t)=\frac q2\{t^{q-1}-(1+t)^{q-1}\}>0.
\]

### 2.1 Positive definiteness

The integral identity

\[
x^q=\frac q{\Gamma(1-q)}\int_0^\infty(1-e^{-sx})s^{-1-q}\,ds
\]

follows by substitution and integration by parts. Therefore the kernel

\[
g(l_i,l_j)=\frac{l_i^q+l_j^q-(l_i+l_j)^q}{2}
=\frac q{2\Gamma(1-q)}\int_0^\infty
(1-e^{-sl_i})(1-e^{-sl_j})s^{-1-q}\,ds
\]

is positive semidefinite. On the diagonal it equals c r_i. Consequently

\[
R=aD+[g(l_i,l_j)]\succ0.
\]

This proves positive definiteness for every positive length vector and every dimension. No assumption about the signs of an inverse vector is made.

### 2.2 A scalar supporting-power inequality

Set K(t)=(1+t)^q-t^q. Then

\[
\boxed{K(t)\le\delta t^{-\beta},\qquad
\beta=\frac{qc}{\delta}>0.}\tag{2.1}
\]

For a proof, write h(s)=log K(e^s) and z=e^s/(1+e^s). Differentiation gives

\[
h'(s)=q\frac{z-z^q}{1-z^q},
\]

\[
h''(s)=
\frac{qz(1-z)\,[1-(1-q)z^q-qz^{q-1}]}{(1-z^q)^2}\le0.
\]

The final sign follows from weighted arithmetic–geometric mean:

\[
(1-q)z^q+qz^{q-1}\ge
(z^q)^{1-q}(z^{q-1})^q=1.
\]

The tangent to h at zero has intercept log delta and slope -beta. Concavity proves (2.1). The inequality is strict unless t=1.

### 2.3 Full-support solutions

Suppose Bw=1 and w>0. Write M=sum_i w_i. The function

\[
F(t)=\sum_j b(t/l_j)w_j
\]

is increasing. Since its diagonal contribution is c w_i rather than w_i,

\[
F(l_i)+a w_i=1.
\]

Thus w_i is non-increasing as l_i increases.

Put t_i=l_i^{-beta}, H=sum_i w_i/t_i and S=sum_i 1/t_i. The row equations also read

\[
M+w_i=2+\sum_{j\ne i}K(l_i/l_j)w_j.
\]

Using (2.1),

\[
M+T w_i-\delta t_i H\le2.
\]

Divide by t_i and sum:

\[
(M-2)S\le\{(n-1)\delta-1\}H.\tag{2.2}
\]

If M<=2 there is nothing to prove. Otherwise the coefficient in braces is positive. The sequences w_i and 1/t_i=l_i^beta are oppositely ordered, so

\[
\frac HS\le\frac Mn.
\]

For completeness, this is the identity

\[
MS-nH=-\sum_{i<j}(w_i-w_j)(l_i^\beta-l_j^\beta)\ge0.
\]

Substitution in (2.2) gives

\[
\{n+1-(n-1)\delta\}M\le2n,
\]

or M<=R_n(T).

### 2.4 Linear packing theorem

**Lemma 2.** For every w>=0 satisfying Bw<=1,

\[
\boxed{\sum_iw_i\le L_n(T).}\tag{2.3}
\]

Proof: maximise sum_i w_i on the polytope w>=0, Bw<=1. It is nonempty and compact: B is positive with diagonal 1, so each w_i<=1. Choose a vertex maximiser.

If one or more coordinates vanish, restrict to its positive support. The surviving row inequalities are precisely the same problem for a smaller length vector. Induction in n applies, since L_k(T)<=L_n(T) for k<=n. The monotonicity follows immediately from R_n=2n/[n(2-T)+T]. The case n=1 is elementary.

If every coordinate is positive, none of the nonnegativity constraints is active. A vertex requires n independent active row constraints; there are only n such constraints, so Bw=1. Section 2.3 applies. This proves (2.3).

This lemma does not assert that R^{-1}1 or R^{-1}r is nonnegative. In particular, it remains valid in the high-dimensional regime that blocked the preceding proof.

## 3. Nonnegative inverse vectors of a general metric

Let e_ij=d(i,j)^q, choose a root o, and set r_i=e_oi. Its Schoenberg matrix is

\[
C_{ij}=\frac{r_i+r_j-e_{ij}}2,
\qquad C_{ii}=r_i.
\]

For every zero-sum vector z, the identity z^T E z=-2 z_{\mathrm{nonroot}}^T C z_{\mathrm{nonroot}} shows that strict q-negative type is equivalent to C being positive definite. In this section assume that condition. Put u=C^{-1}r, v=C^{-1}1 and M=1^Tu=r^Tv.

Choose star lengths l_i=d(o,i). The ordinary triangle inequality implies the entrywise comparison C>=R with identical diagonals.

**Lemma 3.** If either u>=0 or v>=0, then M<=L_n(T).

If v>=0, set w=Dv. Then w>=0 and

\[
Bw=Rv\le Cv=1.
\]

Lemma 2 yields M=sum_i w_i<=L_n.

If u>=0, use C*=D^{-1}CD^{-1}. Its diagonal is r*=1/r and

\[
(C*)^{-1}1=Du\ge0.
\]

The matrix R*=D^{-1}RD^{-1} is the exact-star comparison matrix for lengths 1/l_i; hence C*>=R*. Its mass is the same:

\[
(r*)^T(C*)^{-1}1=1^Tu=M.
\]

The preceding argument applies to C*. No global mass monotonicity or positivity of a radial inverse is used.

## 4. Augmented matrices, inversion and normalised inverse correlations

For e=d^q on n+1 points, adjoin an index infinity and define A_infinity,i=1, A_ij=e_ij, A_ii=0. In the order infinity, root, n leaves,

\[
A=\begin{pmatrix}
0&1&1^T\\1&0&r^T\\1&r&r1^T+1r^T-2C
\end{pmatrix}.
\]

If C>0, a Schur complement with respect to the leading 2x2 block shows that A has inertia (1,n+1), meaning one positive and n+1 negative eigenvalues. Define

\[
P=1^TC^{-1}1,\qquad Q=r^TC^{-1}r.
\]

Direct block inversion gives

\[
\boxed{A^{-1}=\begin{pmatrix}
-Q/2&1-M/2&u^T/2\\
1-M/2&-P/2&v^T/2\\
u/2&v/2&-C^{-1}/2
\end{pmatrix}.}\tag{4.1}
\]

In particular, the normalised inverse entry between infinity and the root is

\[
\rho=\frac{2-M}{\sqrt{PQ}},\qquad PQ\ge M^2.\tag{4.2}
\]

Lemma 3 therefore implies rho>=-k_n(T) when either u or v is nonnegative. If M<=2 then rho>=0. If 2<M<=L_n then

\[
\rho\ge\frac{2-M}{M}\ge\frac2{L_n}-1=-k_n.
\]

### 4.1 Regauging preserves the metric class

Positive diagonal congruence sends A to SAS and A^{-1} to S^{-1}A^{-1}S^{-1}. Signs and normalised inverse entries are unchanged.

For any index p, choose S so that every off-diagonal entry in row p becomes 1. When p is an original finite point, the new finite metric is the ordinary metric inversion

\[
\widehat d(i,j)=\frac{d(i,j)}{d(p,i)d(p,j)},\qquad
\widehat d(\infty,i)=\frac1{d(p,i)}.
\]

Triangles avoiding the new point infinity follow from Ptolemy for d. Triangles containing infinity follow from the original triangle inequalities. Ptolemy inequalities avoiding infinity follow by multiplying by the common denominator. Ptolemy inequalities containing infinity reduce to ordinary triangles of d. Thus the new metric is Ptolemaic. Taking qth powers gives exactly the regauged A.

Every principal submatrix of order at least three can likewise be put in this form for a Ptolemaic metric on one fewer point. An order-two principal matrix has inertia (1,1) directly.

### 4.2 Proper-subset inertia controls inverse blocks

Assume all metrics obtained from the augmented array by deletion and regauging, including the current n+1-point metric, have strict q-negative type. Their augmented matrices are nonsingular with one positive eigenvalue.

Let J be a pair of indices. The complementary principal matrix has one positive eigenvalue. Inertia additivity in A then says that the 2x2 Schur complement on J is negative definite. Its inverse is (A^{-1})_JJ. Therefore every such inverse block is negative definite. In particular

\[
(A^{-1})_{ii}<0,
\qquad
\left|\frac{(A^{-1})_{ij}}
{\sqrt{(A^{-1})_{ii}(A^{-1})_{jj}}}\right|<1.
\]

These facts concern only smaller-point positivity in the main induction below; they do not assume the final metric being proved positive has already been embedded.

## 5. The normalised inverse-triangle induction

**Lemma 4.** Fix 0<q<1 and T=2^q. Suppose every Ptolemaic metric on at most n+1 points has strict q-negative type. If n>=3 and

\[
T\le\frac n{n-2},\tag{5.1}
\]

then every off-diagonal normalised entry of the inverse of an augmented n+1-point metric is at least -k_n(T). The same conclusion holds for n=2 without condition (5.1).

Proof is by induction on n. For n=2, e=d^q has strict triangle inequalities, so its Euclidean triangle is acute. One may also check (4.1) directly: in C=[[r_1,s],[s,r_2]], strict triangles give 0<s<min(r_1,r_2), hence u,v>0 and Lemma 3 gives rho>=0 in every gauge. Here k_2=0.

For the step, lower-dimensional conditions hold because n/(n-2) is decreasing. Write V=A^{-1}. If there are negative off-diagonal entries, let r>0 be their greatest normalised magnitude, attained at indices p,q. By Section 4.2, r<1. Suppose for contradiction that r>k_n.

For any third index j write

\[
s=-\frac{V_{pj}}{\sqrt{(-V_{pp})(-V_{jj})}},\qquad
t=-\frac{V_{qj}}{\sqrt{(-V_{qq})(-V_{jj})}}.
\]

Deleting j from A changes its inverse by

\[
V^{(j)}=V_{\bar j,\bar j}-\frac{V_{\bar j,j}V_{j,\bar j}}{V_{jj}}.
\]

The signed magnitude of the new pq entry is therefore

\[
r'=\frac{r-st}{\sqrt{(1-s^2)(1-t^2)}}.\tag{5.2}
\]

If st<=0 then r'>=r>k_n>=k_{n-1}, contradicting the induction hypothesis. Consequently both entries incident to j are nonzero and have the same sign.

Suppose some j has V_pj<0 and V_qj<0. Then 0<s,t<=r, by maximality of r. Since

\[
(1-st)^2-(1-s^2)(1-t^2)=(s-t)^2\ge0,
\]

and r-st>=r-r^2>0,

\[
r'\ge\frac{r-st}{1-st}
\ge\frac{r-r^2}{1-r^2}
=\frac r{1+r}.\tag{5.3}
\]

The middle inequality uses st<=r^2 and the fact that x -> (r-x)/(1-x) is decreasing when r<1.

The constants satisfy

\[
\boxed{k_{n-1}\le\frac{k_n}{1+k_n}.}\tag{5.4}
\]

If a truncated k vanishes this is immediate. When both are positive, the exact difference is

\[
\frac{k_n}{1+k_n}-k_{n-1}
=\frac{(T-1)[n-(n-2)T]}{T(n-1)}\ge0.
\]

Thus r>k_n and (5.3) contradict the lower-dimensional bound.

The only remaining possibility is that, for every j other than p,q, both incident entries are positive. Regauge p to infinity and q to the root. Formula (4.1) gives u,v>0. Lemma 3 and (4.2) then bound this same inverse entry below by -k_n, another contradiction. The cases are exhaustive and prove the lemma.

**Important distinction.** This is an induction for normalised correlations, not for mass. It never claims the globally false monotonicity M(C)<=M(R). It also avoids the earlier inverse-mass estimate h+2h^2.

## 6. From inverse entries to conditioned residuals

Consider a Ptolemaic metric on a+2 points, with a distinguished anchors and two poles p,q. Assume its Schoenberg matrix is positive definite. Choose one anchor as the root and partition the Gram matrix into the remaining anchors and the poles. Let S be the 2x2 pole Schur complement.

The corresponding leaf block of the augmented inverse is -C^{-1}/2, and its pole block is -S^{-1}/2. For a 2x2 positive definite S,

\[
\frac{(-S^{-1})_{12}}{\sqrt{(-S^{-1})_{11}(-S^{-1})_{22}}}
=\frac{S_{12}}{\sqrt{S_{11}S_{22}}}.
\]

Lemma 4 has n=a+1. It therefore gives

\[
\boxed{\frac{S_{12}}{\sqrt{S_{11}S_{22}}}
\ge-\kappa_a(T),\qquad
\kappa_a(T)=\max\left\{0,\frac{aT-a-1}{a+1}\right\},}\tag{6.1}
\]

provided T<2 and, for a>=2, T<=(a+1)/(a-1), and provided all metrics of size at most a+2 have strict q-negative type. This is the hypothesis discharged from smaller sizes in the next section.

## 7. A noncircular strict-negative-type induction

**Proposition 5.** For every m>=2, every m-point Ptolemaic metric has strict q-negative type whenever 0<q<min(1,log_2 T_m), using only q<1 for m=2.

### 7.1 Bases: at most four points

For 0<q<1, e=d^q is an ordinary metric with strict triangle inequalities on distinct points. Strictness follows from d_ij<=d_ik+d_kj and strict subadditivity of t^q on positive inputs.

For four points, write its root Gram matrix with diagonal s_1,s_2,s_3 and off-diagonal entries p,q_0,t. Strict metric triangles imply

\[
\max(0,p+q_0-s_1,p+t-s_2,q_0+t-s_3)<\min(p,q_0,t).
\]

Choose z strictly between these endpoints. The Gram matrix is the sum of bb^T for b in {111,110,101,011,100,010,001}, with respective positive coefficients

\[
z,\ p-z,\ q_0-z,\ t-z,\
s_1-p-q_0+z,\ s_2-p-t+z,\ s_3-q_0-t+z.
\]

The three singleton terms already give a positive definite diagonal matrix. This proves strict negative type. The two- and three-point cases follow directly or by the same Gram calculation.

### 7.2 Induction step

Assume the proposition for all smaller cardinalities, and let d have m>=5 points. The numbers T_m decrease with m. Hence every proper subset, and every Ptolemaic metric of that smaller cardinality, has strict q-negative type at the current q.

Let z be nonzero and zero-sum. Remove its zero coordinates. If fewer than m coordinates remain, use the induction hypothesis. Otherwise change its overall sign so it has a positive and r negative coordinates with a<=r and a+r=m. Normalise both absolute coefficient sums to one.

If a=1, writing the negative coefficients beta_i>0 gives

\[
\sum_i\beta_i e_{oi}-\sum_{i<j}\beta_i\beta_j e_{ij}
\ge\sum_i\beta_i^2e_{oi}>0.
\]

Now a>=2. Since m>=5 and a<=r, r>=3. In particular

\[
a+2\le m-1.
\]

Every metric used for the two-pole correlation estimate (6.1) is therefore a proper-size metric whose strict negative type has already been proved. The inverse argument never assumes strictness of the full m-point metric.

For fixed a,r define

\[
F(a,r)=\frac{(a+1)r}{a(r-1)}
=1+\frac{m}{a(m-1-a)}.
\]

The integer maximum of a(m-1-a) is floor((m-1)^2/4), so

\[
T<T_m\le F(a,r)\le\frac{a+1}{a-1}.
\]

The last inequality is equivalent to r>=a. Thus the parameter condition for Lemma 4 holds. Moreover

\[
(r-1)\kappa_a(T)<1.\tag{7.1}
\]

Use one positive point as the Gram root. Let K be the block on the other a-1 positive points, L the cross block and H the block on the r negative points. The full Gram matrix need not yet be positive definite. Its anchor block K is positive definite by induction. Set S=H-L^TK^{-1}L.

Each S_ii is positive by strictness on a+1 points, and each pair satisfies (6.1) by strictness and Lemma 4 on a+2 points. Set t_i=beta_i sqrt(S_ii)>0. Then

\[
\begin{aligned}
\beta^TS\beta
&\ge\sum_i t_i^2-2\kappa_a\sum_{i<j}t_it_j\\
&\ge[1-(r-1)\kappa_a]\sum_i t_i^2>0.
\end{aligned}
\]

If alpha denotes the positive coefficients excluding the root, completing the square gives

\[
-\tfrac12z^TEz
=(\alpha-K^{-1}L\beta)^TK(\alpha-K^{-1}L\beta)+\beta^TS\beta>0.
\]

This proves strict negative type and closes the induction. Balanced sign patterns need no separate coefficient transport.

### 7.3 Endpoints

For m>=6, log_2 T_m<=1. For fixed d and fixed zero-sum z, z^T d^q z is continuous in q. Letting q increase to log_2 T_m proves the non-strict endpoint inequality. Since d and z were arbitrary, this is the universal lower bound in Theorem 1.

No uniform bound on distance ratios, nonsingularity at the endpoint or compactness of the space of metrics is needed.

## 8. Matching upper bound and parity formula

The complete split metric CS(a,r) has a points in one part and r in the other, with all distinct distances equal to 1 except distances within the r-part, which are 2.

It is a metric and is Ptolemaic. A quadruple with two points in each part gives the binding equality 2=1+1. With zero, one, three or four points in the r-part, all three opposite-edge products are equal, so the inequalities are automatic. The same statements cover repeated-index cases.

Assign coefficients 1/a to the a-part and -1/r to the r-part. The negative-type inequality is

\[
\frac{a-1}{2a}+\frac{r-1}{2r}2^q\le1,
\]

or 2^q<=F(a,r). Choose a to maximise a(m-1-a). This gives the sharp upper bound T_m. Every exponent above log_2 T_m fails on this one fixed metric.

For m=2k+1, take (a,r)=(k,k+1), giving T_m=((k+1)/k)^2.

For m=2k, take (a,r)=(k-1,k+1) or (k,k), giving T_m=(k+1)/(k-1).

For m>=6 this matches Section 7. The values m=3,4,5 are the established P(3)=2, P(4)=log_2 3 and P(5)=log_2(9/4). The first two are identified in Baker–Huh–Kummer–Lorscheid; the third is Ercan's theorem. The new induction independently reproves P(6)=1 and all larger cases.

## 9. Why the proposed mass route was not used

### 9.1 Global mass monotonicity is false

Take a root, four short leaves of raw length 1, and two long leaves of raw length 99. The star distances between leaves are their length sums. Change only the long–long raw distance from 198 to 197. Both seven-point arrays are Ptolemaic; this is verified by integer enumeration in the exact script (and follows by separating the cases according to the number of long leaves).

At q=1/2 the masses are approximately

\[
M_{\rm star}=2.11231199339264,
\qquad M_{\rm shortened}=2.11233712655318.
\]

Here is an analytic sign proof, rather than a floating-point comparison. Write r=sqrt(99), c=1-1/sqrt(2), b=(r-9)/2 and A_0=1+3c. If the long–long raw distance is s, its constant-block row coefficient is D(s)=2r-sqrt(s)/2. The constant-block determinant is Delta=A_0D-8b^2>0. For a long leaf,

\[
u_B=\frac{A_0r-4b}{\Delta}>0,
\qquad v_B=\frac{A_0-4b}{\Delta}<0.
\]

The inequalities hold throughout 197<=s<=198: A_0>1, 0<b<1/2 and D>r imply Delta>r-2; A_0r-4b>18-r>0. Also

\[
A_0-4b=22-3/\sqrt2-2\sqrt{99}<0,
\]

as is confirmed by squaring, reducing to sqrt(2)>185/132. Thus

\[
\frac{dM}{dD}=-2u_Bv_B>0.
\]

Shortening s increases D, hence increases mass. The contrast eigenvalues remain positive. This disproves M(C)<=M(R_star) even for genuine Ptolemaic metrics, without refuting any claimed universal exponent.

### 9.2 The untruncated star mass bound is false

Take a three-point star with raw root lengths 1 and 15, and q=1/4. Set r=15^(1/4) and k=(r-1)/2. Then

\[
C=\begin{pmatrix}1&k\\k&r\end{pmatrix},\qquad
M=\frac{2r-k(1+r)}{r-k^2}.
\]

The identity

\[
25[2r-k(1+r)]-36[r-k^2]
=-\tfrac12(7r^2+8r-43)
\]

and r<246/125 prove M>36/25. In contrast T=2^(1/4)<119/100 gives

\[
R_2(T)=\frac4{4-T}<\frac{400}{281}<\frac{36}{25}.
\]

Thus the proposed untruncated bound is false. The packing theorem's bound max(2,R_n) and the correlation truncation max(0,k) avoid this error.

## 10. Verification, dependency audit and limits of the claim

The proof is analytic, not a finite computation claiming to cover infinitely many sizes. In particular:

1. The scalar inequality is proved by differentiation and weighted AM–GM.
2. The star packing result covers the full positive orthant, including arbitrarily large length ratios, by a compact finite-dimensional linear programme at each fixed length vector.
3. The inverse-triangle proof takes the maximum of finitely many inverse entries of one fixed array. It does not posit an extremising metric.
4. Lemma 4 assumes strictness only for metrics on at most n+1 points. In Section 7, n+1=a+2<=m-1. Thus all positive-definiteness assumptions have smaller-cardinality proofs.
5. Exponent endpoints are obtained by pointwise continuity for each fixed metric and coefficient vector. Singular endpoint Gram matrices cause no difficulty.
6. No assumption on inverse-star signs is made; no global mass monotonicity is used; no polynomial relaxation, Bernstein certificate or old inverse-mass triangle inequality appears in the new induction.
7. The proof gives the sharp universal exponent and a family of sharp witnesses. It does not classify every equality metric or establish that complete split metrics are the only extremisers.

The accompanying scripts separately check exact matrix identities, the scalar derivatives, the constant comparison, support minimisation, small cut decomposition, exact metric witnesses, and the two counterexamples. Numerical LP and inverse-correlation checks are labelled corroborative only. None is needed for the universal claims.

The incoming audit and predecessor proof are preserved by a recorded SHA-256 of the input archive. They have not been edited. This note supersedes the proposed M1/M2 route and the finite-size inverse-positivity restriction.

## Sources and what is imported

**Conjecture, notation, correspondence and the first small cases**

Baker, M., Huh, J., Kummer, M., & Lorscheid, O. (2026). *Lorentzian polynomials and matroids over triangular hyperfields. Part 2: Analytic aspects* (Version 2) [Preprint]. arXiv. https://arxiv.org/abs/2607.15375v2

**Known five-point endpoint and the preceding inversion/partial-correlation framework**

Ercan, E. (2026). *Ptolemaic negative type and the values q(6) and q(7)* (Version 1) [Preprint]. arXiv. https://arxiv.org/abs/2608.20606v1

The m>=6 proof above reproduces the elementary inversion and Gram identities it uses and does not import the computer-assisted part of Ercan's theorem. The external five-point endpoint is used only to append m=5 to the complete formula. The correspondence with triangular-hyperfield thresholds is imported from Baker–Huh–Kummer–Lorscheid. A comprehensive literature audit of priority for the new packing and inverse-correlation arguments has not been completed.
