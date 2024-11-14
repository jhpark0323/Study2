first = int(input())
board = [[2]*3 for _ in range(3)]
for _ in range(9):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    winner = 0

    if first == 1: board[x][y] = 1
    else: board[x][y] = 0

    result = []
    for i in range(3):
        result.append([board[i][0], board[i][1], board[i][2]])

    for i in range(3):
        result.append([board[0][i], board[1][i], board[2][i]])

    result.append([board[0][0], board[1][1], board[2][2]])
    result.append([board[0][2], board[1][1], board[2][0]])

    if [1, 1, 1] in result: winner = 1
    if [0, 0, 0] in result: winner = 2

    if winner == 0:
        flag = False
        for i in range(len(result)):
            if 2 in result[i]: flag = True
        if not flag: winner = 3

    if winner > 0: break

    if first == 1: first = 2
    else: first = 1

if winner < 3: print(winner)
else: print(0)