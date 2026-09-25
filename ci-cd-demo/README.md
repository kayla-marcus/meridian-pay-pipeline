# mathutils

A deliberately tiny Python project used as a base for a CI/CD and
supply chain security assignment. No CI/CD pipeline is set up yet —
this is just the application and its tests.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -e .
```

## Run the tests

```bash
pytest
```

## Project layout

```
ci-cd-demo/
├── src/mathutils/
│   ├── __init__.py       # exposes the package's public functions
│   └── operations.py     # the actual application logic
├── tests/
│   └── test_operations.py  # unit tests for operations.py
├── pyproject.toml        # package metadata + build system config
├── requirements.txt      # pinned runtime dependencies (none yet)
├── requirements-dev.txt  # pinned dev/test dependencies (pytest)
├── .gitignore
└── README.md
```
