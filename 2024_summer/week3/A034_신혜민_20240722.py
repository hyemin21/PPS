def distinct_remainders(numbers: list) -> int:
    remainders = set()
    for number in numbers:
        remainders.add(number % 42)
    return len(remainders)