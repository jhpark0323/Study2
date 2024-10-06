n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][s] = True

for i in range(1, n + 1):
    for j in range(m + 1):
        if dp[i - 1][j]:
            if j + v[i - 1] <= m:
                dp[i][j + v[i - 1]] = True
            if j - v[i - 1] >= 0:
                dp[i][j - v[i - 1]] = True

result = -1
for i in range(m, -1, -1):
    if dp[n][i]:
        result = i
        break

print(result)