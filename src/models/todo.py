from dataclasses import dataclass, field


@dataclass
class Todo:
    id: int
    description: str
    status: str = "pending"


class TodoList:
    def __init__(self):
        self._todos: dict[int, Todo] = {}
        self._next_id: int = 1

    def add(self, description: str) -> Todo:
        todo = Todo(id=self._next_id, description=description)
        self._todos[self._next_id] = todo
        self._next_id += 1
        return todo

    def list_all(self) -> list[Todo]:
        return list(self._todos.values())

    def get(self, todo_id: int) -> Todo | None:
        return self._todos.get(todo_id)

    def update(self, todo_id: int, description: str) -> Todo | None:
        todo = self._todos.get(todo_id)
        if todo is None:
            return None
        todo.description = description
        return todo

    def complete(self, todo_id: int) -> str:
        todo = self._todos.get(todo_id)
        if todo is None:
            return f"Todo #{todo_id} not found"
        if todo.status == "done":
            return f"Todo #{todo_id} is already complete"
        todo.status = "done"
        return f"Completed todo #{todo_id}"

    def incomplete(self, todo_id: int) -> str:
        todo = self._todos.get(todo_id)
        if todo is None:
            return f"Todo #{todo_id} not found"
        if todo.status == "pending":
            return f"Todo #{todo_id} is already incomplete"
        todo.status = "pending"
        return f"Marked todo #{todo_id} as incomplete"

    def delete(self, todo_id: int) -> bool:
        if todo_id in self._todos:
            del self._todos[todo_id]
            return True
        return False
