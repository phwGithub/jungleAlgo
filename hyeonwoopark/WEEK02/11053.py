# 백준 가장 긴 증가하는 부분 수열

import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().strip().split(" ")))
dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    #print(i, dp)

print(max(dp))