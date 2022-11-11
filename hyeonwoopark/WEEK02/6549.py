# 백준 6549 히스토그램에서 가장 큰 직사각형

import sys

def findLargestRect(histogram: list, st: int, ed: int):
    if len(histogram[st:ed]) == 1:
        return histogram[0]
    
    mid = (st + ed) // 2
    leftLargest = findLargestRect(histogram, st, mid)
    rightLargest = findLargestRect(histogram, mid, ed)
    
    left = mid - 1
    right = mid
    midLargest = 0

    while left >= st and right <= ed:
        left_histo = histogram[left]
        right_histo = histogram[right]

    return max(leftLargest, rightLargest, midLargest)

while True:
    histogram = list(map(int, sys.stdin.readline().strip().split(" ")))

    if histogram[0] == 0:
        break

    print(findLargestRect(histogram, 1, len(histogram)))
