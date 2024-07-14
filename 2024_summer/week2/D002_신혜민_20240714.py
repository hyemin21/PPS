def solution():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    t = int(data[0])
    results = []
    index = 1
    for _ in range(t):
        h, w, n = map(int, data[index:index+3])
        index += 3
        floor = n % h
        room = n // h + 1
        if floor == 0:
            floor = h
            room -= 1
        results.append(floor * 100 + room)
    for result in results:
        print(result)
