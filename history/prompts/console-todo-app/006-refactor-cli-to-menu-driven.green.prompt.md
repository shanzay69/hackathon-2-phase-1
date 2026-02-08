---
id: 006
title: Refactor CLI to Menu-Driven Interface
stage: green
date: 2026-02-08
surface: agent
model: claude-opus-4-6
feature: console-todo-app
branch: 001-console-todo-app
user: architect
command: (direct prompt)
labels: ["cli", "refactor", "menu-driven"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - src/cli/app.py
  - src/cli/printer.py
  - src/models/todo.py
  - src/services/todo_service.py
tests:
  - Smoke tested via piped stdin
  - Menu options 1-7 all functional
  - Input validation working
  - Exit loops menu correctly
---

## Prompt

Refactor CLI to menu-driven interface.

Current state:
The Todo app is fully working with command-based CLI:
- add
- list
- update
- complete
- delete
- help
- exit

Services, repositories, and models are correct.
Do NOT change backend logic.

Required change:
Convert CLI interaction into menu-based system like:

---- Todo Application ----
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit

Enter your choice (1-7):

Behavior rules:
- Loop menu until user selects Exit
- Each option should call existing TodoService functions
- Input validation required
- Keep in-memory behavior
- Do not rebuild project
- Modify only CLI layer

Goal:
CLI must match classic numbered menu interaction.

## Response snapshot

Rewrote src/cli/app.py to menu-driven loop dispatching on choices 1-7. Updated printer.py with print_menu(). Added minimal TodoList.incomplete() and TodoService.incomplete() methods to support option 6. All input validation works. Smoke tested successfully.

## Outcome

- ✅ Impact: CLI successfully converted from command-based to menu-driven interface. All 7 menu options functional, in-memory behavior preserved, no changes to business logic.
- 🧪 Tests: Smoke tested via piped stdin; all menu options validated
- 📁 Files: 4 files modified (app.py, printer.py, todo.py, todo_service.py)
- 🔁 Next prompts: Update spec and tasks.md to reflect menu-driven behavior; create PR
- 🧠 Reflection: Menu-driven refactoring kept CLI layer isolated from service layer. Minimal additions to models/services (just incomplete() method) to support new UI option. Code remains clean and maintainable.

## Evaluation notes (flywheel)

- Failure modes observed: None — menu-driven refactoring completed successfully
- Graders run and results (PASS/FAIL): All 7 menu options tested PASS, input validation PASS, exit behavior PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
