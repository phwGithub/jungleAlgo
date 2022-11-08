# 백준 2630 색종이 자르기

import sys

n = int(sys.stdin.readline())
confetti = [list(map(int, sys.stdin.readline().strip().split(" "))) for i in range(n)]
white_confetti = 0
blue_confetti = 0

def checkAllSame(x : int, y : int, n : int):
    firstCell = confetti[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if confetti[i][j] != firstCell:
                #print(firstCell, confetti[i][j], i, j)
                return False
    
    return True

def cuttingConfetti(x : int, y : int, n : int):
    global white_confetti
    global blue_confetti

    if checkAllSame(x, y, n):
        #print("check pass", end=" ")
        #print(x, y, confetti[x][y])
        if confetti[x][y] == 0:
            white_confetti += 1
        else:
            blue_confetti += 1
        
        return
    
    half_n = n // 2
    cuttingConfetti(x, y, half_n)
    cuttingConfetti(x, y + half_n, half_n)
    cuttingConfetti(x + half_n, y, half_n)
    cuttingConfetti(x + half_n, y + half_n ,half_n)

cuttingConfetti(0, 0, n)
print(white_confetti)
print(blue_confetti)