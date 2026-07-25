# Sidon exact-research package

This repository is a hostile-referee audit and exact-reproduction package for
work on the maximal size

\[
F(N)=\max\{|A|:A\subseteq\{0,\dots,N-1\}\text{ is Sidon}\}.
\]

## Status first

This repository **does not claim** a proof of

\[
F(N)=\sqrt N+N^{o(1)}
\]

or of \(F(N)=\sqrt N+o(N^{1/4})\). Those assertions remain the research target.
The package separates proved statements, exact finite certificates, symbolic
identity checks, and conjectural/conditional routes. `CLAIMS.md` is the claim
ledger.

The strongest fully finite artifact in this package is the exact `m=80`
vector-smoothing certificate proving, conditional only on the written covering
lemma,

\[
F(N)\le \sqrt N+0.942881N^{1/4}+O(1).
\]

The package also contains a self-contained analytic proof of the continuum
one-sided kernel-majorant barrier

\[
\inf\sqrt{AB}=\frac{2\sqrt2}{3},
\]

including the delay profile, dual renewal kernel, and square-and-potential
decomposition. The symbolic scripts check the algebraic identities; the
functional-analytic justifications are written out in the proof notes and are
not misrepresented as computer proofs.

Finally, the repository records an exact incidence hierarchy for cyclic planar
difference sets and a conditional high-moment gateway. It also names the
obstructions that caused each explored route to stop.

## Reproduce everything

Standard-library checks:

```bash
python3 run_all.py --core
```

All checks, including independent SymPy verification:

```bash
python3 -m pip install sympy
python3 run_all.py --all
```

Or with `make`:

```bash
make core
make all
```

Every command exits nonzero on failure. The exact certificate verifiers use
explicit exceptions rather than Python `assert`, so optimization mode cannot
silence the checks.

## One-command reproduction by artifact

| Artifact | Command |
|---|---|
| m=80 certificate, standard library | `python3 certificates/m80/verify_fraction.py` |
| m=80 certificate, independent SymPy | `python3 certificates/m80/verify_sympy.py` |
| Delay-profile algebra | `python3 checkers/check_delay_profile_symbolic.py` |
| Correlation `C(r)` derivation | `python3 checkers/check_C_derivation_symbolic.py` |
| Decomposition (19) algebra | `python3 checkers/check_decomposition19_symbolic.py` |
| Pairwise pseudo-configuration | `python3 checkers/check_pairwise_pseudo.py` |
| Rank-aggregate plateau formulas | `python3 checkers/check_rank_aggregate_plateau.py` |
| Cyclic incidence moments and gap examples | `python3 checkers/check_translate_incidence.py` |
| Cyclic defect identities | `python3 checkers/check_cyclic_defect.py` |
| Carry/block partition identities | `python3 checkers/check_carry_partition.py` |

## Directory map

- `ALL_CONTENTS.txt`: every text/source artifact concatenated into one directly readable file.
- `CLAIMS.md`: exact status of every mathematical claim.
- `proofs/vector_covering_lemma.md`: discrete one-sided and symmetric
  vector-valued covering lemmas.
- `proofs/continuum_barrier.md`: the continuum dual certificate and barrier.
- `proofs/delay_profile.md`: delay equation, transform, decay, and exact
  integrals.
- `proofs/decomposition19.md`: full square-and-potential calculation.
- `proofs/incidence_hierarchy.md`: translate-incidence moments, the
  high-moment gateway, and the exact point at which the argument remains open.
- `proofs/cyclic_defect_reduction.md`: almost-perfect cyclic completion of an
  interval ruler.
- `proofs/rank_aggregate_plateau.md`: why uncoupled rank information does not
  improve the pairwise barrier.
- `research/dead_ends.md`: every attempted route and its named obstruction.
- `research/next_target.md`: the smallest currently admissible strengthening.
- `certificates/m80/`: complete integer data and two exact verifiers.

## Conventions

A Sidon set here means that every nonzero ordered difference has at most one
representation. This is equivalent to uniqueness of unordered pair sums when
diagonal pairs are included.

No decimal is used as evidence. Decimals printed by verifiers are display-only;
all acceptance decisions use integers or exact rationals.
