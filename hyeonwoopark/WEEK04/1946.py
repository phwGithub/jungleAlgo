# 백준 1946 신입사원

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    emp_list = []
    pass_cnt = 0

    for _ in range(n):
        paper, interview = map(int, sys.stdin.readline().strip().split(" "))
        emp_list.append([paper, interview])
    
    emp_list = sorted(emp_list, key= lambda x: x[0])

    temp_interview = emp_list[0][1]
    pass_cnt += 1

    for i in range(1, len(emp_list)):
        if emp_list[i][1] < temp_interview:
            pass_cnt += 1
            temp_interview = emp_list[i][1]
    
    print(pass_cnt)

