'''
첫줄에는 종이의 가로와 세로의 길이가 차례로 자연수로 주어진다. (가로와 세로의 길이는 최대 100㎝이다.)
'''
horzList = []
vertilist = []
area = input("").split(" ")
horzList.append(int(area[0]))
vertilist.append(int(area[1]))
'''
둘째 줄에는 칼로 잘라야하는 점선의 개수가 주어진다.
'''
cntCut = int(input(""))
'''
가로로 자르는 점선은 0과 점선 번호가 차례로 주어지고, 
세로로 자르는 점선은 1과 점선 번호가 주어진다. 
입력되는 두 숫자 사이에는 빈 칸이 하나씩 있다.
'''

for i in range(cntCut):
    item = input("").split(" ")
    typeNum = int(item[0])
    cutLen = int(item[1])
    if typeNum == 1:
        horzList.append(cutLen)
    else:
        vertilist.append(cutLen)
vertilist.sort()
horzList.sort()

cutedLV = []
cutedLH = []
if len(vertilist) == 1:
    cutedLV.append(vertilist[0])
else:
    for i in range(len(vertilist)):
        if i == 0:
            cutedLV.append(vertilist[i])
        else:
            cutedLV.append(vertilist[i]-vertilist[i-1])

if len(horzList) == 1:
    cutedLH.append(horzList[0])
else:
    for i in range(len(horzList)):
        if i == 0:
            cutedLH.append(horzList[i])
        else:
            cutedLH.append(horzList[i]-horzList[i-1])
cutedLH.sort()
cutedLV.sort()
print(cutedLV[-1] * cutedLH[-1])