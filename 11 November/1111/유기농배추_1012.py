import sys
sys.setrecursionlimit(10**6)

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    visited[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if arr[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny)

for _ in range(T):
    M, N, K = list(map(int, input().split())) # 가로, 세로, 배추 개수
    arr = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
    bug = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visited[i][j]:
                dfs(j, i)
                bug += 1
    
    print(bug)