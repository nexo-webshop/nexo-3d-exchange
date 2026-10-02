# N3X — Nexo 3D Exchange

**An open 3D exchange format and reference toolkit by Nexo Studios.**

N3X is designed as a portable container for 3D geometry, metadata, materials, previews and future manufacturing information.

## Project status

**Version:** 0.1.0  
**Specification:** N3X 0.1  
**Status:** Experimental / Alpha

N3X is currently a research and development project. It is **not yet a certified manufacturing standard**.

## Goals

N3X aims to provide one open container for multiple 3D ecosystems, including:

- 3MF
- STL
- OBJ
- PLY
- glTF
- GLB
- future CAD and manufacturing formats

The first release focuses on the container, manifest, metadata, safe reading, writing and validation.

## Repository

- `specification/` — N3X format documentation
- `src/n3x/` — Python reference implementation
- `tests/` — automated tests
- `examples/` — usage examples
- `docs/` — developer documentation

## Quick start

Requires Python 3.10 or newer.

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
python -m pytest
```

## Design principles

N3X is intended to be open, extensible, format-agnostic, safe to parse, suitable for software tooling, and useful beyond 3D printing.

## License

The N3X reference software is licensed under the Apache License 2.0. The specification and documentation may be licensed separately where indicated.

## Maintainer

Nexo Studios

**Building Tomorrow Together.**
