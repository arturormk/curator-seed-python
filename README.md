# curator-seed

A minimal, production-grade starter for **Software Curatorship**.  
It provides the *operational grammar* (baseline recipe, schema, prompts, and guardrail scripts) to make any repository **self-documenting**, **self-verifying**, and **curator-friendly**.

## What’s inside

- `docs/curation/` — the “secret sauce” (baseline, schema, prompts, curation log template).
- `scripts/` — small guardrails (ADR index check, ADR linter, print guard, fast tests).
- `.github/workflows/ci.yml` — sample CI that validates your recipe and runs guardrails.
- `.pre-commit-config.yaml` — pre-commit hooks for fast feedback.
- `pyproject.toml` — minimal Ruff/MyPy config (safe defaults).

## Quickstart (existing project)

1. **Copy the folder** `docs/curation/` into your repo (or use this as a template repo).
2. Add (or adapt) the guardrail `scripts/` you want.
3. Commit, then open your Copilot/AI chat and paste:
   - `docs/curation/PROMPT_upgrade_to_v0.3.md` (baseline alignment), and optionally
   - `docs/curation/PROMPT_upgrade_with_tooling.md` (CI/pre-commit wiring).

> Tip: If your project does not yet have an `AI_CURATOR_RECIPE.md`, start with `PROMPT_instrument_curator_project.md` (for brand-new repos).

## Quickstart (new project)

1. Keep this structure.
2. Ask Copilot/AI to **instrument the project** using `docs/curation/PROMPT_instrument_curator_project.md`.
3. Commit the generated `AI_CURATOR_RECIPE.md` and `docs/curation/CURATION_LOG.md`.
4. Ensure CI is green.

## Philosophy

- **AI drafts; human curator approves.**
- Changes that affect users must be backed by **tests** and **ADRs**.
- **Determinism** and **provenance** are first-class citizens.

## AI / Editor Usage

This repository is instrumented for Software Curatorship. When using AI assistants
(e.g., GitHub Copilot Chat) or IDE integrations:

- All git operations and project checks should be run via explicit terminal
  commands (e.g. `pre-commit run --all-files`, `bash scripts/fast_tests.sh`,
  `python scripts/validate_recipe.py …`).
- The AI assistant should **propose** concrete shell commands and code edits, and
  the human curator runs and reviews them.
- The assistant should **not** rely on hidden IDE or cloud-level automation
  (such as background tooling that performs git operations or runs scripts
  without showing the exact commands), so that every step remains visible and
  auditable to the curator.

---

**License:** MIT.  

**Version of baseline included here:** 0.3 (as of 2025-10-25).
