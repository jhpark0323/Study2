# 검정 1, 흰 2
# 검정 승 1, 흰 승 2 출력 // 둘째줄에 가장 왼쪽(가장 위)에 있는 알의 좌표를 출력 

# dx = [-1, -1, -1, 0, 0, 1, 1, 1]
# dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# def winning(x, y, player, arr):
    
#     for direction in range(8):
#         count = 1
#         nx, ny = x, y

#         while True:
#             nx += dx[direction]
#             ny += dy[direction]

#             if 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] == player:
#                 count += 1
#             else:
#                 break
    
#         if count == 5:
#             px = x - dx[direction]
#             py = y - dy[direction]
#             if 0 <= px < 19 and 0 <= py < 19 and arr[px][py] == player:
#                 continue
#             return True
#         return False

# arr = [list(map(int, input().split())) for _ in range(19)]

# for i in range(19):
#     for j in range(19):
#         if arr[i][j] != 0 and winning(i, j, arr[i][j], arr):
#             print(arr[i][j])
#             print(i+1, j+1)
#             exit()

# print(0)

# 위 코드는 8방향 탐색해서 i,j 가 가장 오른쪽 하단으로 잡힘..

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def winning(x, y, player, arr):
    for direction in range(4):
        count = 1
        nx, ny = x, y

        while True:
            nx += dx[direction]
            ny += dy[direction]

            if 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] == player:
                count += 1
            else:
                break

        if count == 5:
            px = x - dx[direction]
            py = y - dy[direction]
            if 0 <= px < 19 and 0 <= py < 19 and arr[px][py] == player:
                continue
            return True
    return False

arr = [list(map(int, input().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        if arr[i][j] != 0 and winning(i, j, arr[i][j], arr):
            print(arr[i][j])
            print(i+1, j+1)
            exit()

print(0)