import sys
input = sys.stdin.readline

square = 0
for i in range(1, int(input())+1):
    check = []
    for j in range(2, i//2+1):
        if i % j == 0:
            if j not in check:
                square += 1
                check.append(i // j)
    square += 1
print(square)
