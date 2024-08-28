N = int(input()) # 수열의 크기
arr = list(map(int, input().split())) # 수열 목록

dp = [1] * N

# dp[i]는 i에서 시작한 감소하는 부분 수열의 최대 길이

for i in range(N-1, -1, -1):
  for j in range(i+1, N):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
