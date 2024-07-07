def treasure(A, B):
    A.sort()
    B.sort(reverse=True)
    return sum(a * b for a, b in zip(A, B))

A = [1, 1, 1, 6, 0]
B = [2, 7, 8, 3, 1]
print(treasure(A, B))  