# Evidence and reporting ledger
**Version 1.0 · 25 September 2026**

## Provenance and assurance

The four archives in `evidence/received/` are preserved byte-for-byte, including the reviewed version 1.0-rc1. Their hashes are in `review/INPUTS.json`. `review/RECEIVED_REVIEW.md` is the unchanged latest review. `evidence/core/` and `evidence/supplied/` retain the original proof and audit material. The earlier current reports now reside under `evidence/historical/rc1_current/` and in the unchanged prior archive.

The source of the theorem is the analytic proof. Rational and symbolic checks cover stated identities and finite examples. The supplied favourable review is documentary evidence of a reading and replay, not authenticated independent specialist peer review. Its REF assessment and subjective correctness probabilities are not adopted as measured release attributes. No proof assistant or public repository registration has been used.

The mathematics has not been changed in response to this review. The revised paper adds exposition and a seven-point witness calculation, checked exactly. The small-cardinality endpoint imports remain separate from the self-contained proof for `m >= 6`. Novelty-search scope is unchanged and recorded in `SOURCE_LEDGER.md`.

## Authoritative current numerical entry point

Use `evidence/current/CURRENT_NUMERICAL_SUMMARY.json`. It separates four provenance classes:

1. The original broad near-extremal experiment: zero accepted arrays at each of 11, 12, 13 and 14 points. Initial `1e9` sentinels are represented as null, with status `no_observations`. The historical source bytes remain untouched.
2. The historical follow-up: 600 accepted arrays at each cardinality, but only a mixed minimum combining a centred-Gram eigenvalue and `-z^T E z/2`. Its two separate historical values are not recoverable from that aggregate and remain null with status `not_separately_recorded`.
3. The current instrumented follow-up: 600 accepted arrays at each cardinality, with full-precision arrays and separate statistics, saved in `evidence/current/numerics/near_extremal_trials.jsonl`.
4. The current instrumented adversarial runs: all 160 attempts, initial and final arrays, status codes, messages, iterations, feasibility slacks, inverse diagnostics and rejection/exception fields, saved in `adversarial_trials.jsonl`.

The instrumented runs repeat the supplied seeds and designs. They do not create a claim of statistical independence or recover unrecorded historical values.

## Definitions and counts

The centred statistic is `lambda_min(-J E J/2)`, with `J=I-11^T/m`; its structural zero means the unrestricted minimum is not a positive stability margin. The zero-sum statistic is `lambda_min(-Q^T E Q/2)`, where Q has orthonormal columns spanning `1-perp`. The split-vector gap is `-z^T E z/2` for coefficients `1/a` and `-1/r`. Its Rayleigh quotient divides that gap by `z^T z`. These four quantities are never pooled. Each minimum carries its own accepted-sample count.

Near-extremal arrays are accepted with additive triangle/Ptolemy tolerance `1e-9`. The current run attempted and accepted 2,400 arrays, with no numerical exceptions. Restricted-eigenvalue sample minima are positive in this run, but they are not validated lower bounds on the continuous class.

SLSQP uses log distances in `[-4,4]`, at most 300 iterations, `ftol=1e-12`, and final constraint tolerance `1e-8`. Each dimension has 40 attempts. Counts of optimiser convergence plus feasibility are respectively **39, 39, 37, 35**, while all four feasibility counts are **40**. The ten nonconverged-but-feasible runs are retained rather than reclassified or omitted. Four have status 8 (line-search directional derivative), three status 9 (iteration cap), and three status 4 (reported incompatible inequalities); their status messages are preserved verbatim. No exceptions occurred.

The maximum floating-point deficit among all feasibility-accepted valid measurements is about `3.2456e-12`; among converged-and-feasible measurements it is about `5.4845e-13`. These are not validated counterexamples: numerical error and the `1e-8` feasibility allowance are not certified interval bounds on the theorem's inequality.

## Replays and limitations

The original 65-file review archive passed its integrity checks before and after a full replay. Core exact, symbolic and numerical reports and the 13-group manuscript report reproduced identically in this environment. Two supplied exploratory reports (`audit_allsize` and `adversarial_lemma4`) differed in floating-point values. `evidence/current/legacy_replay/REPLAY_REPORT.json` records exact hashes, comparisons and elapsed times; it is a receipt for replaying the prior version, not the current release manifest.

The new revision report checks 16 editorial/example requirements. The current reporting verifier reconstructs all 2,400 saved near-extremal arrays and all 160 saved optimisation candidates; verifies their recorded calculations and counts; and rejects three deliberate missingness/count mutations. It does not prove a universal mathematical statement. Numerical recomputation uses explicit tolerances, documented in `reporting_checks.json`.

Future numerical runs should retain attempted, accepted, rejected and exception counts, along with solver success and status separately from feasibility. The current scripts implement this requirement. Historical scripts are deliberately not retrofitted.

The publication wrapper verifies immutable file hashes before and after execution, uses temporary working copies, and distinguishes exact report equality from floating-point variation. A `PASS` denotes successful specified checks, not formal verification, journal acceptance, external specialist endorsement or exhaustive prior-art search.

## Nonclaims

No equality classification, metric-independent spectral gap, calibrated probability of correctness, formal proof-assistant certificate, external specialist endorsement or exhaustive novelty claim is introduced. The two false stronger inverse-pairing statements remain documented in Appendix A and the untouched history.
