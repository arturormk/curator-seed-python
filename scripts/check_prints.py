#!/usr/bin/env python3
import pathlib
import sys

def scan_dir(root: pathlib.Path) -> int:
    errors = 0
    for p in root.rglob("*.py"):
        # Skip docs/curation and virtualenvs
        if "docs/curation" in p.as_posix() or ".venv" in p.as_posix():
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        for i, line in enumerate(text.splitlines(), start=1):
            if "print(" in line and "file=" not in line:
                print(f"{p}:{i}: bare print() without file= detected", file=sys.stderr)
                errors += 1
    return errors

errors = 0
for root in [pathlib.Path("src"), pathlib.Path("scripts"), pathlib.Path("tests")]:
    if root.exists():
        errors += scan_dir(root)

if errors:
    sys.exit(1)
print("Print guard passed.", file=sys.stderr)
