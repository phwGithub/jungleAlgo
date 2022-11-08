# 백준 18258 큐 2

import sys
from collections import deque

n = int(sys.stdin.readline())
que = deque()

for i in range(n):
    commandLine = sys.stdin.readline().strip().split(" ")

    if len(commandLine) == 2:
        que.append(commandLine[1])
    else:
        command = commandLine[0]

        if command == "pop":
            if len(que) == 0:
                print(-1)
            else:
                print(que.popleft())
        
        elif command == "size":
            print(len(que))
        
        elif command == "empty":
            if len(que) == 0:
                print(1)
            else:
                print(0)
        
        elif command == "front":
            if len(que) == 0:
                print(-1)
            else:
                print(que[0])
        
        elif command == "back":
            if len(que) == 0:
                print(-1)
            else:
                print(que[-1])

        else:
            print("wrong command")
