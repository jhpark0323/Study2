import sys
from collections import Counter

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

# 반올림
mean = round(sum(numbers) / N)

# 중앙값
numbers.sort()
median = numbers[N // 2]

# 최빈값
counter = Counter(numbers)
modes = counter.most_common()

# 최빈값 중 두 번째
max_frequency = modes[0][1]
mode_candidates = [mode[0] for mode in modes if mode[1] == max_frequency]

if len(mode_candidates) > 1:
    mode = sorted(mode_candidates)[1]
else:
    mode = mode_candidates[0]

# 범위
range_value = max(numbers) - min(numbers)

print(mean)
print(median)
print(mode)
print(range_value)
