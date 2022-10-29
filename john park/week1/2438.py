import sys

n = int(sys.stdin.readline())

globalstar = '*'

for i in range(n):
    print(globalstar)
    globalstar += "*"
