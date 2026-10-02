# Getting Started

## Development setup

N3X is currently developed as a Python reference toolkit.

Create a virtual environment:

```bash
python -m venv .venv
```

Install the project:

```bash
python -m pip install -e ".[dev]"
```

Run tests:

```bash
python -m pytest
```

## Current status

N3X 0.1 is experimental. The first implementation focuses on the package container, manifest, safe paths, reading, writing and structural validation.

Format conversion and 3D rendering are future components.
