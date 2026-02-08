# Data Model: Phase I — In-Memory Console Todo App

**Branch**: `001-console-todo-app` | **Date**: 2026-02-08

## Entities

### Todo

Represents a single task managed by the user.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | int | Unique, auto-incrementing, never reused | Stable identifier for the todo |
| description | str | Non-empty, no max length | User-provided text describing the task |
| status | str | One of: "pending", "done" | Current completion state |

**Default values**:
- `status`: "pending" (set on creation)

**State transitions**:

```text
[created] ──► pending ──► done
                │
                └──► [deleted]
```

- A todo is created with status "pending".
- The `complete` command transitions status from "pending" to "done".
- Completing an already "done" todo produces an informational message
  (no state change).
- The `delete` command removes the todo entirely (no soft delete).
- There is no transition from "done" back to "pending" in Phase I.

### TodoList

The in-memory collection managing all Todo instances.

| Field | Type | Description |
|-------|------|-------------|
| _todos | dict[int, Todo] | Maps todo ID to Todo instance |
| _next_id | int | Counter for the next available ID (starts at 1) |

**Invariants**:
- `_next_id` is always greater than any existing todo ID.
- `_next_id` is never decremented, even after deletions.
- No two todos share the same ID.
- The dict preserves insertion order (Python 3.7+ guarantee).

**Operations**:

| Operation | Input | Output | Side Effect |
|-----------|-------|--------|-------------|
| add | description: str | Todo (the created item) | Inserts new Todo, increments _next_id |
| list_all | (none) | list[Todo] | None (read-only) |
| get | id: int | Todo or None | None (read-only) |
| update | id: int, description: str | Todo or None | Updates description if found |
| complete | id: int | str (result message) | Sets status to "done" if pending |
| delete | id: int | bool (success) | Removes Todo from dict if found |

## Relationships

```text
TodoList 1──────* Todo
  (contains)
```

- TodoList owns all Todo instances.
- A Todo does not exist outside a TodoList.
- There is exactly one TodoList per application session.

## Validation Rules

| Rule | Applies To | Error When |
|------|-----------|------------|
| Non-empty description | add, update | Description is empty or whitespace-only |
| Valid ID format | update, complete, delete | ID is not a positive integer |
| ID exists | update, complete, delete | No todo with the given ID |
| Not already complete | complete | Todo status is already "done" (warning, not error) |
