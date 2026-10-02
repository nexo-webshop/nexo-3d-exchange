"""Safe reader for N3X containers."""

from __future__ import annotations

import json
import zipfile
from pathlib import PurePosixPath
from typing import Any

from .validator import validate


class N3XError(Exception):
    """Raised when an N3X package cannot be read safely."""


def _safe_member(name: str) -> bool:
    path = PurePosixPath(name)
    return not path.is_absolute() and ".." not in path.parts and "\\" not in name


def read(path: str) -> dict[str, Any]:
    """Read and validate an N3X package."""
    result = validate(path)
    if not result.valid:
        raise N3XError("; ".join(result.errors))

    with zipfile.ZipFile(path, "r") as archive:
        members = archive.namelist()
        if any(not _safe_member(name) for name in members):
            raise N3XError("Unsafe path found in N3X archive.")

        try:
            manifest = json.loads(archive.read("manifest.json").decode("utf-8"))
        except (KeyError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise N3XError("Invalid manifest.json.") from exc

    return {"manifest": manifest, "members": members}
