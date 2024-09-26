# 프로그래머스 도넛과 막대 그래프

# bfs로 하면 잘 안됨
# from collections import deque

# def solution(edges):
#     ans = [0, 0, 0, 0]
#     n = max(map(max, edges))
#     graph = [[] for _ in range(n+1)]
#     for edge in edges:
#         s, e = edge[0], edge[1]
#         graph[s].append(e)
#     print(graph)
        
#     # 시작 노드
#     # bfs를 이용해 방문 할 때마다 node에 채워서 그 부분은 bfs를 돌리지 않음
#     node = [False] * (n+1)
    
#     def bfs(start):
#         node_cnt = 1
#         edge_cnt = 0
#         visited = [False] * (n+1)
#         visited[start] = True
#         q = deque([start])
#         while q:
#             cur = q.popleft()
            
#             for neighbor in graph[cur]:
#                 # 간선의 갯수는 방문했어도 check해야 하기에 for문에 둠
#                 edge_cnt += 1
#                 if not visited[neighbor]:
#                     visited[neighbor] = True
#                     q.append(neighbor)
#                     node[neighbor] = True
#                     # node_cnt는 방문한 node는 세면 안되므로 여기서 cnt 함
#                     node_cnt += 1
        
#         if node_cnt == edge_cnt:
#             ans[1] += 1
#         elif node_cnt == edge_cnt + 1:
#             ans[2] += 1
#         elif node_cnt == edge_cnt - 1:
#             ans[3] += 1
#         else:
#             ans[0] = start
    
#     for tf in range(1, n+1):
#         print("node :", node)
#         if not node[tf]:
#             node[tf] = True
#             bfs(tf)
    
#     print(ans)
#     return ans


# 생성 정점은 들어오는 간선이 없고 나가는게 2개 이상이다
# 막대 그래프는 들어오는게 한개이상에 나가는게 없다. (제일 위에 노드)
# 8자 그래프는 들어오는게 2개 이상이고 나가는게 2개이다. (가운데 노드)
# 도넛은 생성정점에서 나가는 간선 갯수 - 막대 - 8자
# 그렇기 때문에 모든 now_out, now_in에서 += 1이 되짆 않고 저 기준을 만족 할 때만 올린다
def solution(edges):
    answer = [0, 0, 0, 0] # 생성 정점, 도넛, 막대, 8자
    max_val = max(map(max, edges)) + 1  # +1 은 인덱스 맞춰주기 위함
    in_cnt, out_cnt = [0] * max_val, [0] * max_val
        
    # in, out 간선 저장
    for now_out, now_in in edges:
        out_cnt[now_out] += 1
        in_cnt[now_in] += 1
        
    for now_node in range(1, max_val):
        if in_cnt[now_node] == 0 and out_cnt[now_node] >= 2: # 생성 노드
            answer[0] = now_node 
        elif in_cnt[now_node] >= 1 and out_cnt[now_node] == 0: # 막대 그래프
            answer[2] += 1
        elif in_cnt[now_node] >= 2 and out_cnt[now_node] == 2: # 8자 그래프 
            answer[3] += 1
    answer[1] = out_cnt[answer[0]] - sum(answer[2:])    # 도넛 그래프
    
    return answer