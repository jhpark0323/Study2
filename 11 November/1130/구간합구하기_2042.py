# 존내어렵노
import sys
input = sys.stdin.readline

# 세그먼트 트리를 초기화 함
# node는 현재 노드/ start, end는 현재 노드가 담당하는 범위임
def init(arr, tree, node, start, end):
    # 리프 노드, 배열의 한 원소를 담당
    if start == end:
        tree[node] = arr[start] # 리프 노드는 배열의 값을 그대로 저장함
    else:
        mid = (start + end) // 2 # 내부 노드는 자식 노드들의 합을 저장함
        # 왼쪽 자식 노드와 오른쪽 자식 노드 값의 합
        tree[node] = init(arr, tree, node * 2, start, mid) + init(arr, tree, node * 2 + 1, mid + 1, end)
    return tree[node] # 현재 노드 값을 반환하는 함수

def range_sum(tree, node, start, end, left, right):
    # 현재 노드 범위가 구간 범위와 겹치지 않음
    if left > end or right < start:
        return 0 # 구간 합에 영향 없음
    
    # 현재 노드 범위가 구간 범위에 완전히 포함
    if left <= start and end <= right:
        return tree[node] # 현재 노드 값을 반환해줌
    
    # 현재 노드 범위가 구간과 일부만 겹칠 때
    mid = (start + end) // 2
    left_sum = range_sum(tree, node * 2, start, mid, left, right)
    right_sum = range_sum(tree, node * 2 + 1, mid + 1, end, left, right)
    return left_sum + right_sum # 두 구간의 합을 반환해줌

# 배열 값을 갱신하는 함수
# idx는 갱신하는 배열의 인덱스값, diff는 변경 값
def update(tree, node, start, end, idx, diff):
    # 갱신할 인덱스가 현재 노드 범위 밖
    if idx < start or idx > end:
        return # 갱신 안함
    
    # 현재 범위 안
    tree[node] += diff
    if start != end: # 리프 노드가 아님
        mid = (start + end) // 2
        update(tree, node * 2, start, mid, idx, diff)
        update(tree, node * 2 + 1, mid + 1, end, idx, diff)

n, m, k = map(int, input().split())
arr = [0] * n
for i in range(n):
    arr[i] = int(input())

tree = [0] * (4 * n) # 세그먼트 트리 크기는 배열 크기의 4배
init(arr, tree, 1, 0, n - 1)

for _ in range(m + k):
    cmd, a, b = map(int, input().split())
    if cmd == 1:
        a -= 1
        diff = b - arr[a]
        arr[a] = b
        update(tree, 1, 0, n-1, a, diff)
    elif cmd == 2:
        a -= 1
        b -= 1
        print(range_sum(tree, 1, 0, n-1, a, b))