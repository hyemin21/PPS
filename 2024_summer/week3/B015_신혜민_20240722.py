n = int(input())
stones = list(map(int, input().split()))
start = int(input()) - 1

visited = [False] * n
queue = deque([start])
visited[start] = True
count = 1

while queue:
    current = queue.popleft()
    for next_pos in (current + stones[current], current - stones[current]):
        if 0 <= next_pos < n and not visited[next_pos]:
            queue.append(next_pos)
            visited[next_pos] = True
            count += 1

print(count)
