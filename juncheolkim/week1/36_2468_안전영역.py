import sys

# 런타임 에러(RecursionError) 피하기 위해
sys.setrecursionlimit(10**5)

#상 하 좌 우 변량
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def sink_(x, y, h):  # x,y 지점을 기준으로 주변을 탐색하는 재귀함수 

    for m in range(4):  # x,y 좌표를 기준으로 상하좌우 좌표를 nx 포문으로 가져옴
        nx = x + dx[m]
        ny = y + dy[m]
        
        if (0 <= nx < N) and (0 <= ny < N) and not sink_table[nx][ny] and water_board[nx][ny] > h:  # 자신이 건너갈 nx, ny 좌표에 대한 유효성을 먼저 검증함
            sink_table[nx][ny] = True   #유효성이 검증된 좌표에 한해서 재귀함수를 호출. 이 과정이 없으면 쌓는 스택이
            sink_(nx, ny, h) #실질적으로 재귀함수가 하는 역할은 sink_table에 boolean 값만 바꾸는 역할.


N = int(sys.stdin.readline())
water_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  #입력값에 따른 물 높이 board 생성


ans = 1 # 한 곳도 잠기지 않았을 경우가 최대 개수의 최솟값
for k in range(max(map(max, water_board))):
    sink_table = [[False]*N for _ in range(N)] # 물에 잠김 여부를 확인할 수 있는 Boolean Table 생성.
    count = 0
    for i in range(N):
        for j in range(N):
            if water_board[i][j] > k and not sink_table[i][j]:
                count += 1
                sink_table[i][j] = True
                sink_(i, j, k)
    ans = max(ans, count)

print(ans)