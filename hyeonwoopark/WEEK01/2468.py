# 백준 2468 안전지대

import sys

sys.setrecursionlimit(15000)

n = int(sys.stdin.readline())
heighInfo = [list(map(int, sys.stdin.readline().strip().split(" "))) for i in range(n)]
direction = [[0, -1],[0, 1],[-1, 0],[1, 0]]

answer = -1

def findSafetyZone(x, y, k):
    #print(x, y)
    #print(canVisit)

    for i in range(len(direction)):
        newX = x + direction[i][0]
        newY = y + direction[i][1]

        if newX < 0 or newX >= n or newY < 0 or newY >= n:
            continue
        else:
            if not canVisit[newX][newY] or heighInfo[newX][newY] <= k:
                continue

            canVisit[newX][newY] = False
            findSafetyZone(newX, newY, k)

for k in range(max(max(heighInfo))):
    canVisit = [[True for i in range(n)] for i in range(n)]
    maxSafetyZoneCnt = 0

    for i in range(n):
        for j in range(n):
            if canVisit[i][j] and heighInfo[i][j] > k:
                canVisit[i][j] = False
                maxSafetyZoneCnt += 1
                findSafetyZone(i, j, k)

    #print(maxSafetyZoneCnt)
    answer = max(maxSafetyZoneCnt, answer)
            

print(answer)