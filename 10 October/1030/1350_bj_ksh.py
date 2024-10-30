N = int(input())
files = list(map(int, input().split()))
C = int(input())

disk = 0
for file in files:
    if file%C == 0:
        disk += file
    else:
        disk += (file//C + 1) * C

print(disk)