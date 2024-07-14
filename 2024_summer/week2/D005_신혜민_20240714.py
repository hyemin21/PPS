def find_constructor(n):
    for i in range(1, n):
        if i + sum(map(int, str(i))) == n:
            return i
    return 0
