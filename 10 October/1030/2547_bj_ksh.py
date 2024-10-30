for _ in range(int(input())):
    P = input()
    N = int(input())
    candies = 0
    for i in range(N):
        candies += int(input())

    if candies%N == 0:
        print('YES')
    else:
        print('NO')
