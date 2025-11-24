# Project Blueprint

> This document captures the **intended shape** of the system:
> - What it is for.
> - Which capabilities it should eventually have.
> - Which technologies and constraints we accept.
>
> **Important:** Once a feature has been implemented and/or covered by an ADR,
> the ADR and the actual code override whatever is written here.
>
> **This blueprint is deliberately aspirational.** It records the outcome of
> brainstorming and design discussions. **It is not a normative
> specification.** For this project, the authoritative specification of
> implemented behavior lives in `AI_CURATOR_RECIPE.md` (especially Appendix A)
> and ADRs. New ideas land here first; only once implemented are they
> ported to Appendix A.

---

## 1. Vision & Purpose

- **One-sentence summary**  
  <!-- Example: "A lightweight web service that exposes a curated API for X." -->

- **Who is this for?**  
  <!-- Types of users, environments (dev, ops, external clients, etc). -->

- **Problem statement**  
  <!-- What real-world friction or need does this project address? -->

---

## 2. Scope, Non-Goals & Constraints

### 2.1 In-Scope

- <!-- Bullet list of the main things this project must do. -->

### 2.2 Out-of-Scope / Non-Goals

- <!-- Things people might reasonably ask for, but we explicitly won't do. -->

### 2.3 Constraints

- **Technical**  
  <!-- Required languages, frameworks, deployment targets, data stores, etc. -->

- **Organizational / legal**  
  <!-- Licensing limits, privacy constraints, regulation, etc. -->

- **Performance & scale**  
  <!-- Orders of magnitude, response times, throughput, rough SLAs. -->

---

## 3. Domain Model & Glossary

- **Key domain concepts and entities**  
  - `ConceptName`: short definition.  
  - `AnotherConcept`: short definition.

- **Data invariants**  
  - <!-- Invariants that must hold across the system (e.g. uniqueness, consistency rules). -->

This section should be used by AI as **canonical vocabulary** when reasoning about new features.

---

## 4. System Overview

### 4.1 High-Level Architecture

- **Current state**  
  <!-- Short description + ASCII diagram if helpful. -->

- **Planned evolution**  
  <!-- What components we expect to add later, and why. -->

### 4.2 Main Components / Modules

For each component:

- **Name**  
- **Responsibility**  
- **Collaborators / dependencies**  
- **Notes** (explicitly reference ADRs when they exist)

---

## 5. Technology Choices

> Many of these should get their own ADRs as soon as they stop being hypothetical.

- **Language(s)**  
- **Frameworks & libraries**  
- **Database / storage**  
- **Messaging / integration technologies**  
- **Operational stack** (deployment, monitoring, logging, etc.)

Where an **ADR exists for a given choice**, link it here and treat the blueprint text as secondary.

---

## 6. Feature Map & Roadmap

### 6.1 Current Features

> Short, non-authoritative catalog – ADRs and code are authoritative.

- `FeatureName`
  - Status: `planned | in progress | implemented`
  - ADR(s): `ADR-xxx` (if any)
  - Summary:

### 6.2 Future Features / Ideas

> This is where curation with AI happens: new features are brainstormed, refined, and prioritized.

For each future feature:

- **Name**
- **User story / narrative**
- **Motivation**
- **Rough acceptance criteria**
- **Dependencies / preconditions**
- **Risks / unknowns**

---

## 7. Quality Attributes

Rank or briefly describe priorities:

- **Reliability / robustness**
- **Performance**
- **Security / privacy**
- **Observability**
- **Maintainability**
- **Portability**

Optionally include trade-offs (e.g. “We prefer simplicity over micro-optimizations unless contradicted by an ADR.”).

---

## 8. Integration Points

- **External systems / APIs**
- **Inbound interfaces** (what calls us)
- **Outbound interfaces** (what we call)
- **Contracts & versioning expectations**

---

## 9. Open Questions

> This is where the curator intentionally parks uncertainty for the AI to help with.

- Q1:
- Q2:
- …

---

## 10. Curation Rules for BLUEPRINT vs ADRs

- **ADRs override BLUEPRINT.md for implemented or decided parts of the system.**
- When an ADR contradicts this document:
  1. Respect the ADR.
  2. Update the relevant section in this document to match the ADR (marking that it is now authoritative.)
- When designing **new features**, treat BLUEPRINT.md as the primary context, but:
  - Always check for relevant ADRs.
  - Do not silently “correct” or override ADRs from here.

