import sys

n = int(sys.stdin.readline())
listI =  list(map(int,sys.stdin.readline().rstrip().split(' ')))


#  차이를 절대값으로 리턴해주는 함수
def subT(a,b):
    return abs(a-b)


# 리스트를 넣었을 때 각각의 차이를 절대값으로 바꾼후 더한 수 리턴
def plusL(listA):
    ans = 0
    for i in range(len(listA)-1):
        ans += subT(listA[i],listA[i+1])
    return ans

def factorial(a):
    if a == 0:
        return 1
    return a * factorial(a-1)

listB = [0] * n
listAll = [0] * factorial(n)
listSum = [0] * factorial(n)
cnt=0




# 리스트를 섞는 함수
def shakeL(listA,listB, n):
    global cnt
    global listSum
    global listAll

    if n == 0 :
        listAll[cnt] = listB
        listSum[cnt] = plusL(listB)
        cnt += 1
        return
    else:
        listC = listA[:]
        for i in range(n):
            listC = listA[:]
            listB[n-1] = listC[i]
            del(listC[i])
            shakeL(listC,listB,n-1)
            listC.insert(i,listB[n-1])


shakeL(listI,listB, n)

print(max(listSum))