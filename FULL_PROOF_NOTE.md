# Sidon exact-research: full proof and audit note

## Executive status

This note contains the complete proofs and exact reductions established in the
repository. It does **not** contain a proof of
`F(N)=sqrt(N)+N^{o(1)}`. The unresolved implication is isolated explicitly in
the incidence-hierarchy and cyclic-defect sections; no desired conclusion is
inserted as a lemma.

The proved components are:

1. the finite vector-valued covering lemma;
2. the exact `m=80` certificate interface;
3. the one-sided continuum barrier `inf sqrt(AB)=2sqrt(2)/3`;
4. the almost-perfect cyclic completion identities;
5. the translate-incidence hierarchy and exact high-moment gateway;
6. the uncoupled rank plateau and spectral-selector plateau.

---

---

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

---

# The extremal delay profile

All functions are real-valued on the nonnegative half-line. Define

\[
p_0(u)=2u\,1_{[0,1]}(u).
\]

Let

\[
w_0(t)=e^t-1\quad(0\le t<1)
\]

and for `t>=1` define the right-continuous continuation

\[
w_0(t)=\int_{t-1}^t w_0(s)\,ds.
\tag{1}
\]

Put

\[
z_0=w_0-1,
\qquad h_0=w_0+1=2+z_0.
\]

The value at `t=1` has a downward jump of one:
`w_0(1-)=e-1`, `w_0(1+)=e-2`.

## 1. Decay and integrability

For `t>=1`,

\[
z_0(t)=\int_{t-1}^t z_0(s)\,ds.
\tag{2}
\]

Its Laplace transform, initially for `Re(s)>0`, is

\[
Z(s)=\int_0^\infty e^{-st}z_0(t)\,dt
 =\frac{(2-s)e^s-(2+s)}
 {s((s-1)e^s+1)}.
\tag{3}
\]

This follows by taking the Laplace transform of the distributional equation

\[
z_0'=z_0+2\,1_{(0,1)}-1_{(1,\infty)}z_0(\cdot-1)-\delta_1.
\]

The apparent singularity of (3) at zero is removable; expansion gives

\[
Z(s)=-\frac13+\frac{s}{18}+O(s^2).
\tag{4}
\]

The characteristic equation away from zero is

\[
s=1-e^{-s}.
\tag{5}
\]

Its only root in `Re(s)>=0` is zero. Indeed, if `s=x+iy`, the imaginary part
of (5) gives `y=e^{-x}sin y`. If `x>0` and `y!=0`, then
`|y|<|sin y|<=|y|`, impossible. Thus `y=0`, and
`x=1-e^{-x}` has only `x=0`. At `x=0`, `y=sin y` again forces `y=0`.

There is a spectral gap. For any fixed `delta>0`, a root with
`Re(s)>=-delta` satisfies

\[
|s-1|=e^{-\Re s}\le e^\delta,
\]

so roots in that strip lie in a compact set. Since zero is isolated and
removable in `Z`, some `eta>0` exists for which `Z` is holomorphic on
`Re(s)>=-eta`. On vertical lines in that strip, (3) and its derivative have
the decay required for one integration by parts in the Bromwich integral.
Shifting the contour to `Re(s)=-eta` yields

\[
z_0(t)=O(e^{-\eta t}).
\tag{6}
\]

Thus `z_0` belongs to both `L^1` and `L^2`, and every Fubini interchange below
is absolutely justified.

## 2. Active covering identity

Define

\[
G(x)=\int_0^1 2u\,w_0(x+u)\,du.
\]

Direct integration gives `G(0)=1`. Integration by parts gives, at every point
of differentiability,

\[
G'(x)=2w_0(x+1)-2\int_x^{x+1}w_0(t)\,dt=0
\]

by (1). Hence

\[
\boxed{\int_0^1 2u\,w_0(x+u)\,du=1\quad(x\ge0).}
\tag{7}
\]

Equivalently, `T_{p_0}z_0=0`.

## 3. The first two exact integrals

