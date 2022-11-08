# 백준 2493 탑

import sys

n = int(sys.stdin.readline())
tower_list = list(map(int, sys.stdin.readline().strip().split(" ")))

stack = [(1, tower_list[0])]
target_list = [0]

for i in range(1, n):
    while len(stack) != 0:
        if stack[-1][1] >= tower_list[i]:
            break
        else:
            pop_temp = stack.pop()
    
    if len(stack) == 0:
        target_list.append(0)
        stack.append((i + 1, tower_list[i]))
    else:
        target_list.append(stack[-1][0])
        stack.append((i + 1, tower_list[i]))
        

    #print(stack, target_list)

for target in target_list:
    print(target, end=" ")