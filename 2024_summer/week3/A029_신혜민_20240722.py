def door_problem(n: int, first: int) -> list:
    if n >= 6:
        return ["Love is open door"]
    else:
        results = []
        for i in range(1, n):
            first = 1 - first
            results.append(first)
        return results
