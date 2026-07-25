# Artifact manifest

## Exact data

- `certificates/m80/certificate.json`: complete integer data for the `m=80`,
  `R=8`, `L=4` certificate.

## Exact verifiers

- `certificates/m80/verify_fraction.py`
- `certificates/m80/verify_sympy.py`
- every script in `checkers/`

## Proof notes

- `FULL_PROOF_NOTE.md`
- every file in `proofs/`

## Research audit

- `CLAIMS.md`
- `research/dead_ends.md`
- `research/next_target.md`

The archive contains no generated binary dependency and no inaccessible
external artifact. The only optional dependency is SymPy, used by the
independent symbolic checkers.

- `ALL_CONTENTS.txt`: concatenated complete text/source contents of the repository.
