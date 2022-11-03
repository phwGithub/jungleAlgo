import sys


# 난쟁이들의 키를 받을 리스트
listH = [0] * 9

for i in range(9):
    listH[i] = int(sys.stdin.readline())


def shortMan(i, listH):
    # 삭제하기 위해서 각 반복 시점마다 listH 복사
    
    # i 번째 포함한 나머지 중 합이 100 나오는지 확인
    # 나온다면 해당 조합이 진짜 난쟁이
    # 안나온다면 i 번째 난쟁이가 가짜 난쟁이
    # 최대 2번하면 된다.
    # 2번 안나오면 나머지 7명이 진짜 난쟁이.
    
    # 첫번째 시도
    if i == 2:
        for j in range(1,9):
            listQ = listH[:]
            del(listQ[j])
            for m in range(1,8):
                listA = listQ[:]
                del(listA[m])

                if sum(listA) == 100:
                    listH = listA
                    i == 0
                    return listH
        if i != 0:
            del(listH[0])
            return shortMan(1,listH)
    # 두번째 시도
    elif i == 1:

        for j in range(1,8):
            listQ = listH[:]
            del(listQ[j])
            if sum(listQ) == 100:
                listH = listQ
                i == 0
                return listH
        if i != 0:
            del(listH[0])
            return listH

ans = shortMan(2,listH)
ans.sort()
for i in ans:
    print(i)