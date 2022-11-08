'''
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다
'''
import sys

input = sys.stdin.readline

listStack = []
cnt = int(input().rstrip())
printList = []
while cnt > 0:
    inputItem = input().rstrip().split(' ')
    if inputItem[0] == 'push':
        listStack.append(int(inputItem[1]))
    elif inputItem[0] == "pop":
        if listStack:
            printList.append(listStack.pop())
        else:
            printList.append(-1)
    elif inputItem[0] == "size":
        printList.append(len(listStack))
    elif inputItem[0] == "empty":
        if listStack:
            printList.append(0)
        else:
            printList.append(1)
    elif inputItem[0] == "top":
        if listStack:
            printList.append(listStack[-1])
        else:
            printList.append(-1)
    cnt -= 1

for i in printList:
    print(i)