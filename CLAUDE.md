# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Teaching material for the Princeton mini-course "Mixing Compiled Code and Python". The
deliverable is a set of Jupyter notebooks, one per binding technology, run in order by
students. There is no library and no package.

## Commands

```bash
pixi run check          # verify the environment
pixi run lab            # start JupyterLab
pixi run -e test test   # execute every notebook (what CI does)
prek -a --quiet         # lint (ruff, nbstripout, codespell, prettier)
```

`environment.yml` describes the same conda-forge environment for Binder and for people
who already use conda; keep it in sync with `pixi.toml`.

To run one lesson: `pixi run -e test pytest --nbmake 04-cython/04-cython.ipynb`.

## Structure

Numbered directories are the lesson order, and the story builds up in that order:

- `00-intro.ipynb` — motivation and topic list
- `01-shared-objects` — ctypes and CFFI against a plain `.so`; no Python C API yet
- `02-cpython` — the same `square` written by hand against the CPython C API
- `03-swig`, `04-cython`, `05-pybind`, `06-nanobind`, `07-cppyy` — the binding tools,
  each mostly re-binding the same `Simple` class from `SimpleClass.hpp` so students can
  compare
- `05-pybind/05b-pybind.ipynb` — the one large realistic example: binding Minuit2
  (a vendored standalone copy of the ROOT fitter, in `05-pybind/minuit2/`) with CMake,
  then making it pip-installable with scikit-build-core

`SimpleClass.hpp` is deliberately duplicated by `%%writefile` in each lesson rather than
shared, so each notebook is self-contained. Keep it that way. Module names differ per
lesson (`pysimple`, `cysimple`, ...) because the notebooks `pip install` into the shared
environment, where identical names would collide.

## Notebook conventions

- Notebooks write their own source files with `%%writefile` and build them from `!` shell
  cells. Everything they produce is generated and gitignored — never commit it. The
  `.gitignore` ignores broad patterns (`*.toml`, `*.hpp`, `*CMake*`, ...), so a genuinely
  new tracked file at the root may need a `!negation` entry.
- Builds go through PEP 517: each lesson writes a `pyproject.toml` and installs with
  `!{sys.executable} -m pip install --no-build-isolation .`. `sys.executable` matters —
  shell cells do not inherit the kernel's environment. Do not reintroduce
  `python setup.py build_ext --inplace`.
- macOS needs `SDKROOT` set from `xcrun --show-sdk-path`, which the first code cell of
  each lesson does. That replaced hardcoded `CPATH`/`LIBRARY_PATH` paths into `Xcode.app`.
- `nbstripout` removes all outputs on commit, so committed notebooks have no outputs.
  Do not hand-write outputs into the JSON.
- Cells carry `slideshow` metadata for RISE; edit notebooks in place rather than
  regenerating them, or that metadata is lost.

## Style

- `prek -a --quiet` for linting; ruff formats and lints code cells, configured in
  `ruff.toml`. The `%%cython` magic defines names ruff cannot see, hence the F821
  per-file ignore.
- A local pre-commit hook rejects mis-capitalized spellings of pybind11, nanobind, NumPy,
  CMake, ccache, GitHub, pytest, and scikit-build.
- `05-pybind/minuit2/` is vendored upstream code (LGPL), excluded from codespell,
  prettier, and ruff. The only local change is `cmake_minimum_required`, raised to
  `3.15...4.0` so CMake 4 will still configure it.
