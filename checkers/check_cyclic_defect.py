#!/usr/bin/env python3
"""Exact checks for the almost-perfect cyclic completion of interval rulers."""
from __future__ import annotations

from collections import Counter
from itertools import combinations


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def verify_ruler(A: tuple[int, ...]) -> dict[str, int]:
    k = len(A)
    D = A[-1] - A[0]
    M = k * k - k + 1
    require(D < M, f"diameter {D} is not below M={M}")

    positive: dict[int, tuple[int, int]] = {}
    for i, j in combinations(range(k), 2):
        d = A[j] - A[i]
        require(d not in positive, f"repeated positive difference {d}")
        positive[d] = (i, j)

    nu = Counter()
    for i in range(k):
        for j in range(k):
            if i != j:
                nu[(A[j] - A[i]) % M] += 1

    require(all(nu[r] <= 2 for r in range(1, M)), "a cyclic multiplicity exceeds two")
    holes = [r for r in range(1, M) if nu[r] == 0]
    duplicates = [r for r in range(1, M) if nu[r] == 2]
    require(len(holes) == len(duplicates), "holes and duplicates do not balance")

    g = M - D
    require(all(nu[r] <= 1 for r in range(1, g)), "a protected small residue is duplicated")

    # Unordered residue-pair form.
    pair_counts = []
    for r in range(1, (M + 1) // 2):
        pair_counts.append(int(r in positive) + int(M - r in positive))
    require(pair_counts.count(0) == pair_counts.count(2),
            "empty and double unordered residue pairs do not balance")

    return {
        "k": k,
        "D": D,
        "M": M,
        "g": g,
        "holes": len(holes),
        "duplicates": len(duplicates),
    }

examples = [
    (0, 1, 4, 10),
    (0, 1, 6, 10, 23, 26, 34, 41, 53, 55),
]
for A in examples:
    result = verify_ruler(A)
    print("PASS:", A)
    print(result)
