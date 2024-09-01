def tsp(N, W):
    # 최소는 inf
    INF = float('inf')
    dp = [[INF] * N for _ in range(1 << N)]
    
    # 시작 도시를 0으로 설정
    dp[1][0] = 0
    
    # 모든 상태를 탐색
    for mask in range(1 << N):
        for i in range(N):
            if dp[mask][i] == INF:
                continue
            for j in range(N):
                if (mask & (1 << j)) == 0 and W[i][j] > 0:
                    new_mask = mask | (1 << j)
                    dp[new_mask][j] = min(dp[new_mask][j], dp[mask][i] + W[i][j])
    
    # 모든 도시를 방문한 상태에서 출발 도시로 돌아오는 비용 계산
    final_mask = (1 << N) - 1
    result = INF
    for i in range(1, N):
        if W[i][0] > 0:
            result = min(result, dp[final_mask][i] + W[i][0])
    
    return result

# 입력 처리
N = int(input())
W = []
for _ in range(N):
    W.append(list(map(int, input().split())))

print(tsp(N, W))
