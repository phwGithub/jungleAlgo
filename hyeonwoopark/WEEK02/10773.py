# 백준 10773 제로

import sys

k = int(sys.stdin.readline())

stack = []

for i in range(k):
    callNumber = int(sys.stdin.readline())

    if callNumber == 0:
        stack.pop()
    else:
        stack.append(callNumber)
    
print(sum(stack))