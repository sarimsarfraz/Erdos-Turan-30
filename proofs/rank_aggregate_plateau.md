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
