import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())   # 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
adjl = [[] for _ in range(M)]
for _ in range(M):
    i, j = map(int, input().split())
    adjl[i].append(j)
    adjl[j].append(i)

# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
# V부터 방문된 점을 순서대로 출력하면 된다.

# DFS
stack = [V]
visited = [0] * (N+1)
while stack:
    t = stack.pop()
    if visited[t]:
        for i in visited[t]:
            if visited[i]