Integrate `T_{p_0}z_0=0` over `x>=0`. Fubini gives

\[
0=\int_0^1t^2z_0(t)\,dt+\int_1^\infty z_0(t)\,dt.
\]

Therefore

\[
\int_0^\infty z_0(t)\,dt
 =\int_0^1(1-t^2)(e^t-2)\,dt
 =-\frac13.
\tag{8}
\]

For the square integral, let

\[
\nu=\frac12\delta_0+\frac12z_0(t)\,dt.
\]

The adjoint of `T_{p_0}` satisfies

\[
T_{p_0}^*\nu(t)=
\begin{cases}
 z_0(t)+1-t^2,&0\le t<1,\\
 z_0(t),&t\ge1.
\end{cases}
\tag{9}
\]

For `t<1`, (9) is the elementary identity

\[
t+\int_0^t(t-x)(e^x-2)\,dx=e^t-1-t^2.
\]

For `t>=1`, the density contribution is

\[
\int_{t-1}^t(t-x)z_0(x)\,dx.
\]

Equation (2) gives the unweighted integral `z_0(t)`, while (7), shifted by
`t-1`, says the complementary weighted integral is zero. Hence the displayed
integral equals `z_0(t)`.

Pairing (9) with `z_0` and using `T_{p_0}z_0=0` gives

\[
0=\int_0^\infty z_0(t)^2\,dt
  +\int_0^1(1-t^2)z_0(t)\,dt.
\]

Together with (8),

\[
\boxed{\int_0^\infty z_0(t)^2\,dt=\frac13.}
\tag{10}
\]

Consequently

\[
\int_0^\infty(w_0(t)^2-1)\,dt
 =2\int z_0+\int z_0^2=-\frac13.
\tag{11}
\]

## 4. Positive dual measure and stationarity

Let

\[
\mu_0=\delta_0+h_0(t)\,dt.
\tag{12}
\]

It is positive. The exact adjoint equation is

\[
\boxed{T_{p_0}^*\mu_0=2w_0.}
\tag{13}
\]

For `0<=t<1`,

\[
2t+\int_0^t2(t-x)e^x\,dx=2(e^t-1).
\]

For `t>=1`, the left side is

\[
\int_0^1 2v\,h_0(t-v)\,dv.
\]

The delay relation gives `int_0^1 h_0(t-v)dv=h_0(t)`. The shifted active
identity (7) gives

\[
\int_0^1 2(1-v)h_0(t-v)\,dv=2.
\]

Subtracting yields `2h_0(t)-2=2w_0(t)`.

## 5. Correlation and renewal slack

Define the absolutely convergent regularized correlation

\[
C(r)=h_0(r)+\int_0^\infty
 \big(h_0(x)h_0(x+r)-4\big)\,dx.
\tag{14}
\]

Using `h_0=2+z_0` and (8)--(10), `C(0)=0`.

For `0<r<1`, differentiate after expanding (14) in the integrable function
`z_0`. The distributional delay equation gives

\[
C'(r)=C(r)-C(1-r)+4(1-r).
\tag{15}
\]

For completeness, the extra term is not optional: writing
`R(r)=int z_0(x)z_0(x+r)dx`, one obtains

\[
R'(r)=R(r)-R(1-r)+2\int_0^{1-r}z_0(x)dx-z_0(1-r),
\]

and substituting `z_0(t)=e^t-2` on `[0,1)` produces `4(1-r)` in (15).

Let `F(r)=C(r)-2r`. Equation (15) becomes

\[
F'(r)=F(r)-F(1-r).
\]

Differentiating once more gives `F''=0`. Substitution back forces the slope to
vanish, and `F(0)=0`; hence

\[
\boxed{C(r)=2r\quad(0\le r<1).}
\tag{16}
\]

For `r>=1`, the delay equation applied to `h_0(x+r)` gives

\[
\boxed{C(r)=\int_0^1C(r-v)\,dv.}
\tag{17}
\]

Set

\[
D(r)=2r-C(r),
\]

