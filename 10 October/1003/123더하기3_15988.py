MOD = 1000000009

t = int(input())

max_n = 1000000
dp = [0] * (max_n + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_n + 1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD

for _ in range(t):
    n = int(input())
    print(dp[n])