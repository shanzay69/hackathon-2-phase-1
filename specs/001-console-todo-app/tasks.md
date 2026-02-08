# Tasks: Phase I — In-Memory Console Todo App

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

**Tests**: Not requested for Phase I. Manual verification per quickstart.md.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization with UV and Python package structure

- [x] T001 Initialize Python project with UV (`uv init`) and configure for Python 3.13+ in pyproject.toml
- [x] T002 Create package structure with `__init__.py` files in src/, src/models/, src/services/, src/cli/
- [x] T003 Create entry point in src/__main__.py that imports and runs the CLI app

**Checkpoint**: Project runs with `uv run python -m src` (may exit immediately or show placeholder)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data model and service layer that ALL user stories depend on

- [x] T004 Create Todo dataclass in src/models/todo.py with fields: id (int), description (str), status (str, default "pending")
- [x] T005 Create TodoList class in src/models/todo.py with dict-based storage, _next_id counter, and methods: add, list_all, get, update, complete, delete per data-model.md
- [x] T006 Create TodoService in src/services/todo_service.py that wraps TodoList and implements the service contract from contracts/todo-service-api.md
- [x] T007 [P] Create command parser in src/cli/parser.py that splits input on first whitespace, extracts command keyword (case-insensitive), and returns (command, args) tuple
- [x] T008 [P] Create output printer in src/cli/printer.py with methods: print_todo, print_todo_list, print_empty_list, print_help, print_welcome, print_goodbye, print_error

**Checkpoint**: Foundation ready — models, service, parser, and printer are importable and functional. User story implementation can begin.

---

## Phase 3: User Story 1 — Add and View Todos (Priority: P1)

**Goal**: User can add todos and list all todos in a running REPL session.

**Independent Test**: Launch app, add 3 todos, run `list`, verify all appear with ID/description/status.

### Implementation for User Story 1

- [x] T009 [US1] Create REPL loop in src/cli/app.py with while-True/input() pattern, welcome message, `todo> ` prompt, KeyboardInterrupt handling, and EOFError handling
- [x] T010 [US1] Wire `add` command in src/cli/app.py: parse description from args, call TodoService.add, print confirmation with ID
- [x] T011 [US1] Wire `list` command in src/cli/app.py: call TodoService.list_all, print formatted table or empty-list message
- [x] T012 [US1] Add input validation for `add` command in src/cli/app.py: reject empty/whitespace-only description with error message

**Checkpoint**: User Story 1 fully functional — add and list work end-to-end in the REPL. MVP is achievable.

---

## Phase 4: User Story 2 — Update Todo Description (Priority: P2)

**Goal**: User can update an existing todo's description by ID.

**Independent Test**: Add a todo, update its description, list to verify change.

### Implementation for User Story 2

- [x] T013 [US2] Wire `update` command in src/cli/app.py: parse ID and new description from args, call TodoService.update, print confirmation or not-found error
- [x] T014 [US2] Add input validation for `update` command in src/cli/app.py: reject non-numeric ID, missing description, and empty description

**Checkpoint**: User Stories 1 AND 2 work independently. Add, list, and update are functional.

---

## Phase 5: User Story 3 — Mark Todo as Complete (Priority: P3)

**Goal**: User can mark a todo as complete, changing its status from "pending" to "done".

**Independent Test**: Add a todo, complete it, list to verify status is "done".

### Implementation for User Story 3

- [x] T015 [US3] Wire `complete` command in src/cli/app.py: parse ID from args, call TodoService.complete, print result message (completed, already complete, or not found)
- [x] T016 [US3] Add input validation for `complete` command in src/cli/app.py: reject non-numeric ID and missing ID

**Checkpoint**: User Stories 1, 2, AND 3 work independently. Status transitions are visible in list output.

---

## Phase 6: User Story 4 — Delete a Todo (Priority: P4)

**Goal**: User can permanently remove a todo by ID.

**Independent Test**: Add a todo, delete it, list to confirm it no longer appears.

### Implementation for User Story 4

- [x] T017 [US4] Wire `delete` command in src/cli/app.py: parse ID from args, call TodoService.delete, print confirmation or not-found error
- [x] T018 [US4] Add input validation for `delete` command in src/cli/app.py: reject non-numeric ID and missing ID

**Checkpoint**: Full CRUD lifecycle works. All data-mutating commands functional.

---

## Phase 7: User Story 5 — Exit and Help (Priority: P5)

**Goal**: User can exit gracefully and view help for all commands.

**Independent Test**: Run `help` to see all commands, run `exit` to terminate cleanly.

### Implementation for User Story 5

- [x] T019 [US5] Wire `help` command in src/cli/app.py: call printer.print_help to display all available commands with usage
- [x] T020 [US5] Wire `exit` command in src/cli/app.py: call printer.print_goodbye and break the REPL loop
- [x] T021 [US5] Wire unknown command handling in src/cli/app.py: display help message for unrecognized commands
- [x] T022 [US5] Handle whitespace-only and empty input in src/cli/app.py: skip silently and re-prompt

**Checkpoint**: All 7 commands work. All edge cases handled. Application is feature-complete.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and cleanup across all stories

- [x] T023 Verify all acceptance scenarios from spec.md pass via manual testing per quickstart.md
- [x] T024 [P] Verify Ctrl+C handling exits gracefully without traceback on all platforms
- [x] T025 [P] Verify `uv run python -m src` launches correctly from a clean clone

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion — BLOCKS all user stories
- **User Stories (Phases 3–7)**: All depend on Foundational phase completion
  - Stories can proceed sequentially in priority order (P1 → P2 → P3 → P4 → P5)
  - US2–US4 each add one command to the REPL; no cross-story conflicts
- **Polish (Phase 8)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) — No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) — Independent of US1
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) — Independent of US1/US2
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) — Independent of US1/US2/US3
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) — Independent of other stories

### Within Each User Story

- Wire command handler before adding its validation
- Command handler depends on parser + service (from Foundational)
- All commands modify the same file (src/cli/app.py) so they MUST run sequentially

### Parallel Opportunities

- T007 and T008 can run in parallel (different files: parser.py vs printer.py)
- T023, T024, T025 can run in parallel (independent verification tasks)
- User stories touch the same file (app.py), so sequential execution is required

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001–T003)
2. Complete Phase 2: Foundational (T004–T008)
3. Complete Phase 3: User Story 1 (T009–T012)
4. **STOP and VALIDATE**: Test add + list independently
5. MVP is usable — user can add and view todos

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → MVP!
3. Add User Story 2 → Test update → Increment
4. Add User Story 3 → Test complete → Increment
5. Add User Story 4 → Test delete → Full CRUD
6. Add User Story 5 → Test help/exit → Feature-complete
7. Polish → Verify all edge cases → Done

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story is independently completable and testable
- All user stories modify src/cli/app.py — execute sequentially
- Commit after each phase or logical group
- Stop at any checkpoint to validate the story independently
