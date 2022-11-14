# 백준 1707 이분 그래프

import sys
sys.setrecursionlimit(20000)

k = int(sys.stdin.readline())

def dfs(st: int, next_color: int):
    global error
    if error:
        return
    
    visited[st] = next_color
    #print(visited, st, next_color, error)
    for i in graph[st]:
        if not visited[i]:
            dfs(i, 2 if next_color == 1 else 1)
        elif visited[st] == visited[i]:
            #print("checked : {} {}".format(st, i))
            error = True
            return
        



for i in range(k):
    v, e = map(int, sys.stdin.readline().strip().split(" "))
    graph = [[] for _ in range(v + 1)]
    visited = [0 for _ in range(v + 1)]
    error = False

    for j in range(e):
        st, ed = map(int, sys.stdin.readline().strip().split(" "))
        graph[st].append(ed)
        graph[ed].append(st)
    
    for i in range(1, v + 1):
        if not visited[i]:
            dfs(i, 1)
            if error:
                break

    if error:
        print("NO")
    else:
        print("YES")