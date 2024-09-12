import sys
from collections import deque

input = sys.stdin.readline
N = int(input()) # 주어진 명령의 수

queue = deque()

for _ in range(N):
    alpha = input().split()
    if alpha[0] == 'push_front':
        queue.appendleft(alpha[1])
    elif alpha[0] == 'push_back':
        queue.append(alpha[1])
    elif alpha[0] == 'pop_front':
        print(queue.popleft() if queue else -1)
    elif alpha[0] == 'pop_back':
        print(queue.pop() if queue else -1)
    elif alpha[0] == 'size':
        print(len(queue))
    elif alpha[0] == 'empty':
        print(1 if not queue else 0)
    elif alpha[0] == 'front':
        print(queue[0] if queue else -1)
    else:
        print(queue[-1] if queue else -1)