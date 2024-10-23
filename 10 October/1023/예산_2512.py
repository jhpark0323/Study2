N = int(input())
arr = list(map(int, input().split()))
M = int(input())

min_asset = 0
max_asset = max(arr)
result = 0

while min_asset <= max_asset:
    mid = (min_asset + max_asset) // 2
    total = 0

    for i in arr:
        total += min(i, mid)
    
    if total <= M:
        result = mid
        min_asset = mid + 1
    else:
        max_asset = mid - 1

print(result)