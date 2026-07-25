#!/usr/bin/env python3
"""Run the repository's exact reproduction suite."""
from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

CORE = [
    "certificates/m80/verify_fraction.py",
    "checkers/check_cyclic_defect.py",
    "checkers/check_carry_partition.py",
    "checkers/check_translate_incidence.py",
    "checkers/check_factorial_moment_plateau.py",
]

SYMPY = [
    "certificates/m80/verify_sympy.py",
    "checkers/check_delay_profile_symbolic.py",
    "checkers/check_C_derivation_symbolic.py",
    "checkers/check_decomposition19_symbolic.py",
    "checkers/check_pairwise_pseudo.py",
    "checkers/check_rank_aggregate_plateau.py",
    "checkers/check_spectral_selector.py",
]


def run(relative: str) -> None:
    path = ROOT / relative
    if not path.is_file():
        raise SystemExit(f"missing artifact: {relative}")
    print(f"\n=== {relative} ===", flush=True)
    subprocess.run([sys.executable, str(path)], cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--core", action="store_true", help="standard-library checks")
    group.add_argument("--all", action="store_true", help="core plus SymPy checks")
    args = parser.parse_args()

    for item in CORE:
        run(item)
    if args.all:
        try:
            import sympy  # noqa: F401
        except ImportError as exc:
            raise SystemExit("SymPy is required for --all; install requirements.txt") from exc
        for item in SYMPY:
            run(item)

    print("\nPASS: requested reproduction suite completed.")


if __name__ == "__main__":
    main()
