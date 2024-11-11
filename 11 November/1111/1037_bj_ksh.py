N = int(input())
real = list(map(int, input().split()))
real.sort()

if N == 1:
    print(real[0] ** 2)
else:
    print(real[0] * real[-1])