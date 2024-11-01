import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())   # 도시의 가로 크기 N, 세로 크기 M
city = []
for _ in range(M):   # 도시의 형태를 나타내는 N개의 정수
    city.append(list(map(int, input().split())))

# city : 각 칸이 1이면 진우가 갈 수 있고, 0이면 진우가 갈 수 없다.
# (0, 0) 에서 출발해서 (N-1, M-1)에 도착해야 한다.

q = deque()
q.append([0, 0])
visited = [[0]*N for _ in range(M)]
visited[0][0] = 1
while q:
    now = q.popleft()
    for i in adjl[now[0]][now[1]]:
