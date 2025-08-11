# Building Large Projects

## General
Large python projects can be extremely powerful, 
but they must be organized a certain way to work properly.

A project should always start with a root folder and other 
folders and files will be housed inside the root folder.

There are special ``.py`` files that python will use to do
different things such as ``__init__.py`` and ``__main__.py``.

## Vocabulary

* **Module:** .py file
* **Package:** a folder with ``__init__.py`` file in it. This will have code that can be imported.
* **Library:** One or more packages grouped together and distributed via PyPI. Built to
be reusable blocks of code.

## The Classic Structure (Double Name)

The classic method to package a project is with the double name method.
This uses a root folder to hold all the metadata, README, LICENSE, pyproject, etc. and then 
a subfolder that has the project code. Below is an example:
```
pandas/               # repo root
├─ pyproject.toml / setup.py / setup.cfg
├─ README.md
├─ LICENSE
├─ pandas/            # actual Python package (import name = pandas)
│  ├─ __init__.py
│  ├─ core/
│  ├─ io/
│  ├─ util/
│  └─ ...
├─ doc/               # documentation
├─ tests/             # test suite
└─ ...
```

This lets us run things like:
```bash
python -m pandas

python -m pandas.core
```

This setup gives the least amount of friction, is well established, and 
gives good organization. The downside is that it can cause mask import mistakes
where the script runs in dev but not in prod once you pip install it.

You can avoid these issues by doing ``pip install -e .`` which installs your package
in edit mode. Edit mode means you can make changes to the installed package
and it will hot reload. 

## The Workflow

1. Build your project. 
2. Install your project ``pip install -e .``
3. In ``pyproject.toml`` add:
```toml
[project.scripts]
package_name = "module:callable"
# this creates a command line command. Replace with a command and path to what gets executed.
```
4. Call like ``package_name`` if you want a terminal command.

## A More Modern System

## Goals of a good structure

* **Separation of concerns:** isolate domain logic, I/O, and interfaces.
* **Testability & maintainability:** easy to unit test and refactor.
* **Distributable:** buildable wheel, clean dependency metadata.
* **Usability:** clear public API, stable CLI, sensible configuration.

## Canonical layout (src/ structure)

```
your-project/
├─ pyproject.toml
├─ README.md
├─ LICENSE
├─ .gitignore
├─ src/
│  └─ your_package/
│     ├─ __init__.py
│     ├─ __main__.py           # optional: `python -m your_package`
│     ├─ cli/                  # CLI commands
│     │  └─ __init__.py
│     ├─ core/                 # domain logic (pure, testable)
│     │  ├─ models.py
│     │  ├─ services.py
│     │  └─ rules.py
│     ├─ adapters/             # I/O boundaries (DB, HTTP, FS, APIs)
│     │  ├─ db.py
│     │  ├─ http.py
│     │  └─ storage.py
│     ├─ app/                  # application orchestration/wiring
│     │  ├─ config.py
│     │  ├─ logging.py
│     │  └─ container.py       # dependency wiring/injection
│     └─ utils/                # cross-cutting helpers
│        └─ time.py
├─ tests/
│  ├─ conftest.py
│  ├─ unit/
│  └─ integration/
└─ examples/                    # optional usage demos / notebooks
```

Why `src/`? It prevents tests from accidentally importing 
your **working directory** instead of the installed package, 
catching packaging/import mistakes early.

## pyproject.toml (modern packaging)

Use PEP 621 metadata; pick a backend (e.g., Hatchling, Setuptools).

```toml
[build-system]
requires = ["hatchling>=1.25"]
build-backend = "hatchling.build"

[project]
name = "your-project"
version = "0.1.0"
description = "Does X"
readme = "README.md"
requires-python = ">=3.10"
license = { file = "LICENSE" }
authors = [{ name = "You" }]
dependencies = [
  "requests>=2.32",
]

[project.optional-dependencies]
dev = ["pytest", "mypy", "ruff", "black", "pytest-cov"]

[project.scripts]                 # creates console commands on install
your-cli = "your_package.cli:main"

[tool.hatch.build.targets.wheel]
packages = ["src/your_package"]
```

