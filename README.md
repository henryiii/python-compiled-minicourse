# Mixing Compiled Code and Python
## Princeton mini-course
### By Henry Schreiner

## Installation

#### Adroit


#### Local install:

If you are reading this at least 10 minutes before the course starts or you have anaconda
or miniconda installed, you will probably be best off installing miniconda.
This way you will keep local edits and will have an environment to play with.

Get the repository:

```bash
git clone https://github.com/henryiii/python-performance-minicourse.git
cd python-performance-minicourse
```

Download and install
[miniconda](https://docs.conda.io/en/latest/miniconda.html). On macOS with
homebrew, just run `brew cask install miniconda` [(see my
recommendations)](https://iscinumpy.gitlab.io/post/setup-a-new-mac/).

Run:

```bash
conda env create
```

from this directory. This will create an environment `performance-minicourse`. To use:

```bash
conda activate compiled--minicourse
./check.py # Check to see if you've installed this correctly
jupyter lab
```

And, to disable:

```bash
conda deactivate
```

or restart your terminal.


> If you want to add a package, modify `environment.yml` then run:
> 
> ```bash
> conda env update
> ```


## Lessons


Class participants: please complete the survey that will be posted.
