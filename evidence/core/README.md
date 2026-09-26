# All-size Ptolemaic negative-type proof draft

Read `RESEARCH_NOTE.md` first. It gives the complete new analytic argument for every m >= 6, then appends the established small cases to obtain the full conjectured formula. It records exactly which external results are used.

The decisive new steps are:

- Section 2: a packing inequality for exact snowflaked stars, including arbitrary positive length ratios and nonnegative subsolutions.
- Section 5: a normalised inverse-triangle induction, with an exhaustive sign split and an exact dimension-compatibility calculation.
- Section 7: a strict-negative-type induction that uses positive definiteness only on smaller metrics, followed by endpoint continuity.

No global polynomial relaxation, radial inverse-sign hypothesis, universal mass monotonicity, or numerical search is a premise. The two proposed auxiliary mass statements are explicitly refuted in Section 9. The result is a proof claim awaiting independent mathematical review; the programs are not a proof-assistant certificate.

## Replay

From this directory, using Python 3:

```sh
python verify_exact.py
python verify_symbolic.py
OPENBLAS_NUM_THREADS=1 python verify_numerical.py
```

`verify_exact.py` uses only the standard library. The second requires SymPy. The third requires NumPy, SciPy and mpmath and is corroborative only. All three use paths relative to this directory, make no network calls and recreate JSON reports in `checks/`. The saved `.log` files are their stdout.

`replay.py` checks hashes, runs all three scripts and checks whether the JSON outputs match the saved results byte for byte in this environment. Numerical bitwise equality can depend on library versions and machine architecture; a mismatch is reported rather than silently treated as mathematical failure. The exact and symbolic outputs should reproduce independently of floating-point libraries.

## Files

- `RESEARCH_NOTE.md`: full proof, sharp witnesses, counterexamples and scope.
- `STATUS.json`: machine-readable claims, dependencies and unresolved review items.
- `verify_exact.py`, `verify_symbolic.py`, `verify_numerical.py`: independent styles of algebraic checking and numerical corroboration.
- `checks/`: all generated reports and stdout.
- `provenance/`: input archive hash and unmodified predecessor-verifier replay logs.
- `SHA256SUMS`: distributable-file checksums (excluding itself and generated replay output).

No public submission, persistent-library write or external publication has been made. Historical priority has not been established. The proof establishes the exponent and sharp split examples; it does not classify all equality cases.
