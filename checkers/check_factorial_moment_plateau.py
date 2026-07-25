#!/usr/bin/env python3
"""Exact two-level pseudodistribution for the raw factorial-moment plateau."""
from __future__ import annotations

from fractions import Fraction
from math import prod


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)

for m in range(2, 25):
    p0 = Fraction(1, m + 1)
    p1 = Fraction(m, m + 1)
    height = m + 1
    mean = p1 * height
    second_falling = p1 * height * (height - 1)
    require(mean == m, f"mean mismatch at m={m}")
    require(second_falling == m * m, f"second factorial mismatch at m={m}")
    for r in range(2, min(10, m + 1) + 1):
        falling = prod(range(height - r + 1, height + 1))
        moment = p1 * falling
        require(moment <= m**r, f"factorial moment exceeds m^r at m={m}, r={r}")
    for r in range(2, 6):
        centered = p0 * m ** (2 * r) + p1
        require(centered >= Fraction(m ** (2 * r), m + 1), "centered lower bound fails")

print("PASS: exact two-level factorial-moment plateau for m=2,...,24.")
print("P(X=0)=1/(m+1), P(X=m+1)=m/(m+1).")
