from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

queue = deque()
for _ in range(N):
    order = input().strip().split()
    if order[0] == 'push':
        queue.append(int(order[1]))
    elif order[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)