# 백준 2309 일곱 난쟁이

import sys
import copy

nan_list = []
visited = [False for i in range(9)]
found = False
answer = []
for i in range(9):
    nan_list.append(int(sys.stdin.readline()))

def findRealNan(idx, check_list):
    global found
    if idx == 7:
        if not found and sum(check_list) == 100:
            check_list.sort()
            for check in check_list:
                print(check)
            found = True
        return 
    
    for i in range(len(nan_list)):
        if not visited[i]:
            visited[i] = True
            check_list.append(nan_list[i])
            findRealNan(idx + 1, check_list)
            visited[i] = False
            check_list.remove(nan_list[i])

check_list = []
findRealNan(0, check_list)