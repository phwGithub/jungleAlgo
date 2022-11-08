import sys

input = sys.stdin.readline

listStack = []
cnt = int(input().rstrip())
while cnt > 0:
    inputItem = input().rstrip()
    count = 0
    key = True
    for i in inputItem:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0 :
            key = False
            break
    if not key:
        listStack.append('NO')
    elif count == 0:
        listStack.append('YES')
    else:
        listStack.append('NO')
    cnt -= 1

for i in listStack:
    print(i)