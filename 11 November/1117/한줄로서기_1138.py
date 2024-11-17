N = int(input())
people = list(map(int, input().split()))

dp = [0] * N

for i in range(N):
    count = 0
    for j in range(N):
        if dp[j] == 0 and count == people[i]:
            dp[j] = i + 1
            break
        elif dp[j] == 0:
            count += 1

print(*dp)