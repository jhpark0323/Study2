'''
S = input().strip()
K = input().strip()

# S에서 숫자를 무시하고 K와 일치하는 부분이 있는지 확인
i = 0
found = False
while i <= len(S) - len(K):
    j = 0
    while j < len(K) and (i + j) < len(S) and (S[i + j].isalpha() and S[i + j] == K[j]):
        j += 1
    if j == len(K):  # K가 일치하는 경우
        found = True
        break
    i += 1

print(1 if found else 0)
'''

'''
S = input()
K = input()

# 숫자가 아닌 문자만 남긴 후 문자열로 결합
note = ''.join(filter(str.isalpha, S))

# `K`가 `note`에 포함되는지 확인
if K in note:
    print(1)
else:
    print(0)
'''

'Python3'
S = list(input())
K = input()

N = []
for x in S:
    try:
        x = int(x)
    except:
        N.append(x)

note = ''.join(N)

if K in note:
    print(1)
else:
    print(0)