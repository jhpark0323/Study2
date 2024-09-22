from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
def bfs(shark_x, shark_y, shark_size):
    visited = [[-1] * N for _ in range(N)]
    visited[shark_x][shark_y] = 0
    queue = deque([(shark_x, shark_y)])
    fish_list = []

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                # 지날 수 있음
                if space[nx][ny] <= shark_size:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

                    # 먹을 수 있음
                    if 0 < space[nx][ny] < shark_size:
                        fish_list.append((visited[nx][ny], nx, ny))

    # 먹을 수 있는 것 중 가장 가까운 것
    if fish_list:
        fish_list.sort() 
        return fish_list[0]
    else:
        return None  # 못먹음

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

shark_size = 2
shark_x, shark_y = 0, 0
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            shark_x, shark_y = i, j
            space[i][j] = 0  # 상어위치

time = 0
eat_count = 0

while True:
    result = bfs(shark_x, shark_y, shark_size)

    if result is None:  # 더 못먹음
        break

    dist, fish_x, fish_y = result
    time += dist  # 이동 
    shark_x, shark_y = fish_x, fish_y  # 상어 위치 변경
    space[fish_x][fish_y] = 0  # 물고기 먹었음
    eat_count += 1

    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

print(time)
