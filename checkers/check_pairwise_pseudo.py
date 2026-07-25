#!/usr/bin/env python3
"""Exact checks for the two pairwise saturation pseudomodels."""
from __future__ import annotations

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)

lam, t = sp.symbols("lam t", positive=True)
ell = sp.symbols("ell", integer=True, positive=True)
fell = lam**ell * t ** (ell - 1) * sp.exp(-lam * t) / sp.factorial(ell - 1)
renewal_sum = sp.simplify(sp.summation(fell, (ell, 1, sp.oo)))
require(renewal_sum == lam, "gamma-density renewal sum is not flat")

beta0 = 4 * sp.sqrt(2) / 3
require(sp.simplify(4 - beta0**2) == sp.Rational(4, 9), "beta algebra fails")

# A unique directed labeling can retain all pairwise labels and violate the
# gradient/cocycle identity on one triangle.
for M in (7, 13, 21, 31):
    require((1 + 2) % M != 4 % M, f"triangle example accidentally closes mod {M}")

# Fourier spectrum of nu(0)=k, nu(r)=1 for r!=0 follows from
# sum_{r=0}^{M-1} chi(r)=0 for nontrivial characters:
# k + sum_{r!=0}chi(r)=k-1.
k = sp.symbols("k", integer=True, positive=True)
nontrivial_value = sp.simplify(k - 1)
trivial_value = sp.simplify(k + (k**2 - k))
require(trivial_value == k**2, "trivial Fourier value mismatch")

print("PASS: pairwise pseudoconfiguration identities.")
print("sum_l f_l(t) =", renewal_sum)
print("nontrivial cyclic spectral value =", nontrivial_value)
