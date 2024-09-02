import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))

dp = [1] * n

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if ls[i] > ls[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# print(dp)
print(max(dp))