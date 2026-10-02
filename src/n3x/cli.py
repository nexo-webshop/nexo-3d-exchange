"""Command-line interface for N3X."""

from __future__ import annotations

import argparse
import sys

from . import __version__, read, validate, write


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="n3x",
        description="Nexo 3D Exchange command-line toolkit.",
    )
    parser.add_argument("--version", action="version", version=__version__)
    sub = parser.add_subparsers(dest="command", required=True)

    validate_parser = sub.add_parser("validate", help="Validate an N3X package.")
    validate_parser.add_argument("file")

    inspect_parser = sub.add_parser("inspect", help="Inspect an N3X package.")
    inspect_parser.add_argument("file")

    create_parser = sub.add_parser("create", help="Create a minimal N3X package.")
    create_parser.add_argument("file")

    return parser


def main() -> int:
    args = build_parser().parse_args()

    if args.command == "validate":
        result = validate(args.file)
        if result.valid:
            print("VALID: N3X package")
            return 0
        for error in result.errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if args.command == "inspect":
        package = read(args.file)
        print(f"Format: {package['manifest']['format']}")
        print(f"Version: {package['manifest']['version']}")
        print(f"Generator: {package['manifest']['generator']}")
        print(f"Objects: {len(package['manifest']['objects'])}")
        print("Members:")
        for member in package["members"]:
            print(f"  {member}")
        return 0

    if args.command == "create":
        write(args.file)
        print(f"Created: {args.file}")
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
