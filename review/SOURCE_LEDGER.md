# Source and attribution ledger
**Prior source check recorded 25 September 2026; carried forward for version 1.0.** This is a targeted source check, not an exhaustive novelty review. No claim of unpublished priority follows from it. All references below are external to the supplied proof package; none is a source for the new proof's correctness.

## The conjecture and the imported endpoints

**Baker, M., Huh, J., Kummer, M., & Lorscheid, O. (2026).** *Lorentzian polynomials and matroids over triangular hyperfields 2: Analytic aspects* (Version 2) [Preprint]. arXiv. https://arxiv.org/abs/2607.15375v2

Inspected: versioned HTML https://arxiv.org/html/2607.15375v2 and abstract metadata. Version 2 is dated 18 August 2026. Load-bearing locators: Conjecture 6.4 (sharp parity formula); Proposition 7.5 (`q(n)=P(n−1)`); Theorem 7.16 and Corollary 7.17 (four-point endpoint). The statement used here is the rank-two uniform threshold, not a resolution of every matroid threshold. The source's own AI/Lean disclosure concerns its earlier theorem and is not evidence that our result has been formalised.

**Ercan, E. (2026).** *Ptolemaic negative type and the values q(6) and q(7)* (Version 1) [Preprint]. arXiv. https://arxiv.org/abs/2608.20606v1

Inspected: https://arxiv.org/html/2608.20606v1. Theorem 1.1 supplies `P(5)=log₂(9/4)` and `P(6)=1`. The five-point endpoint is imported only for the all-cardinality corollary. The new manuscript independently proves every cardinality from six onward and does not call its scalar-defect estimate, Bernstein certificate or balanced transport as a proof premise. The preceding inversion/partial-correlation framework is cited for attribution. The complete external Bernstein certificate has not been replayed for this package.

## Classical metric and linear-algebra background

**Schoenberg, I. J. (1938).** Metric spaces and positive definite functions. *Transactions of the American Mathematical Society, 44*(3), 522–536. https://doi.org/10.1090/S0002-9947-1938-1501980-0

Role: historical negative-type/embedding correspondence. The finite Gram identity and embedding construction used in the manuscript are reproved explicitly. A primary scan is available at https://pages.stat.wisc.edu/~wahba/stat860/pdf1/schoenberg.1938.pdf. No full third-party paper is redistributed in this publication package.

**Li, H., & Weston, A. (2010).** Strict p-negative type of a metric space. *Positivity, 14*, 529–545. https://doi.org/10.1007/s11117-009-0035-2. Preprint: https://arxiv.org/abs/0901.0695

Role: strict descent and the classical strict-negative-type literature. This is not an input to the new strong induction. It supports the optional strictness statement below the imported small-case endpoints in Section 7.2. The arXiv metadata and stated strictness theorem were checked.

**Sánchez, S. (2012).** On the supremal p-negative type of finite metric spaces. *Journal of Mathematical Analysis and Applications, 389*(1), 98–107. https://doi.org/10.1016/j.jmaa.2011.11.041. Preprint: https://arxiv.org/abs/1108.0451

Inspected: abstract metadata and primary preprint, including the inverse/determinant characterisation (Corollary 2.4 in the preprint). Role: classical background for inverse-distance criteria. The manuscript's root-dependent mixed inverse pairing `μ` is not equated with the classical metric M-constant. The preprint uses the singular title “of a finite metric space”; the published citation uses “of finite metric spaces”. No new-invariant claim is made.

**Fiedler, M. (2011).** *Matrices and graphs in geometry*. Cambridge University Press. https://doi.org/10.1017/CBO9780511973611

Role: background on augmented distance matrices and geometric matrix identities. Publisher metadata and front matter were checked; the full monograph was not audited. No numbered theorem is imported from it. The relevant barycentric and inverse formulas are derived in the paper. Print year 2011 is used; a later online publication date does not replace it.

**Haynsworth, E. V. (1968).** Determination of the inertia of a partitioned Hermitian matrix. *Linear Algebra and its Applications, 1*(1), 73–81. https://doi.org/10.1016/0024-3795(68)90050-5

Role: attribution for inertia additivity. Bibliographic metadata were checked. The precise block congruence used here is written out and checked independently; no unseen theorem or hypothesis is assumed from the article.

## Context only; not a proof dependency

**Baker, M. (2026, July 21).** *The geometry of snowflaked Ptolemaic metric spaces* [Blog post]. https://mattbaker.blog/2026/07/21/the-geometry-of-snowflaked-ptolemaic-metric-spaces/

Inspected for the public formulation and chronology mentioned in the supplied gate. The blog attributes an earlier four-point proof to an AI-assisted workflow and refers to its Lean formalisation. This context is not a formalisation, specialist endorsement or priority adjudication of the present proof. The manuscript relies on the versioned mathematical preprints rather than the blog.

## Search boundary

The supplied gate reports a bounded search finding no general resolution or antecedent of the two new lemmas. That report is preserved, not converted into a stronger assertion. The prior manuscript-preparation check verified cited versions, theorem locators and bibliographic details. This revision action did not perform a new literature search or silently expand that corpus. It did not search every journal, preprint repository, language, private circulation or newly posted result. A release should describe the contribution by its proved statement and give the literature attribution above without asserting an exhaustive priority search.
