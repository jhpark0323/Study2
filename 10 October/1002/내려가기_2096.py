## 파이썬은 터짐... 파이파이로 돌아감
def max_min_score(n, scores):
    dp_max_prev = scores[0][:]
    dp_min_prev = scores[0][:]

    for i in range(1, n):
        dp_max_curr = [0] * 3
        dp_min_curr = [0] * 3

        dp_max_curr[0] = scores[i][0] + max(dp_max_prev[0], dp_max_prev[1])
        dp_max_curr[1] = scores[i][1] + max(dp_max_prev[0], dp_max_prev[1], dp_max_prev[2])
        dp_max_curr[2] = scores[i][2] + max(dp_max_prev[1], dp_max_prev[2])

        dp_min_curr[0] = scores[i][0] + min(dp_min_prev[0], dp_min_prev[1])
        dp_min_curr[1] = scores[i][1] + min(dp_min_prev[0], dp_min_prev[1], dp_min_prev[2])
        dp_min_curr[2] = scores[i][2] + min(dp_min_prev[1], dp_min_prev[2])

        dp_max_prev = dp_max_curr
        dp_min_prev = dp_min_curr

    max_score = max(dp_max_prev)
    min_score = min(dp_min_prev)

    return max_score, min_score

n = int(input())
scores = [list(map(int, input().split())) for _ in range(n)]
max_result, min_result = max_min_score(n, scores)
print(max_result, min_result)