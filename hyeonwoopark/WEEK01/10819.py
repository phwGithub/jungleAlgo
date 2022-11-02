# 백준 10819 차이를 최대로

import sys

n = int(sys.stdin.readline())
a =  list(map(int, sys.stdin.readline().strip().split(" ")))
visited = [False for i in range(n)]
max_sum = -1

def findDiffAbsSum(a : list):
    sum = 0
    for i in range(len(a) - 1):
        sum += abs(a[i] - a[i + 1])
    
    return sum

def makeRandomA(idx : int, randomA : list):
    global max_sum

    if idx == n:
        max_sum = max(max_sum, findDiffAbsSum(randomA))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            randomA.append(a[i])
            makeRandomA(idx + 1, randomA)
            randomA.pop()
            visited[i] = False

new_a = []
makeRandomA(0, new_a)
print(max_sum)