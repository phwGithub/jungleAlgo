# 백준 2178 미로

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split(" "))
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False for _ in range(m)] for _ in range(n)]
que = deque()

def bfs(st_x, st_y):
    que.append([st_x, st_y, 1])
    visited[st_x][st_y] = True

    while len(que) > 0:
        x, y, c = que.popleft()

        if x == n - 1 and y == m - 1:
            return c

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == "0":
                continue

            if visited[nx][ny]:
                continue
            else:
                que.append([nx, ny, c + 1])
                visited[nx][ny] = True

print(bfs(0, 0))