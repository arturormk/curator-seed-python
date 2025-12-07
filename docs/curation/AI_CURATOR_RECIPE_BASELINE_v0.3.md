---
version: 0.3
project: (fill with repo name)
baseline_commit: (git SHA or tag)
curated_by: (name or org)
---

# AI Curator Recipe — Baseline (v0.3)

> This file defines the common framework for Software Curatorship projects.
> Each repository customizes **§2 Product Contract**, **§10 Releases**, and **Appendix A**.
> All other sections remain normatively identical across curated projects.

> When interpreting requirements or resolving conflicts, prioritize ADRs over
> BLUEPRINT.md, and both over informal notes. BLUEPRINT.md describes the intended
> global shape of the system, but ADRs always win for features that are already
> implemented or explicitly decided.

## 1) Intent & Scope <!-- @curator:required -->
- Keep runtime minimal; favor clarity and determinism.
- All user-visible behavior is test-backed and explained via ADRs.
- Provenance is transparent (README “Attribution & Curation”, ADR-0010, AUTHORS).
- Optional per-repo goals may be listed here.

## 2) Product Contract (plain language) <!-- @curator:required -->
Describe the externally visible behavior of the CLI, API, or service.

| Aspect | Description |
|--------|--------------|
| **Inputs** | Command-line args, API payloads, files, env vars |
| **Outputs/streams** | stdout → data; stderr → diagnostics |
| **Exit codes** | Enumerate all used numeric codes |
| **Determinism** | Define ordering, rounding, locale, or sampling rules |

> See Appendix A for detailed project-specific contracts.

## 3) Curation Principles <!-- @curator:required -->
- AI drafts; human curator approves and is accountable.
- Non-trivial changes: add/update tests and ADRs.
- Prefer stdlib/zero-deps unless ADR justifies otherwise.
- Maintain transparency of reasoning and provenance.

## 4) Repository Map <!-- @curator:required -->
List canonical folders and files expected to exist.
Example: `src/`, `tests/`, `docs/adr/`, `scripts/`, `.github/workflows/ci.yml`, `.pre-commit-config.yaml`.

## 5) ADR Policy <!-- @curator:required -->
- Sections: **Context · Decision · Consequences**
- Status flow: Proposed → Accepted → Superseded
- Index file `docs/adr/README.md` auto-maintained; CI fails if stale.

## 6) Testing Strategy <!-- @curator:required -->
- Cover contracts (inputs, outputs, invariants).
- Add at least one edge case per behavior change.
- Keep deterministic; network-free fast subset (`scripts/fast_tests.sh`).

## 7) Automation — Self-Verifying <!-- @curator:required -->
| Stage | Tools | Purpose |
|--------|--------|---------|
| **Local (pre-commit)** | Ruff, mypy, ADR guards, print-guard, fast tests | Prevent regressions early |
| **CI** | Lint → Type → Tests → Build → ADR checks | Guarantee reproducibility |

Optional additions: locale pinning, determinism diff, version parity check.

## 8) Definition of Done <!-- @curator:required -->
- Lint/types/tests/build all green.
- Tests cover new/changed behavior.
- Docs/ADRs updated.
- Provenance intact.
- Packaging/version sanity verified.

## 9) AI Assistant Operating Procedure <!-- @curator:required -->
1. Read tree & targets.
2. Expand curator’s ask → checklist.
3. Propose minimal diffs.
4. Propose explicit shell commands using this repo’s scripts and tooling
	(e.g. `pre-commit run --all-files`, `bash scripts/fast_tests.sh`,
	`python scripts/validate_recipe.py …`) and let the human curator run
	them in the terminal; avoid hidden IDE/cloud automation that obscures
	the exact operations performed.
5. Run checks; iterate to green or mark deferrals.
6. Summarize deltas (Done/Deferred).
7. Keep attribution; never remove license/provenance.

## 10) Releases & Versioning <!-- @curator:required -->
- Semantic Versioning.
- Define single source of truth for version.
- Tag `vX.Y.Z`; CI green required.
- Release notes + changelog optional but recommended.

## 11) Maintenance Rhythm <!-- @curator:optional -->
Periodic curator duties: run pre-commit on all files, review README accuracy, ADR housekeeping, close incidents with guardrails.

## Deferred with Rationale <!-- @curator:required -->
List any postponed improvements and explain why.

## Appendix A — Project-Specific Contracts <!-- @curator:required -->
Use structured bullets mirroring §2.
Include any CLI/API specifics, determinism rules, and domain invariants.
All listed behaviors must have at least one validating test.

> Validated against `ai_curator_recipe.schema.json`
> Last baseline change: 2025-10-25
