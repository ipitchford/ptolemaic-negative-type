---
title: "Quality-gate report: publication decision for the all-size proof of BHKL Conjecture 6.4"
date: 25 September 2026
---

## 1. Boundary and as-of date

Assess whether the all-size proof package (P(m) = log₂(1 + m/⌊(m−1)²/4⌋), equivalently q(n) = P(n−1) for BHKL Conjecture 6.4) makes an original, significant and rigorous contribution within metric geometry / negative type / Lorentzian polynomials over triangular hyperfields, and whether the evidence is sufficient to decide on a DOI-backed release as of 25 September 2026.

## 2. Claim and intended output

Claim: for every m ≥ 3, every m-point Ptolemaic metric has P(m)-negative type with P(m) as above, and the value is sharp (complete split metrics CS(a,r)). Contribution unit: a complete analytic proof of a stated conjecture, plus two new lemmas (a dimension-free star-packing bound; an induction on normalised entries of the inverse of the bordered powered-distance matrix). Output type: mathematical article with verification package.

## 3. Novelty-gate handoff and prior-art status

Statement unit: COLLISION by design — the statement is Conjecture 6.4 of Baker, Huh, Kummer and Lorscheid (arXiv:2607.15375, July 2026), restated as Conjecture A on Baker's blog (21 July 2026). Small cases: q(4), q(5) proved by BHKL (q(5) formalised in Lean); q(6), q(7) by Ercan (arXiv:2608.20606, 20 August 2026).

