# 백준 5639 이진 검색 트리

import sys

sys.setrecursionlimit(15000)

preOrder = []
while True:
    try:
        preOrder.append(int(sys.stdin.readline()))
    except:
        break

def postOrder(preOrder, st, ed):
    #print("st : {}, ed : {}, st-ed : {}". format(st, ed, preOrder[st:ed]))
    if len(preOrder[st:ed]) < 1:
        return

    if len(preOrder[st:ed]) == 1:
        print(preOrder[st])
        return
    
    root_key = preOrder[st]
    mid = ed
    for i in range(st + 1, ed):
        if preOrder[i] > root_key:
            mid = i
            break
    
    postOrder(preOrder, st + 1, mid)
    postOrder(preOrder, mid, ed)
    print(root_key)

postOrder(preOrder, 0, len(preOrder))