# 백준 10971 외판원 순회

import sys

def findLowestCost(idx, st, before, sum):
    global lowestWeight

    if idx == n and W[before][st] != 0:
        sum += W[before][st]
        lowestWeight = min(lowestWeight, sum)
        return
    
    for i in range(n):
        if not visited[i] and W[before][i] != 0:
            visited[i] = True
            findLowestCost(idx + 1, st, i, sum + W[before][i])
            visited[i] = False

n = int(sys.stdin.readline())

W = [list(map(int, sys.stdin.readline().strip().split(" "))) for i in range(n)]
visited = [False for i in range(n)]
lowestWeight = sys.maxsize

for i in range(n): 
    visited[i] = True
    findLowestCost(1, i, i, 0)
    visited[i] = False
    
print(lowestWeight)