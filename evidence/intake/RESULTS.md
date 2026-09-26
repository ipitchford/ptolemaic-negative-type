# Ptolemaic publication intake replay

Executed 26 September 2026, 21:29:23–21:30:43 UTC (22:29:23–22:30:43 BST).

## Result and scope

All replay, exact-output, supported-mode and negative-control checks passed. The additional local PDF rebuild was blocked by a missing installed TeX package, `needspace.sty`; it is not recorded as a successful rebuild. The supplied PDF and source remain unchanged.

This is internal implementation checking. It is not independent scientific reproduction, external specialist endorsement, formal proof verification, or validation of the universal prose theorem. No providers were contacted and no libraries or TeX packages were installed.

The source was `../evidencepress_ptolemaic_v1_0`. A fresh byte-identical copy was made at `run-20260926T212922800639Z/source-copy`; all generated replay output is outside that copy. Both the supplied source and the fresh copy were checked unchanged afterward.

- The final manifest verified all 130 listed files before and after replay. Its SHA-256 is `2fcee64f127c24aedfbce2afae4d17245aae796e1278e532c505d8eb659128a9`.
- All 103 payload files identified by the historical full-replay input manifest still match.
- Exact mode completed five jobs in 10.347 seconds. All five required reports reproduce the shipped bytes exactly: rational identities, symbolic identities, manuscript checks, revision checks, and reporting checks.
- Full mode completed nine jobs in 55.744 seconds, including the legacy numerical scripts and the current instrumented experiments. The exact reports still match; floating-point files are separately retained and explicitly do not match historical bytes.
- The seven-point revision checker retains the exact form `3*T/4 - 4/3`, endpoint `T=16/9`, and centred Gram eigenvalues `0` twice, `1/2` twice, and `8/9` three times.

## Supported mode and hostile controls

The publication wrapper correctly refuses Python `-O` before replay, because the immutable legacy exact/SymPy verifiers use assertions. It also refuses an output directory inside the bundle. Direct invocation of those old verifier scripts with assertions disabled is not a supported verification route.

Six semantic mutations were rejected by the actual checker code, without merely relying on a changed manifest: an augmented-inverse sign, an inverse-deletion sign, a split-vector gap, a convergence/feasibility flag, a fabricated historical empty-sample minimum, and a raw distance entry. Three additional manifest controls rejected changed, deleted and added files. These eleven expected refusals all returned nonzero with the expected diagnostic. The unchanged reporting checker also exercised its three built-in missingness/count controls.

Mutation fixtures exist only in disposable sibling directories. Historical code and evidence were not patched or resealed.

## Environment and floating-point differences

Python executable: `/Users/admin/.venvs/analysis-py313/bin/python` (Python 3.13.5, macOS 27 arm64). Its resolved executable SHA-256 is `a1f6d9dc20d4787a84dc2fe782094a7bac5946f49a962aa0af48a02f0e8d5bc5`.

Packages: NumPy 2.4.4, SciPy 1.17.1, SymPy 1.14.0, mpmath 1.3.0. BLAS/OMP/MKL threads were limited to one, `PYTHONHASHSEED=0`, and bytecode output was disabled. This is not a recreation of the shipped Linux environment with NumPy 2.3.5/SciPy 1.17.0.

The fresh near-extremal run again accepted 2,400 arrays. The random epsilon and exponent values agree exactly; distance entries differ by at most `2.220446049250313e-16`. Maximum differences in the four recorded Gram/gap measurements are below `7.8e-16`; feasibility decisions agree. The fresh SLSQP run has 156 reported successes and 158 tolerance-feasible attempts out of 160, compared with the historical 150 and 160. All fresh measurements and summary counts pass the reporting checker. The largest fresh feasible deficit is approximately `2.0816681711721685e-13` under the `1e-8` feasibility tolerance; it is not a certified counterexample. These outputs do not replace the preserved historical reports.

## Commands and retained evidence

The complete commands, environment, exit codes, timings, logs and generated-file hashes are in [INTAKE_REPLAY_REPORT.json](run-20260926T212922800639Z/INTAKE_REPLAY_REPORT.json). The reproducible orchestration command was:

```sh
/Users/admin/.venvs/analysis-py313/bin/python -B /Users/admin/Documents/Codex/ptolemaic-publication-20260926.NMT4BM/replay-checks/run_replay_checks.py --source /Users/admin/Documents/Codex/ptolemaic-publication-20260926.NMT4BM/evidencepress_ptolemaic_v1_0
```

The driver SHA-256 is `3ed53dbd0a770f13cde5d75c371c4a66ac85503b883b9f378ca7cd9748d04de7`. It calls the supplied wrapper's `integrity`, `exact`, and `full` modes from the fresh copy with external output paths and a 300-second per-job timeout. No timeout occurred.

| Retained report | SHA-256 |
|---|---|
| `run-20260926T212922800639Z/INTAKE_REPLAY_REPORT.json` | `0477f06e43d65a82ad7c4f72fe7419f3ba073c13af64f208d49e2d4a833649f1` |
| `run-20260926T212922800639Z/exact/REPLAY_REPORT.json` | `1006a6c601e6519b8fcf7332ea43e0c77cd67e3b90a5962b0e5ae7a49c9e1cb3` |
| `run-20260926T212922800639Z/full/REPLAY_REPORT.json` | `d07f733e0051218725d2c8b80505976c837665f6dd0501b6e34890fe51b2370f` |

## PDF rebuild boundary

The supplied `scripts/build_paper.py --output <external typeset directory> --response` was attempted with installed pdfLaTeX and XeLaTeX. It stopped on the main manuscript with `LaTeX Error: File 'needspace.sty' not found`, before reaching the response. The failure log is [ptolemaic.failed.log](run-20260926T212922800639Z/typeset/ptolemaic.failed.log). A bounded search found no existing `needspace.sty` under TinyTeX or the Codex workspace. No source/font substitution or package installation was made. Canonical-PDF visual QA and any authorised TeX dependency recovery remain with the publication orchestrator.
