import sys

n,r,c=map(int, sys.stdin.readline().split(' '))

ans = 0

def whereZ(n,r,c):
    global ans
    n -= 1
    if n < 0:
        print(f'{ans}')
    else:
        # 1사분면
        if r < 2**n and c < 2**n:
            whereZ(n,r,c)
        # 2사분면
        elif r < 2**n and c >= 2**n:
            ans += (2**n) * (2**n)
            c -= 2**n
            whereZ(n,r,c)
        # 3사분면
        elif r >= 2**n and c < 2**n:
            ans += (2**n) * (2**n) * 2
            r -= 2**n
            whereZ(n,r,c)
        # 4사분면
        else:
            ans += (2**n) * (2**n) * 3
            c -= 2**n
            r -= 2**n
            whereZ(n,r,c)

whereZ(n,r,c)