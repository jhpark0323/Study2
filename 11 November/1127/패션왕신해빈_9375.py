import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    clothes = defaultdict(int)
    for _ in range(n):
        name, cate = input().strip().split()
        clothes[cate] += 1
    
    result = 1
    for count in clothes.values():
        result *= (count + 1)
    
    print(result - 1)