from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

# 다리 위 상황을 큐로 구현
bridge = deque([0] * w)  # 트럭 x
current_weight = 0 
time = 0
index = 0

while index < n or current_weight > 0:
    time += 1
    # 트럭 런
    current_weight -= bridge.popleft()
    
    # 다음에 올라가 진다?
    if index < n and current_weight + trucks[index] <= L:
        # 올라가~
        bridge.append(trucks[index])
        current_weight += trucks[index]
        index += 1
    else:
        # 못올라가면 0추가
        bridge.append(0)

print(time)