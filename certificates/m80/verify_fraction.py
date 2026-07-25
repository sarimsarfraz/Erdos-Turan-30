#!/usr/bin/env python3
"""Exact standard-library verifier for the complete m=80 certificate.

Every proof-relevant quantity is a fractions.Fraction.  Explicit exceptions are
used instead of ``assert`` so that ``python -O`` cannot disable a check.
"""
from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
import json
from pathlib import Path
from typing import Any

DATA_PATH = Path(__file__).with_name("certificate.json")


class CertificateError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CertificateError(message)


def load() -> dict[str, Any]:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def verify(data: dict[str, Any]) -> dict[str, Any]:
    R = int(data["R"])
    m = int(data["m"])
    L = int(data["L"])
    n = L * m

    wd = int(data["weights_den"])
    wn = [int(x) for x in data["weights_num"]]
    kd = int(data["kernel_den"])
    kn = [[int(x) for x in row] for row in data["kernels_num"]]
    bd = int(data["boundary_den"])
    bn = [[int(x) for x in row] for row in data["boundary_num"]]
    eta = Fraction(int(data["eta_num"]), int(data["eta_den"]))
    target = Fraction(int(data["target_num"]), int(data["target_den"]))

    require(R > 0 and m > 0 and L > 0, "R, m and L must be positive")
    require(len(wn) == R, "wrong number of mixing weights")
    require(all(x > 0 for x in wn), "mixing weights must be positive")
    require(sum(wn) == wd, "mixing weights do not sum to one")
    weights = [Fraction(x, wd) for x in wn]

    require(len(kn) == R, "wrong number of kernels")
    kernels: list[list[Fraction]] = []
    for r, row in enumerate(kn):
        require(len(row) == m, f"kernel {r} has length {len(row)}, expected {m}")
        require(all(x >= 0 for x in row), f"kernel {r} has a negative entry")
        require(sum(row) == kd, f"kernel {r} is not normalized")
        require(row == row[::-1], f"kernel {r} is not symmetric")
        kernels.append([Fraction(x, kd) for x in row])

    require(len(bn) == R, "wrong number of boundary vectors")
    for r, row in enumerate(bn):
        require(len(row) == n, f"boundary vector {r} has wrong length")

    def boundary_value(r: int, j: int) -> Fraction:
        if j >= n:
            return Fraction(1)
        return Fraction(bn[r][j], bd) + eta

    slacks: list[Fraction] = []
    for q in range(n + 1):
        cover = sum(
            weights[r] * kernels[r][i] * boundary_value(r, q + i)
            for r in range(R)
            for i in range(m)
        )
        slack = cover - 1
        require(slack >= 0, f"covering constraint q={q} fails by {-slack}")
        slacks.append(slack)

    a = m * sum(
        weights[r] * sum(p * p for p in kernels[r])
        for r in range(R)
    )
    rho = sum(
        weights[r] * sum(boundary_value(r, j) ** 2 for j in range(n))
        for r in range(R)
    )
    b = 1 + 2 * (rho / m - L)

    expected_a = Fraction(int(data["a_num"]), int(data["a_den"]))
    expected_b = Fraction(int(data["b_num"]), int(data["b_den"]))
    require(a == expected_a, f"computed a differs from stored a: {a} != {expected_a}")
    require(b == expected_b, f"computed b differs from stored b: {b} != {expected_b}")
    require(b > 0, "b must be positive")

    square_gap = target * target - a * b
    require(square_gap > 0, "target^2 is not strictly larger than a*b")

    positive = [(s, q) for q, s in enumerate(slacks) if s > 0]
    require(bool(positive), "certificate has no positive covering slack")
    least_slack, least_q = min(positive)
    equality_q = [q for q, s in enumerate(slacks) if s == 0]
    expected_least = Fraction(
        int(data["least_positive_num"]), int(data["least_positive_den"])
    )
    require(least_q == int(data["least_positive_q"]), "least-slack index mismatch")
    require(least_slack == expected_least, "least-slack value mismatch")

    return {
        "R": R,
        "m": m,
        "L": L,
        "n": n,
        "eta": eta,
        "target": target,
        "a": a,
        "b": b,
        "square_gap": square_gap,
        "least_slack": least_slack,
        "least_q": least_q,
        "equality_q": equality_q,
    }


def main() -> None:
    result = verify(load())
    getcontext().prec = 70
    a: Fraction = result["a"]
    b: Fraction = result["b"]
    gamma = (
        Decimal(a.numerator)
        * Decimal(b.numerator)
        / (Decimal(a.denominator) * Decimal(b.denominator))
    ).sqrt()

    print("PASS: all exact Fraction checks completed.")
    print(f"R={result['R']}, m={result['m']}, L={result['L']}")
    print(f"covering constraints checked: {result['n'] + 1}")
    print(f"eta = {result['eta']}")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"display-only sqrt(a*b) = {gamma}")
    print(
        "exact comparison: a*b < "
        f"({result['target'].numerator}/{result['target'].denominator})^2"
    )
    print(f"target^2-a*b = {result['square_gap']}")
    print(f"least positive slack: q={result['least_q']}, {result['least_slack']}")
    print(f"equality constraints: {result['equality_q']}")


if __name__ == "__main__":
    main()
