# 백준 1931 회의실 배정

import sys

n = int(sys.stdin.readline())
scrum_list = []
reserve_cnt = 0

for _ in range(n):
    st, ed = map(int, sys.stdin.readline().strip().split(" "))
    scrum_list.append([st, ed])

scrum_list = sorted(scrum_list, key=lambda a: a[0])
scrum_list = sorted(scrum_list, key=lambda a: a[1])

last = 0
for scrum in scrum_list:
    st, ed = scrum
    
    if st >= last:
        reserve_cnt += 1
        last = ed

print(reserve_cnt)
