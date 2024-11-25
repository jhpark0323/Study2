X = int(input())
N = int(input())

sums = 0
for i in range(N):
  price, cnt = map(int, input().split())
  sums += (price * cnt)

if X == sums:
  print("Yes")
else:
  print("No")