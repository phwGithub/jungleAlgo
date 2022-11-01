import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N, r, c = map(int, input().split())

def zzzz(N : int, r : int, c : int) : # r은 행 c은 열
    # 예외처리 
    if N < 1 : 
        return [0, 0, 0]
    # 초기케이스 
    if N == 1 : 
        if r < 1 : 
            if c < 1 : # 0번 0행 0열 
                return [0, 0, 0]
            else : #1번 0행 1열 
                return [1, 0, 1]
        else : 
            if c < 1 : # 2번 1행 0열 
                return [2, 1, 0]
            else : # 3번 1행 1열 
                return [3, 1, 1]    
    else : 
        # 초기 케이스가 아니라면, 1-4 사분면 중 어느 쪽인지 파악하기
        # N = 2
        if r < 2**(N-1) : 
            if c < 2**(N-1) : # 0사분면 
                before_res = zzzz(N-1, r, c)
                # print(before_res)
                return [before_res[0], before_res[1], before_res[2]]
            else : #1사분면 
                before_res = zzzz(N-1, r, c - 2**(N-1))
                # print(before_res)
                return [before_res[0] + 4**(N-1), before_res[1], before_res[2] + 2**(N-1)]
        else : 
            if c < 2**(N-1) : # 2사분면 
                before_res = zzzz(N-1, r - 2**(N-1), c)
                # print(before_res)
                return [before_res[0] + 2*(4**(N-1)), before_res[1] + 2**(N-1), before_res[2]]
            else : # 3사분면 
                before_res = zzzz(N-1, r - 2**(N-1), c - 2**(N-1))
                # print(before_res)
                return [before_res[0] + 3*(4**(N-1)), before_res[1] + 2**(N-1), before_res[2] + 2**(N-1)]
            
print(zzzz(N, r, c)[0])