and extend `D` by zero on negative arguments. Then

\[
D(r)=0\quad(0\le r<1),
\qquad
D(r)=1+\int_0^1D(r-v)\,dv\quad(r\ge1).
\tag{18}
\]

In particular,

\[
\boxed{D(r)\ge0\quad(r\ge0).}
\tag{19}
\]

A weighted renewal identity will be needed. Put

\[
J(r)=\int_0^1(1-v)D(r-v)\,dv.
\]

For `r>1`, changing variables shows

\[
J'(r)=D(r)-\int_{r-1}^{r}D(t)\,dt=1
\]

by (18), and `J(1)=0`. Thus

\[
J(r)=r-1.
\tag{20}
\]

Since `int_0^1D(r-v)dv=D(r)-1`, equation (20) implies

\[
D(r)-\int_0^1vD(r-v)\,dv=r.
\tag{21}
\]

Equivalently,

\[
\boxed{C(r)+\frac12\int_0^1p_0(v)D(r-v)\,dv=r
\quad(r\ge1).}
\tag{22}
\]

Finally define

\[
\Psi(u)=w_0(u)+\int_0^\infty h_0(x)z_0(x+u)\,dx.
\]

Expanding (14) and using (8) gives

\[
\boxed{\Psi(u)=C(u)-\frac13.}
\tag{23}
\]

On `[0,1]`, (16) says `Psi(u)=p_0(u)-1/3`. These are the Euler--Lagrange
stationarity identities used by the barrier proof.

---

# The square-and-potential decomposition

This note proves the global inequality at the heart of the continuum barrier.
All functions and kernels are those defined in `delay_profile.md`.

## 1. Admissible scalar system

Let `H>0`. Let `p>=0` belong to `L^2([0,H])`, with `int p=1`, and extend it by
zero. Let `w-1` belong to `L^1 cap L^2` and suppose

\[
T_pw(x):=\int_0^H p(u)w(x+u)\,du\ge1
\quad\text{for almost every }x\ge0.
\tag{1}
\]

Set

\[
A=\int p^2,
\qquad
B=H+\int_0^\infty(w^2-1).
\]

Write

\[
f=p-p_0,
\qquad
g=w-w_0.
\]

Then `int f=0`.

## 2. The causal operator identity

Define

\[
(Kf)(t)=f(t)+\int_0^t h_0(x)f(t-x)\,dx.
\tag{2}
\]

Then

\[
\boxed{
\|Kf\|_2^2
 =\|f\|_2^2-
 \iint f(u)f(v)D(|u-v|)\,du\,dv.}
\tag{3}
\]

### Proof of (3)

First truncate every outer `t`-integral at `T`, expand the square, and then
let `T` tend to infinity. The cross term between `f` and `h_0*f` is

\[
\iint f(u)f(v)h_0(|u-v|)\,du\,dv.
\]

For the convolution-square term, suppose `v>=u`, put `r=v-u`, and write

\[
\int_v^T h_0(t-u)h_0(t-v)\,dt
 =\int_0^{T-v}h_0(x+r)h_0(x)\,dx.
\]

Since `h_0=2+O(e^{-eta x})`, this equals

\[
4(T-v)+\int_0^\infty(h_0(x+r)h_0(x)-4)\,dx+o(1).
\]

After multiplication by `f(u)f(v)` and symmetric integration, the `4T` term
vanishes because `int f=0`. The terms involving `u+v` also vanish. The only
cutoff remainder is `-2|u-v|`. Hence the convolution-square term is

\[
\iint f(u)f(v)
\left[
\int_0^\infty(h_0(x)h_0(x+|u-v|)-4)\,dx
-2|u-v|
\right]du\,dv.
\]

Adding the cross term and using `C=h_0+int(h_0h_0-4)` gives

\[
\|Kf\|_2^2=\|f\|_2^2+
\iint f(u)f(v)(C(|u-v|)-2|u-v|)du\,dv,
\]

which is (3), because `D(r)=2r-C(r)`. Absolute convergence follows from the
compact support of `f` and exponential decay of `h_0-2`.

