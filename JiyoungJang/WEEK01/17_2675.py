import sys
input = sys.stdin.readline

T = int(input())    #test 개수 

for i in range(0, T) : 
    R, S = input().split()
    result = ''
    for ch in S : 
        # print(ch)
        result += ch * int(R)
    print(result)    
