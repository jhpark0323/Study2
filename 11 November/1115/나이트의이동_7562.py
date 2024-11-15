from collections import deque

T = int(input())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    chess[start_x][start_y] = 1
    
    while queue:
        x, y = queue.popleft()

        if x == x2 and y == y2:
            return chess[x][y] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < chess_len and 0 <= ny < chess_len and chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1
                queue.append((nx, ny))
    
    return -1

for _ in range(T):
    chess_len = int(input())
    x1, y1 = map(int, input().split()) # 시작점
    x2, y2 = map(int, input().split()) # 도착점
    chess = [[0] * chess_len for _ in range(chess_len)]
    result = bfs(x1, y1)
    print(result)