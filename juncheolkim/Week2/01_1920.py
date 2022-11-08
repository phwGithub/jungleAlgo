import sys

N = int(sys.stdin.readline().rstrip())


nList = list(map(int,sys.stdin.readline().rstrip().split(' ')))
nList.sort()
nList = list(set(nList))

T = int(sys.stdin.readline().rstrip())


tList = list(map(int,sys.stdin.readline().rstrip().split(' ')))




def find(a:int,listA:list):
    mid = len(listA)//2 # 중간 피봇 지점
    left = 0
    right = len(listA)
    while left < right-1:
        if a == listA[mid]: # 피봇지점일 경우
            return print(1)
        elif a < listA[mid]: # 피봇지점보다 작을 경우
            right = mid
            mid = (left + right)//2
        elif a > listA[mid]: # 피봇지점보다 클 경우
            left = mid
            mid = (left + right)//2
    if a == listA[mid]:
        print(1)
    else:
        print(0)

for i in tList:
    find(i, nList)



