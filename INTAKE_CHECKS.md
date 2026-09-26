# Fresh publication-intake checks

Executed **26 September 2026, 21:29:23–21:30:43 UTC** (22:29:23–22:30:43 BST) against a fresh copy of the supplied version 1.0 bundle. This is an internal replay/implementation check, not independent scientific reproduction or a universal proof audit. It predates subsequent public-manuscript attribution/metadata edits.

The retained [intake result](evidence/intake/RESULTS.md) and [machine report](evidence/intake/run-20260926T212922800639Z/INTAKE_REPLAY_REPORT.json) identify actual commands, environment, exit codes, logs, source identity and generated-output hashes. The latter report has SHA-256 `0477f06e43d65a82ad7c4f72fe7419f3ba073c13af64f208d49e2d4a833649f1`.

## Completed scope

- Integrity: all **130 supplied manifest files** checked before and after replay; all **103 historical full-replay input files** still matched. The source and fresh copy were unchanged afterward.
- Exact mode: **five jobs**, with all five required reports byte-identical to the supplied rational, symbolic, manuscript, revision and reporting outputs.
- Full mode: **nine jobs**, including bounded numerical experiments. Exact outputs still matched; floating outputs were retained as new results rather than overwritten into history.
- Supported-mode controls: optimized Python and an output directory inside the bundle were both rejected.
- Hostile controls: **six semantic corruptions** were rejected by actual checker code—augmented-inverse sign, inverse-deletion sign, split gap, convergence/feasibility flag, fabricated empty-sample minimum and raw distance entry. **Three manifest corruptions**—added, deleted and changed files—were also rejected. Together with the two mode/path safeguards, these are eleven expected refusals. The unchanged reporting checker additionally exercised its three built-in missingness/count controls.

The [exact replay receipt](evidence/intake/run-20260926T212922800639Z/exact/REPLAY_REPORT.json) has SHA-256 `1006a6c601e6519b8fcf7332ea43e0c77cd67e3b90a5962b0e5ae7a49c9e1cb3`; the [full replay receipt](evidence/intake/run-20260926T212922800639Z/full/REPLAY_REPORT.json) has SHA-256 `d07f733e0051218725d2c8b80505976c837665f6dd0501b6e34890fe51b2370f`.

## Different numerical environment, preserved differences

This run used macOS arm64, Python 3.13.5, NumPy 2.4.4, SciPy 1.17.1, SymPy 1.14.0 and mpmath 1.3.0, with numerical threads limited to one. It is **not** a recreation of the supplied Linux environment pinned to NumPy 2.3.5 and SciPy 1.17.0.

The fresh near-extremal experiment again accepted 2,400 arrays. The fresh SLSQP run reports **156 successes and 158 tolerance-feasible attempts out of 160**, compared with historical **150 and 160**. The fresh counts and saved measurement summaries pass the reporting checker. The largest fresh feasible deficit is approximately `2.08e-13` under a `1e-8` feasibility tolerance; it is not a certified counterexample. Do not substitute fresh values into historical reports or describe the changed optimizer counts as byte-identical reproduction.

The public intake selection retains reports, aggregate outputs, commands and logs. Large disposable source copies, mutation fixtures and the fresh trial JSONL copies are not included in that selection. The host-specific orchestration driver is also omitted from the public selection; its digest and exact invocation remain in the immutable intake record. The unchanged historical raw trials and reusable publication wrapper remain in the supplied evidence layer. The machine report's original absolute runtime paths document the original local run, not promised paths on a recipient's computer; links in this summary are package-relative.

## Dated PDF-build boundary

At intake, installed TeX stopped with `needspace.sty` missing; the main manuscript rebuild did not complete and the response was not reached. The [failure log](evidence/intake/run-20260926T212922800639Z/typeset/ptolemaic.failed.log) remains historical evidence of that runtime limitation. This is **not a claim that a later final-publication rebuild remains blocked**. A later successful build and complete visual inspection require their own receipt and target hash; they do not erase the earlier failure.

These checks support reuse of unchanged scientific inputs and identify what was tested. They do not cover later changed manuscript bytes, a new final manifest/archive, current source-page state, public-provider parity, final PDF rendering, or canonical publication readback. Those are separate release boundaries.
