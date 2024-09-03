def max_happiness(N, L, J):
    # 최대 체력 값은 100
    max_health = 100

    dp = [0] * (max_health + 1)
    
    # 각 사람에 대해 DP 테이블 업데이트
    for i in range(N):
        lost_health = L[i]
        happiness = J[i]
        
        # 뒤에서부터 갱신(중복 계산 방지용)
        for h in range(max_health, lost_health - 1, -1):
            dp[h] = max(dp[h], dp[h - lost_health] + happiness)
    
    return max(dp[1:max_health])

N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

print(max_happiness(N, L, J))
