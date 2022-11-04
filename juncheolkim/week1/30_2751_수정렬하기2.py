import sys

n = int(sys.stdin.readline())

listQ = []
for i in range(n):
    listQ.append(int(sys.stdin.readline()))

listQ.sort()

for i in listQ:
    print(i)