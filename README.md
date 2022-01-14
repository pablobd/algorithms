# Algorithms
Fun with algorithms and data structures

![Python Versions Supported](https://img.shields.io/badge/python-3.8+-blue.svg)
[![Pre-Commit](https://github.com/pablobd/algorithms/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/pablobd/algorithms/actions/workflows/pre-commit.yaml)
[![Test Suite](https://github.com/pablobd/algorithms/actions/workflows/test-suite.yaml/badge.svg)](https://github.com/pablobd/algorithms/actions/workflows/test-suite.yaml)
[![codecov](https://codecov.io/gh/pablobd/algorithms/branch/main/graph/badge.svg?token=XWQC9FZAD9)](https://codecov.io/gh/pablobd/algorithms)
[![CodeQL (vulnerabilities)](https://github.com/pablobd/algorithms/actions/workflows/code-vulnerabilities.yaml/badge.svg)](https://github.com/pablobd/algorithms/actions/workflows/code-vulnerabilities.yaml)

---

## Project Objective

Have fun and learn about algorithmics and data structures.


## Local Development

Though, it's not a requirement, we encourage the usage of `pyenv`, a simple Python version management program, to select the right Python version (>=3.8,<4.0). You can follow the [Windows](https://github.com/pyenv-win/pyenv-win#installation) or the [macOS instructions](https://github.com/pyenv/pyenv#installation), both found in the official `pyenv` repository. Installation on Linux based systems is not so straightforward but it is also doable.

Next, clone the repository locally and get the right python version,

```
> pyenv install 3.9.1
> cd algorithms
> pyenv local 3.9.1
```

You must have a `.python-version` file in the root project directory, specifying the Python version to be used on the project.

Next, install in your computer poetry, the awesome python dependency management software. You can follow the official [instructions](https://python-poetry.org/docs/#installation).

There are some settings, that can be changed to customize your experience with poetry, see [here](https://python-poetry.org/docs/configuration/#available-settings). To make it look more similar to `venv`, you can make poetry install a local virtual environment in the project folder. To change this setting and install the local environment, run in the shell the following command:

```
> poetry config virtualenv.in-project true
> poetry install
```

Now, you must have a `.venv` directory in the root folder of the project with the development environment. Next, activate the environment and install the git hook:

```
> source .venv/bin/activate
> pre-commit install
```

Now, you should be ready to rock.

## Contributors

If you want to collaborate because you believe you can improve some algorithm and make it faster, you are more than welcome. Just open a pull request to the main branch. Before merging, it is required that all continuous integration pipelines pass:

- CodeQL: code vulnerabilities
- Pre-Commit: linting and formatting (black, isort, etc.)
- Test-Suite: unit tests, stress tests, performance tests, etc.
- Coverage: at least a coverage of 98%

And please, provide feedback and have fun!
