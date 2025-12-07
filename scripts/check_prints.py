#!/usr/bin/env python3
import ast
import pathlib
import sys


def scan_file(path: pathlib.Path) -> int:
    errors = 0
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
        tree = ast.parse(text, filename=str(path))
    except SyntaxError:
        return 0

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if not isinstance(func, ast.Name) or func.id != "print":
            continue

        has_file_kw = any(isinstance(kw, ast.keyword) and kw.arg == "file" for kw in node.keywords)
        if has_file_kw:
            continue

        lineno = getattr(node, "lineno", 0)
        print(f"{path}:{lineno}: bare print() without file= detected", file=sys.stderr)
        errors += 1
    return errors


def scan_dir(root: pathlib.Path) -> int:
    errors = 0
    for p in root.rglob("*.py"):
        if "docs/curation" in p.as_posix() or ".venv" in p.as_posix():
            continue
        errors += scan_file(p)
    return errors


errors = 0
for root in [pathlib.Path("src"), pathlib.Path("scripts"), pathlib.Path("tests")]:
    if root.exists():
        errors += scan_dir(root)

if errors:
    sys.exit(1)
print("Print guard passed.", file=sys.stderr)
