n = int(input())  # 손님의 수
customer = list(map(int, input().split()))  # 손님이 앉고 싶어하는 자리
cnt = 0  # 거절당하는 사람의 수
seat = []  # 피시방 자리
for i in range(n):
    if customer[i] in seat:         # 앉고 싶어하는 자리에 사람이 있으면
        cnt += 1                    # 거절
    else:                           # 없으면
        seat.append(customer[i])    # 자리에 앉음
print(cnt)