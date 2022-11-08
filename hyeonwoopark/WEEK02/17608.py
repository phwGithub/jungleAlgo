# 백준 17608 막대기

import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    stick = int(sys.stdin.readline())

    if not len(stack):
        stack.append(stick)
    else:
        while True:
            if not len(stack):
                break

            if stack[-1] <= stick:
                stack.pop()
            else:
                break
        
        stack.append(stick)

print(len(stack))