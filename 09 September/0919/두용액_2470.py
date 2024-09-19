N = int(input())
solutions = list(map(int, input().split()))

solutions.sort()

left = 0
right = N - 1
closest_sum = float('inf')
result = (solutions[left], solutions[right])

while left < right:
    current_sum = solutions[left] + solutions[right]
    
    # 현재 합이 0에 더 가까운 경우 갱신
    if abs(current_sum) < abs(closest_sum):
        closest_sum = current_sum
        result = (solutions[left], solutions[right])
    
    # 합이 0보다 크면 왼쪽
    if current_sum > 0:
        right -= 1
    # 합이 0보다 작으면 오른쪽
    elif current_sum < 0:
        left += 1
    else:
        break

print(result[0], result[1])
