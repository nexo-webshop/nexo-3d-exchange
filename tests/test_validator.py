from pathlib import Path
import json
import zipfile

from n3x.validator import validate


def make_package(path: Path, manifest: dict) -> None:
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("manifest.json", json.dumps(manifest))


def test_valid_manifest(tmp_path: Path) -> None:
    path = tmp_path / "valid.n3x"
    make_package(path, {
        "format": "N3X",
        "version": "0.1",
        "generator": "test",
        "objects": [],
    })
    result = validate(str(path))
    assert result.valid is True
    assert result.errors == []


def test_invalid_format(tmp_path: Path) -> None:
    path = tmp_path / "invalid.n3x"
    make_package(path, {
        "format": "OTHER",
        "version": "0.1",
        "generator": "test",
        "objects": [],
    })
    result = validate(str(path))
    assert result.valid is False
    assert "format" in result.errors[0]
