# Research log: closed routes and named obstructions

Every item below records what was tried, what exact statement survived, and why
the route stopped. None is counted as a bound unless a proof or exact
certificate is present elsewhere in the repository.

## 1. More pairwise kernels

**Attempt.** Add kernels, refine grids, allow one-sided nonsymmetric profiles,
and optimize boundary weights.

**Closure.** `proofs/continuum_barrier.md` proves the exact optimum
`2 sqrt(2)/3` over the one-sided vector kernel-majorant class.

**Obstruction.** **Pairwise-autocorrelation barrier.** The relaxation knows
which lags are occupied but not whether all occupied lags arise from one common
vertex potential.

## 2. Rank sums, concavity, and aggregate floors

**Attempt.** Add the rank variables `d_{i,l}`, exact completion identities,
rank-sum symmetry, concavity, and all band-floor inequalities, but without
one-hot lag incidence.

**Closure.** Central-gap pseudo-configurations pass every such constraint at
all deficit coefficients below two.

**Obstruction.** **Uncoupled rank plateau.** Completion identities without the
lag-to-interval incidence map do not encode difference exclusivity.

## 3. Raw translate factorial moments

**Attempt.** Use all inequalities

`sum_s binom(X_s,r) <= binom(H,r)`

for intersections of an interval with translates of a planar difference set.

**Closure.** The first two moments are sharp; for `r>=3` the raw upper bound is
larger than Poisson scale by `k^{r-2}`. A two-level pseudodistribution passes
all these bounds while retaining zero-window mass of order `1/mu`.

**Obstruction.** **Translate-clustering obstruction.** The hierarchy permits
rare dense intersections because it does not control centered moments.

## 4. Sliding-window Lipschitz and total variation

**Attempt.** Add

`X_{s+1}-X_s in {-1,0,1}`

and `sum |X_{s+1}-X_s| <= 2k`.

**Outcome.** These constraints force ramps between zero and the typical height
`mu`, but a ramp has length only `O(mu)`, negligible next to a critical zero
run of length `M/mu`. They do not change the `k^{3/2}` exponent.

**Obstruction.** **Transition-ramp plateau.** Pointwise regularity of window
counts is too local.

## 5. Initial-difference additive patterns

**Attempt.** If `[1,g]` is almost contained in the difference set, count Schur
and higher additive patterns in that interval.

**Outcome.** An equality `x+y=z` among represented differences need not come
from a composable path of three marks. It may be a nonlocal equality of two-
and three-sums. Sidon uniqueness controls two-sums, not arbitrary higher-sum
representations.

**Obstruction.** **Noncomposable additive-pattern obstruction.** Dense label
patterns do not automatically become gradient paths.

## 6. Higher additive energy of the difference set

**Attempt.** Bound long additive configurations in the represented difference
set through higher energies of `A` or `A-A`.

**Outcome.** Non-chain configurations introduce up to twice as many vertex
variables as path configurations; known or elementary energy bounds are too
large to improve the critical exponent.

**Obstruction.** **Vertex-pattern explosion.** Higher lag equations do not
retain shared endpoints.

## 7. Quotient/residue carry compression

**Attempt.** Divide marks into blocks of size about `k`, and use complementarity
between carry and non-carry representations of every small difference.

**Outcome.** Inversion-count identities reach the square-root critical scale.
The exact residue values and shared endpoints remain unused.

**Obstruction.** **Carry-count plateau.** Counts of carries are not the same as
residue-level incidence realizability.

## 8. Undercompressed algebraic graphs

**Attempt.** Flatten planar-function, Costas, Galois-ring, and length-two local
ring graphs with base `q-lambda sqrt(q)`, then delete a small exceptional set.

**Outcome.** In finite experiments, adjacent carry-level collision hypergraphs
required deletion of a positive fraction of vertices, not `O(sqrt(q))`.

**Obstruction.** **Carry-collision density.** The algebraic seed controls equal
vector differences but not neighboring integer carry levels.

No asymptotic nonexistence theorem is claimed from these experiments.

## 9. Spectral-selector factorization

**Attempt.** Keep the exact polynomial spectral factor

`P P#-(k-1)z^D = S_M(1+(z-1)E)`.

**Closure.** `E` is an exactly balanced complement-palindromic binary word of
length `M-2g+1`.

**Obstruction.** **Selector-factor plateau.** Divisibility and palindromy alone
allow exponentially many selectors for every `g`. The missing condition is
existence of a binary gradient spectral factor `P`.

## 10. Vandermonde and capacity

**Attempt.** Use the exact identity

`prod_{i<j}|zeta^{a_j}-zeta^{a_i}|^2=M`

for a perfect difference set, together with confinement to a long circular
arc.

**Outcome.** The determinant is already exponentially below the Fekete maximum
for `k` points on the full circle, so an upper capacity bound has the wrong
direction and does not constrain the missing arc.

**Obstruction.** **Vandermonde-scale mismatch.** Arc capacity controls the
maximum product, while the exact design product is very small.

## 11. Rankwise AM--GM over cyclic interval sums

**Attempt.** Multiply all rank sums in a perfect cyclic ruler and compare with
`(M-1)!`.

**Outcome.** The total Jensen slack is of order `k log k`; a large gap costs
quadratically across ranks and gives at best a `k^{3/2} sqrt(log k)` scale.

**Obstruction.** **Rankwise Jensen barrier.** Rank means discard the incidence
placement that must supply the improvement.

## 12. Generic combinatorial large sieve

**Attempt.** Apply recent bounded-multiplicity large-sieve mechanisms.

**Outcome.** Their strongest gains use branching from nonlinear algebraic
relations. The linear form `x-y` has no analogous branching once pairwise
uniqueness is imposed.

**Obstruction.** **Linear-form no-branching barrier.** A new source of
incidence growth is required.

## 13. Multiplier/cyclic-code structure

**Attempt.** Reduce a planar cyclic difference set modulo a prime divisor of
its order parameter, use numerical multipliers, cyclic-code roots, and BCH
bounds.

**Outcome.** The group-ring equation supplies many spectral zeros over finite
fields, but a long run of zero *time coefficients* is not a run of consecutive
spectral zeros. Linear-complexity and BCH estimates give only order-`M`
constraints.

**Obstruction.** **Time/spectrum run mismatch.** Multiplier closure does not
convert the desired additive interval gap into a sufficiently long defining
set of a cyclic code.
