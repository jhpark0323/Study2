n = int(input())
ls = list(map(int, input().split()))
# print(ls)

def binary_search(ls, target):
    left, right = 0, len(ls)-1

    while left < right:
        mid = (left + right) // 2

        if ls[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left



# 가장 큰 증가하는 부분 수열
ans = [ls[0]]

for i in range(1, n):

  # 크면 그냥 append
  if ans[-1] < ls[i]:
    ans.append(ls[i])

  # 작으면 위치를 찾아서 그 인덱스에 넣어 버림
  # 이 때 숫자 자체가 바껴서 이해가 안되었었는데
  # 어짜피 우리는 ans안의 숫자랑 상관없이
  # ans의 총 길이만 구하면 되기 때문에 ㄱㅊ
  # ex) 100 10 150 12 1 2 3 4 5 6
  # -> 1 2 3 4 5 6
  # ex) 100 10 150 12 1
  # -> ans에는 1 12가 되어있겠지만
  # 결국 그것은 10 12의 경우와 동일한 느낌으로
  # 전체 ans 길이는 2가 됨
  else:
    ans[binary_search(ans, ls[i])] = ls[i]

print(len(ans))