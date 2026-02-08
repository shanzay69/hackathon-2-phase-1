# Quickstart: Phase I — In-Memory Console Todo App

**Branch**: `001-console-todo-app` | **Date**: 2026-02-08

## Prerequisites

- Python 3.13+
- UV (Python project manager)

## Setup

```bash
# Clone and enter the project
git clone <repo-url>
cd hackathon-2-phase-1
git checkout 001-console-todo-app

# Install (no dependencies to install, but UV sets up the venv)
uv sync
```

## Run

```bash
uv run python -m src
```

You should see:

```text
Welcome to Todo App! Type 'help' for available commands.
todo>
```

## Usage

### Add a todo

```text
todo> add Buy groceries
Added todo #1: Buy groceries
```

### List all todos

```text
todo> list
  ID  Status   Description
  --  ------   -----------
   1  pending  Buy groceries
```

### Update a todo

```text
todo> update 1 Buy organic groceries
Updated todo #1: Buy organic groceries
```

### Mark a todo as complete

```text
todo> complete 1
Completed todo #1
```

### Delete a todo

```text
todo> delete 1
Deleted todo #1
```

### Get help

```text
todo> help
Available commands:
  add <description>          Add a new todo
  list                       List all todos
  update <id> <description>  Update a todo's description
  complete <id>              Mark a todo as complete
  delete <id>                Delete a todo
  help                       Show this help message
  exit                       Exit the application
```

### Exit

```text
todo> exit
Goodbye!
```

## Verification Checklist

- [ ] App starts and shows `todo>` prompt
- [ ] `add` creates a todo and shows confirmation with ID
- [ ] `list` shows all todos with ID, status, and description
- [ ] `list` on empty list shows "No todos yet" message
- [ ] `update` changes description and confirms
- [ ] `complete` changes status to "done" and confirms
- [ ] `delete` removes todo and confirms
- [ ] `help` lists all commands
- [ ] `exit` terminates with farewell message
- [ ] Invalid command shows help message
- [ ] Missing arguments show specific error
- [ ] Non-existent ID shows "not found" error
- [ ] Non-numeric ID shows "must be a number" error
- [ ] Ctrl+C exits gracefully (no traceback)
- [ ] Empty/whitespace input re-prompts silently
