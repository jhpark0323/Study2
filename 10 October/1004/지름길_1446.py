import heapq

n, d = map(int, input().split())
shortcuts = []
for _ in range(n):
    start, end, length = map(int, input().split())
    if end <= d:
        shortcuts.append((start, end, length))

dist = [i for i in range(d + 1)]

for i in range(d + 1):
    if i > 0:
        dist[i] = min(dist[i], dist[i - 1] + 1)

    for start, end, length in shortcuts:
        if i == start and end <= d and dist[i] + length < dist[end]:
            dist[end] = dist[i] + length

print(dist[d])