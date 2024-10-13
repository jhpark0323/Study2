n = int(input())
p = list(map(int, input().split()))
result = 0
alpha = 0
sort_p = sorted(p)

for i in range(len(sort_p)):
    alpha += sort_p[i]
    result += alpha

print(result)