def solution():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        line = data[i]
        left, right = [], []
        for char in line:
            if char == '-':
                if left:
                    left.pop()
            elif char == '<':
                if left:
                    right.append(left.pop())
            elif char == '>':
                if right:
                    left.append(right.pop())
            else:
                left.append(char)
        results.append(''.join(left) + ''.join(reversed(right)))
    for result in results:
        print(result)
