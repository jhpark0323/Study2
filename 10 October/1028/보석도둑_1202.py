# 파이썬 시간초과, 파이파이로 되는 듯
import heapq

N, K = map(int, input().split())
jewels = []
bags = []

for _ in range(N):
    weight, value = map(int, input().split())
    jewels.append((weight, value))

for _ in range(K):
    bags.append(int(input()))

jewels.sort()
bags.sort()

result = 0
temp = []
j = 0

for bag in bags:
    while j < N and jewels[j][0] <= bag:
        heapq.heappush(temp, -jewels[j][1])
        j += 1
    
    if temp:
        result -= heapq.heappop(temp)

print(result)