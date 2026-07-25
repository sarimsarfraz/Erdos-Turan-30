# Translate-incidence hierarchy and the high-moment gateway

This note records the first hierarchy that sees common vertex incidence rather
than only pairwise lag autocorrelation.

## 1. Exact moments for a planar difference set

Let `D` be a cyclic `(M,k,1)` difference set, so

\[
M=k^2-k+1.
\]

Fix the interval

\[
I_H=\{0,1,\ldots,H-1\}\subset\mathbb Z/M\mathbb Z
\]

and define

\[
X_s=|(D+s)\cap I_H|,
\qquad s\in\mathbb Z/M\mathbb Z.
\tag{1}
\]

Double counting gives

\[
\boxed{\sum_sX_s=kH.}
\tag{2}
\]

Every unordered pair of distinct points of `I_H` is contained in exactly one
translate of `D`, because its oriented difference has exactly one ordered
representation in `D`. Therefore

\[
\boxed{\sum_s\binom{X_s}{2}=\binom H2.}
\tag{3}
\]

For every `r>=3`, an `r`-subset of `I_H` is contained in at most one translate
of `D`: any two of its points already determine the translate. Hence

\[
\boxed{\sum_s\binom{X_s}{r}\le\binom Hr.}
\tag{4}
\]

Equations (2)--(4) are exact incidence constraints. The second identity is
pairwise; the higher inequalities retain common-translate compatibility.

## 2. The second-moment plateau

From (2) and (3),

\[
\sum_sX_s^2=H(k+H-1).
\tag{5}
\]

Let `V=#{s:X_s>0}`. Cauchy--Schwarz gives

\[
V\ge\frac{k^2H}{k+H-1}.
\tag{6}
\]

Thus the number `Z_0` of zero windows satisfies the exact bound

\[
\boxed{
Z_0\le M-\frac{k^2H}{k+H-1}
 =\frac{(k-1)(M-H)}{k+H-1}.}
\tag{7}
\]

If the binary cyclic sequence `1_D` has a run of `Z` consecutive zeros, then
for every `H<=Z`, at least `Z-H+1` cyclic intervals of length `H` are empty.
Combining with (7), and taking `H=floor(Z/2)`, gives only

\[
Z=O(k^{3/2}).
\tag{8}
\]

This is the exact second-moment source of the `N^{1/4}` barrier.

## 3. Why the raw higher factorial bounds do not automatically help

The right side of (4), divided by `M`, is of order `H^r/k^2`. If
`mu=kH/M asymp H/k`, Poisson-scale factorial moments would be of order
`mu^r=H^r/k^r`. For `r>=3`, (4) is weaker by a factor of order `k^{r-2}`.
A two-point distribution concentrated at zero and at a value of order `mu`
can saturate the first two moments while staying far below every bound (4).
This is the **translate-clustering obstruction**.

A separate estimate is therefore needed to rule out a population of rare,
dense interval--translate intersections.

## 4. Exact high-moment gateway theorem

Let

\[
\mu=\frac1M\sum_sX_s=\frac{kH}{M}.
\]

Assume that, for some integer `r>=1`, the centered moment estimate

\[
\frac1M\sum_s|X_s-\mu|^{2r}\le C_r\mu^r
\tag{9}
\]

holds for every interval length under consideration. At a zero window,
`|X_s-mu|^{2r}=mu^{2r}`, so

\[
\frac{Z_0}{M}\le C_r\mu^{-r}.
\tag{10}
\]

Let `Z>=4` be a zero run and take `H=floor(Z/2)`. Then

\[
Z-H+1\ge Z/2,
\qquad H\ge Z/3.
\]

Using (10),

\[
\frac Z2
\le M C_r\left(\frac{M}{kH}\right)^r
\le M C_r\left(\frac{3M}{kZ}\right)^r.
\]

Therefore

\[
\boxed{
Z^{r+1}\le 2\,3^r C_r\frac{M^{r+1}}{k^r}.}
\tag{11}
\]

Since `M asymp k^2`, a fixed-order Poisson-scale moment bound gives

\[
Z\ll_r C_r^{1/(r+1)}k^{1+1/(r+1)}.
\tag{12}
\]

If (9) holds for orders `r=r(k)` tending to infinity with

\[
\log C_{r(k)}=o(r(k)\log k),
\]

then

\[
\boxed{Z=k^{1+o(1)}.}
\tag{13}
\]

This implication is unconditional; the moment hypothesis is the open part.
It identifies an exact route from incidence control to subpolynomial cyclic
gaps.

## 5. Extension to an almost-perfect cyclic completion

For the ruler reduction in `cyclic_defect_reduction.md`, let `nu(t)` be the
directed cyclic difference multiplicity. For an interval `I_H`, the translated
window counts satisfy

\[
\sum_sX_s(X_s-1)
 =\sum_{x\ne y\in I_H}\nu(y-x).
\tag{14}
\]

Thus holes and duplicates perturb the second moment by a weighted defect term.
The third and higher moments count compatible collections of directed edges
sharing one translate. They are exactly where the common gradient/vertex
realization enters.

The unresolved target is a stability version of (9) in which the right side
also includes a quantitatively controlled contribution from the cyclic defect.
Combined with the hole--duplicate balance and the protected initial residues,
such an estimate would imply the stability bound `M-D<=k^{1+o(1)}`.

## 6. Exact incidence-coupled Level-2 formulation

For an ordered ruler introduce one-hot variables

\[
X_{i,\ell,t}=1_{\{a_{i+\ell}-a_i=t\}}.
\]

The exact polynomial constraints include

\[
X_{i,\ell,t}^2=X_{i,\ell,t},
\qquad
\sum_tX_{i,\ell,t}=1,
\]

\[
X_{i,\ell,t}X_{j,m,t}=0
\quad\text{for distinct intervals},
\]

and the completion localizers

\[
X_{i,\ell,t}X_{i+\ell,r,s}
 =X_{i,\ell,t}X_{i+\ell,r,s}X_{i,\ell+r,t+s}.
\tag{15}
\]

A Level-2 moment relaxation keeps all moments of degree at most two and the
linearized consequences of (15) whose total degree fits the level. Unlike the
uncoupled rank cone, this system ties each lag to the same vertex potential.
No exact asymptotic optimum for this cone is claimed here.

## 7. Exact pseudodistribution proving the raw factorial plateau

For an integer `mu>=1`, define

\[
\mathbb P(X=0)=\frac1{\mu+1},
\qquad
\mathbb P(X=\mu+1)=\frac\mu{\mu+1}.
\tag{16}
\]

Then

\[
\mathbb EX=\mu,
\qquad
\mathbb E(X)_2=\mu^2,
\]

and, for every `r>=2`,

\[
\mathbb E(X)_r
 =\mu^2(\mu-1)(\mu-2)\cdots(\mu-r+2)
 \le\mu^r.
\tag{17}
\]

Thus even Poisson-scale *factorial* moments permit zero mass of order
`1/mu`, exactly the amount corresponding to the `k^{3/2}` gap scale. By
contrast,

\[
\mathbb E|X-\mu|^{2r}
 =\frac{\mu^{2r}+\mu}{\mu+1}
 \asymp\mu^{2r-1},
\tag{18}
\]

which is far above the centered Poisson scale `mu^r` when `r>1`. This proves
that the gateway must control centered fluctuations or an equivalent
incidence-localizer; raw factorial counts cannot suffice.
