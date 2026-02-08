from src.models.todo import Todo, TodoList


class TodoService:
    def __init__(self):
        self._todo_list = TodoList()

    def add(self, description: str) -> Todo:
        return self._todo_list.add(description)

    def list_all(self) -> list[Todo]:
        return self._todo_list.list_all()

    def update(self, todo_id: int, description: str) -> Todo | None:
        return self._todo_list.update(todo_id, description)

    def complete(self, todo_id: int) -> str:
        return self._todo_list.complete(todo_id)

    def incomplete(self, todo_id: int) -> str:
        return self._todo_list.incomplete(todo_id)

    def delete(self, todo_id: int) -> bool:
        return self._todo_list.delete(todo_id)
