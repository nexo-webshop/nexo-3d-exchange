# N3X Container Structure

An N3X package is a ZIP-compatible archive.

Recommended layout:

```text
model.n3x
├── manifest.json
├── model/
├── materials/
├── textures/
├── previews/
├── metadata/
├── manufacturing/
└── source/
```

Rules:
1. Paths use forward slashes.
2. Paths MUST be relative to the package root.
3. Absolute paths are forbidden.
4. Parent traversal such as `../` is forbidden.
5. File names are case-sensitive.
6. Text files SHOULD use UTF-8.
7. Readers SHOULD protect against excessive archive expansion.

The container is extensible so later specifications can add manufacturing, animation, CAD, scanning, or other asset data.
