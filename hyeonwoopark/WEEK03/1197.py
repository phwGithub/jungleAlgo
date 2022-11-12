# 백준 1197 최소 스패닝 트리

import sys
from heapq import heapify, heappop, heappush
from collections import defaultdict
sys.setrecursionlimit(15000)

v, e = map(int, sys.stdin.readline().strip().split(" "))
edge_list = []
parent = [0 for i in range(v + 1)]
mst_w_sum = 0

for i in range(1, v + 1):
    parent[i] = i

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

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().strip().split(" "))
    edge_list.append((c, a, b))

edge_list.sort()

def kruskal_algo():
    global mst_w_sum

    for edge in edge_list:
        c, a, b = edge
        # print(find_parent(a), find_parent(b), find_parent(a) == find_parent(b), end=" ")
        # print(edge,end=" ")
        # print(parent)

        if find_parent(a) == find_parent(b):
            continue
        else:
            mst_w_sum += c
            union_parent(a, b)
    
    return mst_w_sum

def prim_alog(st):
    global mst_w_sum

    adj = defaultdict(list)
    visited = set()

    for edge in edge_list:
        c, a, b = edge
        adj[a].append((c, a, b))
        adj[b].append((c, b, a))
    
    candidate = adj[st]
    visited.add(st)
    heapify(candidate)

    while candidate:
        c, a, b = heappop(candidate)

        if b in visited:
            continue
        else:
            visited.add(b)
            mst_w_sum += c

        for edge in adj[b]:
            if edge[2] in visited:
                continue
            else:
                heappush(candidate, edge)

    return mst_w_sum

#print(kruskal_algo())
print(prim_alog(edge_list[0][1]))
