from collections import deque

gears = [deque(map(int, input().strip())) for _ in range(4)]

K = int(input())

operations = [list(map(int, input().split())) for _ in range(K)]

def rotate(gear, direction):
    if direction == 1:  # 시계 
        gear.appendleft(gear.pop())
    else:  # 반시계
        gear.append(gear.popleft())

for num, direction in operations:
    num -= 1
    rotate_dir = [0] * 4
    rotate_dir[num] = direction
    
    # 왼
    for i in range(num - 1, -1, -1):
        if gears[i][2] != gears[i + 1][6]:
            rotate_dir[i] = -rotate_dir[i + 1]
        else:
            break
    
    # 오
    for i in range(num + 1, 4):
        if gears[i][6] != gears[i - 1][2]:
            rotate_dir[i] = -rotate_dir[i - 1]
        else:
            break
    
    # 각각
    for i in range(4):
        if rotate_dir[i] != 0:
            rotate(gears[i], rotate_dir[i])

score = 0
for i in range(4):
    if gears[i][0] == 1:
        score += (1 << i)
        
print(score)
