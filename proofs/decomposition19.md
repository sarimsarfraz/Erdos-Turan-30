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
