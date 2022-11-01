# 백준 1181 단어 정렬

import sys  

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
        if len(left[l]) == len(right[r]):
            if left[l] < right[r]:
                merged_list.append(left[l])
                l += 1
            else:
                merged_list.append(right[r])
                r += 1
        elif len(left[l]) < len(right[r]):
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

string_list = []
for _ in range(t):
    string_list.append(sys.stdin.readline().strip())

new_list = []
for string in string_list:
    if string not in new_list:
        new_list.append(string)

new_list = mergeSort(new_list)

for string in new_list:
    print(string)