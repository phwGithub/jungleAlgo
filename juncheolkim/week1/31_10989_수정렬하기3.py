import sys
n = int(sys.stdin.readline())
f = [0] * 10001
for i in range(n):
    f[int(sys.stdin.readline())] += 1
for i in range(10001):
    if f[i] != 0:
        for j in range(f[i]):
            print(i)