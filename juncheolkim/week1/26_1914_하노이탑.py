import sys

def moveCnt(no, x, y):
    if no >1:
        moveCnt(no-1,    x,  6-x-y)
    print(f'{x} {y}')
    if no >1:
        moveCnt(no-1,  6-x-y,  y)

n=int(sys.stdin.readline())
print(2**n -1)
if n <= 20:
    moveCnt(n,1,3)


