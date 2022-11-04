# append 함수를 사용하여 문제를 푸는 방법
# 임시 메모리가 할당된다.
def quicksort(x):
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quicksort(less) + equal + quicksort(more)

print(quicksort([1,67,4,3,9,5,8,3]))