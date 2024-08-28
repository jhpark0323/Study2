# 돌은 1개 또는 3개 가져갈 수 있다.
# 상근이가 먼저 시작한다
# 상근이가 이기면 SK, 창영이가 이기면 CY를 출력한다.
N = int(input())

dp = [0] * (N+1) # dp[N]이 1이면 상근 승, 0이면 창영 승

dp[1] = 1
if N >= 2:
  dp[2] = 0
if N >= 3:  
  dp[3] = 1

for i in range(4, N+1):
  if dp[i-1] == 0 or dp[i-3] == 0:
    dp[i] = 1 # 상근 승
  else:
    dp[i] = 0

if dp[N] == 1:
  print('SK')
else:
  print('CY')