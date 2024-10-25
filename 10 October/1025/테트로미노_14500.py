n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 테트로미노 모양 구현 ㄷㄷㄷ
tetrominoes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, -1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, -1), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, -1), (1, -2)],
    
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 0)],
    [(0, 1), (1, 0), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (0, 1), (2, 1)],
    
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 1), (0, 2), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (2, 0), (0, 1), (1, 1)]
]

def is_valid(x, y, shape):
    for dx, dy in shape:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            return False
    return True

def get_sum(x, y, shape):
    return sum(board[x + dx][y + dy] for dx, dy in shape)

max_sum = 0
for i in range(n):
    for j in range(m):
        for shape in tetrominoes:
            if is_valid(i, j, shape):
                max_sum = max(max_sum, get_sum(i, j, shape))

print(max_sum)