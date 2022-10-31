import sys
input = sys.stdin.readline

N = int(input())
count = 0

if N < 100 : 
    print(N)
else : 
    if N == 1000 : 
        N = 999
    
    for _ in range(100, N + 1) : 
        num100 = int(str(_)[0]) # 100자리 수 
        num10 = int(str(_)[1]) # 10자리 수
        num1 = int(str(_)[2]) # 1자리 수 
        if num100 - num10 == num10 - num1 : 
            count += 1
    
    print(count + 99)
    
    