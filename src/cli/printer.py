from src.models.todo import Todo

MENU = """---- Todo Application ----
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit"""


def print_menu():
    print(MENU)


def print_goodbye():
    print("Goodbye!")


def print_todo(todo: Todo, action: str):
    print(f"{action} todo #{todo.id}: {todo.description}")


def print_todo_list(todos: list[Todo]):
    print(f"  {'ID':>4}  {'Status':<8} Description")
    print(f"  {'--':>4}  {'------':<8} -----------")
    for todo in todos:
        print(f"  {todo.id:>4}  {todo.status:<8} {todo.description}")


def print_empty_list():
    print("No todos yet.")


def print_error(message: str):
    print(f"Error: {message}")
