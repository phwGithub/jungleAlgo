# 백준 9663 N-Queen

nQueenCnt = 0
n = int(input())
board = [-1 for i in range(n)]

def check(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == abs(x - i):
            return False
    
    return True

def findNqueenCnt(idx):
    global nQueenCnt

    if idx == n:
        nQueenCnt += 1
        return
    
    for i in range(n):
        board[idx] = i

        if check(idx):
            findNqueenCnt(idx + 1)

findNqueenCnt(0)
print(nQueenCnt)