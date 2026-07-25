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
