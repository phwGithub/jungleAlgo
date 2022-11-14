# 백준 18352 특정 거리의 도시 찾기

import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().strip().split(" "))
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().strip().split(" "))
    graph[u].append(v)

que = deque()
city_in_k_list = []

def bfs(st: int):
    que.append([st, 0])
    visited[st] = True

    while len(que) > 0:
        x, d = que.popleft()

        if d == k:
            city_in_k_list.append(x)
        
        for des in graph[x]:
            if visited[des]:
                continue

            que.append([des, d + 1])
            visited[des] = True

bfs(x)
city_in_k_list.sort()

if len(city_in_k_list) == 0:
    print(-1)
else:
    for city in city_in_k_list:
        print(city)