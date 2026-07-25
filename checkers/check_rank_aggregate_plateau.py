#!/usr/bin/env python3
"""Exact SymPy checks for the central-gap rank-aggregate plateau formulas."""
from __future__ import annotations

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)

k, L, x, n, q = sp.symbols("k L x n q", positive=True, integer=True)
P = L * (L + 1) / 2
M = k * L - P
rho = sp.simplify(M * (M + 1) / (L * (L + 1)))
formula = k**2 / x + k * x - k - k / x - x**2 / 4 + x / 4 + sp.Rational(1, 2)
require(sp.simplify((k**2 - rho).subs(L, x - 1) - formula) == 0,
        "short-rank formula mismatch")

Pq = q * (q + 1) / 2
c = n**2 - Pq
Mlong = n * (2 * n - 1) - Pq
require(sp.simplify(c - (n**2 - q * (q + 1) / 2)) == 0, "long coefficient mismatch")
require(sp.simplify(Mlong - (n * (2 * n - 1) - q * (q + 1) / 2)) == 0,
        "long band count mismatch")

y = sp.symbols("y", nonnegative=True)
poly = sp.factor(6 * (1 - y) - (2 - y) ** 2)
require(poly == -(y**2 + 2 * y - 2), "normalized polynomial mismatch")
require(sp.simplify(poly.subs(y, sp.Rational(1, 2))) == sp.Rational(3, 4),
        "endpoint bound mismatch")

print("PASS: exact rank-aggregate plateau algebra.")
print("k^2-rho(k,L) =", formula)
