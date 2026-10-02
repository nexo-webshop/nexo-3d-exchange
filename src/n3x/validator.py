"""N3X package validation and CLI."""

from __future__ import annotations

import argparse
import json
import zipfile
from dataclasses import dataclass, field
from pathlib import PurePosixPath


@dataclass
class ValidationResult:
    valid: bool
    errors: list[str] = field(default_factory=list)


def _safe_path(name: str) -> bool:
    path = PurePosixPath(name)
    return not path.is_absolute() and ".." not in path.parts and "\\" not in name


def validate(path: str) -> ValidationResult:
    """Validate the structural requirements of an N3X 0.1 package."""
    errors: list[str] = []

    try:
        with zipfile.ZipFile(path, "r") as archive:
            names = archive.namelist()

            if names.count("manifest.json") != 1:
                errors.append("Package must contain exactly one manifest.json.")

            if any(not _safe_path(name) for name in names):
                errors.append("Package contains unsafe archive paths.")

            if not errors:
                try:
                    manifest = json.loads(
                        archive.read("manifest.json").decode("utf-8")
                    )
                except (UnicodeDecodeError, json.JSONDecodeError):
                    errors.append("manifest.json must be valid UTF-8 JSON.")
                else:
                    if not isinstance(manifest, dict):
                        errors.append("manifest.json root must be an object.")
                    else:
                        if manifest.get("format") != "N3X":
                            errors.append('manifest.json "format" must be "N3X".')
                        if not isinstance(manifest.get("version"), str):
                            errors.append('manifest.json "version" must be a string.')
                        if not isinstance(manifest.get("generator"), str):
                            errors.append('manifest.json "generator" must be a string.')
                        if not isinstance(manifest.get("objects"), list):
                            errors.append('manifest.json "objects" must be an array.')

    except (FileNotFoundError, zipfile.BadZipFile, OSError) as exc:
        errors.append(f"Unable to open N3X package: {exc}")

    return ValidationResult(valid=not errors, errors=errors)


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="n3x-validate",
        description="Validate an N3X package.",
    )
    parser.add_argument("package", help="Path to the .n3x package")
    args = parser.parse_args()

    result = validate(args.package)

    if result.valid:
        print(f"VALID: {args.package}")
        return 0

    print(f"INVALID: {args.package}")
    for error in result.errors:
        print(f"- {error}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
