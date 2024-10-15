import math

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    year = -1
    lcm = (M * N) // math.gcd(M, N)

    while x <= lcm: 
        if (x - 1) % N + 1 == y:
            year = x
            break
        x += M

    print(year)