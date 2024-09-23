# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]
dp[0][0] = cost[0][0]  # 빨
dp[0][1] = cost[0][1]  # 초
dp[0][2] = cost[0][2]  # 파

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]  # 빨
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]  # 초
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]  # 파

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))
