# 백준 2750 수 정렬하기

def straight_insertion_sort(a : list):
    n = len(a)
    
    for i in range(1, n):
        j = i
        temp = a[i]

        while j > 0 and a[j - 1] > temp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = temp
    
    return a


t = int(input())

num_list = []
for i in range(t):
    num_list.append(int(input()))

num_list = straight_insertion_sort(num_list)

for num in num_list:
    print(num)