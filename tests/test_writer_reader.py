from pathlib import Path

from n3x import read, write


def test_write_and_read(tmp_path: Path) -> None:
    path = tmp_path / "model.n3x"
    write(
        str(path),
        objects=[{"id": "cube", "format": "stl"}],
        files={"model/cube.stl": b"example"},
    )
    package = read(str(path))
    assert package["manifest"]["format"] == "N3X"
    assert "model/cube.stl" in package["members"]
