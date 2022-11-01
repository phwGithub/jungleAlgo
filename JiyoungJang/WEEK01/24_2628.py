import sys
from xml.sax.handler import DTDHandler
input = sys.stdin.readline

#가로 세로 인풋 받기 
width, height = map(int, input().split())

w = [0, width]
h = [0, height]

#칼질 횟수 인풋 
knife = int(input())

# knife 번 자를 동안 
for n in range(0, knife) : 
    #가로0, 세로1 그리고 자르는 곳 인풋
    isWH, whereNum = map(int, input().split())
    
    # 가로 세로로 자르면 반대편이 갈라진다. 
    if isWH == 0 : #가로 일 때 
        h.append(whereNum)
    else : #세로 일 때 
        w.append(whereNum)

# 끝나고 list sorting
w.sort()
h.sort()

# for 문 돌려서 차이 max 찾아내기 
subW = []   # 가로 차이 
subH = []   # 세로 차이 
for i in range(1, len(w)) : 
    subW.append(w[i] - w[i - 1])


for i in range(1, len(h)) : 
    subH.append(h[i] - h[i - 1])
 
print(max(subW) * max(subH))