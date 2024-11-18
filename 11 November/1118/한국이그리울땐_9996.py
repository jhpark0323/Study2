# * 이 하나니까 저거 기준으로 잘라서 하면 됨
N = int(input())
pattern = input().strip()
target = pattern.index('*')
prefix = pattern[:target]
suffix = pattern[target + 1:]

for _ in range(N):
    name = input().strip()

    if len(name) < len(prefix) + len(suffix):
        print('NE')
        continue

    if name[:len(prefix)] == prefix and name[-len(suffix):] == suffix:
        print('DA')
    else:
        print('NE')
