import sys
from itertools import permutations
# 도시 개수 N : 1이상 10이하
# (i,j)(j,k),,,,(u,i) 총 N개
N = int(sys.stdin.readline())

W=[[0] for i in range(N+1)]

for i in range(1, N+1):
    W[i]+=list(map(int, sys.stdin.readline().strip().split()))

#여태 방문한 도시 수
visited_num = 0
visited = [False] *(N+1)
k=0
for i in range(1, N+1):
    k+=sum(W[i])
result =k
sum_travel =0

def dfs_travel(start, now, visited_num): #시작하는 도시, 지금 도시, 방문한 도시 수
    # 방문 여부 체크해줘야함
    global sum_travel
    global result
    if visited_num == N and now == start:
        result = min(result, sum_travel)
        return
    
    #다음 도시 탐색
    for i in range(1, N+1):
        if visited[i] == False and W[now][i] >0:
            visited[i] = True
            sum_travel += W[now][i]
            if sum_travel <= result:
                dfs_travel(start, i, visited_num+1)
            visited[i] = False
            sum_travel -= W[now][i]

for i in range(1, N+1):
    dfs_travel(i,i,0)

print(result)
