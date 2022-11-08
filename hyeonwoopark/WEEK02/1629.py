# 백준 1629 곱셈

import sys

a, b, c = map(int, sys.stdin.readline().strip().split(" "))

def findRemainder(a, b, c):
    if b == 1:
        return a % c
    
    dividedRemainder = findRemainder(a, b // 2, c)

    if b % 2 == 0:
        return dividedRemainder * dividedRemainder % c
    else:
        return dividedRemainder * dividedRemainder * a % c

print(findRemainder(a, b, c))

