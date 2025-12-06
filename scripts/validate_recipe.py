#!/usr/bin/env python3
import sys
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


def _split_frontmatter_and_body(md_path: Path) -> tuple[dict, str]:
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"{md_path} does not start with YAML frontmatter ('---').")

    first_sep = text.find("\n---", 3)
    if first_sep == -1:
        raise ValueError(f"{md_path} frontmatter block not properly terminated with '---'.")

    frontmatter_block = text[0:first_sep]
    body = text[first_sep + len("\n---") :].lstrip("\n")

    frontmatter = yaml.safe_load(frontmatter_block.lstrip("-\n")) or {}
    return frontmatter, body


def _extract_headings(markdown_body: str) -> list[str]:
    """Return the text of headings that start with '## ' only."""
    headings: list[str] = []
    for line in markdown_body.splitlines():
        # we care only about second-level headings, literally starting with "## "
        if line.startswith("## "):
            heading_text = line[len("## ") :].strip()
            if heading_text:
                headings.append(heading_text)
    return headings


def _check_heading_order(markdown_body: str, expected_order: list[str]) -> list[str]:
    """
    Check that:
      - for each expected heading text E in expected_order,
      - there is a corresponding '## ' heading whose text CONTAINS E,
      - and they appear in the same order.

    Extra headings are allowed; mismatch in order or missing headings is an error.
    """
    errors: list[str] = []
    actual = _extract_headings(markdown_body)

    # Greedy left-to-right match where each expected string must appear
    # as a substring of some heading, in order.
    idx = 0
    matched: list[str] = []
    for expected in expected_order:
        found_at = None
        while idx < len(actual):
            if expected in actual[idx]:
                found_at = idx
                matched.append(actual[idx])
                idx += 1
                break
            idx += 1
        if found_at is None:
            errors.append(
                f"Missing or out-of-order heading containing: {expected!r}.\n"
                f"  All '## ' headings: {actual}"
            )
            # stop early; further checks won't be meaningful
            return errors

    # Optional: if you want to ensure there are no unexpected extra headings
    # or stricter equality, you could add more checks here.
    return errors


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if len(argv) != 2:
        print("Usage: validate_recipe SCHEMA_JSON_PATH AI_CURATOR_RECIPE.md", file=sys.stderr)
        return 1

    schema_path = Path(argv[0])
    recipe_path = Path(argv[1])

    if not schema_path.is_file():
        print(f"Schema file not found: {schema_path}", file=sys.stderr)
        return 1
    if not recipe_path.is_file():
        print(f"Markdown file not found: {recipe_path}", file=sys.stderr)
        return 1

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    frontmatter, body = _split_frontmatter_and_body(recipe_path)

    # JSON Schema: front-matter
    validator = Draft202012Validator(schema)
    schema_errors = sorted(validator.iter_errors(frontmatter), key=lambda e: e.path)

    # Heading order from schema definitions.required_headings.enum
    required_headings = (
        schema.get("definitions", {})
        .get("required_headings", {})
        .get("enum", [])
    )
    heading_errors: list[str] = []
    if required_headings:
        heading_errors = _check_heading_order(body, required_headings)

    if not schema_errors and not heading_errors:
        print(f"{recipe_path} is valid according to {schema_path} and heading rules", file=sys.stderr)
        return 0

    print(f"{recipe_path} is INVALID:", file=sys.stderr)
    for err in schema_errors:
        loc = ".".join(map(str, err.path)) or "<root>"
        print(f" - schema:{loc}: {err.message}", file=sys.stderr)
    for msg in heading_errors:
        print(f" - heading: {msg}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
