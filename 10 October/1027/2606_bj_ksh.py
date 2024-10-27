import sys
from collections import deque
input = sys.stdin.readline

N = int(input())   # 컴퓨터의 수 N
C = int(input())   # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
adjl = [[] for _ in range(N+1)]
for _ in range(C):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

def bfs():
    q = deque()
    count = 0   # 감염된 컴퓨터 수
    q.append(1)
    visited[1] = True
    while q:
        cur = q.popleft()
        for i, val in enumerate(adjl[cur]):   # 감염된 컴퓨터로부터 연결된 컴퓨터들에서
            if visited[val] == False:   # 감염되지 않았다면
                q.append(val)   # 감염 리스트에 추가
                visited[val] = True   # 감염완료
                count += 1   # 감염된 컴퓨터 수 1 증가
    print(count)   # 모두 감염되었을 때 결과 출력

visited = [False for _ in range(N+1)]
bfs()