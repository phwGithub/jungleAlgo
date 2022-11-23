# 백준 9251 LCS

import sys

first_str = sys.stdin.readline().strip()
second_str = sys.stdin.readline().strip()

f_len = len(first_str)
s_len = len(second_str)
dp = [[0] * (s_len + 1) for _ in range(f_len + 1)]

for i in range(1, f_len + 1):
    for j in range(1, s_len + 1):
        if first_str[i-1] == second_str[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
print(dp[-1][-1])