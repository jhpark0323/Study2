E, S, M = map(int, input().split())   # 15, 28, 19
year = 1

while 1:
    if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
        break
    year += 1

print(year)