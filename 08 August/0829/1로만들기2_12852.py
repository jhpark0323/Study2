# 1로 만들기 2
# 정수 x가 3으로 나누어떨어지면 => 조건, 3으로 나눈다
# 정수 X가 2로 나누어 떨어지면 => 조건, 2로 나눈다.
# 1을 뺀다.
# 둘째 줄에는 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력한다.
# 정답이 여러 가지인 경우에는 아무거나 출력한다.

N = int(input())  # 1~ 1000000(백만)
dp = [0] * (N + 1)
trace = [0] * (N + 1)  # 이전 숫자를 추적하기 위한 리스트

# dp[i]를 채워 나가는 과정
for i in range(2, N + 1):
    # 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    trace[i] = i - 1
    
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
        dp[i] = dp[i // 2] + 1
        trace[i] = i // 2
    
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
        dp[i] = dp[i // 3] + 1
        trace[i] = i // 3

# 최소 횟수 출력
print(dp[N])

# 경로 추적 및 출력
result = []
while N > 0:
    result.append(N)
    N = trace[N]

# 경로를 출력 (거쳐간 숫자들)
print(' '.join(map(str, result)))


  