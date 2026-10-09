# One-Sided Smoothing for Finite Sidon Sets

Artifact repository accompanying the paper:

> **Sarim Sarfraz**, *One-sided smoothing for finite Sidon sets: the coefficient 2√2/3 and its optimality*, 2026. arXiv link to be added upon announcement.

Let F(N) denote the largest cardinality of a Sidon subset of {0, 1, …, N−1}.
The paper proves:

1. **Record coefficient.** F(N) ≤ √N + (2√2/3) N^{1/4} + o(N^{1/4}), with
   2√2/3 = 0.9428090415…, improving the previously published coefficient
   0.9435 (Hou–Zhao, arXiv:2607.01169) and all previously announced values.
2. **Finite certificate.** F(N) ≤ √N + 0.942881 N^{1/4} + O(1), established by
   an exact rational certificate verified in integer/rational arithmetic only.
3. **Optimality (barrier theorem).** Over the entire class of finite
   vector-valued one-sided kernel–majorant systems — whose only Sidon input is
   the pairwise injectivity of differences — the infimum of the achievable
   coefficient is exactly 2√2/3, attained by the linear ramp kernel p(u) = 2u
   and the delay-equation boundary profile.
4. **Aggregate plateau.** The rank-sum, concavity, band-floor, and uncoupled
   completion layer provably does not improve the barrier.

This repository contains every certificate, symbolic checker, and proof note
supporting these results, together with the exploratory material and recorded
dead ends of the surrounding research program.

## Dates and later work

This repository was created privately on 25 July 2026 and made public on
9 October 2026. Apart from this section, its contents are unchanged since
25 July 2026 (commit `97fc7ba` and the GitHub-signed commit `e6eb784`), so
"previously announced values" above refers to the literature as of that date.
Since then, Haoyu Chen has independently obtained and publicly announced the
coefficient 2√2/3, with explicit additive constant 1 for N ≥ 120⁴
(Zenodo, 2 October 2026, doi:10.5281/zenodo.23103979). John Akwei has
announced a finite certificate and a barrier for symmetric and two-sided
certificates (github.com/johnakwei/Science, 1–5 October 2026).

## Scope of claims

This repository does **not** claim a proof of F(N) = √N + N^{o(1)}
(Erdős Problem 30) or of F(N) = √N + o(N^{1/4}); those remain open.
`CLAIMS.md` is the authoritative claim ledger, separating (i) theorems proved
in the paper, (ii) exact machine-verified certificates and algebraic
identities, (iii) analytic arguments verified by hand and written in the proof
notes, and (iv) conditional or exploratory statements. Symbolic scripts
certify algebraic identities only; functional-analytic steps (measure-theoretic
justifications, contour shifting) are proved in the notes and are not
represented as computer proofs.

## Reproduction

Requires Python 3 (standard library suffices for the certificate; SymPy for
the symbolic checkers):

```
python3 -m pip install sympy
python3 run_all.py --all
```

Expected output: every checker reports PASS. The certificate alone can be
verified with no third-party dependencies:

```
python3 certificates/m80/verify_fraction.py
```

An independent SymPy-based verifier (`certificates/m80/verify_sympy.py`)
performs the same acceptance test with separately written code. Acceptance is
the exact rational comparison a·b < (942881/10^6)²; no floating-point quantity
enters any proof.

## Repository layout

| Path | Contents |
|---|---|
| `certificates/m80/` | Exact m = 80 certificate (`certificate.json`: 8 kernels × 80 bins, boundary vectors, weights, all integers) and two independent exact verifiers |
| `proofs/` | Proof notes: continuum barrier, delay profile, square-and-potential decomposition, vector-valued covering lemma, aggregate plateau, spectral-selector factorization, cyclic-defect reduction, incidence hierarchy |
| `checkers/` | Exact symbolic checkers for the C(r) derivation, decomposition identity, delay-profile integrals, plateau algebra, pseudo-configurations, and selector factorization |
| `research/` | Research notes: named obstructions, dead-end reports, next targets |
| `FULL_PROOF_NOTE.md` | Consolidated proof and audit note |
| `CLAIMS.md` | Claim ledger |
| `REPRODUCTION_LOG.txt` | Log of a complete verification run |
| `MANIFEST.md` | SHA-256 manifest of all artifacts |

## Context

The coefficient of N^{1/4} in the Erdős–Turán upper bound has the history
1 (Lindström 1969) → 0.998 (Balogh–Füredi–Roy 2023) → 0.99703 (O'Bryant 2024)
→ 0.98183 (Carter–Hunter–O'Bryant 2025) → 0.97633 (announced,
Carter–Georgiev–Gómez-Serrano–Hunter–O'Bryant–Tao–Wagner) → 0.9435
(Hou–Zhao 2026). The barrier theorem identifies 2√2/3 as the exact limit of
the underlying method; the paper isolates the incidence-coupled Level-2 moment
cone as the unique admissible source of further improvement. See
`REFERENCES.md` for full citations and the Erdős Problems entry for
Problem 30.

## Disclosure

Portions of this work were carried out with the assistance of large language
model systems. All mathematical statements and proofs were verified by the
author, who takes sole responsibility for their correctness; the verification
suite above is provided so that no claim need be taken on trust.

## License and citation

See `LICENSE`. If you use the certificate or checkers, please cite the paper
above; a Zenodo DOI for this repository will be minted at public release
(tag `v1.0` corresponds to arXiv v1).
