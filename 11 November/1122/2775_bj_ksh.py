for _ in range(int(input())):
    K = int(input())
    N = int(input())

    zero = [x for x in range(1, N + 1)]
    for k in range(K):
        for i in range(1, N):
            zero[i] += zero[i-1]
    print(zero[-1])