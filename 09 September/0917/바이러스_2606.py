def dfs(graph, v, visited):
    visited[v] = True  
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

N = int(input())  
M = int(input())  

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

dfs(graph, 1, visited)

print(visited.count(True) - 1)
