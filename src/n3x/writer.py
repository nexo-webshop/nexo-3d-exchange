"""N3X package writer."""

from __future__ import annotations

import json
import zipfile
from pathlib import Path
from typing import Any


def write(
    path: str,
    *,
    objects: list[dict[str, Any]] | None = None,
    generator: str = "Nexo 3D Exchange",
    version: str = "0.1",
    files: dict[str, bytes] | None = None,
) -> None:
    """Create a minimal N3X package."""
    objects = objects or []
    files = files or {}

    manifest = {
        "format": "N3X",
        "version": version,
        "generator": generator,
        "objects": objects,
    }

    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(
            "manifest.json",
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        )

        for member, content in files.items():
            normalized = Path(member).as_posix()
            if normalized.startswith("/") or ".." in Path(normalized).parts:
                raise ValueError(f"Unsafe package path: {member}")
            if normalized == "manifest.json":
                raise ValueError("manifest.json is generated automatically.")
            archive.writestr(normalized, content)
