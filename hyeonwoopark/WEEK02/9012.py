# 백준 9012 괄호

import sys

t = int(sys.stdin.readline())

for i in range(t):
    ps = sys.stdin.readline().strip()

    stack = []
    flag = True
    for j in ps:
        if j == "(":
            stack.append(j)
        else:
            if len(stack):
                stack.pop()
            else:
                print("NO")
                flag = False
                break
    
    if flag:
        if len(stack):
            print("NO")
        else:
            print("YES")