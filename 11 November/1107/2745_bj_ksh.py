num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 백준에서 입력을 받을 때 input() 함수 사용
N, B = input().split()
B = int(B)  # B를 정수로 변환

result = 0
for i, num in enumerate(N[::-1]):  # N을 뒤집고 각 자리마다 접근
    result += B ** i * num_list.index(num)  # num_list에서 해당 문자 인덱스를 찾아서 계산

print(result)