Proof unit: bounded search (arXiv full text, Baker's blog, the Pith review of Ercan, and the negative-type literature: Lennard–Tonge–Weston 1997, Li–Weston 2010, Sánchez 2012, Doust–Weston, Wolf) found no proof of the general case and no statement of either new lemma. The "mass" quantity is classical in disguise: 1ᵀD_p⁻¹1-type expressions characterise the supremal negative type of a finite metric space in Sánchez (2012), and the bordered-matrix inverse gives circumcentre barycentrics (Fiedler 2011). That affects how the lemmas should be framed, not whether the theorem is new. Outcome for the proof unit: CLEAR TO PROVE within the recorded boundary; absolute novelty language is not licensed (BOUNDED UNCERTAINTY on the two lemmas: cross-disciplinary aliases in Euclidean distance geometry and copositive programming were searched only by keyword).

## 4. Scores (ex post; confidence in brackets)

Originality 3 [medium–high]. The theorem is a stated open conjecture's resolution; the proof route (tangent-line concavity bound → linear packing → sign-free comparison → correlation induction with the exact compatibility k_{n−1} ≤ k_n/(1+k_n)) is not in the literature searched. It is not 4: the objects and the conjecture are others', and the ingredients are elementary.

Significance 3 [medium]. It settles the rank-2 uniform case q(U_{2,n}) of the BHKL programme for all n, gives sharp universal negative-type exponents for Ptolemaic metrics of every size, and identifies complete split metrics as extremal. Uptake route: direct citation by the BHKL/Ercan line and by the negative-type/generalised-roundness community. Not 4: the rank-2 case is one strand of a larger programme.

Rigour 3 [medium]. The proof was read in full by a second, independent reviewer (this audit) with no gap found; every load-bearing identity was re-derived symbolically or verified numerically; the four package scripts replay in a clean environment; adversarial optimisation against the key lemma at its parameter boundary (n = 3…6, T just below n/(n−2)) returns a maximal deficit of 10⁻¹¹ or smaller, i.e. the lemma is tight and never violated; near-extremal tests at m = 11–14 are consistent. Two auxiliary conjectures from an earlier round were shown false and are explicitly not used. Not 4: no formal verification and no external human review; the induction carries several interlocking hypotheses (strictness of all smaller Ptolemaic metrics, including inverted ones, at the same exponent) that were traced by reading only.

Local decision aid: Q = 100 × (3/4 · 3/4 · 3/4)^{1/3} = 75. Not an official score.

## 5. Evidence ledger

- Package: `ptolemaic_all_size_proof.zip` (SHA256SUMS inside), scripts `verify_exact.py`, `verify_symbolic.py`, `verify_numerical.py`, `replay.py`; replayed here, logs in `replay/`.
- Independent audit: `audit_allsize.py/.json`, `near_extremal.py/.json`, `adversarial_lemma4.py/.json` (this bundle and the previous one).
- Prior art: arXiv:2607.15375 (BHKL), arXiv:2608.20606 (Ercan), Baker blog 2026-07-21, Sánchez 2012 (doi:10.1016/j.jmaa.2011.11.041 — supremal p-negative type via the distance matrix), Li–Weston 2010, Fiedler 2011. Access date 25 Sept 2026.

## 6. Assurance status and its limits

Status: replayed from a clean environment; load-bearing identities independently re-derived; adversarially tested; independently read by a second reviewer. Not formally verified. Not externally peer reviewed. The limit: a reading can miss a hypothesis mismatch in a multi-level induction; the adversarial tests cover the lemma numerically but not the logical dependency chain.

## 7. Reception and maturity

Immature (unreleased). Reception to be recorded after 12 months.

## 8. Red flags, missing evidence and reviewer disagreement

- Two earlier auxiliary lemmas proposed in this thread were false; the current proof does not use them, but the episode shows how a tight-looking numerical picture can mislead. Publishing the counterexamples is a control, not a flaw.
- The verification scripts check identities and witnesses, not the universal statement; the note says so.
- No human expert has read the argument.
- Priority language for the two lemmas must stay bounded (see §3).
- No reviewer disagreement is recorded because there is only one independent reviewer.

## 9. Decision and next reassessment

Decision: **go with controls.**

Controls:
1. Release as a versioned, DOI-backed proof paper with the verification package and the false-lemma ledger; state the assurance level of §6 in the abstract or introduction in one sentence, and avoid absolute priority language for the lemmas.
2. Cite BHKL, Ercan and Sánchez for the objects (conjecture, small cases, transport, distance-matrix characterisation of supremal negative type) and Fiedler for the bordered-inverse/circumcentre reading.
3. Start a formalisation of the two new lemmas (the packing theorem and the correlation induction); both are finite linear algebra plus one scalar inequality, and the q(5) Lean formalisation by BHKL is precedent that this is feasible. A successful formalisation moves rigour to 4 and assurance to "formally verified"; a failed one is the fastest route to finding an error.
4. Re-run this gate on any objection, any material revision, or on completion of formalisation; scheduled reassessment 25 December 2026.

Timeliness, named as such and not as quality: the problem is active (three groups of results in July–August 2026), so a delayed release risks being pre-empted; a wrong release risks a public correction. The controls above are the trade-off.

Structured prior, not a calibrated probability: I put the chance that the proof is correct as written, or correct after minor local repairs, at about 0.85, and the chance of a fatal defect at 0.10–0.15, on the basis of the reading, the replay and the tight adversarial tests, against the base rate of long agent-produced inductions.

## 10. Sources and metric definitions

No bibliometric metrics were used; the output is unreleased. Sources are listed in §5 and below.

Baker, M. (2026, July 21). The geometry of snowflaked Ptolemaic metric spaces [Blog post]. https://mattbaker.blog/2026/07/21/the-geometry-of-snowflaked-ptolemaic-metric-spaces/

Baker, M., Huh, J., Kummer, M., & Lorscheid, O. (2026). Lorentzian polynomials and matroids over triangular hyperfields 2: Analytic aspects [Preprint]. arXiv. https://arxiv.org/abs/2607.15375

Ercan, E. (2026). Ptolemaic negative type and the values q(6) and q(7) [Preprint]. arXiv. https://arxiv.org/abs/2608.20606

Fiedler, M. (2011). Matrices and graphs in geometry. Cambridge University Press. https://doi.org/10.1017/CBO9780511973611

Li, H., & Weston, A. (2010). Strict p-negative type of a metric space. Positivity, 14(3), 529–545. https://doi.org/10.1007/s11117-009-0035-2

Sánchez, S. (2012). On the supremal p-negative type of finite metric spaces. Journal of Mathematical Analysis and Applications, 389(1), 98–107. https://doi.org/10.1016/j.jmaa.2011.11.041