## 3. Pairing the majorant with the positive dual measure

Since `T_{p_0}w_0=1`, (1) is

\[
T_fw_0+T_pg\ge0.
\]

Pair this nonnegative function with

\[
\mu_0=\delta_0+h_0(x)dx.
\]

The pairing is finite after subtracting the limiting constants; this is
legitimate because `int f=0`, `g in L^1`, and `h_0-2` decays exponentially.
Using `T_{p_0}^*mu_0=2w_0`, one obtains

\[
0\le\int f(u)\Psi(u)\,du
 +2\int g(t)w_0(t)\,dt
 +\int g(t)(Kf)(t)\,dt.
\tag{4}
\]

Here `Psi=C-1/3` is equation (23) of `delay_profile.md`.

The objective difference from the extremizer is

\[
\begin{aligned}
\frac A2+B-\frac43
={}&H-1+\int p_0f+\frac12\|f\|_2^2\\
&+2\int w_0g+\|g\|_2^2.
\end{aligned}
\tag{5}
\]

Use (4) to eliminate `2 int w_0g`, complete the square in `g`, and invoke
(3). This yields

\[
\frac A2+B-\frac43
\ge\left\|g-\frac12Kf\right\|_2^2+Q_H(p),
\tag{6}
\]

where

\[
\begin{aligned}
Q_H(p)={}&H-1-\int_{u>1}p(u)C(u)\,du
 +\frac14\|p-p_0\|_2^2\\
&+\frac14\iint
 (p-p_0)(u)(p-p_0)(v)D(|u-v|)\,du\,dv.
\end{aligned}
\tag{7}
\]

The term involving `C` follows because `p_0-Psi` is constant `1/3` on
`[0,1]`, and `int f=0` removes that constant.

## 4. Exact reduction of `Q_H`

Since `D=0` when both arguments lie in `[0,1]`, expand (7). The cross term with
`p_0` is evaluated by the weighted renewal identity

\[
C(u)+\frac12\int_0^1p_0(v)D(u-v)\,dv=u
\quad(u\ge1).
\]

After cancellation,

\[
\boxed{
\begin{aligned}
Q_H(p)={}&H-\frac23-\int_0^Hup(u)\,du
 +\frac14\int_0^Hp(u)^2\,du\\
&+\frac14\int_0^H\int_0^H
 p(u)p(v)D(|u-v|)\,du\,dv.
\end{aligned}}
\tag{8}
\]

The last term is nonnegative because `p>=0` and `D>=0` pointwise.

## 5. Pointwise endpoint certificate

Put `x=H-u` and `q(x)=p(H-x)`. For all `x,q>=0`,

\[
xq+\frac{q^2}{4}\ge q-(1-x)_+^2.
\tag{9}
\]

For `0<=x<=1`, the difference is exactly

\[
\left(\frac q2-(1-x)\right)^2.
\]

For `x>=1`, the difference is

\[
(x-1)q+\frac{q^2}{4}.
\]

Integrating (9), using `int q=1` and
`int_0^1(1-x)^2dx=1/3`, gives

\[
H-\int up+\frac14\int p^2\ge\frac23.
\tag{10}
\]

Equations (6), (8), and (10) prove

\[
\boxed{\frac A2+B\ge\frac43.}
\tag{11}
\]

Every term discarded in this proof is displayed as a square or as an integral
of a pointwise nonnegative kernel.

## 6. Vector-valued systems

Let `lambda_r>0`, `sum lambda_r=1`. Let each `p_r` be a probability density on
the common interval `[0,H]`, and assume only the combined covering inequality

\[
\sum_r\lambda_rT_{p_r}w_r\ge1.
\tag{12}
\]

Pair (12) once with `mu_0`, then repeat the preceding algebra componentwise and
sum with weights `lambda_r`. The term `H-1` occurs once; every square,
`D`-energy, first moment, and pointwise endpoint certificate averages linearly.
Thus, with

