import heapq # 힙 큐는 뭐다? 신

N = int(input())

# 최소 힙 초기화
min_heap = []

for _ in range(N):
    row = list(map(int, input().split()))
    
    for num in row:
        heapq.heappush(min_heap, num)
        if len(min_heap) > N:
            heapq.heappop(min_heap)

print(min_heap[0])