import sys
input = sys.stdin.readline

num = int(input())
j = 0
for i in range(0, num): # 줄 넘어가는 for
    j += 1
    for j in range(0, i + 1): # 줄마다 찍히는 갯수
        print('*', end='')
    print('')    
        
        