N = int(input())

aptmap = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    aptmap[x][y] = 0
    count = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and  0 <= ny < N and aptmap[nx][ny] == 1:
            count += dfs(nx, ny)
    
    return count

danji_count = 0
danji = []

for i in range(N):
    for j in range(N):
        if aptmap[i][j] == 1:
            danji.append(dfs(i, j))
            danji_count += 1

danji.sort()
print(danji_count)
for house in danji:
    print(house)