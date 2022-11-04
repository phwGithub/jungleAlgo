# 백준 1920 수 찾기

import sys

n = int(sys.stdin.readline())
num_list = sorted(list(map(int, sys.stdin.readline().strip().split(" "))))

m = int(sys.stdin.readline())
target_list = list(map(int, sys.stdin.readline().strip().split(" ")))

def binarySearch(num_list : list, key):
    pl = 0
    pr = len(num_list) - 1

    while True:
        pc = (pl + pr) // 2

        if num_list[pc] == key:
            #print(key, pc)
            return pc
        
        elif num_list[pc] < key:
            pl = pc + 1
        
        else:
            pr = pc - 1
        
        if pl > pr:
            break

    return -1

for target in target_list:
    if binarySearch(num_list, target) != -1:
        print(1)
    else:
        print(0)
