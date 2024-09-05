def max_stair_score(n, scores):
    if n == 0:
        return 0
    if n == 1:
        return scores[0]
    if n == 2:
        return scores[0] + scores[1]

    # dp 배열을 초기화
    dp = [0] * n
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2] + scores[i],  # 두 계단을 밟고 오는 경우
                    dp[i-3] + scores[i-1] + scores[i])  # 연속된 세 계단 방지

    # 마지막 계단을 반드시 밟아야 하므로 dp[n-1]을 반환
    return dp[n-1]

n = int(input())
scores = [int(input()) for _ in range(n)]

print(max_stair_score(n, scores))
