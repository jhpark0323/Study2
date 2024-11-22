import sys
input = sys.stdin.readline

string = list(input().strip())
M = int(input())
left = string 
right = []
for _ in range(M):
    command = input().strip()
    
    if command.startswith('P'):
        _, char = command.split()
        left.append(char)
    elif command[0] == 'L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'B':
        if left:
            left.pop()

print(''.join(left + right[::-1]))