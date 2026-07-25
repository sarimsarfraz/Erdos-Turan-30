#!/usr/bin/env python3
"""Exact block/carry decomposition on the 10-mark planar ruler."""
from __future__ import annotations

from itertools import combinations


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)

A = (0, 1, 6, 10, 23, 26, 34, 41, 53, 55)
B = 10
representations: dict[int, tuple[int, int]] = {}
for i, j in combinations(range(len(A)), 2):
    d = A[j] - A[i]
    require(d not in representations, f"repeated difference {d}")
    representations[d] = (i, j)

# The cut gap is 36, hence every 1,...,35 is represented.
for t in range(1, 36):
    require(t in representations, f"initial difference {t} is missing")
    i, j = representations[t]
    qi, si = divmod(A[i], B)
    qj, sj = divmod(A[j], B)
    d, r = divmod(t, B)
    if sj >= si:
        require(d == qj - qi and r == sj - si,
                f"non-carry decomposition fails for t={t}")
    else:
        require(d == qj - qi - 1 and r == B + sj - si,
                f"carry decomposition fails for t={t}")

print("PASS: exact quotient/residue carry partition for differences 1,...,35.")
