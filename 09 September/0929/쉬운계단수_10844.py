MOD = 1000000000 # 이걸로 나눠요

N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]  # 마지막 자리가 0이면 1만 가능
        elif j == 9:
            dp[i][j] = dp[i-1][8]  # 마지막 자리가 9면 8만 가능
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD
result = sum(dp[N]) % MOD

print(result)