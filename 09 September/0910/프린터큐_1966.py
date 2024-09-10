# 현재 queue의 가장 앞에 있는 문서의 중요도를 확인한다
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고
# queue의 가장 뒤에 재배치한다. 그렇지 않다면 바로 인쇄를 한다
from collections import deque

def printer_queue(test_cases):
    for case in test_cases:
        N, M = case['N'], case['M']
        priorities = case['priorities']

        queue = deque([(i, p) for i, p in enumerate(priorities)])
        count = 0

        while queue:
            current = queue.popleft()
            if any(current[1] < q[1] for q in queue):
                queue.append(current)
            else:
                count += 1
                if current[0] == M:
                    print(count)
                    break

T = int(input())  # 테케
test_cases = []

for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    test_cases.append({'N': N, 'M': M, 'priorities': priorities})

printer_queue(test_cases)
