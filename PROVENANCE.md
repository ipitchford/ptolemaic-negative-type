# Provenance

Scholarly creator: **Anonymous**. Publisher: **Evidence Press**. Manuscript version: **1.0**, prepared **25 September 2026** according to the supplied package. This preparation date is not a publication, DOI-registration or deployment timestamp.

The work is described by its manuscript and prior provenance record as AI-assisted mathematical research with iterative checking and computational support. No human research contribution, reviewer identity, model identity for an undocumented step, or external independence is inferred from account ownership or from the existence of a report.

## Source package and immutable history

This documentation was prepared as a separate publication-intake overlay on 26 September 2026. It does not modify the supplied source bundle. The inspected source identities are:

| Source object | SHA-256 |
|---|---|
| `paper/ptolemaic.tex` | `656436a846986b52a0a35d3509fdfe7ff3ead93f4c5ce8fd40b8952c16139a01` |
| `paper/ptolemaic.pdf` | `6462410728018721e5894c9580d910f066a718b857bac673579a4b8c7b0a0cfc` |
| Supplied root `SHA256SUMS` | `2fcee64f127c24aedfbce2afae4d17245aae796e1278e532c505d8eb659128a9` |
| `review/RECEIVED_REVIEW.md` | `d0c2779c21909fbff769893a02f18cfb52cb799206ac3f248d29abeb15f02cfe` |
| Supplied full replay report | `4022ef9b13f453388a18b76f44b041efdfd4a72054484693feaf57ff650dd259` |

These are **intake source hashes**, not a declaration that later publication copies retain identical metadata or source bytes. Any subsequent citation, author-label or rights update must be recorded separately, manifested and checked against its own frozen publication target.

[INPUTS.json](review/INPUTS.json) records the four received archives and the original received-review hash. The archive identities recorded there are:

- `ptolemaic_all_size_proof.zip`: `892f6870f33df206c02fa82de9d71ee72832806930102af0b0a4160abee9e648`.
- `allsize_proof_audit.zip`: `944b88cd760713c802a5690802633f8087385dc8332a2cedfcb5356b653c4d09`.
- `allsize_publication_gate.zip`: `6c60c5b6cafc0d1035de54505eb51eda79297caa9105b7c521dfb042b9aec18e`.
- `ptolemaic_final_review_v1.zip`: `3d43a7889b97bd6569dc822ce171dd1b6c56f77bd1c644406ee06951e3b7117e`.

`evidence/received/` preserves those inputs. `evidence/core/` and `evidence/supplied/` preserve original proof and audit material; `evidence/historical/rc1_current/` preserves the previous reporting layer. Their existence does not authenticate third-party rights or reviewer independence.

## Evidence chronology

The supplied review concerns version `1.0-rc1`. The [response](review/RESPONSE_TO_REVIEW.md) and [change log](review/CHANGELOG.md) describe the version 1.0 exposition/reporting changes. The [source-invariance record](evidence/current/SOURCE_INVARIANCE.json) reports 72 retained labels, 43 byte-identical numbered equation environments, and preservation of core/supplied source files. The new seven-point worked example has separate exact checks.

The historical full replay froze 103 input files before its nine jobs. Its later receipts and finalization notes were additional documentation; the supplied final manifest covered 130 files. A newly assembled publication archive will have a different inventory and must not reuse 130 as a claimed final count. See [REPLAY_SCOPE.md](evidence/current/REPLAY_SCOPE.md).

The [historical environment](evidence/current/environment.json) records Python 3.13.5 on Linux and the pinned NumPy, SciPy, SymPy and mpmath versions. It is not a claim that the current release host or an external reproducer uses the same environment.

The [source ledger](review/SOURCE_LEDGER.md) records a targeted 25 September comparison. This overlay imports that history transparently and does not backdate the publication coordinator's current literature refresh. See [CITATION_AUDIT.md](CITATION_AUDIT.md).

## Rights and public identity

The original `publication/RIGHTS_AND_ATTRIBUTION.md` and null licence fields describe the preparation-stage history. The new [component licence map](LICENSES.md) applies the authorised Evidence Press standing terms to original material without rewriting those historical records or extending them to third-party content.

No repository URL, immutable tag, DOI, canonical page or actual publication timestamp is invented here. The coordinator must supply and verify those identities for the final release. Documentation work itself is not public publication.
