from src.cli.printer import (
    print_menu,
    print_goodbye,
    print_todo,
    print_todo_list,
    print_empty_list,
    print_error,
)
from src.services.todo_service import TodoService

PROMPT = "\nEnter your choice (1-7): "


def run():
    service = TodoService()
    print_menu()

    try:
        while True:
            try:
                choice = input(PROMPT).strip()
            except EOFError:
                print()
                print_goodbye()
                break

            if choice == "1":
                _handle_add(service)
            elif choice == "2":
                _handle_list(service)
            elif choice == "3":
                _handle_update(service)
            elif choice == "4":
                _handle_delete(service)
            elif choice == "5":
                _handle_complete(service)
            elif choice == "6":
                _handle_incomplete(service)
            elif choice == "7":
                print_goodbye()
                break
            elif choice == "":
                print_menu()
                continue
            else:
                print_error("Invalid choice. Please enter a number between 1 and 7.")

            print_menu()

    except KeyboardInterrupt:
        print()
        print_goodbye()


def _read_input(prompt: str) -> str | None:
    try:
        return input(prompt).strip()
    except EOFError:
        return None


def _read_id(prompt: str) -> int | None:
    value = _read_input(prompt)
    if value is None:
        return None
    try:
        return int(value)
    except ValueError:
        print_error("ID must be a number.")
        return None


def _handle_add(service: TodoService):
    description = _read_input("Enter task description: ")
    if not description:
        print_error("Description cannot be empty.")
        return
    todo = service.add(description)
    print_todo(todo, "Added")


def _handle_list(service: TodoService):
    todos = service.list_all()
    if not todos:
        print_empty_list()
    else:
        print_todo_list(todos)


def _handle_update(service: TodoService):
    todo_id = _read_id("Enter task ID to update: ")
    if todo_id is None:
        return
    description = _read_input("Enter new description: ")
    if not description:
        print_error("Description cannot be empty.")
        return
    todo = service.update(todo_id, description)
    if todo is None:
        print_error(f"Todo #{todo_id} not found.")
    else:
        print_todo(todo, "Updated")


def _handle_delete(service: TodoService):
    todo_id = _read_id("Enter task ID to delete: ")
    if todo_id is None:
        return
    if service.delete(todo_id):
        print(f"Deleted todo #{todo_id}")
    else:
        print_error(f"Todo #{todo_id} not found.")


def _handle_complete(service: TodoService):
    todo_id = _read_id("Enter task ID to mark complete: ")
    if todo_id is None:
        return
    result = service.complete(todo_id)
    print(result)


def _handle_incomplete(service: TodoService):
    todo_id = _read_id("Enter task ID to mark incomplete: ")
    if todo_id is None:
        return
    result = service.incomplete(todo_id)
    print(result)
