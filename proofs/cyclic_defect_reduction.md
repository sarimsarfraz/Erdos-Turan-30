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
