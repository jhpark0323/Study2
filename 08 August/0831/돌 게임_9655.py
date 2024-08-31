n = int(input())

dp = [0] * (n+1)
# 상근 win
dp[1] = 1

if n >= 3:
    dp[3] = 1

for i in range(4, n+1):
    if dp[i-1] == 1 or dp[i-3] == 1:
        continue
    else:
        dp[i] = 1

if dp[n] == 1:
    print('SK')
else:
    print('CY')