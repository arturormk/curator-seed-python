# Prompt: Upgrade repository to Software Curatorship Baseline v0.3

You are assisting in bringing this repository up to **Software Curatorship Baseline v0.3**.

Follow these steps carefully and output a complete, diff-ready `AI_CURATOR_RECIPE.md` at the end.

1. Read `docs/curation/AI_CURATOR_RECIPE_BASELINE_v0.3.md` and use it as the normative template.
2. Retain all repository-specific content from the current `AI_CURATOR_RECIPE.md` (especially §2 Product Contract, §10 Releases, and Appendix A).
3. Add a **YAML front-matter block** at the top with:
   ```yaml
   ---
   version: 0.3
   project: <repo name>
   baseline_commit: <current git commit SHA>
   curated_by: <your name or “Control Equis”>
   ---
   ```
4. Insert `<!-- @curator:required -->` and `<!-- @curator:optional -->` markers exactly as in the baseline for every heading.
5. Validate headings against `docs/curation/ai_curator_recipe.schema.json` and fix any omissions or order errors.
6. Ensure a `Deferred with Rationale` section exists even if empty.
7. Append or update **Appendix A — Project-Specific Contracts** with this repo’s concrete CLI/API/determinism rules.
8. Generate a short `docs/curation/CURATION_LOG.md` entry using the template (today’s date, version 0.3, status “accepted”).

Finally, print only:
- the **full updated AI_CURATOR_RECIPE.md**, and  
- the **new CURATION_LOG.md entry**.

Do *not* modify the baseline or schema files in `docs/curation/`; they are shared assets.
