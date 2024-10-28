N = int(input())   # 통화의 개수 N
calls = list(map(int, input().split()))   # 통화 시간 N개

# 영식 | 10원/30초
# 민식 | 15원/60초

Y, M = 0, 0
for call in calls:
    Y += (call//30 + 1) * 10
    M += (call//60 + 1) * 15

if Y == M:
    print('Y M', Y)
elif Y < M:
    print('Y', Y)
else:
    print('M', M)