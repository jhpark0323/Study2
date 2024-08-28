import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))

up = [1 for _ in range(n)]
down = [0 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if ls[j] < ls[i]:
            up[i] = max(up[j]+1, up[i])

for i in range(n-1, -1, -1):
    for j in range(i, n):
        if ls[j] < ls[i]:
            down[i] = max(down[i], down[j]+1)

ans = 0
for i in range(n):
    ans = max(ans, up[i] + down[i])

print(ans)