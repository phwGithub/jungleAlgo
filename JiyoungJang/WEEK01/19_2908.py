import sys
input = sys.stdin.readline

# 두 숫자가 주어지면 거꾸로 읽고 그것들의 크기비교 

numList = list(input().split())
newNumList = []

for nums in numList : 
    newNum = ''
    for lone in reversed(nums) : 
        newNum += lone
    
    newNumList.append(int(newNum))

print(max(newNumList))