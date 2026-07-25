#!/usr/bin/env python3
"""Exact finite checks for translate-incidence moment identities."""
from __future__ import annotations

from math import comb


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def verify_difference_set(D: tuple[int, ...], M: int) -> None:
    k = len(D)
    counts = [0] * M
    for a in D:
        for b in D:
            if a != b:
                counts[(a - b) % M] += 1
    require(counts[0] == 0, "zero directed difference occurred")
    require(all(counts[r] == 1 for r in range(1, M)),
            f"not a planar difference set: counts={counts}")
    require(M == k * k - k + 1, "parameter equation fails")


def window_counts(D: tuple[int, ...], M: int, H: int) -> list[int]:
    I = set(range(H))
    return [sum(1 for d in D if (d + s) % M in I) for s in range(M)]


def verify_moments(D: tuple[int, ...], M: int, H: int) -> None:
    X = window_counts(D, M, H)
    k = len(D)
    require(sum(X) == k * H, "first moment identity fails")
    require(sum(comb(x, 2) for x in X) == comb(H, 2),
            "second factorial moment identity fails")
    for r in range(3, min(H, k) + 1):
        require(sum(comb(x, r) for x in X) <= comb(H, r),
                f"higher factorial moment bound fails at r={r}")


def max_zero_run(D: tuple[int, ...], M: int) -> int:
    bits = [1 if x in D else 0 for x in range(M)]
    doubled = bits + bits
    best = cur = 0
    for b in doubled:
        if b == 0:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return min(best, M - len(D))

examples = [
    ((0, 1, 3, 9), 13),
    ((0, 1, 6, 10, 23, 26, 34, 41, 53, 55), 91),
]
for D, M in examples:
    verify_difference_set(D, M)
    for H in range(1, min(12, M) + 1):
        verify_moments(D, M, H)
    Z = max_zero_run(D, M)
    print(f"PASS: (M,k)=({M},{len(D)}), maximum zero run={Z}, gap distance={Z+1}")
