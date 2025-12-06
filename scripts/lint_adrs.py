#!/usr/bin/env python3
import pathlib
import re
import sys

ADR_DIR = pathlib.Path("docs/adr")
if not ADR_DIR.exists():
    print("docs/adr/ does not exist; nothing to lint.", file=sys.stderr)
    sys.exit(0)

errors = 0
for p in sorted(ADR_DIR.glob("[0-9][0-9][0-9][0-9]-*.md")):
    text = p.read_text(encoding="utf-8")
    required = ["## Context", "## Decision", "## Consequences"]
    for h in required:
        if h not in text:
            print(f"{p}: missing heading '{h}'", file=sys.stderr)
            errors += 1

if errors:
    sys.exit(1)
print("ADR lint passed.", file=sys.stderr)
