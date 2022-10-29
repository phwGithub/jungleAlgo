import sys

N, X = map(int, sys.stdin.readline().split())

list = list(map(int, sys.stdin.readline().split()))
now_list = []

if len(list) == N:
    for i in range(N):
        if list[i] < X:
            now_list.append(list[i])
        else:
            continue    
else:
    exit

for i in now_list:
    print(i, end=" ")
