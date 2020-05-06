#!/usr/bin/env python3

import sys

try:
    assert sys.version_info >= (3, 8), "Python should be 3.8+"

    import numba
    import pybind11
except (AssertionError, ImportError) as e:
    print("Environment not setup property! Use conda, see readme.")
    print("Maybe `conda activate compiled-minicourse` is missing?")
    print(e)
    sys.exit(1)

print("Environment appears correct, congratulations!")
