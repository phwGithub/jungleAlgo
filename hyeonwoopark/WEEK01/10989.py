# 백준 10989 수 정렬하기 3
import sys

n = int(sys.stdin.readline())

# 10001 크기의 배열을 만들고  1 ~ 10000의 수가 입력될 때 마다 해당 수의 인덱스에 +1 하기
dosu_list = [0 for i in range(10001)]

for i in range(n):
    idx = int(sys.stdin.readline())
    dosu_list[idx] += 1

for i in range(1, 10001):
    if dosu_list[i] != 0:
        for j in range(dosu_list[i]):
            print(i)
