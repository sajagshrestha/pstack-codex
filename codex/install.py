#!/usr/bin/env python3
"""Install the self-contained skill without replacing an existing skill."""

import argparse
from pathlib import Path
import shutil
import tempfile


SOURCE = Path(__file__).resolve().parent / "skills" / "poteto-mode"


def snapshot(root):
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }


def install(destination):
    destination = Path(destination).expanduser()
    target = destination / SOURCE.name
    if target.is_symlink():
        raise FileExistsError(f"Refusing to replace symlink: {target}")
    if target.exists():
        if target.is_dir() and not any(p.is_symlink() for p in target.rglob("*")):
            if snapshot(target) == snapshot(SOURCE):
                return target, False
        raise FileExistsError(f"Existing skill differs; preserve or move it first: {target}")

    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".pstack-install-", dir=destination) as staging:
        staged = Path(staging) / SOURCE.name
        shutil.copytree(SOURCE, staged)
        # mkdir reserves the destination without overwriting a concurrent install.
        target.mkdir()
        # On failure, preserve partial files; a retry refuses to overwrite them.
        for item in staged.iterdir():
            shutil.move(str(item), target / item.name)
    return target, True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument("--project", type=Path, help="Install into PROJECT/.agents/skills")
    scope.add_argument("--user", action="store_true", help="Install into ~/.agents/skills")
    args = parser.parse_args()
    destination = (
        args.project.resolve() / ".agents" / "skills"
        if args.project is not None
        else Path.home() / ".agents" / "skills"
    )
    try:
        target, created = install(destination)
    except (OSError, shutil.Error) as error:
        parser.exit(1, f"Installation failed: {error}\n")
    print(f"{'Installed' if created else 'Already installed'}: {target}")


if __name__ == "__main__":
    main()
