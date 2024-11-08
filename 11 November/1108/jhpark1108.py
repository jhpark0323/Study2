def find_initial_passengers(k):
    passengers = 0  # 마지막 정류장에서 승객 수가 0명이므로 초기화
    for _ in range(k):
        passengers = (passengers * 2) + 1
    return passengers

# 입력 처리 및 결과 출력
t = int(input())  # 테스트 케이스 수
for _ in range(t):
    k = int(input())  # 정류장 수
    print(find_initial_passengers(k))
