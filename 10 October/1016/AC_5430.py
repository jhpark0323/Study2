from collections import deque

def AC(p, arr):
    reverse = False
    dq = deque(arr)

    for word in p:
        if word == 'R':
            reverse = not reverse
        elif word == 'D':
            if dq:
                if reverse:
                    dq.pop()
                else:
                    dq.popleft()
            else:
                return 'error'
    if reverse:
        dq.reverse()
    return list(dq)

T = int(input())

for _ in range(T):
    p = input().strip() # R 이나 D, 뒤집기 / 첫 번째 수 버리기 배열이 없는데 D는 에러
    n = int(input())
    arr = input().strip()[1:-1]
    if arr:
        arr2 = list(map(int, arr.split(',')))
    else:
        arr2 = []

    result = AC(p, arr2)
    if result == 'error':
        print('error')
    else:
        print(f"[{','.join(map(str, result))}]")