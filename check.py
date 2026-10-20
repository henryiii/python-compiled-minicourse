#!/usr/bin/env python3

"""Check that the course environment is complete."""

import importlib.util
import shutil
import sys

MODULES = ["cffi", "cppyy", "Cython", "nanobind", "numba", "numpy", "pybind11"]
PROGRAMS = ["cmake", "swig"]

if sys.platform.startswith("win"):
    MODULES.remove("cppyy")


def main() -> int:
    missing = [m for m in MODULES if importlib.util.find_spec(m) is None]
    missing += [p for p in PROGRAMS if shutil.which(p) is None]

    if sys.version_info < (3, 11):
        print(f"Python should be 3.11+, you have {sys.version.split()[0]}")
        missing.append("python")

    if missing:
        print("Environment not set up properly! See the readme.")
        print("Missing:", ", ".join(missing))
        print("Did you forget `pixi shell` or `conda activate compiled-minicourse`?")
        return 1

    print("Environment appears correct, congratulations!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
