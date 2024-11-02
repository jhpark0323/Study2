N, M = map(int, input().split())
baskets = list(range(1, N+1))
for _ in range(M):
    i, j = map(int, input().split())
    baskets = baskets[0:i-1] + list(reversed(baskets[i-1:j])) + baskets[j:N]

print(*baskets)