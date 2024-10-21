K, N = map(int, input().split())

length = [int(input()) for _ in range(K)]

start, end = 1, max(length)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0

    for len in length:
        total += len // mid

    if total >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)