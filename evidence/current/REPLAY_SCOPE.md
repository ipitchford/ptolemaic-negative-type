# Replay scope and final packaging

The complete publication replay in `full_replay/REPLAY_REPORT.json` verified an immutable 103-file input snapshot before and after all nine jobs. `FULL_REPLAY_INPUT_SHA256SUMS` preserves that exact input manifest. All of those payload files remain unchanged in this release. The only subsequent additions are replay receipts, this scope note and finalisation metadata; the root manifest was then regenerated to cover the complete final bundle.

A prior foreground invocation was interrupted by the execution tool wall-time limit before completion. Its partial output was not treated as a successful replay. The separate completed run is the authoritative full receipt. It repeated the instrumented numerical files and current summary byte-for-byte; two legacy exploratory reports differed from their historical versions, as recorded.

The final ZIP is also extracted into a fresh directory and checked with the publication wrapper. The external final-replay receipt accompanies the ZIP rather than introducing a circular self-hash inside it. Any recipient can reproduce that check with the shipped wrapper.
