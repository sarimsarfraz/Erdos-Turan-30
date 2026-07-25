#!/usr/bin/env python3
"""Exact symbolic checks for the delay profile.

This script verifies identities that reduce to finite symbolic integration or
formal series algebra.  It does not replace the contour-shift or Fubini
arguments in the proof note.
"""
from __future__ import annotations

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)

u, t, x, s = sp.symbols("u t x s", real=True)

# Active covering at x=0.
active = sp.simplify(sp.integrate(2 * u * (sp.exp(u) - 1), (u, 0, 1)))
require(active == 1, f"active integral is {active}, expected 1")

# Laplace transform has removable value -1/3 at zero.
Z = ((2 - s) * sp.exp(s) - (2 + s)) / (s * ((s - 1) * sp.exp(s) + 1))
series = sp.series(Z, s, 0, 4)
require(sp.limit(Z, s, 0) == -sp.Rational(1, 3), "Z(0) mismatch")

# First integral.
z_initial = sp.exp(t) - 2
first = sp.simplify(sp.integrate((1 - t**2) * z_initial, (t, 0, 1)))
require(first == -sp.Rational(1, 3), f"first integral is {first}")

# Adjoint identity on 0<t<1.
y = sp.symbols("y", nonnegative=True)
adjoint_initial = sp.simplify(
    y + sp.integrate((y - x) * (sp.exp(x) - 2), (x, 0, y))
)
expected = sp.exp(y) - 1 - y**2
require(sp.simplify(adjoint_initial - expected) == 0, "initial adjoint identity fails")

# Positive dual stationarity on 0<t<1.
dual_initial = sp.simplify(
    2 * y + sp.integrate(2 * (y - x) * sp.exp(x), (x, 0, y))
)
require(sp.simplify(dual_initial - 2 * (sp.exp(y) - 1)) == 0,
        "initial positive-dual identity fails")

# Candidate constants.
A0 = sp.integrate((2 * u) ** 2, (u, 0, 1))
Z1 = -sp.Rational(1, 3)
Z2 = sp.Rational(1, 3)
B0 = sp.simplify(1 + 2 * Z1 + Z2)
require(A0 == sp.Rational(4, 3), "A0 mismatch")
require(B0 == sp.Rational(2, 3), "B0 mismatch")
require(sp.simplify(A0 * B0 - sp.Rational(8, 9)) == 0, "product mismatch")
require(sp.simplify(A0 / 2 + B0 - sp.Rational(4, 3)) == 0,
        "linear objective mismatch")

print("PASS: exact delay-profile symbolic identities.")
print("Laplace series at zero:", series)
print("A0 =", A0)
print("B0 =", B0)
print("A0*B0 =", A0 * B0)
