# 2원과 5원짜리로만 거스름돈...
# 동전의 개수가 최소가 되도록
# 거스름돈이 n, 못 거슬러주면 -1 출력

n = int(input())

dp = [float('inf')] * (n+1)

if n >= 2:
  dp[2] = 1
if n >= 5:
  dp[5] = 1

for i in range(3, n + 1):
  if i >= 2:
    dp[i] = min(dp[i], dp[i-2] + 1)
  if i >= 5:
    dp[i] = min(dp[i], dp[i-5]+1)

# print(dp)
if dp[n] == float('inf'):
  print(-1)
else:
  print(dp[n]) 