import sys, math
from bisect import bisect_left

N = int(sys.stdin.readline().rstrip())

K = int(math.log2(N)) # N 은 2 의 K 승

L = [ list(map(int,sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]

offCnt = 0
onCnt = 0

tmp = []
for i in L :
    tmp += i

def splitSq(k:int, l:list):
    global onCnt
    global offCnt

    a = []
    b = []
    c = []
    d = []
    if k == 0:
        if l[0] == 1:
            onCnt += 1
            return
        offCnt += 1
        return

    if 0 in l : # 해당 배열에 0 이 존재
        if 1 in l : # 해당 배열에 1 이 존재 / 나눠줘야한다.
            for i in range(2**(k-1)): # 2의 k-1 승 만큼 계산
                a += l[i*2**k : i*2**k+2**(k-1)]
                b += l[i*2**k+2**(k-1) :i*2**k+2**(k)]
                c += l[2**(2*k-1) + i*2**k : 2**(2*k-1) + i*2**k+2**(k-1)]
                d += l[2**(2*k-1) + i*2**k+2**(k-1) : 2**(2*k-1) + i*2**k+2**(k)]

            splitSq(k-1,a)
            splitSq(k-1,b)
            splitSq(k-1,c)
            splitSq(k-1,d)
            return
        else: # 해당 배열에 0 만 존재
            offCnt += 1
            return # 0 카운트 하고 함수 종료
    else: # 해당 배열에 1만 존재
        onCnt += 1
        return

splitSq(K,tmp)

print(offCnt)
print(onCnt)

