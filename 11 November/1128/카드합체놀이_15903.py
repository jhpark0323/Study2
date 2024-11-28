import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

heapq.heapify(arr)

for _ in range(m):
    x = heapq.heappop(arr)
    y = heapq.heappop(arr)
    new_value = x + y
    heapq.heappush(arr, new_value)
    heapq.heappush(arr, new_value)

print(sum(arr))