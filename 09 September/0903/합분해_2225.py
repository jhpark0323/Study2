from pprint import pprint

n, k = map(int, input().split())

arr = [[1] * (k+1) for _ in range(n+1)]

for i in range(1, k+1):
    for j in range(1, n+1):
        if i == 1:
            continue

        elif i == 2:
            arr[j][i] = j+1

        else:
            arr[j][i] = arr[j-1][i] + arr[j][i-1]

# pprint(arr)
print(arr[n][k] % 1000000000)