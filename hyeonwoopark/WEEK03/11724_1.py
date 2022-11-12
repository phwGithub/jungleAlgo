# 백준 11724 연결 요소의 개수_Answer02

import sys

n, m = map(int, sys.stdin.readline().strip().split(" "))
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().strip().split(" "))
    graph[u][v] = 1
    graph[v][u] = 1

def dfs(graph, st, idx):
    if idx == n:
        return
    
    visited[st] = True
    for i in range(1, n + 1):
        if graph[st][i] == 0 or visited[i]:
            continue
        else:
            dfs(graph, i, idx + 1)

cc_cnt = 0
for i in range(1, n + 1):
    #print(visited)
    if visited[i]:
        continue
    else:
        dfs(graph, i, 0)
        cc_cnt += 1

print(cc_cnt)