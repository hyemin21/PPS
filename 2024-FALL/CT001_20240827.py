"""
https://school.programmers.co.kr/learn/courses/30/lessons/250136
프로그래머스 - PCCP 기출문제 <석유 시추>

세로 길이 n, 가로 길이 m인 격자 모양의 땅에서 석유는 덩어리로 나눠져서 묻혀져 있음
가장 많은 석유를 뽑을 수 있는 시추관의 위치를 찾아야 함
"""

def dfs(x, y, land, visited, oil_id, oil_map):
    n = len(land)
    m = len(land[0])
    stack = [(x, y)]
    size = 0
    
    while stack:
        cx, cy = stack.pop()
        if visited[cx][cy]:
            continue
        visited[cx][cy] = True
        oil_map[cx][cy] = oil_id
        size += 1
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and not visited[nx][ny]:
                stack.append((nx, ny))
    
    return size

def solution(land):
    n = len(land)
    m = len(land[0])
    
    visited = [[False] * m for _ in range(n)]
    oil_map = [[-1] * m for _ in range(n)]
    oil_sizes = []
    
    oil_id = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                size = dfs(i, j, land, visited, oil_id, oil_map)
                oil_sizes.append(size)
                oil_id += 1
    
    max_oil = 0
    for col in range(m):
        current_oil = set()
        oil_sum = 0
        for row in range(n):
            if oil_map[row][col] != -1:
                oil_chunk = oil_map[row][col]
                if oil_chunk not in current_oil:
                    oil_sum += oil_sizes[oil_chunk]
                    current_oil.add(oil_chunk)
        max_oil = max(max_oil, oil_sum)
    
    return max_oil
