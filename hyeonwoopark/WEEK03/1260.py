# 백준 1260 DFS와 BFS

import sys
from collections import deque

n, m, st = map(int, sys.stdin.readline().strip().split(" "))
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visted = [False for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().strip().split(" "))
    graph[u][v] = 1
    graph[v][u] = 1

def dfs(graph: list, st, idx):
    #print(st, idx)
    if idx == n:
        return
    
    visted[st] = True
    print(st, end=" ")
    for i in range(1, n + 1):
        if graph[st][i] == 0 or visted[i]:
            continue
        else:
            dfs(graph, i, idx + 1)

def bfs(graph, st):
    que = deque()
    que.append(st)
    visted = [False for _ in range(n + 1)]
    visted[st] = True

    while len(que) > 0:
        vt = que.popleft()
        print(vt, end=" ")

        for i in range(1, n + 1):
            if graph[vt][i] == 0 or visted[i]:
                continue
            else:
                que.append(i)
                visted[i] = True
    
dfs(graph, st, 0)
print()
bfs(graph, st)
