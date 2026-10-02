from pathlib import Path

from n3x.cli import main


def test_cli_validate(monkeypatch, tmp_path: Path, capsys) -> None:
    path = tmp_path / "test.n3x"
    from n3x import write

    write(str(path))
    monkeypatch.setattr("sys.argv", ["n3x-validate", str(path)])
    assert main() == 0
    assert "VALID" in capsys.readouterr().out
