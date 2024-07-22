def bfs(a, b, c):
    q = deque([(0, 0, c)])
    visited = set([(0, 0, c)])
    result = set()

    while q:
        x, y, z = q.popleft()
        if x == 0:
            result.add(z)
        for nx, ny, nz in ((x, y, c - x - y), (x, y, c - x - z), (x, b - x, y), (a - x, y, z), (x, b - x - z, y), (a - x - y, y, z)):
            if 0 <= nx <= a and 0 <= ny <= b and 0 <= nz <= c and (nx, ny, nz) not in visited:
                q.append((nx, ny, nz))
                visited.add((nx, ny, nz))
    return sorted(result)
