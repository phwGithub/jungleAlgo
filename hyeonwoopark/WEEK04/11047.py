# 백준 11047 동전 0

import sys

n, k = map(int, sys.stdin.readline().strip().split(" "))
coins = []
min_cnt = 0

for _ in range(n):
    coins.append(int(sys.stdin.readline()))

temp_k = k
for coin in coins[::-1]:
    min_cnt += temp_k // coin
    temp_k = temp_k % coin

print(min_cnt)