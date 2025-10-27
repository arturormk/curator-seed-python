# Prompt: Instrument a new project for Software Curatorship

You are assisting in **instrumenting a completely new project** to apply the Software Curatorship methodology.

The folder `docs/curation/` already contains the core curator assets:
- `AI_CURATOR_RECIPE_BASELINE_v0.3.md`
- `ai_curator_recipe.schema.json`
- `CURATION_LOG_template.md`
- `PROMPT_upgrade_to_v0.3.md`
- `PROMPT_upgrade_with_tooling.md`

Follow these steps to turn this repository into a **curator-ready** project.

---

## 1. Read the Baseline
Open and read `docs/curation/AI_CURATOR_RECIPE_BASELINE_v0.3.md`.  
This file defines the canonical structure, headings, and required curator comments (`<!-- @curator:required -->`, etc.).

## 2. Create the Initial AI_CURATOR_RECIPE.md
Generate a new `AI_CURATOR_RECIPE.md` at the root of the repository by copying the baseline and filling in the required metadata:

```yaml
---
version: 0.3
project: <project name>
baseline_commit: <current git SHA>
curated_by: <your name or organization>
---
```

Then:
- Keep all baseline sections and headings.
- Fill **§2 Product Contract** with the project’s current or intended inputs/outputs/contracts.
- Leave **Deferred with Rationale** and **Appendix A** empty or marked *TBD* if the project is new.

## 3. Add a Curation Log Entry
Copy `docs/curation/CURATION_LOG_template.md` to `docs/curation/CURATION_LOG.md` and fill in:
- `project`
- `baseline_version = 0.3`
- `round_date = <today>`
- `status = in-progress`

## 4. Validate the Recipe
Add or verify a CI step that validates the new recipe:

```bash
python -m jsonschema -F frontmatter docs/curation/ai_curator_recipe.schema.json AI_CURATOR_RECIPE.md
```

If the validation fails, fix headings or front-matter until it passes.

## 5. Add Tooling Hooks
- Add Ruff, MyPy, ADR lint, and fast-test hooks as defined in `PROMPT_upgrade_with_tooling.md`.
- Exclude `docs/curation/` from all lint and type checks.
- Ensure `.github/workflows/ci.yml` runs the recipe validation.

## 6. Initialize ADR and Incident Structure
Create the following minimal directories and files:
```
docs/adr/README.md     # ADR index
scripts/check_adr_index.py
scripts/lint_adrs.py
```
Optionally create `docs/incidents/` with a placeholder `.gitkeep` file.

## 7. Verify Pre-commit & CI Run
Execute:
```bash
pre-commit run --all-files
pytest -q || echo "No tests yet"
```
Ensure CI passes linting and recipe validation steps.

## 8. Produce Summary Output
Output:
- The generated `AI_CURATOR_RECIPE.md`
- The created `CURATION_LOG.md` entry
- A short bullet list summarizing added scripts, config changes, or deferrals

---

**Goal:** Turn this repository into a baseline-compliant, self-documenting, self-verifying project ready for AI-assisted Software Curatorship.

**After this step:** you can immediately start curating — write ADR-0001 to document the project’s purpose, and use the baseline as the project’s living contract.
