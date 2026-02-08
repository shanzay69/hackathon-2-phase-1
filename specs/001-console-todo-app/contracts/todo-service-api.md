# Internal API Contract: TodoService

**Branch**: `001-console-todo-app` | **Date**: 2026-02-08

Phase I is a console application with no HTTP/REST API. This document
defines the internal Python API contract for the service layer, which
the CLI layer calls. This contract becomes the foundation for the
FastAPI endpoints in Phase II.

## TodoService Interface

### add(description: str) -> Todo

Create a new todo with the given description.

**Input**:
- `description` (str): Non-empty text for the todo.

**Output**:
- `Todo`: The newly created todo with auto-assigned ID and
  status "pending".

**Errors**:
- Returns error message if `description` is empty or whitespace.

**Example**:

```text
Input:  add("Buy groceries")
Output: Todo(id=1, description="Buy groceries", status="pending")
```

---

### list_all() -> list[Todo]

Return all todos in insertion order.

**Input**: None

**Output**:
- `list[Todo]`: All todos, may be empty.

**Errors**: None (empty list is a valid response).

**Example**:

```text
Input:  list_all()
Output: [Todo(id=1, ...), Todo(id=2, ...)]
```

---

### update(id: int, description: str) -> Todo | None

Update the description of an existing todo.

**Input**:
- `id` (int): The todo identifier.
- `description` (str): New non-empty description text.

**Output**:
- `Todo`: The updated todo if found.
- `None`: If no todo with the given ID exists.

**Errors**:
- Returns error message if `description` is empty or whitespace.

**Example**:

```text
Input:  update(1, "Buy organic groceries")
Output: Todo(id=1, description="Buy organic groceries", status="pending")
```

---

### complete(id: int) -> str

Mark a todo as complete.

**Input**:
- `id` (int): The todo identifier.

**Output**:
- `str`: Result message — one of:
  - Confirmation that the todo was completed.
  - Message that the todo is already complete.
  - Message that the todo was not found.

**Example**:

```text
Input:  complete(1)
Output: "Completed todo #1"

Input:  complete(1)  # already done
Output: "Todo #1 is already complete"

Input:  complete(99)  # not found
Output: "Todo #99 not found"
```

---

### delete(id: int) -> bool

Permanently remove a todo.

**Input**:
- `id` (int): The todo identifier.

**Output**:
- `True`: Todo was found and deleted.
- `False`: No todo with the given ID exists.

**Example**:

```text
Input:  delete(1)
Output: True

Input:  delete(99)
Output: False
```

## Command-to-Service Mapping

| CLI Command | Service Method | Parser Extracts |
|-------------|---------------|-----------------|
| `add <desc>` | `add(description)` | Everything after "add " |
| `list` | `list_all()` | Nothing |
| `update <id> <desc>` | `update(id, description)` | First token as int, rest as description |
| `complete <id>` | `complete(id)` | First token as int |
| `delete <id>` | `delete(id)` | First token as int |
| `help` | (handled by CLI) | Nothing |
| `exit` | (handled by CLI) | Nothing |

## Phase II Migration Path

In Phase II, each service method maps to a REST endpoint:

| Service Method | REST Endpoint | HTTP Method |
|---------------|---------------|-------------|
| `add` | `/api/todos` | POST |
| `list_all` | `/api/todos` | GET |
| `update` | `/api/todos/{id}` | PUT |
| `complete` | `/api/todos/{id}/complete` | PATCH |
| `delete` | `/api/todos/{id}` | DELETE |

The service layer remains unchanged; only the CLI layer is replaced
by a FastAPI router layer.
