import sys

N, H = map(int,sys.stdin.readline().rstrip().split(' ')) # 나무의 갯수 / 필요 나무 길이 H >= sum(나무_리스트) 중단점이 될 것

trees = list(map(int,sys.stdin.readline().rstrip().split(' ')))

maxH = max(trees) # 나무 최대 높이. 

def cutT(height:int,treesList:list):
    sum = 0
    for i in treesList:
        if i - height > 0:
            sum += i - height
    return sum


mid = maxH//2
left = 0
right = maxH

key = True

while left < right -1 :
    
    getH = cutT(mid, trees)
    if getH == H: # 피봇지점이 H 와 같을경우 해당 높이 출력
        print(mid)
        key = False
        break
    elif getH > H: # 피봇지점이 H 보다 클 경우
        left = mid
        mid = (left + right)//2
    elif getH < H: # 피봇지점이 H 보다 작을
        right = mid
        mid = (left + right)//2

if key:
    if cutT(right, trees) >= H:
        print(right)
    else:
        print(left)