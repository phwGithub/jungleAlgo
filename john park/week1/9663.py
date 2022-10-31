# 일단 체스판 만들기
import sys

N = int(sys.stdin.readline())
board = [0]*(N) # index는 행의 위치, value는 열의 위치
count = 0

# 아래 함수는, x번째 행에 이미 queen을 놓고나서(즉 board[x]의 value가 존재), 이게 가능한지 확인하는 함수
def QueenPossibility(x : int):
    for i in range(x):
        if board[x] == board[i] or (abs(board[i]-board[x])) == abs(x-i):
            return False
    return True

#이제 체스판에 실제로 queen을 차례대로 놓으면서 가능한지 여부 판별. 판별이 하나씩 될 때마다 count +=1
def N_Queens(x):
    #index를 따져보면, 해당if문은 이미 마지막 행까지 다 돌고나서임.
    if x == N:
        global count
        count+=1
        return
    for i in range(N):
        board[x] =i
        if QueenPossibility(x):
            N_Queens(x+1)

N_Queens(0)
print(count)
