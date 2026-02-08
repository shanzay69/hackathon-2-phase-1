# Research: Phase I — In-Memory Console Todo App

**Branch**: `001-console-todo-app` | **Date**: 2026-02-08

## Research Tasks

### R1: Python REPL Loop Pattern

**Decision**: Use a `while True` loop with `input()` for the
interactive prompt. Catch `KeyboardInterrupt` to handle Ctrl+C
gracefully. Catch `EOFError` to handle piped input or Ctrl+D/Ctrl+Z.

**Rationale**: `input()` is the standard Python mechanism for reading
from stdin. It blocks until the user provides a line, which is the
expected behavior for a synchronous CLI application. No external
libraries (like `cmd` module or `readline`) are needed for Phase I's
simple command structure.

**Alternatives considered**:
- `cmd.Cmd` module: Provides a built-in command framework with help
  generation and tab completion. Rejected because it introduces an
  opinionated structure that may conflict with the explicit command
  parsing required by the constitution (Principle V). It also makes
  the REPL harder to swap for an API layer in Phase II.
- `sys.stdin` direct reads: Lower-level than `input()` with no
  practical benefit for this use case. Adds complexity without value.

### R2: In-Memory Data Structure for Todos

**Decision**: Use a Python `dict` keyed by integer ID, with each
value being a `Todo` dataclass instance. Maintain a separate
`_next_id` counter for auto-incrementing IDs.

**Rationale**: Dict provides O(1) lookup by ID, which is the primary
access pattern for update, complete, and delete operations. A list
would require linear scan for ID-based operations. The dict naturally
handles non-contiguous IDs after deletions (IDs are never reused per
spec assumptions).

**Alternatives considered**:
- `list` of Todo objects: O(n) lookup by ID. Would require either
  index-based access (fragile after deletions) or linear search.
  Rejected for performance and correctness.
- `OrderedDict`: Preserves insertion order but is unnecessary since
  Python 3.7+ dicts already maintain insertion order.

### R3: Command Parsing Strategy

**Decision**: Split input on first whitespace to extract the command
keyword. The remainder of the line is the argument string. For
commands needing an ID + description (e.g., `update`), split the
argument string on first whitespace again.

**Rationale**: Simple string splitting is sufficient for the five
commands. No regex or argument parsing library is needed. This
approach handles multi-word descriptions naturally (everything after
the ID is the description).

**Alternatives considered**:
- `argparse`: Overkill for 7 commands with simple arguments. Adds
  complexity and non-standard error messages that would need
  customization. Rejected per Principle I (Simplicity-First).
- `shlex.split()`: Handles quoted strings but adds unnecessary
  complexity. Users are not expected to use quotes in Phase I.

### R4: Project Tooling — UV

**Decision**: Use UV as the Python project manager and runner.
Initialize with `uv init`, run with `uv run python -m src`.

**Rationale**: The user explicitly specified Python 3.13+ with UV.
UV provides fast dependency resolution and virtual environment
management. For Phase I there are no dependencies, but UV establishes
the project structure for future phases.

**Alternatives considered**:
- Raw `python` without UV: Would work for Phase I but loses the
  project structure benefits and is inconsistent with user
  requirements.
- `poetry`: Heavier than UV, slower, and not requested.

### R5: Error Handling Pattern

**Decision**: Define distinct error messages for each failure mode
and return them from the service layer. The CLI layer displays
messages to stdout (not stderr) for consistency with the interactive
REPL pattern. Tracebacks are never shown to the user.

**Rationale**: Per Constitution Principle IV (Deterministic Behavior),
every error path must be explicit and produce a clear message. Using
return values rather than exceptions keeps the flow simple and
avoids try/except proliferation in the CLI layer.

**Alternatives considered**:
- Custom exception hierarchy: Would be appropriate for a larger
  application but is over-engineering for Phase I's 5 commands.
  Rejected per Principle I.
- Stderr for errors: Conventional for CLI tools, but in an
  interactive REPL, mixing stdout and stderr creates confusing output
  in some terminals. All output goes to stdout for Phase I.

## Summary

All technical context items are resolved. No NEEDS CLARIFICATION
items remain. The research confirms that Python's standard library
provides everything needed for Phase I with no external dependencies.
