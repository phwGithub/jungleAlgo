# 백준 10828 스택

import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    sentence = sys.stdin.readline().strip().split(" ")
    command = ""
    value = ""
    if len(sentence) >= 2:
        command = sentence[0]
        value = sentence[1]
    else:
        command = sentence[0]
    
    #print(command)
    if command == "push":
        stack.append(value)
        #print(stack)
    elif command == "pop":
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif command == "top":
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    else:
        if len(stack):
            print(0)
        else:
            print(1)