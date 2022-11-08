import sys

input = sys.stdin.readline

listStack = []
cnt = int(input().rstrip())
while cnt > 0:
    inputItem = int(input().rstrip())
    if inputItem != 0:
        listStack.append(inputItem)
    else:
        listStack.pop()
    cnt -= 1

print(sum(listStack))