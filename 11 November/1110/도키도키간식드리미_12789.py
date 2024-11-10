import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

stack = []
check = 1

for i in range(N):
    while stack and stack[-1] == check:
        stack.pop()
        check += 1
    
    if arr[i] == check:
        check += 1
    else:
        stack.append(arr[i])

while stack and stack[-1] == check:
    stack.pop()
    check += 1

if check == N + 1:
    print('Nice')
else:
    print('Sad')