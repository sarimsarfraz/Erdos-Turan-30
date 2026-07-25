# The next admissible target

The pairwise barrier and every uncoupled aggregate plateau are closed. The next
step must use a property that all the exact pseudomodels violate.

## 1. Smallest missing property

An actual ruler supplies one common ordered vertex set and therefore one common
potential `a_i`. Every lag indicator and every completion identity is generated
by that same potential:

\[
X_{i,\ell,t}=1_{\{a_{i+\ell}-a_i=t\}}.
\]

The smallest missing property is not merely the cocycle equation and not merely
lag exclusivity. It is their **incidence-coupled conjunction**:

- each interval occupies exactly one lag;
- each lag is occupied by at most one interval;
- adjacent intervals compose to the containing interval;
- all these statements use the same one-hot variables.

## 2. Two equivalent research interfaces

### A. Moment/localizer interface

Use the one-hot variables and the degree-two localizers in
`proofs/incidence_hierarchy.md`. Search for a dual inequality that controls the
cyclic defect `g=M-D`. Any finite computation must end in a rational primal or
dual certificate.

### B. Translate-window interface

For a planar difference set, prove centered moment bounds

\[
M^{-1}\sum_s|X_s-\mu|^{2r}\le C_r\mu^r
\]

at orders tending to infinity. For an almost-perfect completion, add a defect
term controlled by holes and duplicate shifted pair sums. The exact gateway
theorem then gives `g=k^{1+o(1)}`.

These interfaces encode the same missing information at different resolutions:
common endpoint compatibility of many pair incidences.

## 3. Concrete termination criteria

A successful hierarchy must produce one of the following exact outcomes.

1. **Drop.** A rational/algebraic dual certificate gives a smaller asymptotic
   deficit. Record the new bound and open the next level only after exact
   verification.
2. **Plateau.** An explicit feasible pseudomodel and a matching exact dual prove
   that the level is insufficient. Name the missing property.
3. **Vanishing hierarchy.** Prove that the exact optima tend to zero. This gives
   `F(N)=sqrt(N)+o(N^{1/4})`.
4. **Subpolynomial stability.** Prove `M-D<=k^{1+o(1)}` through the full
   incidence hierarchy or the translate-moment gateway. This gives the upper
   assertion `F(N)<=sqrt(N)+N^{o(1)}`.

## 4. What is not an admissible result

- a floating-point optimum without a rationalized certificate;
- a finite-size trend extrapolated to an asymptotic theorem;
- another kernel within the closed pairwise class;
- a rank or moment inequality that can be passed by the explicit plateau
  pseudomodels;
- a statement of the desired stability estimate as an unproved lemma.
