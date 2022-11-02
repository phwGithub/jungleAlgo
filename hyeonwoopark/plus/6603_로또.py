# 백준 6603 로또

import sys

def select6nums(idx, select_list : list, last):
    if idx == 6:
        for num in select_list:
            print(num, end=" ")
        print()
        return
    
    for i in range(idx, len(s)):
        if s[i] > last:
            select_list.append(s[i])
            last = s[i]
            select6nums(idx + 1, select_list, last)
            select_list.pop()
        

while True:
    t = sys.stdin.readline().strip()
    if t == "0":
        break

    s = list(map(int, t.split(" ")[1:]))

    #visited = [False for i in range(len(s))]

    select6nums(0, [], 0)

    print()

    
