"""
B020 - https://www.acmicpc.net/problem/2210
"""
def problem_2210(board):
    def dfs(x, y, num):
        if len(num) == 6:
            result.add(num)
            return
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5:
                dfs(nx, ny, num + board[nx][ny])

    result = set()
    for i in range(5):
        for j in range(5):
            dfs(i, j, board[i][j])
    return len(result)
