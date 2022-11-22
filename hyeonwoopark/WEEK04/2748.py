# 백준 2748 피보나치 수 2

import sys

n = int(sys.stdin.readline())
fibo = []
fibo.append(0)
fibo.append(1)

for i in range(n - 1):
    fibo.append(fibo[i] + fibo[i + 1])

print(fibo[n])