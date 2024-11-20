N = int(input()) - 1

pibo = [0, 1]

if N < 1:
    print(pibo[N+1])
else:
    while N:
        pibo.append(pibo[-1] + pibo[-2])
        N -= 1
    print(pibo[-1])