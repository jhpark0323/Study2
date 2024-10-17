# 0 빈칸 1 벽 2 바이러스, 벽은 3개 추가가능
# 바이러스는 벽이 없는 인접 영역으로 확산 가능
# 안전 영역의 최대 크기 출력
from itertools import combinations
from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(lab, virus, n, m):
    dq = deque(virus)
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                dq.append((nx, ny))

def safe_area(lab, n, m):
    area = 0
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                area += 1
    return area

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

empty = []
virus = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

max_area = 0

for walls in combinations(empty, 3):
    new_lab = copy.deepcopy(lab)

    for x, y in walls:
        new_lab[x][y] = 1
    
    bfs(new_lab, virus, N, M)
    area = safe_area(new_lab, N, M)
    max_area = max(area, max_area)

print(max_area)