# 백준 2470 두 용액

import sys

n = int(sys.stdin.readline())
liq_list = list(map(int, sys.stdin.readline().strip().split(" ")))
liq_list = sorted(liq_list)

liq_tuple_list = []
ans = sys.maxsize
ans_tuple = ()

pl = 0
pr = n - 1
while pl < pr:
    sum_two_liq = liq_list[pl] + liq_list[pr]

    if abs(sum_two_liq) < ans:
        ans = abs(sum_two_liq)
        ans_tuple = (pl, pr)
        #print(ans, ans_tuple)

    if sum_two_liq == 0:
        break
    elif sum_two_liq > 0:
        pr -= 1
    else:
        pl += 1

print(liq_list[ans_tuple[0]], liq_list[ans_tuple[1]])
    