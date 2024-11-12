nums = {}

for _ in range(10):
    N = int(input())
    if N in nums:
        nums[N] += 1
    else:
        nums[N] = 1

sums = 0
mx = 0
M = 0
for i in nums:
    sums += i * nums[i]
    if nums[i] >= mx:
        mx = nums[i]
        M = i

print(sums // 10)
print(M)