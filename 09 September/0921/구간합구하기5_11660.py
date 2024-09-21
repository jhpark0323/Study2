import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
arr = [list(map(int, data[i+1].split())) for i in range(N)]
queries = [list(map(int, data[i+1+N].split())) for i in range(M)]

sum_arr = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        sum_arr[i][j] = arr[i-1][j-1] + sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1]

result = []
for x1, y1, x2, y2 in queries:
    res = sum_arr[x2][y2] - sum_arr[x1-1][y2] - sum_arr[x2][y1-1] + sum_arr[x1-1][y1-1]
    result.append(str(res))

sys.stdout.write("\n".join(result) + "\n")
