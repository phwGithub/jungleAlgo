# 백준 11866 요세푸스 문제

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split(" "))
que = deque()
yose_seq = []

for i in range(1, n + 1):
    que.append(i)

while len(que) != 0:
    for i in range(k - 1):
        que.append(que.popleft())
    
    yose_seq.append(que.popleft())

print("<",end="")
for i in range(n - 1):
    print(yose_seq[i], end=", ")
print(yose_seq[n - 1], end=">")
 
