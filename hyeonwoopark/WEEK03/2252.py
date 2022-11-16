# 백준 2252 줄세우기

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split(" "))
graph = [[] for i in range(n + 1)]
degree_list = [0 for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().strip().split(" "))
    graph[u].append(v)
    degree_list[v] += 1

# print(graph)
# print(degree_list)

def topology_sort():
    que = deque()
    result = []

    for i in range(1, n + 1):
        if degree_list[i] == 0:
            que.append(i)
    
    while len(que) > 0:
        node = que.popleft()
        result.append(node)

        for i in graph[node]:
            degree_list[i] -= 1

            if degree_list[i] == 0:
                que.append(i)
    
    for ret in result:
        print(ret, end=" ")

topology_sort()