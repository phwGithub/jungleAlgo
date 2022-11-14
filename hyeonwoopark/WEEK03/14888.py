# 백준 14888 연산자 끼워넣기

import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().strip().split(" ")))
op_cnts = list(map(int, sys.stdin.readline().strip().split(" ")))
max_sum = -sys.maxsize
min_sum = sys.maxsize

def dfs(op_list: list, idx: int):
    global max_sum
    global min_sum

    if len(op_list) == n - 1:
        total = num_list[0]
        for i in range(len(op_list)):
            if op_list[i] == 0:
                total += num_list[i + 1]
            if op_list[i] == 1:
                total -= num_list[i + 1]
            if op_list[i] == 2:
                total *= num_list[i + 1]
            if op_list[i] == 3:
                if total < 0:
                    total = -1 * ((-1 * total) // num_list[i + 1])
                else:
                    total = total // num_list[i + 1]

        #print(op_list, total, max_sum, min_sum)
        max_sum = max(max_sum, total)
        min_sum = min(min_sum, total)
        
        return
    
    for i in range(4):
        if op_cnts[i] <= 0:
            continue
        else:
            op_cnts[i] -= 1
            op_list.append(i)
            dfs(op_list, idx + 1)
            op_list.pop()
            op_cnts[i] += 1

dfs([], 0)
print(max_sum)
print(min_sum)