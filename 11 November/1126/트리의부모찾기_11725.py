from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N + 1)

def bfs():
    que = deque([1])
    while que:
        node = que.popleft()
        for neighbor in graph[node]:
            if parent[neighbor] == 0:
                parent[neighbor] = node
                que.append(neighbor)

bfs()

for i in range(2, N + 1):
    print(parent[i])