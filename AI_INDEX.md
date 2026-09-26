# Sharp negative type of finite Ptolemaic metrics

Scholarly creator: **Anonymous**. Publisher: **Evidence Press**. Research manuscript version: **1.0**. Status: **unrefereed candidate**; the presence of these files does not assert public deployment, a DOI, external peer review or formal verification.

## Result and scope

For every integer `m >= 6`, the manuscript gives an analytic proof that the largest exponent universally available to `m`-point Ptolemaic metrics is

`P(m) = log_2(1 + m / floor((m-1)^2/4))`.

Every such metric has strict `p`-negative type for `0 < p < P(m)` and non-strict negative type at the endpoint. Complete split metrics fail negative type for every larger exponent. The proof has no distance-ratio bound. Relative to the cited Ercan predecessor, which already determines `P(5)` and `P(6)`, the first new cardinality is **7**, not 6. The bounded intake comparison identified a KSL attribution correction, now present in the working public source; see the [citation audit](CITATION_AUDIT.md). Exhaustive priority is not asserted.

The all-cardinality corollary imports the four- and five-point endpoints. The rank-two uniform Lorentzian correspondence is `q(n)=P(n-1)`. This is not a theorem about every matroid threshold or a classification of all extremal metrics.

## Read the argument

- [Manuscript PDF](paper/ptolemaic.pdf) and [editable LaTeX](paper/ptolemaic.tex): Theorem 1.1, Corollary 1.2, star packing in Theorem 3.4, conditional inverse-correlation induction in Theorem 5.1, and the separate cardinality induction in Proposition 6.1.
- [Structured claims](CLAIMS.json): quantifiers, hypotheses, imported endpoints, proof locations and limitations.
- [Claim-to-check map](review/CLAIM_CHECK_MAP.csv): which finite checks support each proof component and which universal obligations remain analytic.
- Appendix A of the manuscript: two false stronger inverse-pairing claims and their counterexamples. Appendix B: the strictness-dependency map.

The inverse theorem assumes universal strict negative type at its working cardinality, including inverted metrics. The outer induction uses it only on `a+2 <= m-1` points. Endpoint passage is by pointwise continuity after strict subcritical negative type is proved; no matrix inverse is taken at the endpoint.

## Replay and evidence

Use [replay_publication.py](replay_publication.py) from the package root using the reference **Python 3.13.5** environment and the [pinned requirements](requirements.txt). Installation may require network access; the replay scripts themselves do not. Outputs must be outside the package.

```sh
python replay_publication.py --mode integrity
python replay_publication.py --mode exact --output /tmp/ptolemaic-exact
python replay_publication.py --mode full --output /tmp/ptolemaic-full
```

Do **not** run the historical verifiers with `python -O`: they contain assertions. The wrapper explicitly refuses optimized execution and launches its children with optimization disabled. That refusal is a safeguard, not evidence of a successful optimized replay.

The [supplied full replay receipt](evidence/current/full_replay/REPLAY_REPORT.json) records a 103-file input snapshot before and after nine jobs; see the [replay scope](evidence/current/REPLAY_SCOPE.md). Exact and symbolic outputs are compared separately from exploratory floating-point outputs. Two historical exploratory reports differ numerically in that receipt. The [fresh intake checks](INTAKE_CHECKS.md) add exact/full replay and hostile controls against the supplied 130-file package in a separately recorded macOS environment. They do not automatically cover later manuscript or archive changes.

Use the [current numerical summary](evidence/current/CURRENT_NUMERICAL_SUMMARY.json) and [reporting ledger](review/EVIDENCE_LEDGER.md), not superseded sentinel values or mixed historical statistics. Empty samples and unavailable historical components remain null. The 2,400 stored near-extremal samples and 160 optimization attempts are bounded corroboration, not a universal certificate. Optimizer feasibility is distinct from convergence, and small positive floating deficits under a feasibility tolerance are not certified counterexamples.

## Trust, sources and rights

- [Assurance](ASSURANCE.md): analytic proof versus finite checking, supplied review, and absent external/formal assurances.
- [Sources](SOURCES.md), [citation audit](CITATION_AUDIT.md) and [research-gate record](RESEARCH_GATES.json): dependencies, reported historical reading scope, current refresh status and nonclaims.
- [Provenance](PROVENANCE.md), [received-input hashes](review/INPUTS.json), [received review](review/RECEIVED_REVIEW.md) and [response](review/RESPONSE_TO_REVIEW.md): immutable inputs and revision boundaries.
- [Component licences](LICENSES.md) and [public-domain statement](PUBLIC_DOMAIN.md): CC0-1.0 for original research prose/data, MIT for original code, and preserved third-party/historical rights. A supplied review is not automatically relicensed or authenticated.
- [Package manifest](SHA256SUMS): file integrity only. Final archive identity and any later repository, tag, DOI and public-readback identities must be supplied by the release coordinator.

No SAT certificate, proof-assistant formalization, independent reimplementation, authenticated specialist endorsement or calibrated correctness probability is claimed. Successful execution and schema/link checks do not establish the adequacy of the proof or literature search.
