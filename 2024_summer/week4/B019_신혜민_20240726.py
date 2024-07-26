"""
B019 - https://www.acmicpc.net/problem/10026
"""
def problem_10026(n, grid):
    from collections import deque

    def bfs(x, y, color, is_color_blind):
        queue = deque([(x, y)])
        visited[x][y] = True
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if is_color_blind:
                        if grid[nx][ny] in color:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                    else:
                        if grid[nx][ny] == color:
                            visited[nx][ny] = True
                            queue.append((nx, ny))

    visited = [[False] * n for _ in range(n)]
    normal_count = 0
    color_blind_count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, grid[i][j], False)
                normal_count += 1

    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, 'RG' if grid[i][j] in 'RG' else grid[i][j], True)
                color_blind_count += 1

    return normal_count, color_blind_count
