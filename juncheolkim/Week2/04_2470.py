import sys

N = int(sys.stdin.readline().rstrip())
Nlist = list(map(int,sys.stdin.readline().rstrip().split(' ')))
Nlist.sort()

# 이중포인터 설정
left = 0
right = N-1

answer = sys.maxsize # 기준값
final = [] # 정답

while left < right: # 투포인터 진행

    s_left = Nlist[left]
    s_right = Nlist[right]
    tot = s_left + s_right
    
    if abs(tot) < answer: # 두 용액의 합이 0과 가장 가까운 용액을 정답에 담아주기
        answer = abs(tot)
        final = [s_left, s_right]
	
   
    if tot < 0:  # 합이 0보다 작다면 왼쪽의 값을 늘려 조금 더 0에 가깝게 만들어준다
        left += 1
    
    else: # 합이 0보다 크다면 오른쪽의 값을 줄여서 조금 더 0에 가깝게 만들어준다
        right -= 1

print(final[0], final[1])