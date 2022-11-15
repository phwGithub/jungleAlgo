# 백준 1916 최소비용 구하기

import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
dist = [sys.maxsize for _ in range(n + 1)]

for _ in range(m):
    u, v, cost = map(int, sys.stdin.readline().strip().split(" "))
    graph[u].append([v, cost])
    
#print(graph)
st, des = map(int, sys.stdin.readline().strip().split(" "))
min_cost = sys.maxsize

# dijkstra 알고리즘 : 우선순위 큐
def dijkstra(st):
    que = []
    heappush(que, [0, st])

    while que:
        cost, cur_node = heappop(que)

        if dist[cur_node] < cost:
            continue

        for busInfo in graph[cur_node]:
            new_cost = cost + busInfo[1]

            if new_cost < dist[busInfo[0]]:
                dist[busInfo[0]] = new_cost
                heappush(que, [new_cost, busInfo[0]])

dijkstra(st)
min_cost = dist[des]
print(min_cost)

# # dijkstra 알고리즘 : 선형
# def dijkstra(st):
#     visited[st] = True

#     for i in range(len(graph[st])):
#         dist[st][i] = graph[st][i]
    
#     for _ in range(n - 1):
#         # 최소 비용 노드 찾기 : 선형탐색
#         temp_min = sys.maxsize
#         idx = 0
#         for i in range(1, n + 1):
#             if visited[i]:
#                 continue
            
#             if dist[st][i] < temp_min:   
#                 temp_min = min(temp_min, dist[st][i])
#                 idx = i

#         visited[idx] = True
#         #print(idx, visited, graph[idx])
#         for i in range(1, n + 1):
#             if dist[st][idx] + graph[idx][i] < dist[st][i]:
#                 dist[st][i] = dist[st][idx] + graph[idx][i]

# dijkstra(st)
# min_cost = dist[st][des]
# print(min_cost)

### 처음 시도 BFS : 메모리 초과

# def bfs(st, des): 
#     global min_cost

#     que = deque()
#     que.append([st, 0])

#     while len(que) > 0:
#         x, cost = que.popleft()
#         #print("x, cost = {}, {}".format(x, cost))

#         if x == des:
#             #print(x, cost)
#             min_cost = min(cost, min_cost)
#             continue
            
#         for target in graph[x]:
#             que.append([target[0], cost + target[1]])

# bfs(st, des)


