#!/usr/bin/env python3
"""Exact polynomial check of the spectral-selector factorization."""
from __future__ import annotations

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)

z = sp.symbols("z")
A = (0, 1, 6, 10, 23, 26, 34, 41, 53, 55)
k = len(A)
M = k * k - k + 1
D = A[-1]
g = M - D
P = sum(z**a for a in A)
Psharp = sp.expand(z**D * P.subs(z, z**-1))
Q = sp.Poly(sp.expand(P * Psharp - (k - 1) * z**D), z)

coeffs = [int(Q.nth(i)) for i in range(2 * D + 1)]
require(all(c in (0, 1) for c in coeffs), "Q is not binary")
require(sum(coeffs) == M, "Q does not have M ones")

S = sp.Poly(sum(z**r for r in range(M)), z)
quotient, remainder = sp.div(Q, S)
require(remainder.is_zero, "S_M does not divide Q")

# Recover selector E from Q = S + (z^M-1)E.
Qexpr = Q.as_expr()
selector_num = sp.Poly(sp.expand(Qexpr - S.as_expr()), z)
E_poly, rem2 = sp.div(selector_num, sp.Poly(z**M - 1, z))
require(rem2.is_zero, "selector division has a remainder")
Ecoeff = [int(E_poly.nth(i)) for i in range(max(0, E_poly.degree()) + 1)]
require(all(c in (0, 1) for c in Ecoeff), "E is not binary")

L = M - 2 * g + 1
Efull = [int(E_poly.nth(i)) for i in range(L)]
require(all(int(E_poly.nth(i)) == 0 for i in range(L, M)), "E exceeds predicted support")
require(all(Efull[r] + Efull[L - 1 - r] == 1 for r in range(L)),
        "selector is not complement-palindromic")
require(sum(Efull) * 2 == L, "selector is not balanced")

R_expected = sp.Poly(1 + (z - 1) * E_poly.as_expr(), z)
require(sp.Poly(quotient, z) == R_expected, "quotient formula fails")

print("PASS: exact spectral-selector factorization.")
print(f"M={M}, D={D}, g={g}, selector length L={L}, selector weight={sum(Efull)}")
print("selector bits =", "".join(map(str, Efull)))
