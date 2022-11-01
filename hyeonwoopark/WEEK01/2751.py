# 백준 2751 수 정렬하기 2

import sys  

sys.setrecursionlimit(10**5) # 10^5 까지 늘림.

# -----------------------------------------------

# 퀵소트 구현 (메모리 초과)

# def doQuickSort(a : list, left : int, right : int):
#     pl = left
#     pr = right
#     pivot = a[(left + right) // 2]

#     while pl <= pr:
#         while a[pl] < pivot: pl += 1
#         while a[pr] > pivot: pr -= 1

#         if pl <= pr:
#             a[pl], a[pr] = a[pr], a[pl]
#             pl += 1
#             pr -= 1

#     if left < pr : doQuickSort(a, left, pr)
#     if pl < right: doQuickSort(a, pl, right)

# def quickSort(a : list):
#     doQuickSort(a, 0, len(a) - 1)
 
 # ------------------------------------------

def mergeSort(a : list):
    if len(a) < 2:
        return a
    
    mid = len(a) // 2

    left = mergeSort(a[:mid])
    right = mergeSort(a[mid:])

    return mergeLeftRight(left, right)

def mergeLeftRight(left, right):
    merged_list = []

    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_list.append(left[l])
            l += 1
        else:
            merged_list.append(right[r])
            r += 1
            
    
    while l < len(left):
        merged_list.append(left[l])
        l += 1
    
    while r < len(right):
        merged_list.append(right[r])
        r += 1
    
    return merged_list


t = int(sys.stdin.readline().strip())

num_list = []
for _ in range(t):
    num_list.append(int(sys.stdin.readline()))

num_list = mergeSort(num_list)

for num in num_list:
    print(num)