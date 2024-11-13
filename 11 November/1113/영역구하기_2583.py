import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 1
    area_size = 1

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                queue.append((nx, ny))
                area_size += 1
    
    return area_size

areas = []

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            area_size = bfs(i, j)
            areas.append(area_size)

areas.sort()
print(len(areas))
print(*areas)