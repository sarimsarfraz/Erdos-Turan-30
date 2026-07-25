# Exact continuum barrier for one-sided kernel-majorant smoothing

## Theorem

Let `lambda_1,...,lambda_R>0` sum to one. For every `r`, let `p_r>=0` belong
to `L^2([0,H])`, with `int p_r=1`, and let `w_r-1` belong to
`L^1(0,infinity) cap L^2(0,infinity)`. Assume

\[
\sum_{r=1}^R\lambda_r\int_0^H p_r(u)w_r(x+u)\,du\ge1
\quad\text{for almost every }x\ge0.
\tag{1}
\]

Define

\[
A=\sum_r\lambda_r\int_0^Hp_r(u)^2\,du,
\qquad
B=H+\sum_r\lambda_r\int_0^\infty(w_r(t)^2-1)\,dt.
\tag{2}
\]

Then

\[
\boxed{\frac A2+B\ge\frac43.}
\tag{3}
\]

Consequently

\[
\boxed{AB\ge\frac89}
\qquad\text{and}\qquad
\boxed{\inf\sqrt{AB}=\frac{2\sqrt2}{3}.}
\tag{4}
\]

The infimum is attained in the scalar system

\[
p_0(u)=2u\,1_{[0,1]}(u)
\]

with the delay profile `w_0` of `delay_profile.md`.

## Proof

The delay-profile note proves:

1. `T_{p_0}w_0=1`;
2. `int p_0^2=4/3`;
3. `int(w_0^2-1)=-1/3`;
4. the positive dual equation `T_{p_0}^*mu_0=2w_0`;
5. a pointwise nonnegative renewal slack `D`;
6. the weighted renewal identity required to cancel the cross term.

The complete square-and-potential calculation in `decomposition19.md` proves
(3), including the vector-valued case.

It remains to pass from (3) to the product. Dilate any admissible system by
`s>0`:

\[
p_{r,s}(u)=s^{-1}p_r(u/s),
\qquad
w_{r,s}(t)=w_r(t/s),
\qquad
H_s=sH.
\]

The covering inequality is preserved, while

\[
A_s=A/s,
\qquad B_s=sB.
\]

Applying (3) for every `s>0`,

\[
\frac{A}{2s}+sB\ge\frac43.
\]

This also forces `B>0`. Minimizing the left side at
`s=sqrt(A/(2B))` gives

\[
\sqrt{2AB}\ge\frac43,
\]

which is (4). For the displayed scalar system,

\[
A_0=\frac43,
\qquad B_0=1-\frac13=\frac23,
\]

so `A_0B_0=8/9`. `QED`

## Euler--Lagrange closure

At the extremizer, every inequality in the proof is active:

\[
T_{p_0}w_0=1,
\qquad
T_{p_0}^*\mu_0=2w_0,
\]

\[
\Psi(u)=p_0(u)-\frac13\quad(0<u<1),
\]

and scale stationarity is

\[
A_0=2B_0.
\]

The endpoint square is active because, after the substitution `x=1-u`,

\[
p_0(1-x)=2(1-x)
\quad(0<x<1).
\]

Thus the theorem is a dual optimum certificate, not only a lower bound.

## Relation to finite Sidon bounds

The causal covering lemma in `vector_covering_lemma.md` discretizes any
piecewise smooth admissible system. The theorem therefore proves that no
one-sided pairwise-autocorrelation kernel-majorant system in this class can
produce a coefficient below

\[
2\sqrt2/3
\]

in front of `N^{1/4}`. The theorem does not say that every possible Sidon-set
argument has this barrier. It names the information discarded by this class:
pairwise autocorrelation retains lag occupancy but not the common
vertex-incidence/gradient realization of all lags.
