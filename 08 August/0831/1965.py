# 증가하는 부분 수열은 goat다...
def longest_box(sizes):
    n = len(sizes)
    if n == 0:
        return 0
    
    dp = [1] * n  # 각 상자에서 시작하는 가장 긴 증가하는 부분 수열의 길이는 최소 1
    
    for i in range(1, n):
        for j in range(i):
            if sizes[j] < sizes[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# 입력 예시
n = int(input())
sizes = list(map(int, input().split()))

# 결과 출력
print(longest_box(sizes))
