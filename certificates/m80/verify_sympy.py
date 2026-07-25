#!/usr/bin/env python3
"""Independent SymPy-rational verifier for the m=80 certificate."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp


class CertificateError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CertificateError(message)


path = Path(__file__).with_name("certificate.json")
d = json.loads(path.read_text(encoding="utf-8"))
R, m, L = map(int, (d["R"], d["m"], d["L"]))
n = m * L
Q = sp.Rational
weights = [Q(int(x), int(d["weights_den"])) for x in d["weights_num"]]
kernels = [
    [Q(int(x), int(d["kernel_den"])) for x in row]
    for row in d["kernels_num"]
]
eta = Q(int(d["eta_num"]), int(d["eta_den"]))
boundaries = [
    [Q(int(x), int(d["boundary_den"])) + eta for x in row]
    for row in d["boundary_num"]
]
target = Q(int(d["target_num"]), int(d["target_den"]))

require(sum(weights) == 1, "mixing weights do not sum to one")
require(all(x > 0 for x in weights), "a mixing weight is not positive")
for r, row in enumerate(kernels):
    require(sum(row) == 1, f"kernel {r} is not normalized")
    require(row == list(reversed(row)), f"kernel {r} is not symmetric")
    require(all(x >= 0 for x in row), f"kernel {r} has a negative entry")

slacks: list[sp.Rational] = []
for q in range(n + 1):
    c = sp.S.Zero
    for r in range(R):
        for i in range(m):
            w = sp.S.One if q + i >= n else boundaries[r][q + i]
            c += weights[r] * kernels[r][i] * w
    slack = sp.factor(c - 1)
    require(bool(slack >= 0), f"covering constraint q={q} fails")
    slacks.append(slack)

a = sp.factor(m * sum(
    weights[r] * sum(x * x for x in kernels[r]) for r in range(R)
))
rho = sum(weights[r] * sum(x * x for x in boundaries[r]) for r in range(R))
b = sp.factor(1 + 2 * (rho / m - L))
require(a == Q(int(d["a_num"]), int(d["a_den"])), "a mismatch")
require(b == Q(int(d["b_num"]), int(d["b_den"])), "b mismatch")
gap = sp.factor(target**2 - a * b)
require(bool(gap > 0), "target^2-a*b is not positive")

print("PASS: independent SymPy rational checks completed.")
print("a =", a)
print("b =", b)
print("target^2-a*b =", gap)
print("equality q =", [i for i, s in enumerate(slacks) if s == 0])
