# 백준 2606 바이러스

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
parent = [i for i in range(n + 1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    
    return parent[x]

def union_parent(u, v):
    u = find_parent(u)
    v = find_parent(v)

    if u < v:
        parent[v] = u
    else:
        parent[u] = v

for i in range(m):
    u, v = map(int, sys.stdin.readline().strip().split(" "))
    union_parent(u, v)

for i in range(1, n + 1):
    find_parent(i)

virus_host = parent[1]
infected_cnt = 0
for i in range(2, n + 1):
    if virus_host == parent[i]:
        infected_cnt += 1

print(infected_cnt)
    