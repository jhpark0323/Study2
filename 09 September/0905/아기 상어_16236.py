# import sys
# from collections import deque
#
# input = sys.stdin.readline
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# fish = []
# for i in range(n):
#     for j in range(n):
#         # 상어의 위치
#         if arr[i][j] == 9:
#             shark = [i, j]
#
#         # 물고기들의 크기, 위치
#         elif arr[i][j]:
#             fish.append([arr[i][j], i, j])
#
# di = [-1, 0, 1, 0]
# dj = [0, -1, 0, 1]
#
# def bfs(shark_r, shark_c, shark_size, time):
#     visited = [[0] * n for _ in range(n)]
#     visited[shark_r][shark_c] = 1
#     arr[shark_r][shark_c] = 0
#     q = deque([[shark_size, shark_r, shark_c, time]])
#     eat = 0
#
#     while q:
#         size, row, col, time = q.popleft()
#
#         # 종료 조건
#         # 그 위치에 물고기 존재 and 물고기보다 상어의 사이즈가 크면
#         if arr[row][col] and arr[row][col] < size:
#             # 물고기 제거
#             print(fish)
#             print([arr[row][col], row, col])
#             fish.remove([arr[row][col], row, col])
#             arr[row][col] = 0
#
#             # 사이즈 증가
#             if eat + 1 == size:
#                 eat = 0
#                 size += 1
#             else:
#                 eat += 1
#
#             # 남아있는 물고기 확인
#             for left_fish in fish:
#                 # 남은 물고기 중에 사이즈 작은게 있으면
#                 if left_fish[0] < size:
#                     # visited 초기화
#                     visited = [[0] * n for _ in range(n)]
#                     visited[row][col] = 1
#                     # q 초기화
#                     q = deque([[size, row, col, time]])
#                     print("size : ", size)
#                     break
#             # 남은 물고기가 없으면
#             else:
#                 return time
#
#             continue
#
#         for dij in range(4):
#             next_r = row + di[dij]
#             next_c = col + dj[dij]
#
#             if 0 <= next_r < n and 0 <= next_c < n and not visited[next_r][next_c] and arr[next_r][next_c] <= size:
#                 visited[next_r][next_c] = 1
#                 q.append([size, next_r, next_c, time+1])
#
#         # q 우선순위 다시 정해주기
#
#
# if not fish:
#     print(0)
# else:
#     print(bfs(shark[0], shark[1], 2, 0))


from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
m = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j
        elif graph[i][j]:
            m += 1

size = 2
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]


def bfs(x, y, visited):
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y, 0))
    temp = 0
    selected = (n, n, -1)
    while queue:
        x, y, s = queue.popleft()
        if temp != s and selected[-1] != -1:
            return selected
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] or graph[nx][ny] > size:
                continue
            if graph[nx][ny] and graph[nx][ny] < size:
                selected = min(selected, (nx, ny, s + 1))
            visited[nx][ny] = 1
            queue.append((nx, ny, s + 1))
        temp = s
    return (-1, -1, -1)


result, count = 0, 0
graph[x][y] = 0
while 1:
    visited = [[0] * n for _ in range(n)]
    x, y, s = bfs(x, y, visited)
    if s == -1:
        break
    graph[x][y] = 0
    result += s
    count += 1
    if count == size:
        size += 1
        count = 0

print(result)