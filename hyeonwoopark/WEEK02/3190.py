# 백준 3190 뱀

import sys
from collections import deque

n = int(sys.stdin.readline())
board = [[0 for i in range(n)] for i in range(0, n)]

k = int(sys.stdin.readline())
for i in range(k):
    x, y = map(int, sys.stdin.readline().strip().split(" "))
    board[x - 1][y - 1] = 1

l = int(sys.stdin.readline())
move_list = []
for i in range(l):
    x, y = sys.stdin.readline().strip().split(" ")
    x = int(x)
    move_list.append([x, y])

direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def change_direction(cur_dir : int, c : str):
    if cur_dir == 0:
        if c == "L":
            return 3
        else:
            return 2

    if cur_dir == 1:
        if c == "L":
            return 2
        else:
            return 3

    if cur_dir == 2:
        if c == "L":
            return 0
        else:
            return 1

    if cur_dir == 3:
        if c == "L":
            return 1
        else:
            return 0

pos_que = deque()
pos_que.append((0, 0))
time = 0
cur_dir = 0

#print(board)
#print(pos_que)
while True:
    cur_pos = pos_que[-1]
    #print(pos_que)
    #print(cur_pos, time, end=" ")
    
    board[cur_pos[0]][cur_pos[1]] = 2
    nx = cur_pos[0] + direction[cur_dir][0]
    ny = cur_pos[1] + direction[cur_dir][1]
    #print(nx, ny, board[nx][ny])
    #print(board)
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        #print("out of bounds : {}, {}".format(nx, ny))
        time += 1
        break
    
    if board[nx][ny] == 2:
        #print("body attack : {}, {}".format(nx, ny))
        time += 1
        break

    if board[nx][ny] != 1:
        pop_tail = pos_que.popleft()
        board[pop_tail[0]][pop_tail[1]] = 0
        
    
    pos_que.append((nx, ny))
    
    time += 1
    for move in move_list:
        if move[0] == time:
            cur_dir = change_direction(cur_dir, move[1])

print(time)
