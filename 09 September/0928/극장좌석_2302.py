n = int(input())
m = int(input())  
vip = [int(input()) for _ in range(m)]

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

result = 1
previous_vip = 0

for vip_seat in vip:
    result *= dp[vip_seat - previous_vip - 1]
    previous_vip = vip_seat

result *= dp[n - previous_vip]

print(result)