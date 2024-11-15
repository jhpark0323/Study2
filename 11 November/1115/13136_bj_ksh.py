R, C, N = map(int, input().split())

x, y = R // N, C // N

if R % N != 0:
    x += 1
if C % N != 0:
    y += 1

print(x * y)