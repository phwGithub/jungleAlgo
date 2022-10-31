import sys
input = sys.stdin.readline

# 소수 판별 함수 
# 소수일때 0, 소수가 아닐 때 1 반환
def isPrime(numData : int) :
    # 1 처리 (소수가 아님)
    if numData == 1 : 
        return 1
    keynum = int(numData/2)
    
    # 2 부터 keynum 까지 나눠지는지 본다
    for count in range(2, keynum + 1) : 
        if numData % count == 0 : 
            # 인수 있음, 소수 아님 
            return 1
    return 0    # 소수임

T = int(input())

for testCases in range(0, T) : 
    n = int(input())    # n은 골드바흐 파티션을 만드려는 짝수
    nChild1 = int(n/2)
    nChild2 = int(n/2)
    
    # nChild1, 2 양쪽에 각각 +1,-1을 해가면서 답을 찾는다 
    while isPrime(nChild1) or isPrime(nChild2) == 1 : # 둘 다 소수일때까지 진행 
        nChild1 -= 1
        nChild2 += 1
    
    print(nChild1, nChild2)
    