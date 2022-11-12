# 백준 11724 연결 요소의 개수_Answer01

import sys

n, m = map(int, sys.stdin.readline().strip().split(" "))
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
parent = [i for i in range(0, n + 1)]
#print(parent)

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    u, v = map(int, sys.stdin.readline().strip().split(" "))
    # graph[u][v] = 1
    # graph[v][u] = 1

    union_parent(u, v)

for i in range(1, n + 1):
    find_parent(i)

root_list = set()

for i in range(1, n + 1):
    root_list.add(parent[i])

print(len(root_list))
