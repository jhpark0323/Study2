import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

land_flatten = [height for row in land for height in row]

min_height = min(land_flatten)
max_height = max(land_flatten)

min_time = float('inf')
best_height = -1

for target_height in range(min_height, max_height + 1):
    remove_blocks = 0
    add_blocks = 0
    
    for height in land_flatten:
        if height > target_height:
            remove_blocks += height - target_height
        else:
            add_blocks += target_height - height
    if remove_blocks + b >= add_blocks:
        time = remove_blocks * 2 + add_blocks
        if time <= min_time:
            min_time = time
            best_height = target_height

print(min_time, best_height)