\[
A=\sum_r\lambda_r\int p_r^2,
\qquad
B=H+\sum_r\lambda_r\int(w_r^2-1),
\]

one again obtains (11).

---

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

---

# Almost-perfect cyclic completion of an interval ruler

Let

\[
A=\{0=a_0<a_1<\cdots<a_{k-1}=D\}
\]

be a `k`-mark Golomb ruler. Put

\[
M=k^2-k+1.
\]

This note concerns the nontrivial range `D<M`; if `D>=M`, the desired main
term lower bound for the diameter already holds.

## 1. Exact residue multiplicities

Let

\[
\Delta=\{a_j-a_i:0\le i<j<k\}.
\]

All elements of `Delta` are distinct and

\[
|\Delta|=\binom{k}{2}=\frac{M-1}{2}.
\]

For `1<=r<=(M-1)/2`, define

\[
m_r=1_\Delta(r)+1_\Delta(M-r).
\tag{1}
\]

Because `Delta` lies in `[1,D]` and `D<M`,

\[
m_r\in\{0,1,2\}.
\]

There are `(M-1)/2` unordered nonzero residue pairs and

\[
\sum_{r=1}^{(M-1)/2}m_r=|\Delta|=\frac{M-1}{2}.
\]

Therefore

\[
\boxed{\#\{r:m_r=0\}=\#\{r:m_r=2\}.}
\tag{2}
\]

In directed form, let

\[
\nu(t)=\#\{(i,j):i\ne j,\ a_j-a_i\equiv t\pmod M\}.
\]

Then `nu(t)` belongs to `{0,1,2}` for every nonzero residue, and the number of
holes `nu=0` equals the number of duplicates `nu=2`.

## 2. Protected initial residues

Put

\[
g=M-D.
\]

For every `1<=r<g`, one has `M-r>D`, so the second indicator in (1) vanishes.
Hence

\[
\boxed{m_r=1_\Delta(r)\in\{0,1\}\quad(1\le r<g).}
\tag{3}
\]

No protected initial residue can be duplicated. A missing small difference
must be compensated by a double residue pair elsewhere through (2).

When every `m_r=1`, `A` is a cyclic planar difference set modulo `M`; cutting
at its empty arc of length `g-1` recovers the interval ruler.

## 3. Exact shifted pair-sum interpretation of duplicates

A double pair `m_r=2` means that both `r` and `M-r` occur as positive
ordinary differences. Thus there are indices with

\[
(a_j-a_i)+(a_\ell-a_m)=M,
\]

or equivalently

\[
a_j+a_\ell=M+a_i+a_m.
\tag{4}
\]

Because `A` is Sidon, both unordered pair sums in (4) have unique
representations. The cyclic defect is therefore an exact matching between a
set of low pair sums and the corresponding pair sums shifted by `M`.
Pairwise autocorrelation records only how many such matches exist; the
incidence-coupled hierarchy records which endpoints participate.

## 4. Gateway to the upper subpolynomial error

Suppose one proves the following stability assertion uniformly for all
`k`-mark rulers:

\[
M-D\le k^{1+o(1)}.
\tag{5}
\]

Let `A subset {0,...,N-1}` be extremal and `k=|A|`. If its diameter is at least
`M`, then `k^2-k+1<=N-1`. Otherwise (5) gives

\[
N-1\ge D\ge k^2-k+1-k^{1+o(1)}.
\]

The elementary bound `k=O(sqrt N)` then implies

\[
\boxed{F(N)\le\sqrt N+N^{o(1)}.}
\tag{6}
\]

Thus the upper half of the subpolynomial-error assertion is exactly a
`k^{1+o(1)}` stability theorem for the almost-perfect cyclic completion.
Equation (5) is not proved in this repository.

---

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

---

# Exact plateau for the uncoupled rank-aggregate relaxation

Let

\[
d_{i,\ell}=a_{i+\ell}-a_i.
\]

The following information is imposed:

- all completion identities
  `d_{i,ell+r}=d_{i,ell}+d_{i+ell,r}`;
- rank-sum symmetry and concavity;
- every aggregate band floor

\[
\sum_{\ell\le L}\sum_i d_{i,\ell}
\ge\frac{M_L(M_L+1)}2,
\quad
M_L=kL-\frac{L(L+1)}2.
\]

No one-hot variable identifies which integer lag belongs to which interval.

For even `k=2n`, put essentially all diameter `D` in the central gap. For
`L<=n`, the central gap appears in

\[
P_L=\frac{L(L+1)}2
\]

band intervals, so

\[
Q_L=P_LD.
\]

The floor requires

\[
D\ge\rho(k,L):=\frac{M_L(M_L+1)}{L(L+1)}.
\]

Writing `x=L+1`, exact algebra gives

\[
\begin{aligned}
k^2-\rho(k,L)
={}&\frac{k^2}{x}+kx-k-\frac{k}{x}\\
&-\frac{x^2}{4}+\frac{x}{4}+\frac12.
\end{aligned}
\tag{1}
\]

Uniformly for `L<=k/2`, the right side is at least

\[
2k^{3/2}-O(k)
\]

at its critical minimum. For `L>k/2`, the corresponding floor is only
`(3/4)k^2+O(k)`. Consequently, for every fixed `beta<2`,

\[
D=k^2-\beta k^{3/2}
\]

passes every aggregate floor for all sufficiently large even `k`.

Small positive dyadic side gaps may be inserted and subtracted from the
central gap. This makes the marks strictly increasing while preserving every
inequality. Because the variables come from an actual gap vector, all
completion identities hold exactly, the moment matrix is rank one and PSD,

\[
R_\ell=R_{k-\ell},
\]

and

\[
R_{\ell+1}-2R_\ell+R_{\ell-1}
=-(g_\ell+g_{k-\ell})\le0.
\]

The pairwise-autocorrelation deficit in ruler normalization is

\[
\beta_0=\frac{4\sqrt2}{3}<2.
\]

Therefore this uncoupled rank-aggregate layer admits the pairwise value and
cannot improve it. The missing information is the incidence equivalence

\[
\text{lag }t\text{ is occupied}
\Longleftrightarrow
\text{one specific interval }d_{i,\ell}\text{ equals }t,
\]

with its degree-two localizers.

---

# Exact quotient/residue carry partition

Fix an integer block size `B`. Write every mark as

\[
a_i=Bq_i+s_i,
\qquad0\le s_i<B.
\]

For `i<j`, put `t=a_j-a_i` and write `t=Bd+r`, `0<=r<B`. Then exactly one of
the following holds:

1. **No carry:** `s_j>=s_i`, and
   \[
   d=q_j-q_i,
   \qquad r=s_j-s_i.
   \]

2. **Borrow/carry:** `s_j<s_i`, and
   \[
   d=q_j-q_i-1,
   \qquad r=B+s_j-s_i.
   \]

Thus full coverage of a block of consecutive differences imposes a
complementarity relation between non-carry edges at row lag `d` and carry
edges at row lag `d+1`.

Counting only how many edges fall in each carry class recovers an inversion
balance and reaches the same square-root critical scale as pairwise smoothing.
The information that remains unused is **residue-level complementarity**: for
every individual `r`, exactly one compatible endpoint pair must realize
`Bd+r`. The checker verifies this partition on the 10-mark planar ruler whose
initial differences are exactly `1,...,35`.

This route stopped at the **carry-count plateau**. A further step must couple
residue values and shared vertices, not only inversion totals.

---

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

---

# Final audit conclusion

The exact package closes the pairwise-autocorrelation optimization and several
strictly stronger but uncoupled relaxations. It does not close the
incidence-coupled stability problem. The missing theorem is a bound of the form

\[
M-D\le k^{1+o(1)}
\]

for the almost-perfect cyclic completion, or an equivalent family of centered
translate-incidence moment estimates with orders tending to infinity.

Until that statement is proved, the repository makes no claim of a
subpolynomial error term.
