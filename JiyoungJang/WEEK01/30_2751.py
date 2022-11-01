import sys
input = sys.stdin.readline

n = int(input())
max = -1000
numList = []


# 1. list의 길이의 반을 구한다 
# 2. left, right으로 나눈다 
# 3. 가운데 원소와 비교해서 크면 right, 작으면 left에 포함시킨다
# 4. 재귀함수다. 
# 5. 초기 조건 : 원소가 한개 일 때        
        
def sorting(sortList : list) : 
    llen = len(sortList)
    for i in range(1, llen) : 
        keyNum = sortList[i]    #비교를 진행할 기준숫자 
        left = 0
        right = i - 1
        
        while True : 
            here = (left + right) // 2
            if sortList[here] == keyNum : 
                return 0
            elif sortList[here] < keyNum : 
                left = here + 1
            else : 
                right = here - 1
            if left > right : 
                break
        
            


for i in range(0, n) : 
    sorting(int(input()), numList)

print(numList)
    