# Prompt: Extend upgrade to include tooling verification

After updating `AI_CURATOR_RECIPE.md`, review this repository’s CI and pre-commit configuration.

## 1. CI validation step

If missing, add a CI step that validates the recipe’s YAML front-matter and required headings:

```bash
python3 ./scripts/validate_recipe.py docs/curation/ai_curator_recipe.schema.json AI_CURATOR_RECIPE.md
```

Place this step after lint/type/test stages.

## 2. Pre-commit and linting configuration

If no `.pre-commit-config.yaml` exists, create one that runs Ruff, mypy, ADR index check, and fast tests as per the baseline. Also ensure curator docs are excluded from linting and type checks.

### Ruff configuration (`pyproject.toml`)

```toml
[tool.ruff]
# existing settings…
exclude = [
    "docs/curation/*",  # ignore curator baselines and prompts
]
```

### MyPy configuration (`mypy.ini` or `pyproject.toml`)

```ini
[mypy]
exclude = ^docs/curation/
```

Or, inside `pyproject.toml`:

```toml
[tool.mypy]
exclude = ["^docs/curation/"]
```

### Pre-commit configuration (`.pre-commit-config.yaml`)

Add an `exclude:` pattern at the root level so every hook skips curator docs automatically:

```yaml
exclude: ^docs/curation/
```

### Markdownlint configuration (optional)

If using markdownlint, add the following to `.markdownlint.yaml` or `.mdlrc`:

```yaml
MD013: false  # line length
MD033: false  # inline HTML allowed
MD041: false  # first line heading not required
MD002: false  # disable heading level checks for prompts
MD009: false  # allow trailing spaces

ignores:
  - docs/curation
```

## 3. Git include/exclude rules

Ensure that `docs/curation/` is **committed** and version-controlled:

```gitignore
# Always include curator documentation and prompts
!docs/curation/**
```

## 4. Output requirements

Output a summary of:
- Files changed or added
- Commands added to CI/pre-commit
- Any deferrals recorded in `CURATION_LOG.md`

---

**TL;DR setup summary**

| Tool | Config file | Add |
|------|--------------|-----|
| Git | `.gitignore` | `!docs/curation/**` (if docs ignored globally) |
| Ruff | `pyproject.toml` | `exclude = ["docs/curation/*"]` |
| MyPy | `mypy.ini` | `exclude = ^docs/curation/` |
| Pre-commit | `.pre-commit-config.yaml` | `exclude: ^docs/curation/` |
| Markdownlint | `.markdownlint.yaml` | `ignores: - docs/curation` |

---

**Goal:** every repository can self-verify that its AI curator documentation is valid, lint-free, and versioned while remaining untouched by runtime automation or type checking.
