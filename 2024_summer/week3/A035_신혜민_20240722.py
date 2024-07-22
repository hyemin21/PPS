def martian_math(commands: list) -> float:
    result = float(commands[0])
    for command in commands[1:]:
        if command == '@':
            result *= 3
        elif command == '%':
            result += 5
        elif command == '#':
            result -= 7
    return result
