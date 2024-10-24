class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 전위 순회
def pre_order(node):
    if node is not None:
        print(node.value, end='')  # 루트
        pre_order(node.left)       # 왼쪽 자식
        pre_order(node.right)      # 오른쪽 자식

# 중위 순회
def in_order(node):
    if node is not None:
        in_order(node.left)        # 왼쪽 자식
        print(node.value, end='')  # 루트
        in_order(node.right)       # 오른쪽 자식

# 후위 순회
def post_order(node):
    if node is not None:
        post_order(node.left)      # 왼쪽 자식
        post_order(node.right)     # 오른쪽 자식
        print(node.value, end='')  # 루트

def build_tree(nodes):
    tree = {}
    for node, left, right in nodes:
        if node not in tree:
            tree[node] = Node(node)
        if left != '.':
            tree[node].left = Node(left) if left not in tree else tree[left]
            tree[left] = tree[node].left
        if right != '.':
            tree[node].right = Node(right) if right not in tree else tree[right]
            tree[right] = tree[node].right
    return tree

N = int(input())
nodes = [input().split() for _ in range(N)]

tree = build_tree(nodes)

root = tree['A'] # A는 항상 루트 노드

pre_order(root)
print()
in_order(root)
print()
post_order(root)