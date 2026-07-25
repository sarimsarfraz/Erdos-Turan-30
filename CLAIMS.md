# Claim ledger

The labels below are part of the mathematical audit.

## PROVED IN THIS REPOSITORY

### P1. Discrete vector covering lemma

The exact finite lemma in `proofs/vector_covering_lemma.md` derives an upper
bound from a finite list of rational covering inequalities. Its proof uses only
nonnegative autocorrelation, the Sidon difference condition, and weighted
Cauchy--Schwarz.

### P2. Exact m=80 rational certificate

The integer data in `certificates/m80/certificate.json` satisfy every covering
constraint and prove

\[
ab<(942881/10^6)^2.
\]

The standard-library and SymPy verifiers are independent implementations.

### P3. One-sided continuum kernel-majorant barrier

For every finite vector-valued one-sided admissible system as defined in
`proofs/continuum_barrier.md`,

\[
\frac A2+B\ge\frac43,
\qquad AB\ge\frac89.
\]

Equality is attained by `p(u)=2u` on `[0,1]` and the delay profile. Therefore

\[
\inf\sqrt{AB}=2\sqrt2/3.
\]

The proof is analytic. Symbolic scripts verify its exact local identities and
algebraic decompositions, not the measure-theoretic arguments.

### P4. Exact cyclic-completion defect identities

For a `k`-mark ruler of diameter `D<M=k^2-k+1`, reduction modulo `M` gives
multiplicities in `{0,1,2}`; the number of holes equals the number of duplicate
residue classes. For every `1<=r<M-D`, residue `r` cannot be duplicated.

### P5. Translate-incidence moment identities for a planar difference set

For a `(q^2+q+1,q+1,1)` cyclic difference set and an interval of length `H`,
window counts satisfy exact first and second factorial-moment identities, while
all higher factorial moments obey the unique-translate bound in
`proofs/incidence_hierarchy.md`.

### P6. Rank-aggregate plateau

Rank-sum symmetry, concavity, aggregate band floors, and uncoupled completion
identities admit central-gap pseudo-configurations at every fixed ruler deficit
coefficient below `2`. They therefore do not improve the pairwise coefficient
`4 sqrt(2)/3` in ruler normalization.

## CONDITIONAL THEOREMS

### C1. High-moment gateway for planar difference-set gaps

If centered translate-window moments satisfy the Poisson-scale estimates stated
in `proofs/incidence_hierarchy.md` up to orders tending to infinity, then the
maximum cyclic gap is `q^{1+o(1)}`. This implication is proved; its hypothesis
is not.

### C2. Gateway to the upper half of Erdős Problem 30

A `k^{1+o(1)}` stability theorem for the almost-perfect cyclic completion in
P4 implies

\[
F(N)\le\sqrt N+N^{o(1)}.
\]

The stability theorem is not proved.

## NOT CLAIMED

- No proof of `F(N)=sqrt(N)+o(N^{1/4})`.
- No proof of `F(N)=sqrt(N)+N^{o(1)}`.
- No proof of the all-`N` lower error required for the full two-sided Erdős
  Problem 30 assertion.
- No numerical Level-2 moment optimum is reported as a theorem.
- No continuum or finite bound is accepted solely from floating-point output.
