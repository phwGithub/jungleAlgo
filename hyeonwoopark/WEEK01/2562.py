# 백준 2562 최댓값

num_list = []

for i in range(9):
    num_list.append(int(input()))

max_num = -1

for num in num_list:
    if num > max_num:
        max_num = num

print(max_num)
print(num_list.index(max(num_list)) + 1)