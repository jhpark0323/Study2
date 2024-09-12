# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

# 스택 구현
stack = []
N = int(input())  # 첫 번째 입력은 명령어의 개수

for _ in range(N):
    alpha = input().split()
    
    if alpha[0] == 'push':
        stack.append(alpha[1])
    
    elif alpha[0] == 'pop':
        print(stack.pop() if stack else -1)
    
    elif alpha[0] == 'size':
        print(len(stack))
    
    elif alpha[0] == 'empty':
        print(0 if stack else 1)
    
    elif alpha[0] == 'top':
        print(stack[-1] if stack else -1)
