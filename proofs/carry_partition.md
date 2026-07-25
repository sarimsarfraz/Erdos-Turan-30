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
