import sys

input = sys.stdin.readline

listStack = []
cnt = int(input().rstrip())
while cnt > 0:
    inputItem = int(input().rstrip())
    listStack.append(inputItem)
    cnt -= 1


last = list(reversed(listStack))
tmp = 0
cnt = 0
for i in last:
    if i > tmp:
        cnt += 1
        tmp = i

print (cnt)