import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
max = -1000
numList = []

for _ in range(0, n) : 
    numList.append(int(input()))

for i in range(0, n) : 
    temp = numList[i]
    for j in range(0, n - 1) : 
        if numList[j + 1] < numList[j] : 
            numList[j + 1], numList[j] = numList[j], numList[j + 1]
            
for _ in numList : 
    print(_)            
            