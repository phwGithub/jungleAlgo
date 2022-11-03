
import sys

n=int(sys.stdin.readline())


#  i 번째 인덱스(행) value(열)에 퀸 위치 / 퀸 위치(인덱스와 요소를 활용하여
# 좌표 표현) 세팅
listQ = [n+1] * n

# i 번째 행에 퀸이 배치 됐는지 아닌지 검색 / 퀸 배치 세팅
listTF = [False] * n

# 경우의 수
cnt = 0

# m번째 행에 퀸 배치
def setQ(m, n, listQ, listTF):
    global cnt
    if m == n :
        cnt += 1
    else:
        for i in range(n):
            if not listTF[m] and i not in listQ[:m]:
                key = False
                for k in range(m):
                    if ((listQ[k] - i) / (k - m) == 1) or ((listQ[k] - i) / (k - m) == -1):
                        key = True
                if not key:
                    listQ[m] = i
                    listTF[m] = True
                    setQ(m+1, n,listQ, listTF)
                    listTF[m] = False

setQ(0, n, listQ, listTF)

print(cnt)
