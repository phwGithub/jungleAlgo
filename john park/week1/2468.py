from glob import glob
from itertools import count
import sys
from collections import deque

#DFS의 기본 원칙 : 앞으로 찾아가야할 노드, 이미 방문한 노드 기준으로 데이터 탐색
# Stack/queue로 구현하거나, "recursion" 이용
#BFS도 마찬가지. 다만, 어떤 자료를 우선 추출할 것이냐가 차이.

N = int(sys.stdin.readline().strip())
arr = [] # 실제 입력 값들 받는 곳

#입력받기
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

max_h = max(max(arr))

def check_safety(i,j,h):
    visited_list[i][j] = 1
    direction = [[0, -1], [-1,0], [0,1], [1,0]]
    q = deque() # 진행할 수 있는, 안전한 영역들을 모아두는
    q.append([i,j])
    
    while q:
        a = q.popleft()
        curr_X = a[0]
        curr_Y = a[1]   
             
        for k in range(4):
            new_X = curr_X + direction[k][0]
            new_Y = curr_Y + direction[k][1]
                        
            if new_X >= 0 and new_X < N and new_Y >= 0 and new_Y < N:
                #만약 나아간 좌표가 '안전영역'이면서 '방문한적없는 곳'이라면
                if arr[new_X][new_Y]> h and visited_list[new_X][new_Y]==0:
                    q.append([new_X, new_Y])
                    visited_list[new_X][new_Y] = 1

h_list=[]

for h in range(0, max_h+1):
    visited_list = [[0 for i in range(N)] for i in range(N)] #방문했으면 1로 변경해두기
    count = 0
    for i in range(N):
        for j in range(N):#방문하지 않았거나 안전한 영역(특정 물높이보다 높은지)인지 확인
            if visited_list[i][j] == 0 and arr[i][j] > h:
                check_safety(i,j,h) #(i,j)에 진입해서 근방의 좌표들이 안전영역인지 확인하는 함수
                count += 1
    h_list.append(count)

print(max(h_list))
