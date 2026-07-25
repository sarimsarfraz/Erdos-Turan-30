# Exact spectral-selector factorization for a perfect ruler

This is a separate attempt to move beyond autocorrelation smoothing by keeping
the full spectral factor.

Let

\[
A=\{0=a_0<\cdots<a_{k-1}=D\}
\]

be a perfect cyclic ruler modulo

\[
M=k^2-k+1,
\]

meaning that its positive differences choose exactly one element from every
pair `{r,M-r}`. Put `g=M-D`.

Define

\[
P(z)=\sum_{a\in A}z^a,
\qquad
P^\#(z)=z^DP(z^{-1}),
\]

and

\[
Q(z)=P(z)P^\#(z)-(k-1)z^D.
\tag{1}
\]

## 1. Binary selector polynomial

The coefficient of `z^{D+d}` in `P P#` is the number of ordered pairs with
difference `d`. The ruler property makes every nonzero coefficient zero or
one, and the center coefficient becomes one after subtracting `k-1`. Hence
`Q` is a binary polynomial with exactly

\[
1+k(k-1)=M
\]

nonzero coefficients.

Those exponents represent every residue modulo `M` exactly once. Therefore

\[
Q(z)\equiv S_M(z):=1+z+\cdots+z^{M-1}\pmod{z^M-1}.
\tag{2}
\]

There is a unique binary selector polynomial

\[
E(z)=\sum_{r=0}^{M-1}\varepsilon_rz^r,
\qquad\varepsilon_r\in\{0,1\},
\]

such that

\[
Q(z)=S_M(z)+(z^M-1)E(z).
\tag{3}
\]

Since `z^M-1=(z-1)S_M`,

\[
\boxed{Q(z)=S_M(z)\bigl(1+(z-1)E(z)\bigr).}
\tag{4}
\]

This is an integral factorization, not only a root-of-unity identity.

## 2. Exact support and complement symmetry

Since `deg Q=2D=2M-2g`, a lifted exponent `r+M` can occur only when

\[
0\le r\le M-2g.
\]

Put

\[
L=M-2g+1.
\]

Then `E` is supported on `{0,...,L-1}`. Polynomial `Q` is palindromic about
`D`. If the representative of residue `r` is lifted to `r+M`, its mirror is
the unlifted exponent `L-1-r`; conversely an unlifted `r` mirrors to a lifted
`L-1-r`. Hence

\[
\boxed{\varepsilon_r+\varepsilon_{L-1-r}=1
\quad(0\le r<L).}
\tag{5}
\]

In particular, `L` is even and

\[
\boxed{E(1)=L/2=(M+1)/2-g.}
\tag{6}
\]

The same identity follows by differentiating (4) at one: palindromy gives
`Q'(1)=DM`, while `S_M'(1)=M(M-1)/2`.

## 3. What this machinery sees and what it does not

Equations (4)--(6) retain the exact spectral factorization and ordinary
support gap. They reduce the residue-lift pattern to a balanced
anti-palindromic binary word. But that class has `2^{L/2}` elements and exists
for every admissible `g`; divisibility and palindromy alone impose no
subpolynomial bound on `g`.

The missing constraint is that

\[
Q+(k-1)z^D=P P^\#
\]

must have a **binary spectral factor** `P` whose exponents form a gradient
set. Characterizing which selector words admit that factor is equivalent to a
nonlinear incidence-realizability problem. This is the
**selector-factor plateau**.
