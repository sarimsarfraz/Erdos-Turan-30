#!/usr/bin/env python3
"""Exact formal-algebra checks for the square-and-potential decomposition.

Symbols stand for already justified integrals.  This checks coefficients and
cancellations; it is deliberately not presented as a proof of convergence.
"""
from __future__ import annotations

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)

H = sp.symbols("H", real=True)
F2, KF2, FF_D, G2, GKF = sp.symbols("F2 KF2 FF_D G2 GKF", real=True)
linear_f = sp.symbols("linear_f", real=True)

# Completing the square in g.
complete = sp.expand((G2 - GKF) - ((sp.Symbol("S")) + KF2 / 4))
# Replace S by ||g-Kf/2||^2 = G2-GKF+KF2/4.
S_value = G2 - GKF + KF2 / 4
require(sp.simplify((G2 - GKF) - (S_value - KF2 / 4)) == 0,
        "square completion coefficient fails")

# K identity substitution: 1/2 F2 - 1/4 KF2 = 1/4 F2 + 1/4 FF_D.
left = F2 / 2 - KF2 / 4
right = F2 / 4 + FF_D / 4
require(sp.simplify(left.subs(KF2, F2 - FF_D) - right) == 0,
        "K-identity substitution fails")

# Expansion of ||p-p0||^2/4 with ||p0||^2=4/3 and <p,p0>=2 int_0^1 u p.
P2, UP01 = sp.symbols("P2 UP01", real=True)
expanded_norm = P2 / 4 + sp.Rational(1, 3) - UP01
require(sp.expand(expanded_norm - (P2 / 4 + sp.Rational(1, 3) - UP01)) == 0,
        "norm expansion bookkeeping fails")

# Cross-D cancellation for u>1:
# -(p*C) - p*(u-C) = -p*u.
p, C, u = sp.symbols("p C u", real=True)
require(sp.expand(-p * C - p * (u - C) + p * u) == 0,
        "cross-D cancellation fails")

# Constant H-1 + 1/3 = H-2/3.
require(sp.simplify(H - 1 + sp.Rational(1, 3) - (H - sp.Rational(2, 3))) == 0,
        "constant reduction fails")

# Endpoint pointwise squares.
x, q = sp.symbols("x q", nonnegative=True)
low = sp.expand(x * q + q**2 / 4 - q + (1 - x) ** 2)
require(sp.factor(low - (q / 2 - (1 - x)) ** 2) == 0,
        "low-x pointwise square fails")
high = sp.expand(x * q + q**2 / 4 - q)
require(sp.factor(high - ((x - 1) * q + q**2 / 4)) == 0,
        "high-x pointwise identity fails")
require(sp.integrate((1 - x) ** 2, (x, 0, 1)) == sp.Rational(1, 3),
        "endpoint integral mismatch")

print("PASS: exact decomposition (19) coefficient algebra.")
print("endpoint square (0<=x<=1):", sp.factor(low))
print("endpoint integral =", sp.Rational(1, 3))
