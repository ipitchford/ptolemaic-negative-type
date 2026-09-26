---
title: "Audit of the all-size proof of Conjecture 6.4 (P(m) for every m)"
date: 25 September 2026
---

## 1. Verdict

I read the note in full and found no gap. All four package scripts replay unchanged here (`replay/`). The argument has three new pieces, each of which I re-derived or tested independently (`audit_allsize.py`, `audit_allsize.json`):

**Star packing (Section 2).** The scalar inequality K(t) = (1+t)^p − t^p ≤ δ t^{−β} is the tangent-line bound for the concave function h(s) = log K(e^s): the displayed formula for h″ matches SymPy at a sample point, and 1 − (1−p)z^p − p z^{p−1} ≤ 0 on (0,1) is weighted AM–GM (checked on a grid, maximum −1e-10). The inequality itself holds on a grid of 25 exponents × 4001 ratios with zero excess. The row manipulation M + Tw_i − δ t_i H ≤ 2 requires w ≥ 0 and follows from the row equation; the Chebyshev step H/S ≤ M/n needs w non-increasing in ℓ, which follows from the row differences because b(t) = (1 + t^p − (1+t)^p)/2 is increasing (b′ = p(t^{p−1} − (1+t)^{p−1})/2 > 0). The LP extension is standard: a bounded polytope, a vertex maximiser, and either a zero coordinate (restrict and use monotonicity of L_n in n) or n active rows. LP tests on 4,000 random stars never exceeded L_n (maximum excess −8e-6). The Laplace representation R = (T/2)diag(r) + G with G a Gram matrix of the functions 1 − e^{−sℓ_i} in L²(s^{−1−p}ds) is exact: ∫(1 − e^{−sℓ})s^{−1−p}ds = ℓ^p Γ(1−p)/p and the diagonal gives c r_i.

**Sign-free comparison (Section 3).** If v = C⁻¹1 ≥ 0 then w = diag(r)v ≥ 0 and Bw = Rv ≤ Cv = 1 entrywise because C ≥ R; if u ≥ 0, the same argument applies to diag(r)⁻¹C diag(r)⁻¹, whose star comparison has reciprocal lengths, whose inverse vector is diag(r)u ≥ 0, and whose mass is unchanged. Nothing about the star's own inverse is used. This is the step that removes the dimension cap.

**Inverse-correlation induction (Section 5).** The deletion formula r′ = (r − st)/√((1−s²)(1−t²)) is the partial-correlation formula for N = −A⁻¹; verified numerically to 2e-15. The three cases are exhaustive: st ≤ 0 gives r′ ≥ r; s,t > 0 gives r′ ≥ r/(1+r) via (1−st)² − (1−s²)(1−t²) = (s−t)² and monotonicity of x ↦ (r−x)/(1−x); both incident entries positive for every third index means u, v > 0 after regauging, so Section 3 applies. Compatibility (5.4) re-factored symbolically: k_n/(1+k_n) − k_{n−1} = (T−1)[n − (n−2)T]/(T(n−1)). Deleting the infinity index is legitimate because the deleted matrix is regauged into an augmented matrix of an inverted Ptolemaic metric, and the induction hypothesis covers all Ptolemaic metrics of the smaller size. The bound |r| < 1 comes from Haynsworth inertia additivity applied to the complement of a pair, which is itself an augmented matrix of a strict-negative-type metric. On 4,150 random Ptolemaic metrics with 4–8 points and exponents inside the lemma's range, the minimum over all normalised inverse entries plus k_n was 0.040 or larger; the bound is never approached by random metrics, as expected.

