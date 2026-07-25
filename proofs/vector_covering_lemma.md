# Vector-valued covering lemmas

This note gives the analytic bridge used by the finite certificate and the
one-sided continuum problem. No optimization statement is used in either
proof.

## 1. Energy estimate requiring no kernel symmetry

Let `A` be a Sidon subset of `{0,...,N-1}`, with `|A|=k`. Let `K` be a
nonnegative probability sequence on the integers with finite support. Put

\[
u=1_A*K,
\qquad
C(d)=\sum_s K(s)K(s+d).
\]

The autocorrelation `C` is nonnegative and even, whether or not `K` is
symmetric, and

\[
\sum_{d\in\mathbb Z}C(d)=1.
\]

If `Delta(A)` is the set of positive differences, then

\[
\begin{aligned}
\|u\|_2^2
 &=kC(0)+2\sum_{d\in\Delta(A)}C(d)\\
 &\le kC(0)+2\sum_{d\ge1}C(d)\\
 &=1+(k-1)C(0).
\end{aligned}
\tag{1}
\]

The only Sidon input is that each positive difference occurs at most once.

For kernels `K_r` and weights `lambda_r>=0`, `sum lambda_r=1`, averaging (1)
gives

\[
\sum_r\lambda_r\|1_A*K_r\|_2^2
\le 1+(k-1)\sum_r\lambda_r C_r(0).
\tag{2}
\]

## 2. Exact finite symmetric covering lemma

Fix integers `m,L,R>=1`. For each `r`, let

\[
p^{(r)}=(p_0^{(r)},\ldots,p_{m-1}^{(r)})
\]

be a nonnegative symmetric probability vector. Let `lambda_r>=0` sum to one.
Choose real numbers `w_j^{(r)}` for `0<=j<Lm` and extend them by
`w_j^{(r)}=1` for `j>=Lm`. Assume

\[
\sum_{r=1}^R\lambda_r\sum_{i=0}^{m-1}
 p_i^{(r)}w_{q+i}^{(r)}\ge1
\qquad(0\le q\le Lm).
\tag{3}
\]

Define

\[
a=m\sum_r\lambda_r\sum_i(p_i^{(r)})^2,
\tag{4}
\]

and

\[
b=1+2\left(
 \frac1m\sum_r\lambda_r\sum_{j=0}^{Lm-1}(w_j^{(r)})^2-L
\right).
\tag{5}
\]

### Lemma 2.1

If `b>0`, then

\[
F(N)\le \sqrt N+\sqrt{ab}\,N^{1/4}+O(1).
\tag{6}
\]

The implied constant depends on the fixed finite data, not on `N`.

### Proof

Choose a positive integer `h` and set `H=mh`. Define

\[
K_r(s)=\frac{p_i^{(r)}}h
\quad\text{for }ih\le s<(i+1)h,
\]

and zero otherwise. Then

\[
C_r(0)=\frac{m}{H}\sum_i(p_i^{(r)})^2,
\]

so (2) becomes

\[
\mathcal E:=\sum_r\lambda_r\|1_A*K_r\|_2^2
\le1+\frac{a(k-1)}H.
\tag{7}
\]

For sufficiently large `N`, take `N>=2LH`. On

\[
J=\{0,1,\ldots,N+H-2\},
\]

put the block values `w_j^{(r)}` on the first `LH` sites, put the reflected
block values on the last `LH` sites, and put `1` elsewhere. Call the resulting
sequence `Q_r`.

For any `x` with `0<=x<N`, the interval `[x,x+H-1]` meets at most one modified
boundary. At the left boundary, writing `x=qh+t`, `0<=t<h`, the convolution

\[
\sum_r\lambda_r\sum_sK_r(s)Q_r(x+s)
\]

is a convex combination, with coefficients `1-t/h` and `t/h`, of covering
constraints `q` and `q+1` in (3). It is therefore at least one. Symmetry of
`p^{(r)}` reduces the right boundary to the same calculation. In the interior
the convolution equals one. Thus

