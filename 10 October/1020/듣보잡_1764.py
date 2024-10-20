N, M = map(int, input().split())

listen = set(input().strip() for _ in range(N))
view = set(input().strip() for _ in range(M))

result = sorted(listen & view)
print(len(result))
for alpha in result:
    print(alpha)