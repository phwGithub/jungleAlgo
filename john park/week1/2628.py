import sys

w, h = map(int, sys.stdin.readline().split())

rep = int(sys.stdin.readline())

vNumList = [0, w]
hNumList = [0, h]

for i in range(rep):
    isVertical, cutNum = map(int, sys.stdin.readline().split())
    if isVertical == 1:
        vNumList.append(cutNum)
    else:
        hNumList.append(cutNum)

vNumList.sort()
hNumList.sort()

vInterval = []
hInterval = []

for i in range(len(vNumList)-1):
    vInterval.append(vNumList[i+1]-vNumList[i])
for i in range(len(hNumList)-1):
    hInterval.append(hNumList[i+1]-hNumList[i])

print(max(hInterval)*max(vInterval))
