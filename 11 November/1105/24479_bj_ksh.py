C = 1
def dfs(adjl, t, visited):
    global C
    visited[t] = C

    for i in adjl[t]:
        if visited[i] == 0:
            C += 1
            dfs(adjl, i, visited)   # 재귀

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
adjl = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    adjl[u].append(v)
    adjl[v].append(u)

for a in adjl:
    a.sort()

dfs(adjl, R, visited)

for i in range(1, N+1):
    print(visited[i])
