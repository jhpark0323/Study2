odds = []

for _ in range(7):
    N = int(input())
    if N % 2:
        odds.append(N)

if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)