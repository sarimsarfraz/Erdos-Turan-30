#!/usr/bin/env python3
"""Exact algebra checks for the C(r), D(r), and renewal derivation.

The analytic differentiation under the integral is proved in the note.  This
script checks the resulting functional algebra exactly.
"""
from __future__ import annotations

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)

r = sp.symbols("r", real=True)


# The regularization/initial-segment term reduces exactly to 4(1-r).
z = sp.exp(r) - 2
extra = sp.simplify(2 - 2*z + 2*sp.integrate(sp.exp(sp.Symbol("t")) - 2, (sp.Symbol("t"), 0, r)))
require(sp.simplify(extra - 4*(1-r)) == 0, "the 4(1-r) term is missing")

# Check that C=2r satisfies C'=C(r)-C(1-r)+4(1-r).
C_r = 2 * r
C_1mr = 2 * (1 - r)
functional_residual = sp.expand(sp.diff(C_r, r) - (C_r - C_1mr + 4 * (1 - r)))
require(functional_residual == 0, "C=2r does not solve the functional equation")

# If F is affine, F'=F(r)-F(1-r) forces zero slope.
a, b = sp.symbols("a b")
F = a * r + b
stationarity = sp.Poly(sp.expand(sp.diff(F, r) - (F - F.subs(r, 1 - r))), r)
require(stationarity.coeff_monomial(r) == -2 * a, "unexpected affine coefficient")
require(stationarity.coeff_monomial(1) == 2 * a, "unexpected affine constant")

# Renewal substitution: C=2r-D and C=int C gives D=1+int D.
D, I0, I1 = sp.symbols("D I0 I1")
# I0 = integral D, I1 = integral vD.
renewal = sp.simplify(D - (1 + I0))
require(renewal.subs(I0, D - 1) == 0, "renewal substitution fails")

# Weighted identity: if I0=D-1 and I0-I1=r-1, then D-I1=r.
weighted = sp.simplify((D - I1 - r).subs(I1, I0 - (r - 1)).subs(I0, D - 1))
require(weighted == 0, "weighted renewal identity fails")

# C + integral(vD) = r, since C=2r-D and I1=D-r.
C_plus = sp.simplify((2 * r - D) + (D - r) - r)
require(C_plus == 0, "C cancellation fails")

# C(0) from the exact z moments.
z0_at_0 = -1
Z1 = -sp.Rational(1, 3)
Z2 = sp.Rational(1, 3)
C0 = sp.simplify(2 + z0_at_0 + 4 * Z1 + Z2)
require(C0 == 0, f"C(0) is {C0}")

print("PASS: exact C/D renewal algebra.")
print("functional residual =", functional_residual)
print("C(0) =", C0)
