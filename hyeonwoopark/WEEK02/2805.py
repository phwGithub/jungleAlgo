# 백준 2805 나무 자르기

import sys

n, m = map(int, sys.stdin.readline().strip().split(" "))
tree_list = list(map(int, sys.stdin.readline().strip().split(" ")))
max_h = sys.maxsize * -1

def getCutTree(h : int):
    cutTreeSum = 0

    for tree in tree_list:
        cutTree = tree - h

        if cutTree <= 0:
            continue
            
        cutTreeSum += cutTree
    
    return cutTreeSum
    
pl = 0
pr = 2000000000

while True:
    h = (pl + pr) // 2

    cutTreeSum = getCutTree(h)

    if cutTreeSum >= m:
        max_h = max(max_h, h)
        pl = h + 1
    else:
        pr = h - 1
    
    if pl > pr:
        break

print(max_h)