\[
\sum_r\lambda_r(K_r*Q_r)(x)\ge1
\qquad(0\le x<N).
\tag{8}
\]

Summing (8) over `x in A`, interchanging sums, and applying weighted
Cauchy--Schwarz gives

\[
k^2\le
\left(\sum_r\lambda_r\|Q_r\|_2^2\right)\mathcal E.
\tag{9}
\]

The first factor is exact. Starting from the constant sequence one on `J`,
the two modified boundaries contribute

\[
2h\sum_r\lambda_r\sum_{j=0}^{Lm-1}
\big((w_j^{(r)})^2-1\big).
\]

Using (5),

\[
\sum_r\lambda_r\|Q_r\|_2^2=N+bH-1.
\tag{10}
\]

Combining (7), (9), and (10),

\[
k^2\le(N+bH-1)\left(1+\frac{a(k-1)}H\right).
\tag{11}
\]

The elementary difference count gives `k=O(sqrt N)`. Choose `H`, constrained
to be a multiple of `m`, so that

\[
H=\sqrt{a/b}\,N^{3/4}+O(1).
\]

Expanding (11), first with `k=O(sqrt N)` and then substituting the resulting
`k=sqrt N+O(N^{1/4})`, yields

\[
k^2\le N+2\sqrt{ab}\,N^{3/4}+O(N^{1/2}).
\]

Taking square roots proves (6). `QED`

## 3. Exact causal one-sided covering lemma

Kernel symmetry in Lemma 2.1 is used only to copy one boundary certificate to
the other end. A causal kernel needs only one modified boundary.

Let `K_r` be nonnegative probability sequences supported on
`{0,...,H-1}`. Let `Q_r` be real sequences on `{0,...,N+H-2}`. Suppose

\[
\sum_r\lambda_r\sum_{s=0}^{H-1}K_r(s)Q_r(x+s)\ge1
\qquad(0\le x<N).
\tag{12}
\]

Then the same summation and Cauchy argument gives the exact inequality

\[
k^2\le
\left(\sum_r\lambda_r\|Q_r\|_2^2\right)
\left(1+(k-1)\sum_r\lambda_r\sum_sK_r(s)^2\right).
\tag{13}
\]

No condition is placed on the right edge because a causal convolution from a
mark `x` uses only sites `x,...,x+H-1`; the baseline support extension by `H`
accounts for that edge.

## 4. Continuum-to-discrete corollary

Normalize continuum kernels to a common support `[0,H_0]`. Suppose
`p_r>=0`, `int p_r=1`, and `w_r-1` is integrable and square-integrable, with

\[
\sum_r\lambda_r\int_0^{H_0}p_r(u)w_r(x+u)\,du\ge1
\quad(x\ge0).
\tag{14}
\]

Set

\[
A=\sum_r\lambda_r\int_0^{H_0}p_r(u)^2\,du,
\quad
B=H_0+\sum_r\lambda_r\int_0^\infty(w_r(t)^2-1)\,dt.
\tag{15}
\]

Assume the profiles are piecewise `C^1` with finitely many jumps and decay
exponentially to one. Midpoint discretization at physical scale `h` gives
causal kernels and boundary weights satisfying

\[
\sum_r\lambda_r\sum_sK_{r,h}(s)^2
 =\frac Ah+O(h^{-2}),
\tag{16}
\]

and

\[
\sum_r\lambda_r\|Q_{r,h}\|_2^2
 =N+Bh+o(h)+O(N/h).
\tag{17}
\]

A common upward correction `O(1/h)` makes every discrete covering inequality
exact. Its norm cost is `O(N/h)`. Taking `h asymp N^{3/4}` makes both errors
`o(N^{3/4})`. Equation (13) therefore gives

\[
F(N)\le\sqrt N+\sqrt{AB}\,N^{1/4}+o(N^{1/4}).
\tag{18}
\]

The proof of the continuum barrier establishes `AB>=8/9` for every such
one-sided system and exhibits equality.
