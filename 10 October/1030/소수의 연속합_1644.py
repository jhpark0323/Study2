n = int(input())

ls = [1] * 4000001
ls[0] = ls[1] = 0
primes = []

for i in range(2, n+1):
    if ls[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            ls[j] = 0

# print(primes)
if n == 1:
    print(0)
    exit()
dp = [0, primes[0]]
for i in range(1, len(primes)):
    dp.append(dp[-1] + primes[i])
# print(dp)

ans = 0
left, right = 0, 1
while 0 <= right < len(primes)+1:

    if dp[right] - dp[left] == n:
        # print(dp[right], dp[left])
        ans += 1
        right += 1
    elif dp[right] - dp[left] < n:
        right += 1
    else:
        left += 1

print(ans)