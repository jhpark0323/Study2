# 얘도 파이파이로 돌려야 시간초과안남 ㅇㅇ
import heapq

N = int(input())
lectures = []

for _ in range(N):
    S, T = map(int, input().split())
    lectures.append((S, T))

lectures.sort()

heap = []

heapq.heappush(heap, lectures[0][1])

for i in range(1, N):
    if heap[0] <= lectures[i][0]:
        heapq.heappop(heap)
    
    heapq.heappush(heap, lectures[i][1])

print(len(heap))