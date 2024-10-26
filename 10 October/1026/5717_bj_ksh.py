import sys
input = sys.stdin.readline

while 1:
    M, F = map(int, input().split())
    if M == 0 and F == 0:
        exit()
    print(M + F)