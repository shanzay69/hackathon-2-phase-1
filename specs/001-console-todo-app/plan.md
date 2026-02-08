# Implementation Plan: Phase I — In-Memory Console Todo App

**Branch**: `001-console-todo-app` | **Date**: 2026-02-08 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-console-todo-app/spec.md`

## Summary

Build a pure Python console-based todo application that manages tasks
entirely in memory. The app supports five commands (add, list, update,
delete, complete) plus help and exit, with deterministic input
validation and graceful error handling. No external dependencies, no
persistence, no network — runs offline in a single process.

## Technical Context

**Language/Version**: Python 3.13+ (managed via UV)
**Primary Dependencies**: None (Python standard library only)
**Storage**: In-memory (Python dict); no files, no database
**Testing**: Manual verification + simple assertion scripts
**Target Platform**: Any OS with Python 3.13+ and a terminal (stdin/stdout)
**Project Type**: Single project
**Performance Goals**: Interactive responsiveness (<1s per command)
**Constraints**: Zero external dependencies; offline-only; single-user
**Scale/Scope**: Single-user, single-session, unbounded todo count
  (limited only by available memory)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Status |
|-----------|------|--------|
| I. Simplicity-First | No external deps; in-memory only; console I/O | PASS |
| II. Separation of Concerns | Business logic separated from CLI parsing; single-responsibility modules | PASS |
| III. Progressive Enhancement | Command vocabulary (add, list, update, delete, complete) stable for future phases | PASS |
| IV. Deterministic Behavior | Same input + same state = same output; explicit error messages; no hidden side effects | PASS |
| V. Developer Clarity | Readable names; Given/When/Then scenarios in spec; explicit command handling | PASS |
| Phase I Rules | Python 3.13+; in-memory state; CLI only; no deps; manual testing | PASS |

All gates pass. No violations to justify.

## Project Structure

### Documentation (this feature)

```text
specs/001-console-todo-app/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (internal API contracts)
├── checklists/          # Spec quality checklist
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
├── __init__.py
├── __main__.py          # Entry point: python -m src
├── models/
│   ├── __init__.py
│   └── todo.py          # Todo entity + TodoList collection
├── services/
│   ├── __init__.py
│   └── todo_service.py  # Business logic (CRUD + complete)
└── cli/
    ├── __init__.py
    ├── app.py            # Main REPL loop
    ├── parser.py         # Command parsing + validation
    └── printer.py        # Output formatting

tests/
└── test_todo.py          # Simple assertion-based tests
```

**Structure Decision**: Single project layout. Three packages under
`src/` enforce separation of concerns: `models` owns data structures,
`services` owns business logic, `cli` owns user interaction. This maps
directly to Constitution Principle II and enables Phase II to swap the
CLI layer for a FastAPI layer without touching models or services.

## Complexity Tracking

> No violations detected. All gates pass.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| (none) | — | — |
