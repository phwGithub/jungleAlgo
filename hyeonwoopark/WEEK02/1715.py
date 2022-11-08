# 백준 1715 카드 정렬하기

import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
deck_cnts = []
min_comp = 0

for i in range(n):
    heappush(deck_cnts, int(sys.stdin.readline()))

if n == 1:
    print(0)
else:
    while len(deck_cnts) > 1:
        temp_x = heappop(deck_cnts)
        temp_y = heappop(deck_cnts)
        min_comp += temp_x + temp_y
        heappush(deck_cnts, temp_x + temp_y)

    print(min_comp)
