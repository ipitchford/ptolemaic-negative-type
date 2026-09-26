# Sharp negative type of finite Ptolemaic metrics

**Anonymous · Evidence Press · Unrefereed candidate · Manuscript version 1.0**

For every integer `m >= 6`, the manuscript presents an analytic proof of the sharp universal negative-type exponent for `m`-point Ptolemaic metrics:

`P(m) = log_2(1 + m / floor((m-1)^2/4))`.

Negative type is strict below this exponent. Complete split metrics attain the threshold and fail above it. The proof places no bound on distance ratios. Relative to the inspected Ercan predecessor, the first new cardinality is **7**; the six-point value is independently recovered. The all-cardinality corollary combines this argument with the cited smaller endpoints and the established rank-two uniform correspondence `q(n)=P(n-1)`.

## Start here

- [Manuscript PDF](paper/ptolemaic.pdf), [LaTeX source](paper/ptolemaic.tex) and [structured claims](CLAIMS.json).
- [AI index](AI_INDEX.md) for claim locations, evidence routes, reproducibility and trust boundaries.
- [Assurance](ASSURANCE.md), [sources](SOURCES.md), [citation audit](CITATION_AUDIT.md), and [provenance](PROVENANCE.md).
- [Current reporting summary](evidence/current/CURRENT_NUMERICAL_SUMMARY.json) and [fresh intake checks](INTAKE_CHECKS.md). Historical and fresh floating-point measurements are kept distinct.

The theorem rests on the analytic argument. Exact and symbolic checks support identities and witnesses; numerical experiments are bounded corroboration. No SAT certificate, proof-assistant verification, authenticated external specialist peer review, independent reimplementation or exhaustive priority determination is claimed. The received favourable review is retained as a qualified documentary artifact, not an authenticated endorsement.

## Reproduce the supplied checks

From the package root using the reference **Python 3.13.5** environment and the [pinned requirements](requirements.txt):

```sh
python -m pip install -r requirements.txt
python replay_publication.py --mode integrity
python replay_publication.py --mode exact --output /tmp/ptolemaic-exact
python replay_publication.py --mode full --output /tmp/ptolemaic-full
```

Installation may require network access; the replay itself does not. Put all outputs outside the package. The wrapper refuses `python -O` because archived verifiers rely on assertions. That expected refusal must not be described as a successful optimized replay.

`integrity` checks manifest coverage and bytes. `exact` runs rational, symbolic, manuscript, revision and reporting checks; `full` also repeats the supplied numerical designs. A PASS is scoped to those checks, not a universal proof certificate. Public-repository packaging changes and later manuscript metadata/citation edits need their own exact target and checks.

To rebuild the paper and response with a suitably provisioned LaTeX installation:

```sh
python scripts/build_paper.py --output /tmp/ptolemaic-typeset --response
```

No TeX packages are automatically downloaded by that command. The earlier intake rebuild encountered missing local dependencies. The final manuscript was subsequently rebuilt successfully and all 15 pages inspected: see [final typeset receipt](evidence/intake/FINAL_TYPESET_RECEIPT.json) and [presentation QA](publication/PDF_QA.md). The unchanged historical response PDF is preserved; its local rebuild requires DejaVu Serif to be available to XeLaTeX. This optional response build is not a premise of the mathematical result. Review rendered output after changing the source or TeX environment.

## Package boundaries

`paper/` contains the public manuscript; `review/` contains received review and response history; `evidence/core/`, `evidence/supplied/` and `evidence/received/` preserve original proof/audit inputs; `evidence/historical/` retains superseded reports; `evidence/current/` is the supplied corrected reporting layer; `evidence/intake/` adds dated source-comparison and fresh replay records. The root manifest belongs to the assembled publication package; historical manifests keep their original scope.

The work does not classify all extremizers, determine every matroid threshold, or provide a metric-independent spectral gap without normalization. Original prose/data use CC0-1.0 and original code uses MIT; [component exclusions](LICENSES.md) preserve third-party and historical rights. Supplied preparation metadata with blank licence/publication fields is retained as history, not silently rewritten into a past public release.

Public release identifiers: [GitHub candidate release](https://github.com/ipitchford/ptolemaic-negative-type/releases/tag/v1.0.0-candidate), [version DOI](https://doi.org/10.5281/zenodo.22983333), [all-version DOI](https://doi.org/10.5281/zenodo.22983332) and [Evidence Press page](https://evidencepress.org/releases/ptolemaic-negative-type/). Provider publication timestamps and live availability must be read from those records, not inferred from this pre-publication package snapshot.