**Bootstrap (Section 7).** With a ≤ r and a ≥ 2 one has r ≥ 3, so a + 2 ≤ m − 1 and every two-pole residual lives in a strictly smaller metric; the lemma's parameter condition T ≤ (a+1)/(a−1) follows from T < T_m ≤ (a+1)r/(a(r−1)) and r ≥ a. Balanced patterns need no transport. The m = 5 case is covered by the same induction for p < 1 (pattern 2+3 with n = 3, condition T < 9/4), so the only imported small cases are the thresholds P(3), P(4), P(5) themselves, where p > 1. Strictness below the endpoint and non-strictness at the endpoint by continuity are as stated. Sharpness on CS(a,r) gives 2^p ≤ 1 + m/(a(m−1−a)), maximised at a(m−1−a) = ⌊(m−1)²/4⌋, which reproduces both parity branches of the conjecture.

Residual risks: the case analysis and inertia bookkeeping were checked by reading, not by a proof assistant; the induction has many interlocking hypotheses (strictness for all smaller Ptolemaic metrics, including inverted ones, at the same exponent), and I traced each use but a formal check is the natural next verification. Baker, Huh, Kummer and Lorscheid report a Lean formalisation of their q(5) theorem, so the infrastructure for that exists.

## 2. Corrections to my previous note

Both auxiliary statements I proposed are false, and the package's counterexamples verify:

- (M1) mass monotonicity: star (1,1,1,1,99,99) at p = 1/2 has mass 2.11231199; shortening the long-long distance from 198 to 197 keeps the metric Ptolemaic and raises the mass to 2.11233713. My searches missed this because they used moderate length ratios and the effect is 2.5e-5.
- (M2) star mass bound without truncation: the two-leaf star (1,15) at p = 1/4 has mass 1.4417 > 4/(4 − 2^{1/4}) = 1.4231. My probes only tested parameters with R_n(T) > 2, where the truncation max{2, R_n} is inactive.

The reduction of the conjecture to (M1)+(M2) that I stated was therefore a reduction to false statements. The package's replacement uses neither: the packing theorem controls nonnegative subsolutions of Bw ≤ 1 rather than inverse vectors, and the correlation induction replaces mass comparison.

## 3. Corroboration at the first new sizes

Near-extremal Ptolemaic metrics were sampled by shrinking CS(a,r) inward (A-part and cross distances in [1−ε, 1], B-part in [2−4ε, 2−2ε], ε ≤ 0.06, Ptolemy checked exactly), 600 per size. At p = P(m) the centred Gram matrix had no negative eigenvalue beyond rounding (minimum −6e-16) for m = 11, 12, 13, 14, and CS(a,r) itself fails at p + 0.001 (`near_extremal.json`). This is consistency, not evidence for the proof.

## 4. Prior-art status (bounded search, 25 September 2026)

Baker, Huh, Kummer and Lorscheid state the conjecture (their 6.4) and prove q(4), q(5); Ercan proves q(6), q(7); Baker's blog post of 21 July 2026 restates it as Conjecture A and reports the q(5) proof as originally produced by GPT-5.5 Pro. I found no published or preprint resolution of the general case. The formula P(m) = log₂(1 + m/⌊(m−1)²/4⌋) agrees with the conjecture's two parity branches for every m ≥ 3 (checked m = 3,…,8 by hand).

## Files

- `replay/`: the package's four scripts as run here, with logs.
- `audit_allsize.py`, `.json`, `.log`; `near_extremal.py`, `.json`, `.log`.
- `uploaded_package/`: the package as received, unchanged.

## Sources

Baker, M. (2026, July 21). The geometry of snowflaked Ptolemaic metric spaces [Blog post]. https://mattbaker.blog/2026/07/21/the-geometry-of-snowflaked-ptolemaic-metric-spaces/

Baker, M., Huh, J., Kummer, M., & Lorscheid, O. (2026). Lorentzian polynomials and matroids over triangular hyperfields 2: Analytic aspects [Preprint]. arXiv. https://arxiv.org/abs/2607.15375

Ercan, E. (2026). Ptolemaic negative type and the values q(6) and q(7) [Preprint]. arXiv. https://arxiv.org/abs/2608.20606

Li, H., & Weston, A. (2010). Strict p-negative type of a metric space. Positivity, 14(3), 529–545. https://doi.org/10.1007/s11117-009-0035-2
