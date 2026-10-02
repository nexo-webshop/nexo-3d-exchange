# N3X Format Specification

**N3X — Nexo 3D Exchange**  
Specification version: **0.1**

## Purpose

N3X is an open container format for exchanging 3D assets and related information. It is designed to hold model geometry, metadata, previews, materials, and future manufacturing information in one portable package.

N3X is intentionally format-agnostic. Source assets may originate from formats such as STL, OBJ, PLY, 3MF, glTF, and GLB.

## File extension

N3X files use the `.n3x` extension.

## Container

An N3X file is a ZIP-compatible container. The package MUST contain `manifest.json`.

Recommended directories:
- `model/`
- `materials/`
- `textures/`
- `previews/`
- `metadata/`
- `manufacturing/`
- `source/`

Only `manifest.json` is mandatory in N3X 0.1.

## Manifest

Minimum structure:

```json
{
  "format": "N3X",
  "version": "0.1",
  "generator": "Nexo 3D Exchange",
  "objects": []
}
```

Required fields:
- `format`: MUST be `"N3X"`
- `version`: N3X specification version
- `generator`: software that created the package
- `objects`: array describing contained 3D objects

## Geometry

Geometry SHOULD be stored under `model/`. The manifest identifies the encoding.

The reference toolkit is intended to support interchange with STL, OBJ, PLY, 3MF, glTF and GLB.

## Metadata

Metadata MAY contain creator, application, creation date, license, source format, source filename, units and coordinate system.

## Security

N3X readers MUST treat packages as untrusted input. Readers SHOULD reject path traversal, unsafe absolute paths, duplicate required manifest entries, invalid JSON, and unreasonable archive expansion.

## Compatibility

Future versions MUST preserve format/version identification. Unknown optional sections SHOULD be ignored by readers that do not understand them.

## Status

N3X 0.1 is experimental and is not a production or manufacturing certification standard.
