# 백준 13334 철로

import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
way_list = []

for i in range(n):
    h, o = map(int, sys.stdin.readline().strip().split(" "))
    way_list.append((h, o))

d = int(sys.stdin.readline())



