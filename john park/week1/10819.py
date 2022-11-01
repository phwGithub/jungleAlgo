import sys
from itertools import permutations
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

permutation = list(permutations(A))
result_list =[]

def absValue(arr):
    result = 0
    for i in range(len(arr)-1):
        result += abs(arr[i]-arr[i+1])
    return result

for perm in permutation:
    absVal = absValue(perm)
    result_list.append(absVal)

print(max(result_list))
