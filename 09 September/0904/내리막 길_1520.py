import sys

input = sys.stdin.readline
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

visited = [[-1] * n for _ in range(m)]

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0

    for dij in range(4):
        next_x = x + di[dij]
        next_y = y + dj[dij]

        if 0 <= next_x < m and 0 <= next_y < n:
            if arr[x][y] > arr[next_x][next_y]:
                visited[x][y] += dfs(next_x, next_y)

    return visited[x][y]

print(dfs(0, 0))