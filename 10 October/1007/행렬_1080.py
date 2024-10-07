def flip(matrix, x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            matrix[i][j] = 1 - matrix[i][j]

def count_flips(n, m, A, B):
    flips = 0
    
    for i in range(n - 2):
        for j in range(m - 2):
            if A[i][j] != B[i][j]:
                flip(A, i, j)
                flips += 1

    if A == B:
        return flips
    else:
        return -1

n, m = map(int, input().split())
A = [list(map(int, list(input().strip()))) for _ in range(n)]
B = [list(map(int, list(input().strip()))) for _ in range(n)]

print(count_flips(n, m, A, B))