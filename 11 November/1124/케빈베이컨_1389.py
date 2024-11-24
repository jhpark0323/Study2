import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

# 플로이드-와샬
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_bacon = INF
result_node = -1

for i in range(n):
    bacon_sum = sum(graph[i])
    if bacon_sum < min_bacon:
        min_bacon = bacon_sum
        result_node = i + 1

print(result_node)