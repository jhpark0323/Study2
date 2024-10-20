import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

data = []
for _ in range(N):
    data.append(input().strip())

word_count = defaultdict(int) # 디폴트 값은 0

for i in range(N):
    word = data[i]
    if len(word) >= M:
        word_count[word] += 1
sorted_words = sorted(word_count.keys(), key= lambda x: (-word_count[x], -len(x), x))

sys.stdout.write("\n".join(sorted_words) + "\n")