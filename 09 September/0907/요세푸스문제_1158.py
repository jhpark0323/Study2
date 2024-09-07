from collections import deque

def josephus_problem(n, k):
    dq = deque(range(1, n+1))  # 1부터 n까지의 숫자를 deque에 삽입
    result = []
    
    while dq:
        dq.rotate(-(k-1))  # 왼쪽으로 k-1만큼 회전
        result.append(dq.popleft())  # 가장 앞의 원소를 제거하고 결과에 추가
    
    return result


n, k = map(int, input().split())
result = josephus_problem(n, k)
print(f"<{', '.join(map(str, result))}>")

