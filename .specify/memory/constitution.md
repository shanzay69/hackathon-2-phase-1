<!--
Sync Impact Report
====================
Version change: 0.0.0 → 1.0.0 (MAJOR — initial ratification)

Modified principles: N/A (first version)

Added sections:
  - Core Principles (5 principles: Simplicity-First, Separation of Concerns,
    Progressive Enhancement, Deterministic Behavior, Developer Clarity)
  - Phase Constraints (Phases I–V technology and architecture rules)
  - Development Workflow (standards, testing, tooling, code quality)
  - Governance (amendment procedure, versioning, compliance)

Removed sections: N/A

Templates requiring updates:
  - .specify/templates/plan-template.md — ✅ No updates needed
    (Constitution Check section is dynamic; will be filled per-feature)
  - .specify/templates/spec-template.md — ✅ No updates needed
    (User story and requirements structure aligns with principles)
  - .specify/templates/tasks-template.md — ✅ No updates needed
    (Phase-based task structure aligns with progressive enhancement)

Follow-up TODOs: None
-->

# In-Memory Console-Based Todo Application Constitution

## Core Principles

### I. Simplicity-First Design

- Phase I MUST be fully in-memory with zero external dependencies.
- Console-based interaction only (stdin/stdout) for Phase I.
- Pure Python implementation for Phase I; no third-party packages.
- YAGNI: do not build for future phases during current phase work.
- The smallest viable diff is always preferred over speculative
  generalization.

**Rationale**: A minimal footprint ensures the application works
without internet, storage, or configuration. Complexity is introduced
only when a concrete phase demands it.

### II. Separation of Concerns

- Specifications, plans, tasks, and implementation MUST be maintained
  as distinct artifacts (`spec.md`, `plan.md`, `tasks.md`, source code).
- Business logic MUST NOT leak into interface handling; command parsing
  and state management are separate layers.
- Each module/file MUST have a single, clearly stated responsibility.
- Data contracts (entities, APIs) MUST be defined before implementation
  begins.

**Rationale**: Clean boundaries make the codebase navigable, testable,
and safe to evolve across five phases without cascading rewrites.

### III. Progressive Enhancement

- Each phase MUST build on the previous phase's concepts and code
  without requiring breaking redesigns.
- Interfaces introduced in Phase I (e.g., command vocabulary: add, list,
  update, delete, complete) MUST remain semantically stable in later
  phases.
- New capabilities (persistence, web UI, AI, orchestration) are additive
  layers, not replacements.
- Migration paths between phases MUST be documented before work begins.

**Rationale**: A five-phase roadmap is only sustainable if earlier work
is preserved. Progressive enhancement protects investment in each phase.

### IV. Deterministic Behavior

- Application state MUST be predictable: identical inputs produce
  identical outputs given the same starting state.
- No hidden side effects; every state mutation MUST be explicit and
  traceable through the command interface.
- Error paths MUST be stated explicitly in specifications and handled
  gracefully in implementation (clear user-facing messages, no silent
  failures).
- AI integrations (Phase III+) MUST map to deterministic backend
  operations; the AI is an assistant, never the source of truth.

**Rationale**: Determinism enables reliable testing, debugging, and
user trust. It also ensures AI-augmented flows remain auditable.

### V. Developer Clarity

- Code MUST be self-explanatory: favor readable names and simple
  control flow over clever abstractions.
- Every feature spec MUST include acceptance scenarios written in
  Given/When/Then format.
- Command handling MUST be explicit; no implicit argument inference
  or hidden defaults.
- Documentation (specs, plans, tasks) MUST be current; stale docs
  are treated as defects.

**Rationale**: Multiple phases with evolving technology stacks demand
that any contributor can understand intent quickly. Clarity reduces
onboarding cost and defect rate.

## Phase Constraints

Technology and architecture boundaries for each phase. Violations
require a documented Complexity Tracking entry in `plan.md`.

| Phase | Stack | Key Constraint |
|-------|-------|----------------|
| I | Python (pure) | In-memory only; no files, no DB, no deps |
| II | Next.js + FastAPI + SQLModel + Neon DB | API-first; auth-ready |
| III | OpenAI ChatKit, Agents SDK, MCP SDK | AI maps to deterministic ops |
| IV | Docker, Minikube, Helm, kubectl-ai, kagent | Reproducible local cluster |
| V | Kafka, Dapr, DigitalOcean DOKS | Observability hooks required |

### Phase I Specific Rules

- Language: Python 3.10+
- Architecture: single-process, in-memory state (dict/list)
- Persistence: none (data resets on exit)
- Interface: CLI commands only (add, list, update, delete, complete)
- Testing: manual verification or simple assertions
- Tooling: Claude Code, Spec-Kit Plus
- External dependencies: NONE

### Phase II–V Guardrails

- Each phase MUST define its own spec, plan, and tasks before
  implementation begins.
- No phase may remove or break commands established in Phase I.
- Secrets and tokens MUST use environment variables (`.env`); never
  hardcoded.
- Database schemas MUST include migration and rollback scripts
  (Phase II+).
- Observability (logs, metrics, traces) MUST be enabled from
  Phase IV onward.

## Development Workflow

### Standards

- Prefer the smallest viable diff; do not refactor unrelated code.
- Cite existing code with precise file:line references.
- All PRs and reviews MUST verify compliance with this constitution.
- Commit after each task or logical group; atomic commits preferred.

### Testing Expectations

- Phase I: manual or simple assertion-based testing.
- Phase II+: automated tests required (unit, integration, contract)
  per the tasks template.
- When tests are requested, Red-Green-Refactor cycle applies:
  write tests first, confirm they fail, then implement.

### Code Quality

- No unused imports, dead code, or commented-out blocks in committed
  code.
- Error handling MUST cover all user-facing paths; internal errors
  MUST NOT surface raw tracebacks to the user.
- Functions SHOULD be < 30 lines; modules SHOULD be < 300 lines.
  Exceptions require justification.

### Tooling

- Spec-Kit Plus (`/sp.*` commands) is the primary workflow driver.
- Prompt History Records (PHRs) MUST be created for every
  substantive interaction.
- Architecture Decision Records (ADRs) MUST be suggested when
  significant decisions are detected (never auto-created).

## Governance

- This constitution supersedes all other development practices for
  this project.
- Amendments require:
  1. A documented proposal describing the change and its rationale.
  2. Version bump per semantic versioning (MAJOR/MINOR/PATCH).
  3. Updated Sync Impact Report at the top of this file.
  4. Propagation check across dependent templates.
- Compliance review: every spec, plan, and task document MUST include
  a Constitution Check section verifying alignment with active
  principles.
- Complexity MUST be justified: any deviation from a principle
  requires a Complexity Tracking entry in `plan.md` with the
  rejected simpler alternative documented.

**Version**: 1.0.0 | **Ratified**: 2026-02-08 | **Last Amended**: 2026-02-08
