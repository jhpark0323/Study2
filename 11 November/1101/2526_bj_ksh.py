n, p = map(int, input().split())

l = []  # 반복되는 숫자 저장할 배열 생성
r = n  # 초기 n 값 저장 + 나머지 저장 할 변수

while True:  # 조건 맞을때까지 무한반복
    r = (r * n) % p
    if r in l:
        print(len(l) - l.index(r))  # 마지막 반복 숫자 인덱스 차감
        break
    l.append(r)
