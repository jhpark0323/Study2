from collections import deque

M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

que = deque()

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            que.append((i, j))

def bfs():
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                que.append((nx, ny))

bfs()

count = 0
for row in tomatoes:
    for value in row:
        if value == 0:
            print(-1)
            exit()
        count = max(count, value)
print(count - 1)