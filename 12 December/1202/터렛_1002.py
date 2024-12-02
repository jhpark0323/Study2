import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    count = 0
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if d == 0 and r1 == r2:
        print(-1)
    
    elif d > r1 + r2 or d < abs(r2 - r1):
        print(0)
    
    elif d == r1 + r2 or d == abs(r2 - r1):
        print(1)
    
    else:
        print(2)