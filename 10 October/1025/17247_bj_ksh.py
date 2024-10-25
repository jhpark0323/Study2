import sys
input = sys.stdin.readline

N, M = map(int, input().split())
points = []
for i in range(N):
    street = list(map(int, input().split()))
    if 1 in street:
        points.append([street.index(1), i])

print(abs(points[0][0] - points[1][0]) + abs(points[0][1] - points[1][1]))