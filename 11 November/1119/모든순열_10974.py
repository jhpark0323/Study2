from itertools import permutations

N = int(input())
arr = []
for i in range(1, N + 1):
    arr.append(i)
for perm in permutations(arr, N):
    print(' '.join(map(str, perm)))