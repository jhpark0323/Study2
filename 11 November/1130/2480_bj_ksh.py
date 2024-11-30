x, y, z = map(int, input().split())

if x == y == z:
    print(10000 + x * 1000)
elif x == y or x == z:
    print(1000 + x * 100)
elif y == z:
    print(1000 + y * 100)
else:
    print(100 * max(x, y, z))