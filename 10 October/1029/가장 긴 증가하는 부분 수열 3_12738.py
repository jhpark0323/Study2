n = int(input())
ls = list(map(int, input().split()))

def binary(target):
    left, right = 0, len(ans)-1
    while left < right:
        mid = (left + right)//2

        if ans[mid] == target:
            return mid

        if ans[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

ans = [ls[0]]

for i in range(1, n):
    if ls[i] > ans[-1]:
        ans.append(ls[i])
    else:
        idx = binary(ls[i])
        ans[idx] = ls[i]

print(len(ans))