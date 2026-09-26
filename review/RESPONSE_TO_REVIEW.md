# Response to the minor-revisions review
**Sharp negative type of finite Ptolemaic metrics · version 1.0**  
**Prepared for Evidence Press · 25 September 2026**

## Disposition

All required and recommended bounded revisions have been implemented. The theorem and proof have not changed. The received review is preserved unchanged in `RECEIVED_REVIEW.md`; this response records actions, not an additional specialist endorsement. The public manuscript remains unrefereed and anonymously presented.

## Principal requests

### R4.1 — Make the induction dependency visible

Immediately after Theorem 5.1 and before its proof, the manuscript now states:

> In the proof for m points, this theorem is applied with n+1=a+2≤m−1, so its strictness hypothesis comes entirely from the outer induction.

The definition of universal strictness and Appendix B are retained. The inserted sentence changes exposition, not the hypothesis or argument.

### R4.2 — Correct the current machine-readable numerical summary

`evidence/current/CURRENT_NUMERICAL_SUMMARY.json` is the current reporting entry point. The four historical empty experiments now have null minima and accepted count zero. Their initial sentinels remain only in the preserved source files. The two components of the historical mixed statistic cannot be reconstructed from its aggregate: they are null with status `not_separately_recorded`, rather than silently inferred.

The supplied follow-up experiment has been rerun with its original seed and sampling design. It now records four distinct measurements: centred-Gram minimum eigenvalue, minimum on an orthonormal zero-sum subspace, the split-vector gap, and its Rayleigh quotient. Each has an accepted-sample count. All 2,400 arrays and measurements are saved at full floating-point precision and independently recomputed by the reporting verifier.

The adversarial rerun retains all 160 attempts, including solver status, convergence flag, iterations, constraint slacks and exceptions/rejections. All 160 met the feasibility tolerance; 150 also reported convergence. Ten tolerance-feasible runs did not converge according to the solver. Their inclusion is explicit and they are excluded from the converged-only maxima. The maximum recorded deficit, about 3.25×10⁻¹², is not a validated counterexample under a 10⁻⁸ feasibility allowance.

The reporting verifier checks every stored array, every aggregate and three deliberate null/count failures. Original reports and scripts remain byte-for-byte unchanged.

### R4.3 — Identify the advance over the predecessor

Section 1.1 now says explicitly that the new numerical values begin at P(7); P(6) is independently recovered. It explains how star packing handles nonnegative inverse vectors in arbitrary dimension and how recursive inverse-entry control handles the other signs, avoiding separate higher-cardinality case analyses. Attribution for inversion, Schur complements, the conjecture, smaller endpoints and complete split witnesses is retained.

## Minor and presentation requests

| Request | Action |
|---|---|
| Define snowflake. | Section 1 defines d raised to an exponent α with 0<α≤1. The abstract says “powered star metrics” before the definition. |
| Explain the split graph. | Proposition 7.1 specifies its clique, independent part, complete cross edges and shortest-path metric. |
| Show the first new values. | The introduction displays P(7)=log₂(16/9) and P(8)=log₂(5/3). |
| Attach the sharpness regime to packing. | Theorem 3.4 now states equal-length attainment when R_n(T)≥2, alongside the bound. The complementary-range caveat remains. |
| Retain Appendix B. | Retained unchanged, with the same theorem/equation references. |
| Keep the assurance distinctions. | Retained in the abstract/assurance line, Section 8 and metadata; the review's REF grade and probabilities are not adopted as release attributes. |
| Add a seven-point illustration. | Section 7 calculates zᵀdᵖz=2/3+(3/4)2ᵖ−2 for CS(3,4), with its exact zero and sharp sign. |
| Record future optimiser diagnostics. | The new reusable script records all attempts and distinguishes convergence, feasibility and measurement validity. |

Equality classification, normalised stability and proof-assistant formalisation remain future work, as permitted by the review. No new claims about them have been added.

## Verification and scope

The original 65-file archive passed full replay. Core exact, symbolic and numerical reports and the 13-group manuscript checks reproduced identically; two exploratory reports differed in floating-point values. The new revision verifier passes 16 checks, including exact seven-point and eight-point calculations. All current numerical measurements have been recomputed from their stored arrays, with explicit numerical tolerances. The immutable publication replay records exact and numerical comparisons separately.

The revised PDF has 15 pages. Theorem and equation labels remain unchanged. The proof for m≥6 still does not import the external five-point certificate. A pointwise endpoint argument still avoids inversion of singular endpoint matrices. The prepared manuscript does not imply website deployment, DOI registration, newly assigned licensing, or authenticated external peer review.
