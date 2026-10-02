"""PyInstaller entry point for the N3X Windows application."""

from n3x.validator import main


if __name__ == "__main__":
    raise SystemExit(main())
