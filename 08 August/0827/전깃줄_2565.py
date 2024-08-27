# 이거 최대 증가 부분 수열임;;
# dp류에 수열 적용이 가능 하네요

N = int(input())
wires = [tuple(map(int, input().split())) for _ in range(N)]

wires.sort(key=lambda x: x[0])
b_values = [b for _, b in wires]

dp = [1] * len(b_values)
for i in range(1, len(b_values)):
    for j in range(i):
        if b_values[i] > b_values[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# dp의 최댓값이 최대 부분 증가 수열이므로
# 전체 전깃줄 수에서 저걸 빼주면 제거할 전깃줄의 최솟값

wires_length = N - max(dp)
print(wires_length)