import sys
from heapq import heappush, heappop
input = sys.stdin.readline
v, e, p = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(e)]

def dijkstra(start):
    path = [inf] * (v + 1)
    path[start] = 0
    pq = []
    heappush(pq, [0, start])

    while pq:
        cur_w, cur = heappop(pq)

        if path[cur] < cur_w:
            continue

        for dij in graph[cur]:
            next_w = cur_w + dij[0]
            next_e = dij[1]

            if path[next_e] >= next_w:
                path[next_e] = next_w
                heappush(pq, [next_w, next_e])
    return path

graph = [[] for _ in range(v+1)]
for i in range(e):
    start, end, weight = arr[i]
    graph[start].append([weight, end])
    graph[end].append([weight, start])

inf = float('inf')

shortest = dijkstra(1)[v]
p_shortest = dijkstra(1)[p] + dijkstra(p)[v]

if shortest == p_shortest:
    print('SAVE HIM')
else:
    print('GOOD BYE')
