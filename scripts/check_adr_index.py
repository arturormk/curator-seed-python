#!/usr/bin/env python3
import pathlib
import re
import sys

ADR_DIR = pathlib.Path("docs/adr")
INDEX = ADR_DIR / "README.md"
if not ADR_DIR.exists():
    print("docs/adr/ does not exist; nothing to check.", file=sys.stderr)
    sys.exit(0)

adrs = sorted([p for p in ADR_DIR.glob("[0-9][0-9][0-9][0-9]-*.md")])
if not adrs:
    print("No ADR files found under docs/adr/; nothing to index.", file=sys.stderr)
    sys.exit(0)

lines = ["# Architecture Decision Records\n", "\n"]
for p in adrs:
    num = p.name.split("-", 1)[0]
    title = re.sub(r"\.md$", "", p.name.split("-", 1)[1]).replace("-", " ").title()
    lines.append(f"- ADR-{num}: [{title}]({p.name})\n")

INDEX.parent.mkdir(parents=True, exist_ok=True)
current = INDEX.read_text() if INDEX.exists() else ""
content = "".join(lines)
if current != content:
    INDEX.write_text(content)
    print("ADR index updated. Please stage docs/adr/README.md.", file=sys.stderr)
    sys.exit(1)
print("ADR index up-to-date.")