* **\[project.scripts]** wires a **console script** (entry point). It points to a callable (e.g., `def main(): ...`).
* Prefer **runtime deps** under `[project.dependencies]` and dev tools under an optional extra (e.g., `pip install .[dev]`).

## Public API design

* Use `__init__.py` to **re-export** the small, stable surface you commit to:

  ```python
  # src/your_package/__init__.py
  from .core.models import Thing
  from .core.services import Service

  __all__ = ["Thing", "Service"]
  ```
* Keep internal modules private-ish (don’t re-export them) so refactors don’t break users.

## Layers that scale

* **core/**: pure business rules, no network/filesystem. Most unit tests live here.
* **adapters/**: concrete I/O implementations (Postgres, S3, HTTP, etc.).
* **app/** (or **service/**): composition, config, logging, dependency injection, runtime wiring.
* **cli/**: thin commands that call into **app/** (don’t bury logic in click/argparse handlers).

This “ports & adapters” (hexagonal) approach keeps logic decoupled from I/O so you can swap adapters (e.g., SQLite → Postgres) or test with fakes.

## Configuration & secrets

* Read config **from environment** first, with optional `.env` during development.
* Centralize in `app/config.py`:

  ```python
  from dataclasses import dataclass
  import os

  @dataclass
  class Settings:
      db_url: str = os.environ.get("APP_DB_URL", "sqlite:///local.db")
      log_level: str = os.environ.get("APP_LOG_LEVEL", "INFO")

  settings = Settings()
  ```
* Avoid global state; pass `settings` into your app wiring or use a small container.

## Logging

* Configure once in `app/logging.py` and call it from your CLI entry:

  ```python
  import logging, sys

  def setup(level: str = "INFO"):
      logging.basicConfig(
          level=level,
          format="%(asctime)s %(levelname)s %(name)s: %(message)s",
          stream=sys.stdout,
      )
  ```

## Testing strategy

* **pytest** with `tests/unit` for pure logic and `tests/integration` for external systems.
* Use fakes or fixtures for adapters; avoid hitting the network in unit tests.
* Keep test imports identical to users: `from your_package import Service`.

## Types, linting, formatting

* **Type hints** everywhere; enforce with **mypy** (or pyright).
* **ruff** for lint; **black** for formatting.
* Run in CI (pre-commit is nice).

## Versioning & metadata

* Use **SemVer**. For libs exposed to others, keep breaking changes behind major bumps.
* Store version in one place (pyproject or `your_package/__init__.py`) and, if helpful, use tools that auto-bump and tag (hatch, setuptools-scm).

## Data and resources

* Keep runtime data in the package only if truly needed; prefer external files or embedded resources loaded via `importlib.resources` rather than relative paths.
* For large assets, ship them separately or fetch at runtime.

## CLI vs library

* Treat the **package as a library** first; keep the CLI thin. That makes automation and testing easier and lets others use your code programmatically.

## Common pitfalls to avoid

* **Logic in scripts**: move code out of `if __name__ == "__main__":` into functions/classes.
* **Tight coupling to I/O**: keep core pure; push side effects to adapters.
* **Leaky imports**: don’t rely on import side effects; be explicit.
* **Messy init**: avoid heavy work at import time; initialize in `main()` / app wiring.

## Minimal example for a CLI

```python
# src/your_package/cli.py
import argparse
from .app.logging import setup as setup_logging
from .app.config import settings
from .core.services import Service

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--log-level", default=settings.log_level)
    args = parser.parse_args()

    setup_logging(args.log_level)
    Service().run()
```

## Build, install, run

```bash
# dev install
pip install -e ".[dev]"

# run tests/type checks
pytest -q
mypy src

# build a wheel/sdist
python -m build    # or hatch build

# use the CLI after install
your-cli --help
```

---
