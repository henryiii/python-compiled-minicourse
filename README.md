# Mixing Compiled Code and Python

## Princeton mini-course

### By Henry Schreiner

## Installation

#### Binder:

In the minicourse, if you haven't prepared beforehand, please use this link to run online via Binder: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/henryiii/python-compiled-minicourse/master?urlpath=lab)

#### Adroit

See class.

#### Local install:

Get the repository:

```bash
git clone https://github.com/henryiii/python-compiled-minicourse.git
cd python-compiled-minicourse
```

The lessons need compilers, CMake, SWIG, and Cling, so the environment comes from
conda-forge. The quickest way to get it is [pixi](https://pixi.sh), which needs no
other setup and keeps everything inside this directory:

```bash
pixi run check   # Check that the environment is complete
pixi run lab     # Start JupyterLab
```

Pixi installs the environment on the first run. Use `pixi shell` if you want an
activated shell, and `exit` to leave it.

<details><summary>Using conda instead</summary>

If you already have conda or miniforge, `environment.yml` describes the same
environment:

```bash
conda env create
conda activate compiled-minicourse
./check.py
jupyter lab
```

To add a package, modify `environment.yml`, then run `conda env update`.

</details>

## Lessons

Run the notebooks in order:

| Lesson                                   | Topic                                           |
| ---------------------------------------- | ----------------------------------------------- |
| [00-intro](./00-intro.ipynb)             | Why and when to compile                         |
| [01-shared-objects](./01-shared-objects) | ctypes and CFFI: calling a plain shared library |
| [02-cpython](./02-cpython)               | The CPython C API by hand, Stable ABI           |
| [03-swig](./03-swig)                     | SWIG: bindings for many languages at once       |
| [04-cython](./04-cython)                 | Cython: Python and C in one language            |
| [05-pybind](./05-pybind)                 | pybind11, including a full Minuit2 binding      |
| [06-nanobind](./06-nanobind)             | nanobind: pybind11's smaller, faster successor  |
| [07-cppyy](./07-cppyy)                   | cppyy: bindings from a C++ interpreter          |

Class participants: please complete the survey that will be posted.

## Development

Linting uses [pre-commit](https://pre-commit.com):

```bash
pipx run pre-commit run -a
```

CI runs the linters and executes every notebook. To do that locally:

```bash
pixi run -e test test
```
