# 백준 11279 최대 힙

import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
heap_que = []

for i in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(heap_que) == 0:
            print(0)
        else:
            print(-1 * heappop(heap_que))
            
    else:
        heappush(heap_que, -x)