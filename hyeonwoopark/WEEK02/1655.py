# 백준 1655 가운데를 말해요

import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())

max_heap = []
min_heap = []
answers = []

for i in range(n):
    call_num = int(sys.stdin.readline())

    if len(max_heap) == len(min_heap):
        heappush(max_heap, call_num * -1)
    else:
        heappush(min_heap, call_num)
    
    if min_heap and min_heap[0] < -max_heap[0]:
        min_heap_root = heappop(min_heap)
        max_heap_root = heappop(max_heap) * -1
        heappush(max_heap, min_heap_root * -1)
        heappush(min_heap, max_heap_root)
    
    print(-max_heap[0])