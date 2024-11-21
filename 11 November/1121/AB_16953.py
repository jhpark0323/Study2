# *2 또는 1을 수의 오른쪽에 추가
from collections import deque

def bfs(A, B):
    queue = deque([(A, 1)])

    while queue:
        current, count = queue.popleft()

        if current == B:
            return count
        
        if current * 2 <= B:
            queue.append((current * 2, count + 1))
        
        if current * 10 + 1 <= B:
            queue.append((current * 10 + 1, count + 1))

    return -1

A, B = map(int, input().split())

print(bfs(A, B))