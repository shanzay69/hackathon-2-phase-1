def parse_command(user_input: str) -> tuple[str, str]:
    stripped = user_input.strip()
    if not stripped:
        return ("", "")
    parts = stripped.split(None, 1)
    command = parts[0].lower()
    args = parts[1] if len(parts) > 1 else ""
    return (command, args)


def parse_id_and_args(args: str) -> tuple[int | None, str]:
    if not args.strip():
        return (None, "")
    parts = args.strip().split(None, 1)
    try:
        todo_id = int(parts[0])
    except ValueError:
        return (None, "")
    remaining = parts[1] if len(parts) > 1 else ""
    return (todo_id, remaining)


def is_valid_id_string(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False
